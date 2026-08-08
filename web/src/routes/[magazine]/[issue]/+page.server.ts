import { error } from '@sveltejs/kit';
import {
	coverUrl,
	enrichArticles,
	formatDanishDate,
	getIssue,
	getMagazine,
	listIssues,
	listMagazineSlugs,
	pdfUrl
} from '$lib/server/content';
import { isNarratableArticle } from '$lib/audioPolicy';
import type { EntryGenerator, PageServerLoad } from './$types';

export const entries: EntryGenerator = () => {
	const out: { magazine: string; issue: string }[] = [];
	for (const magazine of listMagazineSlugs()) {
		// Only published issues are prerendered / public.
		for (const issue of listIssues(magazine)) {
			out.push({ magazine, issue: issue.slug });
		}
	}
	return out;
};

export const load: PageServerLoad = async ({ params }) => {
	try {
		const magazine = getMagazine(params.magazine);
		const issue = getIssue(params.magazine, params.issue);
		if (issue.status !== 'published') error(404, 'Nummer ikke fundet');
		const articles = enrichArticles(params.magazine, issue);
		const listeningTracks = articles
			.filter((article) => article.audio && isNarratableArticle(article.section))
			.map((article) => ({
				slug: article.slug,
				href: article.href,
				title: article.title,
				section: article.section,
				audio: article.audio!
			}));

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
				coverCredit: issue.coverCredit ?? null,
				coverSource: issue.coverSource ?? null,
				imageCredits: issue.imageCredits ?? null,
				pdf: pdfUrl(params.magazine, issue)
			},
			articles,
			listeningTracks
		};
	} catch {
		error(404, 'Nummer ikke fundet');
	}
};
