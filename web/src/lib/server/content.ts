import { readdirSync, readFileSync, existsSync, statSync } from 'node:fs';
import path from 'node:path';
import matter from 'gray-matter';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import remarkRehype from 'remark-rehype';
import rehypeRaw from 'rehype-raw';
import rehypeStringify from 'rehype-stringify';
import type { Article, ArticleMeta, Issue, Magazine, MagazineSummary } from '$lib/types';

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
	const html = await markdownToHtml(resolveFigures(content, figureUrls));

	return {
		slug: meta.slug,
		file: meta.file,
		order: meta.order,
		title: (data.title as string) ?? meta.title,
		section: (data.section as string) ?? meta.section,
		byline: (data.byline as string) ?? meta.byline,
		standfirst: (data.standfirst as string | undefined) ?? meta.standfirst,
		image: (data.image as string | undefined) ?? meta.image,
		html,
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
