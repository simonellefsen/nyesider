import { error } from '@sveltejs/kit';
import {
	adjacentArticles,
	articleImageUrl,
	getArticle,
	getIssue,
	getMagazine,
	listIssueSlugs,
	listMagazineSlugs
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
				published: issue.published
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
				tocHref: `/${params.magazine}/${params.issue}`
			}
		};
	} catch {
		error(404, 'Artikel ikke fundet');
	}
};
