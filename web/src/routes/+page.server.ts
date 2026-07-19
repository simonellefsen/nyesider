import { coverUrl, formatDanishDate, listMagazines } from '$lib/server/content';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const magazines = listMagazines().map((m) => ({
		slug: m.slug,
		name: m.name,
		tagline: m.tagline,
		colors: m.theme.colors,
		issueCount: m.issueCount,
		latest: m.latestIssue
			? {
					slug: m.latestIssue.slug,
					title: m.latestIssue.title,
					number: m.latestIssue.number,
					published: m.latestIssue.published,
					publishedLabel: formatDanishDate(m.latestIssue.published),
					issueTheme: m.latestIssue.issueTheme ?? null,
					cover: coverUrl(m.slug, m.latestIssue)
				}
			: null
	}));

	return { magazines };
};
