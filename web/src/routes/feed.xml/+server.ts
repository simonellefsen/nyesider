import { siteFeedXml, rssResponse } from '$lib/server/rss';

/** Prerendered to static/feed.xml on Vercel (also at /feed.xml). */
export const prerender = true;
export const trailingSlash = 'never';

export function GET() {
	return rssResponse(siteFeedXml());
}
