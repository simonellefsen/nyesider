import {
	coverUrl,
	listIssueSlugs,
	listMagazineSlugs,
	listIssues,
	getIssue
} from '$lib/server/content';
import { SITE_URL } from '$lib/seo';

export const prerender = true;

function escapeXml(s: string): string {
	return s
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;')
		.replace(/'/g, '&apos;');
}

function urlEntry(opts: {
	loc: string;
	lastmod?: string;
	changefreq?: string;
	priority?: string;
	image?: string | null;
	imageTitle?: string;
}): string {
	const lastmod = opts.lastmod
		? `\n    <lastmod>${escapeXml(opts.lastmod)}</lastmod>`
		: '';
	const changefreq = opts.changefreq
		? `\n    <changefreq>${opts.changefreq}</changefreq>`
		: '';
	const priority = opts.priority ? `\n    <priority>${opts.priority}</priority>` : '';
	let image = '';
	if (opts.image) {
		const imgLoc = opts.image.startsWith('http') ? opts.image : `${SITE_URL}${opts.image}`;
		image = `
    <image:image>
      <image:loc>${escapeXml(imgLoc)}</image:loc>${
			opts.imageTitle
				? `\n      <image:title>${escapeXml(opts.imageTitle)}</image:title>`
				: ''
		}
    </image:image>`;
	}
	return `  <url>
    <loc>${escapeXml(opts.loc)}</loc>${lastmod}${changefreq}${priority}${image}
  </url>`;
}

export function GET() {
	const urls: string[] = [];

	urls.push(
		urlEntry({
			loc: `${SITE_URL}/`,
			changefreq: 'weekly',
			priority: '1.0'
		})
	);

	for (const mag of listMagazineSlugs()) {
		const issues = listIssues(mag);
		const latest = issues[0];
		urls.push(
			urlEntry({
				loc: `${SITE_URL}/${mag}`,
				lastmod: latest?.published,
				changefreq: 'weekly',
				priority: '0.9',
				image: latest ? coverUrl(mag, latest) : null,
				imageTitle: latest?.title
			})
		);

		for (const issueSlug of listIssueSlugs(mag)) {
			const issue = getIssue(mag, issueSlug);
			if (issue.status !== 'published') continue;
			const cover = coverUrl(mag, issue);
			urls.push(
				urlEntry({
					loc: `${SITE_URL}/${mag}/${issue.slug}`,
					lastmod: issue.published,
					changefreq: 'monthly',
					priority: '0.8',
					image: cover,
					imageTitle: issue.title
				})
			);
			for (const art of [...issue.articles].sort((a, b) => a.order - b.order)) {
				const img = art.image
					? `/content/${mag}/issues/${issue.slug}/${art.image.replace(/^\.\.\//, '').replace(/^\.\//, '')}`
					: cover;
				urls.push(
					urlEntry({
						loc: `${SITE_URL}/${mag}/${issue.slug}/${art.slug}`,
						lastmod: issue.published,
						changefreq: 'monthly',
						priority: '0.7',
						image: img,
						imageTitle: art.title
					})
				);
			}
		}
	}

	const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
${urls.join('\n')}
</urlset>
`;

	return new Response(body, {
		headers: {
			'Content-Type': 'application/xml; charset=utf-8',
			'Cache-Control': 'public, max-age=3600'
		}
	});
}
