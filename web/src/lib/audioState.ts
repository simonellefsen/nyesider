/** Client-only listen position. A new audio hash always starts at the beginning. */

const STORAGE_KEY = 'nyesider:listening-v1';

type ListenEntry = {
	contentHash: string;
	currentTime: number;
	updatedAt: number;
};

type ListenState = Record<string, ListenEntry>;

function load(): ListenState {
	if (typeof localStorage === 'undefined') return {};
	try {
		const value = JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '{}') as ListenState;
		return value && typeof value === 'object' ? value : {};
	} catch {
		return {};
	}
}

export function getListenPosition(path: string, contentHash: string): number {
	const item = load()[path];
	return item?.contentHash === contentHash && Number.isFinite(item.currentTime)
		? Math.max(0, item.currentTime)
		: 0;
}

export function saveListenPosition(path: string, contentHash: string, currentTime: number) {
	if (typeof localStorage === 'undefined' || !Number.isFinite(currentTime)) return;
	try {
		const state = load();
		state[path] = { contentHash, currentTime: Math.max(0, currentTime), updatedAt: Date.now() };
		localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
	} catch {
		// Private browsing and storage quota must not break audio playback.
	}
}
