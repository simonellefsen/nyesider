import { siteFeedXml, rssResponse } from '$lib/server/rss';

export const prerender = true;

export function GET() {
	return rssResponse(siteFeedXml());
}
