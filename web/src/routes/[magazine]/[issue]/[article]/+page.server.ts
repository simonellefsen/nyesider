import { error } from '@sveltejs/kit';
import {
	adjacentArticles,
	articleImageUrl,
	coverUrl,
	enrichArticles,
	getArticle,
	getIssue,
	getMagazine,
	listIssueSlugs,
	listMagazines,
	listMagazineSlugs,
	pdfUrl
} from '$lib/server/content';
import type { EntryGenerator, PageServerLoad } from './$types';

export const entries: EntryGenerator = () => {
	const out: { magazine: string; issue: string; article: string }[] = [];
	for (const magazine of listMagazineSlugs()) {
		for (const issueSlug of listIssueSlugs(magazine)) {
			const issue = getIssue(magazine, issueSlug);
			for (const art of issue.articles) {
				out.push({ magazine, issue: issueSlug, article: art.slug });
			}
		}
	}
	return out;
};

export const load: PageServerLoad = async ({ params }) => {
	try {
		const magazine = getMagazine(params.magazine);
		const issue = getIssue(params.magazine, params.issue);
		const article = await getArticle(params.magazine, params.issue, params.article);
		const { prev, next } = adjacentArticles(issue, params.article);

		const sortedArticles = [...issue.articles].sort((a, b) => a.order - b.order);
		const positionIndex = sortedArticles.findIndex((a) => a.slug === params.article);

		const otherMagazines = listMagazines()
			.filter((m) => m.slug !== params.magazine && m.latestIssue)
			.map((m) => ({
				slug: m.slug,
				name: m.name,
				tagline: m.tagline,
				issueHref: `/${m.slug}/${m.latestIssue!.slug}`,
				cover: coverUrl(m.slug, m.latestIssue!)
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
				pdf: pdfUrl(params.magazine, issue)
			},
			article: {
				slug: article.slug,
				title: article.title,
				section: article.section,
				byline: article.byline,
				standfirst: article.standfirst ?? null,
				html: article.html,
				image: articleImageUrl(params.magazine, params.issue, article.image),
				order: article.order
			},
			articles: enrichArticles(params.magazine, issue),
			nav: {
				prev: prev
					? {
							slug: prev.slug,
							title: prev.title,
							href: `/${params.magazine}/${params.issue}/${prev.slug}`
						}
					: null,
				next: next
					? {
							slug: next.slug,
							title: next.title,
							href: `/${params.magazine}/${params.issue}/${next.slug}`
						}
					: null,
				tocHref: `/${params.magazine}/${params.issue}`,
				position: { index: positionIndex + 1, total: sortedArticles.length }
			},
			otherMagazines
		};
	} catch {
		error(404, 'Artikel ikke fundet');
	}
};
