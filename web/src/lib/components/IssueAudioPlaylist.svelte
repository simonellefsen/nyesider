<script lang="ts">
	import { onMount, tick } from 'svelte';
	import type { ArticleAudio } from '$lib/types';

	type PlaylistTrack = {
		slug: string;
		href: string;
		title: string;
		section: string;
		audio: ArticleAudio;
	};

	let { tracks, magazine }: { tracks: PlaylistTrack[]; magazine: string } = $props();

	let element: HTMLAudioElement | undefined = $state();
	let activeIndex = $state(0);
	let playing = $state(false);
	let currentTime = $state(0);
	let duration = $state(0);
	let speed = $state(1);
	let errorMessage = $state('');
	let completed = $state(false);

	const active = $derived(tracks[activeIndex]);
	const availableDuration = $derived(duration || active.audio.durationSeconds);
	const percentage = $derived(availableDuration > 0 ? Math.min(100, (currentTime / availableDuration) * 100) : 0);
	const progressLabel = $derived(`${formatTime(currentTime)} af ${formatTime(availableDuration)}`);

	function formatTime(value: number) {
		const seconds = Math.max(0, Math.round(value || 0));
		return `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, '0')}`;
	}

	function setMediaSession() {
		if (!('mediaSession' in navigator) || !('MediaMetadata' in window)) return;
		navigator.mediaSession.metadata = new MediaMetadata({
			title: active.title,
			artist: magazine,
			album: `Nye Sider · ${tracks.length} artikler`
		});
		navigator.mediaSession.setActionHandler('play', () => void element?.play());
		navigator.mediaSession.setActionHandler('pause', () => element?.pause());
		navigator.mediaSession.setActionHandler('seekbackward', () => skip(-15));
		navigator.mediaSession.setActionHandler('seekforward', () => skip(15));
		navigator.mediaSession.setActionHandler('seekto', (details) => {
			if (typeof details.seekTime === 'number') seekTo(details.seekTime);
		});
	}

	async function playActive() {
		if (!element) return;
		errorMessage = '';
		try {
			await element.play();
		} catch {
			errorMessage = 'Lyden kunne ikke startes. Tjek din forbindelse og prøv igen.';
		}
	}

	async function togglePlayback() {
		if (!element) return;
		if (element.paused) await playActive();
		else element.pause();
	}

	function seekTo(value: number) {
		if (!element || !Number.isFinite(value)) return;
		element.currentTime = Math.min(Math.max(0, value), availableDuration || 0);
		currentTime = element.currentTime;
	}

	function skip(seconds: number) {
		seekTo((element?.currentTime ?? 0) + seconds);
	}

	function changeSpeed() {
		const options = [0.75, 1, 1.25, 1.5];
		speed = options[(options.indexOf(speed) + 1) % options.length];
		if (element) element.playbackRate = speed;
	}

	async function activate(index: number, shouldPlay = true) {
		activeIndex = index;
		completed = false;
		currentTime = 0;
		duration = 0;
		await tick();
		if (element) {
			element.playbackRate = speed;
			element.currentTime = 0;
		}
		setMediaSession();
		if (shouldPlay) await playActive();
	}

	async function handleEnded() {
		if (activeIndex + 1 >= tracks.length) {
			playing = false;
			completed = true;
			return;
		}
		await activate(activeIndex + 1);
	}

	onMount(() => setMediaSession());
</script>

<section class="playlist" aria-label="Lyt til alle artikler">
	<div class="playlist-heading">
		<div>
			<p class="playlist-kicker">Lyt til alle artikler</p>
			<p class="playlist-note">AI-genereret oplæsning · fortsætter automatisk</p>
		</div>
		<span class="playlist-count">{tracks.length} artikler</span>
	</div>

	<p class="playlist-now" aria-live="polite">
		{#if completed}
			Alle artikler er afspillet.
		{:else}
			Spiller {activeIndex + 1} af {tracks.length}: <a href={active.href}>{active.title}</a>
		{/if}
	</p>

	<audio
		bind:this={element}
		src={active.audio.url}
		preload="metadata"
		onloadedmetadata={() => {
			duration = element?.duration || active.audio.durationSeconds;
			setMediaSession();
		}}
		onplay={() => (playing = true)}
		onpause={() => (playing = false)}
		onended={handleEnded}
		ontimeupdate={() => (currentTime = element?.currentTime ?? 0)}
		onerror={() => (errorMessage = 'Lydfilen er ikke tilgængelig lige nu.')}
	></audio>

	<div class="playlist-controls">
		<button type="button" class="play" onclick={togglePlayback} aria-label={playing ? 'Sæt lyd på pause' : 'Start alle artikler'}>{playing ? 'Ⅱ' : '▶'}</button>
		<button type="button" class="skip" onclick={() => skip(-15)} aria-label="15 sekunder tilbage">↶ 15</button>
		<input type="range" min="0" max={availableDuration || 0} step="0.1" value={currentTime} aria-label="Afspilningsposition" aria-valuetext={progressLabel} style:--progress={`${percentage}%`} oninput={(event) => seekTo(Number(event.currentTarget.value))} />
		<button type="button" class="skip" onclick={() => skip(15)} aria-label="15 sekunder frem">15 ↷</button>
		<button type="button" class="speed" onclick={changeSpeed} aria-label="Skift afspilningshastighed">{speed}×</button>
	</div>
	<div class="playlist-time" aria-live="off"><span>{formatTime(currentTime)}</span><span>{formatTime(availableDuration)}</span></div>

	<ol class="playlist-tracks">
		{#each tracks as track, index (track.slug)}
			<li class:active={index === activeIndex}>
				<button type="button" onclick={() => activate(index)} aria-label={`Afspil ${track.title}`}>{index === activeIndex && playing ? 'Ⅱ' : '▶'}</button>
				<a href={track.href}>{track.title}</a>
			</li>
		{/each}
	</ol>
	{#if errorMessage}<p class="playlist-error" role="status">{errorMessage}</p>{/if}
</section>

<style>
	.playlist { margin-top: 1rem; padding: 1rem 1.1rem; border: 1px solid color-mix(in srgb, var(--mag-primary, #0b1220) 22%, transparent); border-radius: 0.8rem; background: color-mix(in srgb, var(--mag-primary, #0b1220) 5%, white); }
	.playlist-heading, .playlist-controls, .playlist-time { display: flex; align-items: center; }
	.playlist-heading { justify-content: space-between; gap: 1rem; }
	.playlist-kicker, .playlist-note, .playlist-now, .playlist-time, .playlist-count { margin: 0; }
	.playlist-kicker { font: 700 0.95rem/1.1 var(--font-sans, system-ui); }
	.playlist-note, .playlist-count, .playlist-time { color: #58616a; font: 0.8rem/1.3 var(--font-sans, system-ui); }
	.playlist-now { margin-top: 0.7rem; font-size: 0.9rem; }
	.playlist-now a, .playlist-tracks a { color: inherit; }
	.playlist-controls { gap: 0.45rem; margin-top: 0.85rem; }
	button { min-height: 2.4rem; border: 0; border-radius: 999px; color: #fff; background: var(--mag-primary, #0b1220); cursor: pointer; font: 700 0.78rem/1 var(--font-sans, system-ui); }
	.play { width: 2.4rem; font-size: 1.05rem; }
	.skip, .speed { padding: 0 0.65rem; }
	input[type='range'] { appearance: none; flex: 1; min-width: 3.5rem; height: 0.45rem; border-radius: 999px; background: linear-gradient(to right, var(--mag-primary, #0b1220) var(--progress), #d6dbe0 var(--progress)); cursor: pointer; }
	input[type='range']::-webkit-slider-thumb { appearance: none; width: 0.95rem; height: 0.95rem; border-radius: 50%; background: var(--mag-primary, #0b1220); }
	.playlist-time { justify-content: space-between; margin: 0.35rem 5.2rem 0 2.9rem; }
	.playlist-tracks { display: grid; gap: 0.3rem; margin: 0.9rem 0 0; padding-left: 1.4rem; font-size: 0.87rem; }
	.playlist-tracks li { padding: 0.15rem 0; }
	.playlist-tracks li.active { font-weight: 700; }
	.playlist-tracks button { min-height: 1.65rem; width: 1.65rem; margin-right: 0.45rem; font-size: 0.65rem; }
	.playlist-error { margin: 0.65rem 0 0; color: #a72525; font-size: 0.86rem; }
	@media (max-width: 430px) { .playlist-controls { gap: 0.3rem; } .skip { padding: 0 0.45rem; font-size: 0.7rem; } .speed { padding: 0 0.45rem; } .playlist-time { margin-right: 3.6rem; } }
</style>
