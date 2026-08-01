import { error } from '@sveltejs/kit';
import { listMagazineSlugs } from '$lib/server/content';
import { magazineFeedXml, rssResponse } from '$lib/server/rss';
import type { EntryGenerator } from './$types';

export const prerender = true;

export const entries: EntryGenerator = () =>
	listMagazineSlugs().map((magazine) => ({ magazine }));

export function GET({ params }) {
	if (!listMagazineSlugs().includes(params.magazine)) {
		error(404, 'Ukendt magasin');
	}
	return rssResponse(magazineFeedXml(params.magazine));
}
