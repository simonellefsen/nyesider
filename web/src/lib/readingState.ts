/** Client-only reading progress (localStorage). Survives restarts on this device. */

const STORAGE_KEY = 'nyesider:reading-v1';
const DISMISS_INSTALL_KEY = 'nyesider:install-banner-dismissed';

export type ReadingEntry = {
	path: string;
	title: string;
	magazine: string;
	magazineSlug: string;
	issueSlug: string;
	articleSlug: string;
	/** 0–100 scroll progress through the page */
	progress: number;
	/** pixels from top when last saved */
	scrollY: number;
	updatedAt: number;
	/** true when progress reached ~read threshold */
	finished?: boolean;
};

export type ReadingState = {
	/** Most recent article being read */
	current: ReadingEntry | null;
	/** path → entry for resume / history */
	byPath: Record<string, ReadingEntry>;
};

function empty(): ReadingState {
	return { current: null, byPath: {} };
}

export function loadReadingState(): ReadingState {
	if (typeof localStorage === 'undefined') return empty();
	try {
		const raw = localStorage.getItem(STORAGE_KEY);
		if (!raw) return empty();
		const parsed = JSON.parse(raw) as ReadingState;
		if (!parsed || typeof parsed !== 'object') return empty();
		return {
			current: parsed.current ?? null,
			byPath: parsed.byPath && typeof parsed.byPath === 'object' ? parsed.byPath : {}
		};
	} catch {
		return empty();
	}
}

function saveReadingState(state: ReadingState) {
	if (typeof localStorage === 'undefined') return;
	try {
		localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
	} catch {
		/* quota / private mode */
	}
}

export function saveArticleProgress(entry: Omit<ReadingEntry, 'updatedAt' | 'finished'> & { finished?: boolean }) {
	const state = loadReadingState();
	const finished = entry.finished ?? entry.progress >= 88;
	const full: ReadingEntry = {
		...entry,
		finished,
		updatedAt: Date.now()
	};
	state.byPath[full.path] = full;
	state.current = full;
	saveReadingState(state);
	return full;
}

export function getArticleProgress(path: string): ReadingEntry | null {
	const state = loadReadingState();
	return state.byPath[path] ?? null;
}

export function getContinueReading(): ReadingEntry | null {
	const state = loadReadingState();
	const cur = state.current;
	if (!cur?.path) return null;
	// Don't surface "continue" if already finished and near end
	if (cur.finished && cur.progress >= 95) {
		// still allow if they only finished — show latest unfinished if any
		const unfinished = Object.values(state.byPath)
			.filter((e) => !e.finished && e.progress > 5)
			.sort((a, b) => b.updatedAt - a.updatedAt)[0];
		return unfinished ?? cur;
	}
	return cur;
}

export function isInstallBannerDismissed(): boolean {
	if (typeof localStorage === 'undefined') return true;
	return localStorage.getItem(DISMISS_INSTALL_KEY) === '1';
}

export function dismissInstallBanner() {
	if (typeof localStorage === 'undefined') return;
	localStorage.setItem(DISMISS_INSTALL_KEY, '1');
}

export function isStandaloneDisplay(): boolean {
	if (typeof window === 'undefined') return false;
	const mq = window.matchMedia('(display-mode: standalone)').matches;
	// iOS Safari
	const nav = window.navigator as Navigator & { standalone?: boolean };
	return mq || nav.standalone === true;
}
