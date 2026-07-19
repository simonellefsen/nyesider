import { error } from '@sveltejs/kit';
import {
	coverUrl,
	enrichArticles,
	formatDanishDate,
	getIssue,
	getMagazine,
	listIssueSlugs,
	listMagazineSlugs,
	pdfUrl
} from '$lib/server/content';
import type { EntryGenerator, PageServerLoad } from './$types';

export const entries: EntryGenerator = () => {
	const out: { magazine: string; issue: string }[] = [];
	for (const magazine of listMagazineSlugs()) {
		for (const issue of listIssueSlugs(magazine)) {
			out.push({ magazine, issue });
		}
	}
	return out;
};

export const load: PageServerLoad = async ({ params }) => {
	try {
		const magazine = getMagazine(params.magazine);
		const issue = getIssue(params.magazine, params.issue);
		const articles = enrichArticles(params.magazine, issue);

		return {
			magazine: {
				slug: magazine.slug,
				name: magazine.name,
				colors: magazine.theme.colors
			},
			issue: {
				slug: issue.slug,
				title: issue.title,
				number: issue.number,
				published: issue.published,
				publishedLabel: formatDanishDate(issue.published),
				issueTheme: issue.issueTheme ?? null,
				cover: coverUrl(params.magazine, issue),
				pdf: pdfUrl(params.magazine, issue)
			},
			articles
		};
	} catch {
		error(404, 'Nummer ikke fundet');
	}
};
