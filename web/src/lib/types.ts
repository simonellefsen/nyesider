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
	/** Short credit shown under the figure (e.g. agency or "AI-genereret"). */
	imageCredit?: string;
	/** URL for the image source / generator; linked from the credit. */
	imageSource?: string;
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
	/** Credit line for the cover image. */
	coverCredit?: string;
	/** URL linked from the cover credit. */
	coverSource?: string;
	images?: string[];
	/** Free-text kolofon for all issue imagery. */
	imageCredits?: string;
	articles: ArticleMeta[];
	productionCostUSD?: number | null;
};

/** Interactive multi-year trend chart (KRAFTEN online, etc.). */
export type ChartSeries = {
	name: string;
	values: number[];
	color?: string;
};

export type ChartSpec = {
	id: string;
	title: string;
	unit?: string;
	note?: string;
	source?: string;
	sourceUrl?: string;
	years: number[];
	series: ChartSeries[];
};

export type ArticleBodyPart =
	| { type: 'html'; html: string }
	| { type: 'chart'; chart: ChartSpec };

export type Article = ArticleMeta & {
	html: string;
	/** Segmented body for interactive charts; falls back to `html` only if empty. */
	body: ArticleBodyPart[];
	charts: ChartSpec[];
	bodyMarkdown: string;
};

export type MagazineSummary = Magazine & {
	latestIssue: Issue | null;
	issueCount: number;
};
