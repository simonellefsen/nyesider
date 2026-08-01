import { coverUrl, formatDanishDate, listIssues, listMagazines } from '$lib/server/content';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const magazines = listMagazines().map((m) => {
		const issues = listIssues(m.slug);
		const latest = issues[0] ?? null;
		// Prefer latest cover; if nr. N has no art yet, fall back to the newest issue that has one.
		const cover =
			(latest && coverUrl(m.slug, latest)) ||
			issues.map((i) => coverUrl(m.slug, i)).find((c) => !!c) ||
			null;

		return {
			slug: m.slug,
			name: m.name,
			tagline: m.tagline,
			colors: m.theme.colors,
			issueCount: m.issueCount,
			latest: latest
				? {
						slug: latest.slug,
						title: latest.title,
						number: latest.number,
						published: latest.published,
						publishedLabel: formatDanishDate(latest.published),
						issueTheme: latest.issueTheme ?? null,
						cover,
						href: `/${m.slug}/${latest.slug}`,
						// true when we are showing an older cover as stand-in
						coverIsFallback: !coverUrl(m.slug, latest) && !!cover
					}
				: null,
			archiveHref: `/${m.slug}`
		};
	});

	return { magazines };
};
