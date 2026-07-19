/** Public site origin — set PUBLIC_SITE_URL for a custom domain. */
export const SITE_URL = (
	(typeof import.meta !== 'undefined' &&
		(import.meta as ImportMeta & { env?: { PUBLIC_SITE_URL?: string } }).env?.PUBLIC_SITE_URL) ||
	'https://nyesider.vercel.app'
).replace(/\/$/, '');

export const SITE_NAME = 'Nye Sider';
export const SITE_DESCRIPTION =
	'Danske magasiner produceret af AI-redaktioner. Læs PULSEN, SPÆNDING m.fl. på skærmen — eller hent PDF-udgaven.';
export const SITE_LOCALE = 'da_DK';
export const SITE_LANGUAGE = 'da';

export function absoluteUrl(path = '/'): string {
	if (!path || path === '/') return SITE_URL + '/';
	if (path.startsWith('http://') || path.startsWith('https://')) return path;
	return SITE_URL + (path.startsWith('/') ? path : `/${path}`);
}

export function absoluteAssetUrl(path: string | null | undefined): string | null {
	if (!path) return null;
	return absoluteUrl(path);
}

export function pageTitle(parts: string[]): string {
	const clean = parts
		.map((p) => p.trim())
		.filter((p) => p && p !== SITE_NAME);
	if (clean.length === 0) return SITE_NAME;
	return [...clean, SITE_NAME].join(' — ');
}

export function organizationJsonLd() {
	return {
		'@context': 'https://schema.org',
		'@type': 'Organization',
		name: SITE_NAME,
		url: SITE_URL,
		description: SITE_DESCRIPTION,
		logo: absoluteUrl('/favicon.svg')
	};
}

export function websiteJsonLd() {
	return {
		'@context': 'https://schema.org',
		'@type': 'WebSite',
		name: SITE_NAME,
		url: SITE_URL,
		description: SITE_DESCRIPTION,
		inLanguage: SITE_LANGUAGE,
		publisher: { '@type': 'Organization', name: SITE_NAME, url: SITE_URL }
	};
}

export function periodicalJsonLd(opts: {
	name: string;
	url: string;
	description: string;
}) {
	return {
		'@context': 'https://schema.org',
		'@type': 'Periodical',
		name: opts.name,
		url: opts.url,
		description: opts.description,
		inLanguage: SITE_LANGUAGE,
		publisher: { '@type': 'Organization', name: SITE_NAME, url: SITE_URL }
	};
}

export function publicationIssueJsonLd(opts: {
	name: string;
	url: string;
	description?: string | null;
	issueNumber: number;
	datePublished: string;
	image?: string | null;
	periodicalName: string;
	periodicalUrl: string;
}) {
	return {
		'@context': 'https://schema.org',
		'@type': 'PublicationIssue',
		name: opts.name,
		url: opts.url,
		issueNumber: opts.issueNumber,
		datePublished: opts.datePublished,
		description: opts.description || undefined,
		image: opts.image ? absoluteUrl(opts.image) : undefined,
		isPartOf: {
			'@type': 'Periodical',
			name: opts.periodicalName,
			url: opts.periodicalUrl
		},
		inLanguage: SITE_LANGUAGE,
		publisher: { '@type': 'Organization', name: SITE_NAME, url: SITE_URL }
	};
}

export function articleJsonLd(opts: {
	headline: string;
	url: string;
	description?: string | null;
	image?: string | null;
	datePublished: string;
	authorName: string;
	section?: string;
	magazineName: string;
	issueName: string;
}) {
	return {
		'@context': 'https://schema.org',
		'@type': 'Article',
		headline: opts.headline,
		url: opts.url,
		mainEntityOfPage: opts.url,
		description: opts.description || undefined,
		image: opts.image ? absoluteUrl(opts.image) : undefined,
		datePublished: opts.datePublished,
		dateModified: opts.datePublished,
		author: {
			'@type': 'Person',
			name: opts.authorName
		},
		articleSection: opts.section,
		isPartOf: {
			'@type': 'PublicationIssue',
			name: opts.issueName,
			isPartOf: {
				'@type': 'Periodical',
				name: opts.magazineName
			}
		},
		inLanguage: SITE_LANGUAGE,
		publisher: {
			'@type': 'Organization',
			name: SITE_NAME,
			url: SITE_URL
		}
	};
}

export function jsonLdScript(data: object | object[]): string {
	return JSON.stringify(data).replace(/</g, '\\u003c');
}
