import { coverUrl, getMagazine, listIssues, listMagazines } from '$lib/server/content';
import { SITE_DESCRIPTION, SITE_NAME, SITE_URL, absoluteUrl } from '$lib/seo';
import type { Issue, Magazine } from '$lib/types';

export function escapeXml(s: string): string {
	return s
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;')
		.replace(/'/g, '&apos;');
}

/** RFC-822 style date for RSS (UTC). */
export function rssDate(iso: string): string {
	const d = new Date(iso.length === 10 ? `${iso}T12:00:00Z` : iso);
	return d.toUTCString();
}

export type RssItem = {
	title: string;
	link: string;
	guid: string;
	pubDate: string;
	description: string;
	/** Absolute image URL when available */
	enclosureUrl?: string | null;
};

export function issueToRssItem(magazine: Magazine, issue: Issue): RssItem {
	const path = `/${magazine.slug}/${issue.slug}`;
	const link = absoluteUrl(path);
	const cover = coverUrl(magazine.slug, issue);
	const titles = [...issue.articles]
		.sort((a, b) => a.order - b.order)
		.map((a) => a.title);
	const listed = titles.slice(0, 8);
	const more =
		titles.length > 8 ? `\n… og ${titles.length - 8} artikler mere` : '';
	const theme = issue.issueTheme ? ` Tema: ${issue.issueTheme}.` : '';
	const toc = listed.length
		? `\n\nI dette nummer:\n${listed.map((t) => `• ${t}`).join('\n')}${more}`
		: '';
	// Plain text — escaped once when serializing the feed
	const description = `${issue.title}.${theme}${toc}\n\nLæs nummeret: ${link}`;
	const title = issue.issueTheme
		? `${issue.title} — ${issue.issueTheme}`
		: issue.title;

	return {
		title,
		link,
		guid: link,
		pubDate: rssDate(issue.published),
		description,
		enclosureUrl: cover ? absoluteUrl(cover) : null
	};
}

export function collectSiteRssItems(limit = 40): RssItem[] {
	const items: RssItem[] = [];
	for (const summary of listMagazines()) {
		const mag = getMagazine(summary.slug);
		for (const issue of listIssues(summary.slug)) {
			items.push(issueToRssItem(mag, issue));
		}
	}
	items.sort((a, b) => (a.pubDate < b.pubDate ? 1 : -1));
	return items.slice(0, limit);
}

export function collectMagazineRssItems(magazineSlug: string, limit = 30): RssItem[] {
	const mag = getMagazine(magazineSlug);
	return listIssues(magazineSlug)
		.slice(0, limit)
		.map((issue) => issueToRssItem(mag, issue));
}

export function buildRssXml(opts: {
	title: string;
	description: string;
	link: string;
	feedUrl: string;
	items: RssItem[];
	language?: string;
}): string {
	const lang = opts.language ?? 'da';
	const channelImage = absoluteUrl('/icon-512.png');

	const itemXml = opts.items
		.map((item) => {
			const enclosure = item.enclosureUrl
				? `\n      <enclosure url="${escapeXml(item.enclosureUrl)}" type="image/png" />`
				: '';
			return `    <item>
      <title>${escapeXml(item.title)}</title>
      <link>${escapeXml(item.link)}</link>
      <guid isPermaLink="true">${escapeXml(item.guid)}</guid>
      <pubDate>${escapeXml(item.pubDate)}</pubDate>
      <description>${escapeXml(item.description)}</description>${enclosure}
    </item>`;
		})
		.join('\n');

	return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${escapeXml(opts.title)}</title>
    <link>${escapeXml(opts.link)}</link>
    <description>${escapeXml(opts.description)}</description>
    <language>${escapeXml(lang)}</language>
    <lastBuildDate>${escapeXml(new Date().toUTCString())}</lastBuildDate>
    <atom:link href="${escapeXml(opts.feedUrl)}" rel="self" type="application/rss+xml" />
    <image>
      <url>${escapeXml(channelImage)}</url>
      <title>${escapeXml(opts.title)}</title>
      <link>${escapeXml(opts.link)}</link>
    </image>
${itemXml}
  </channel>
</rss>
`;
}

export function siteFeedXml(): string {
	return buildRssXml({
		title: `${SITE_NAME} — nye numre`,
		description: SITE_DESCRIPTION + ' Feed med nye magasinernumre.',
		link: absoluteUrl('/'),
		feedUrl: absoluteUrl('/feed.xml'),
		items: collectSiteRssItems()
	});
}

export function magazineFeedXml(magazineSlug: string): string {
	const mag = getMagazine(magazineSlug);
	return buildRssXml({
		title: `${mag.name} — ${SITE_NAME}`,
		description: `${mag.tagline} Nye numre af ${mag.name}.`,
		link: absoluteUrl(`/${mag.slug}`),
		feedUrl: absoluteUrl(`/${mag.slug}/feed.xml`),
		items: collectMagazineRssItems(mag.slug)
	});
}

export function rssResponse(xml: string): Response {
	return new Response(xml, {
		headers: {
			'Content-Type': 'application/rss+xml; charset=utf-8',
			'Cache-Control': 'public, max-age=1800'
		}
	});
}
