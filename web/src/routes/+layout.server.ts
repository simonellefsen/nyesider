import { listMagazines } from '$lib/server/content';
import type { LayoutServerLoad } from './$types';

/** Shared primary nav for every page. */
export const load: LayoutServerLoad = async () => {
	const magazines = listMagazines().map((m) => ({
		slug: m.slug,
		name: m.name
	}));

	return { navMagazines: magazines };
};
