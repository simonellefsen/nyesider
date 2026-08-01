import { readdirSync, readFileSync, existsSync, statSync } from 'node:fs';
import path from 'node:path';
import matter from 'gray-matter';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import remarkRehype from 'remark-rehype';
import rehypeRaw from 'rehype-raw';
import rehypeStringify from 'rehype-stringify';
import type {
	Article,
	ArticleBodyPart,
	ArticleMeta,
	ChartSpec,
	Issue,
	Magazine,
	MagazineSummary
} from '$lib/types';

/**
 * Repo content/ directory (sibling of web/).
 * Resolve from process.cwd() (web/) so the path stays correct after Vite bundles
 * server modules into .svelte-kit/output/server/chunks/.
 */
export const CONTENT_ROOT = path.resolve(process.cwd(), '../content');

function readJson<T>(file: string): T {
	return JSON.parse(readFileSync(file, 'utf-8')) as T;
}

function listDirs(dir: string): string[] {
	if (!existsSync(dir)) return [];
	return readdirSync(dir)
		.filter((name) => {
			const p = path.join(dir, name);
			return statSync(p).isDirectory() && !name.startsWith('.') && !name.startsWith('_');
		})
		.sort();
}

export function listMagazineSlugs(): string[] {
	return listDirs(CONTENT_ROOT);
}

export function getMagazine(slug: string): Magazine {
	const file = path.join(CONTENT_ROOT, slug, 'magazine.json');
	if (!existsSync(file)) throw new Error(`Unknown magazine: ${slug}`);
	return readJson<Magazine>(file);
}

export function listIssueSlugs(magazine: string): string[] {
	return listDirs(path.join(CONTENT_ROOT, magazine, 'issues'));
}

export function getIssue(magazine: string, issueSlug: string): Issue {
	const dir = path.join(CONTENT_ROOT, magazine, 'issues', issueSlug);
	const file = path.join(dir, 'issue.json');
	if (!existsSync(file)) throw new Error(`Unknown issue: ${magazine}/${issueSlug}`);
	const raw = readJson<Omit<Issue, 'slug'>>(file);
	return { ...raw, slug: issueSlug, magazine };
}

/** Public URL for a file living under content/<mag>/issues/<issue>/… */
export function contentAssetUrl(
	magazine: string,
	issueSlug: string,
	relativePath: string | undefined | null
): string | null {
	if (!relativePath) return null;
	// frontmatter may use ../images/foo.png — normalize to images/foo.png
	const cleaned = relativePath.replace(/^\.\.\//, '').replace(/^\.\//, '');
	return `/content/${magazine}/issues/${issueSlug}/${cleaned}`;
}

export function pdfUrl(magazine: string, issue: Issue): string | null {
	if (!issue.pdf) return null;
	return contentAssetUrl(magazine, issue.slug, issue.pdf);
}

export function coverUrl(magazine: string, issue: Issue): string | null {
	return contentAssetUrl(magazine, issue.slug, issue.cover);
}

export function articleImageUrl(
	magazine: string,
	issueSlug: string,
	image: string | undefined
): string | null {
	return contentAssetUrl(magazine, issueSlug, image);
}

const FIGURE_MARKER_RE = /^\[FIGUR\s*\d*\]$/gim;

/**
 * Replace [FIGUR N] placeholder lines with <figure> markup, positionally —
 * the Nth marker gets the Nth url in figureUrls (mirrors production/build_magazine.py).
 */
function resolveFigures(md: string, figureUrls: string[]): string {
	if (!figureUrls.length) return md;
	let i = 0;
	return md.replace(FIGURE_MARKER_RE, () => {
		const url = figureUrls[i++];
		if (!url) return '';
		return `<figure class="prose-figure"><img src="${url}" alt="" loading="lazy" /></figure>`;
	});
}

async function markdownToHtml(md: string): Promise<string> {
	const file = await unified()
		.use(remarkParse)
		.use(remarkGfm)
		.use(remarkRehype, { allowDangerousHtml: true })
		.use(rehypeRaw)
		.use(rehypeStringify)
		.process(md);

	// GFM footnotes ship with an English sr-only heading; surface it in Danish.
	return String(file)
		.replace(
			'<h2 class="sr-only" id="footnote-label">Footnotes</h2>',
			'<h2 class="footnotes-heading" id="footnote-label">Kilder &amp; links</h2>'
		)
		.replaceAll('aria-label="Back to reference', 'aria-label="Tilbage til henvisning')
		.replaceAll(' rel="noopener noreferrer"', '') // avoid doubles if re-run
		.replaceAll(
			/<a href="(https?:\/\/[^"]+)"/g,
			'<a href="$1" rel="noopener noreferrer" target="_blank"'
		);
}

const CHART_MARKER_RE = /\[CHART\s+([a-z0-9_-]+)\]/gi;

function normalizeChartObject(
	item: unknown,
	fallbackId?: string
): ChartSpec | null {
	if (!item || typeof item !== 'object') return null;
	const c = item as Record<string, unknown>;
	const id =
		typeof c.id === 'string' && c.id
			? c.id
			: fallbackId && fallbackId.length
				? fallbackId
				: null;
	if (!id || !Array.isArray(c.years) || !Array.isArray(c.series)) return null;
	const years = (c.years as unknown[]).map(Number).filter((n) => !Number.isNaN(n));
	const series = (c.series as unknown[])
		.map((s) => {
			if (!s || typeof s !== 'object') return null;
			const row = s as Record<string, unknown>;
			if (typeof row.name !== 'string' || !Array.isArray(row.values)) return null;
			return {
				name: row.name,
				values: (row.values as unknown[]).map(Number),
				color: typeof row.color === 'string' ? row.color : undefined
			};
		})
		.filter((s): s is NonNullable<typeof s> => !!s);
	if (!years.length || !series.length) return null;
	return {
		id,
		title: typeof c.title === 'string' ? c.title : id,
		unit: typeof c.unit === 'string' ? c.unit : undefined,
		note: typeof c.note === 'string' ? c.note : undefined,
		source: typeof c.source === 'string' ? c.source : undefined,
		sourceUrl: typeof c.sourceUrl === 'string' ? c.sourceUrl : undefined,
		years,
		series
	};
}

function normalizeCharts(raw: unknown): ChartSpec[] {
	if (!Array.isArray(raw)) return [];
	const out: ChartSpec[] = [];
	for (const item of raw) {
		const chart = normalizeChartObject(item);
		if (chart) out.push(chart);
	}
	return out;
}

/**
 * Load reusable chart specs from content/<mag>/issues/<issue>/charts/*.json
 * (canonical long-term home for multi-year series).
 */
function loadIssueChartLibrary(magazine: string, issueSlug: string): Map<string, ChartSpec> {
	const dir = path.join(CONTENT_ROOT, magazine, 'issues', issueSlug, 'charts');
	const map = new Map<string, ChartSpec>();
	if (!existsSync(dir)) return map;
	for (const name of readdirSync(dir)) {
		if (!name.endsWith('.json')) continue;
		const fileId = name.replace(/\.json$/i, '');
		try {
			const raw = JSON.parse(readFileSync(path.join(dir, name), 'utf-8')) as unknown;
			const chart = normalizeChartObject(raw, fileId);
			if (chart) map.set(chart.id, chart);
		} catch {
			// skip invalid chart files
		}
	}
	return map;
}

function mergeCharts(
	library: Map<string, ChartSpec>,
	fromFrontmatter: ChartSpec[]
): Map<string, ChartSpec> {
	const map = new Map(library);
	for (const c of fromFrontmatter) map.set(c.id, c); // article frontmatter overrides
	return map;
}

async function buildBodyParts(
	md: string,
	byId: Map<string, ChartSpec>
): Promise<{ parts: ArticleBodyPart[]; used: ChartSpec[] }> {
	const parts: ArticleBodyPart[] = [];
	const used: ChartSpec[] = [];
	let last = 0;
	const re = new RegExp(CHART_MARKER_RE.source, 'gi');
	let m: RegExpExecArray | null;
	const matches: { index: number; end: number; id: string }[] = [];
	while ((m = re.exec(md)) !== null) {
		matches.push({ index: m.index, end: m.index + m[0].length, id: m[1] });
	}
	if (!matches.length) {
		const html = await markdownToHtml(md);
		return { parts: html.trim() ? [{ type: 'html', html }] : [], used };
	}
	for (const match of matches) {
		const before = md.slice(last, match.index).trim();
		if (before) {
			parts.push({ type: 'html', html: await markdownToHtml(before) });
		}
		const chart = byId.get(match.id);
		if (chart) {
			parts.push({ type: 'chart', chart });
			if (!used.find((c) => c.id === chart.id)) used.push(chart);
		}
		last = match.end;
	}
	const after = md.slice(last).trim();
	if (after) {
		parts.push({ type: 'html', html: await markdownToHtml(after) });
	}
	return { parts, used };
}

export async function getArticle(
	magazine: string,
	issueSlug: string,
	articleSlug: string
): Promise<Article> {
	const issue = getIssue(magazine, issueSlug);
	const meta = issue.articles.find((a) => a.slug === articleSlug);
	if (!meta) throw new Error(`Unknown article: ${magazine}/${issueSlug}/${articleSlug}`);

	const mdPath = path.join(CONTENT_ROOT, magazine, 'issues', issueSlug, meta.file);
	const raw = readFileSync(mdPath, 'utf-8');
	const { data, content } = matter(raw);

	const figureUrls = ((data.figures as string[] | undefined) ?? [])
		.map((f) => articleImageUrl(magazine, issueSlug, f))
		.filter((u): u is string => !!u);
	const withFigures = resolveFigures(content, figureUrls);
	const library = loadIssueChartLibrary(magazine, issueSlug);
	const fromFm = normalizeCharts(data.charts);
	const byId = mergeCharts(library, fromFm);
	const { parts: body, used: charts } = await buildBodyParts(withFigures, byId);
	const html = body
		.filter((p): p is { type: 'html'; html: string } => p.type === 'html')
		.map((p) => p.html)
		.join('\n');

	return {
		slug: meta.slug,
		file: meta.file,
		order: meta.order,
		title: (data.title as string) ?? meta.title,
		section: (data.section as string) ?? meta.section,
		byline: (data.byline as string) ?? meta.byline,
		standfirst: (data.standfirst as string | undefined) ?? meta.standfirst,
		image: (data.image as string | undefined) ?? meta.image,
		imageCredit:
			(data.imageCredit as string | undefined) ?? meta.imageCredit,
		imageSource:
			(data.imageSource as string | undefined) ?? meta.imageSource,
		html,
		body,
		charts,
		bodyMarkdown: content
	};
}

export function listIssues(magazine: string): Issue[] {
	return listIssueSlugs(magazine)
		.map((slug) => getIssue(magazine, slug))
		.filter((i) => i.status === 'published')
		.sort((a, b) => (a.published < b.published ? 1 : -1));
}

export function getLatestIssue(magazine: string): Issue | null {
	const issues = listIssues(magazine);
	return issues[0] ?? null;
}

export function listMagazines(): MagazineSummary[] {
	return listMagazineSlugs().map((slug) => {
		const mag = getMagazine(slug);
		const issues = listIssues(slug);
		return {
			...mag,
			latestIssue: issues[0] ?? null,
			issueCount: issues.length
		};
	});
}

export function enrichArticles(
	magazine: string,
	issue: Issue
): (ArticleMeta & { href: string; imageUrl: string | null })[] {
	return [...issue.articles]
		.sort((a, b) => a.order - b.order)
		.map((a) => ({
			...a,
			href: `/${magazine}/${issue.slug}/${a.slug}`,
			imageUrl: articleImageUrl(magazine, issue.slug, a.image)
		}));
}

export function adjacentArticles(
	issue: Issue,
	articleSlug: string
): { prev: ArticleMeta | null; next: ArticleMeta | null } {
	const sorted = [...issue.articles].sort((a, b) => a.order - b.order);
	const idx = sorted.findIndex((a) => a.slug === articleSlug);
	return {
		prev: idx > 0 ? sorted[idx - 1] : null,
		next: idx >= 0 && idx < sorted.length - 1 ? sorted[idx + 1] : null
	};
}

/** Danish long date: "19. juli 2026" */
export function formatDanishDate(iso: string): string {
	const d = new Date(iso + (iso.length === 10 ? 'T12:00:00' : ''));
	return new Intl.DateTimeFormat('da-DK', {
		day: 'numeric',
		month: 'long',
		year: 'numeric'
	}).format(d);
}
