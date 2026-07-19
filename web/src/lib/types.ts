export type ThemeColors = {
	primary: string;
	accent: string;
	highlight?: string;
};

export type Magazine = {
	slug: string;
	name: string;
	tagline: string;
	language: string;
	audience?: string;
	sections: string[];
	theme: {
		colors: ThemeColors;
	};
};

export type ArticleMeta = {
	slug: string;
	file: string;
	order: number;
	title: string;
	section: string;
	byline: string;
	standfirst?: string;
	image?: string;
};

export type Issue = {
	magazine: string;
	slug: string; // folder name, e.g. 2026-07-nr1
	number: number;
	title: string;
	issueTheme?: string;
	published: string;
	status: string;
	pdf?: string;
	cover?: string;
	images?: string[];
	articles: ArticleMeta[];
	productionCostUSD?: number | null;
};

export type Article = ArticleMeta & {
	html: string;
	bodyMarkdown: string;
};

export type MagazineSummary = Magazine & {
	latestIssue: Issue | null;
	issueCount: number;
};
