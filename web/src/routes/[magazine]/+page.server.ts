import { error } from '@sveltejs/kit';
import {
	coverUrl,
	formatDanishDate,
	getMagazine,
	listIssues,
	listMagazineSlugs
} from '$lib/server/content';
import type { EntryGenerator, PageServerLoad } from './$types';

export const entries: EntryGenerator = () => {
	return listMagazineSlugs().map((magazine) => ({ magazine }));
};

export const load: PageServerLoad = async ({ params }) => {
	try {
		const magazine = getMagazine(params.magazine);
		const issues = listIssues(params.magazine).map((issue) => ({
			slug: issue.slug,
			title: issue.title,
			number: issue.number,
			published: issue.published,
			publishedLabel: formatDanishDate(issue.published),
			issueTheme: issue.issueTheme ?? null,
			cover: coverUrl(params.magazine, issue),
			articleCount: issue.articles.length
		}));

		return {
			magazine: {
				slug: magazine.slug,
				name: magazine.name,
				tagline: magazine.tagline,
				audience: magazine.audience,
				colors: magazine.theme.colors
			},
			issues
		};
	} catch {
		error(404, 'Magasin ikke fundet');
	}
};
