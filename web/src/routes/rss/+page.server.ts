import { listMagazines } from '$lib/server/content';
import { absoluteUrl } from '$lib/seo';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const magazines = listMagazines().map((m) => ({
		slug: m.slug,
		name: m.name,
		tagline: m.tagline,
		feedUrl: absoluteUrl(`/${m.slug}/feed.xml`),
		feedPath: `/${m.slug}/feed.xml`
	}));

	return {
		siteFeedUrl: absoluteUrl('/feed.xml'),
		siteFeedPath: '/feed.xml',
		magazines
	};
};
