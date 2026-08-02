<script lang="ts">
	import { onMount } from 'svelte';
	import type { ArticleAudio } from '$lib/types';
	import { getListenPosition, saveListenPosition } from '$lib/audioState';

	let { audio, title, magazine, articlePath }: {
		audio: ArticleAudio;
		title: string;
		magazine: string;
		articlePath: string;
	} = $props();

	let element: HTMLAudioElement | undefined = $state();
	let playing = $state(false);
	let currentTime = $state(0);
	let duration = $state(0);
	let speed = $state(1);
	let errorMessage = $state('');
	let restored = false;

	const availableDuration = $derived(duration || audio.durationSeconds);
	const percentage = $derived(availableDuration > 0 ? Math.min(100, (currentTime / availableDuration) * 100) : 0);
	const progressLabel = $derived(`${formatTime(currentTime)} af ${formatTime(availableDuration)}`);

	function formatTime(value: number) {
		const seconds = Math.max(0, Math.round(value || 0));
		return `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, '0')}`;
	}

	function persist() {
		if (element) saveListenPosition(articlePath, audio.contentHash, element.currentTime);
	}

	async function togglePlayback() {
		if (!element) return;
		errorMessage = '';
		try {
			if (element.paused) await element.play();
			else element.pause();
		} catch {
			errorMessage = 'Lyden kunne ikke startes. Tjek din forbindelse og prøv igen.';
		}
	}

	function seekTo(value: number) {
		if (!element || !Number.isFinite(value)) return;
		element.currentTime = Math.min(Math.max(0, value), availableDuration || 0);
		currentTime = element.currentTime;
		persist();
	}

	function skip(seconds: number) {
		seekTo((element?.currentTime ?? 0) + seconds);
	}

	function changeSpeed() {
		const options = [0.75, 1, 1.25, 1.5];
		speed = options[(options.indexOf(speed) + 1) % options.length];
		if (element) element.playbackRate = speed;
	}

	function setMediaSession() {
		if (!('mediaSession' in navigator)) return;
		navigator.mediaSession.metadata = new MediaMetadata({ title, artist: magazine, album: 'Nye Sider' });
		navigator.mediaSession.setActionHandler('play', () => void element?.play());
		navigator.mediaSession.setActionHandler('pause', () => element?.pause());
		navigator.mediaSession.setActionHandler('seekbackward', () => skip(-15));
		navigator.mediaSession.setActionHandler('seekforward', () => skip(15));
		navigator.mediaSession.setActionHandler('seekto', (details) => {
			if (typeof details.seekTime === 'number') seekTo(details.seekTime);
		});
	}

	onMount(() => {
		setMediaSession();
		return () => persist();
	});
</script>

<section class="audio-player" aria-label="Lyt til artiklen">
	<div class="audio-heading">
		<div>
			<p class="audio-kicker">Lyt til artiklen</p>
			<p class="audio-note">AI-genereret oplæsning</p>
		</div>
		<span class="duration">{formatTime(availableDuration)}</span>
	</div>

	<audio
		bind:this={element}
		src={audio.url}
		preload="metadata"
		onloadedmetadata={() => {
				duration = element?.duration || audio.durationSeconds;
			if (!restored && element) {
				restored = true;
				const saved = getListenPosition(articlePath, audio.contentHash);
				if (saved > 1 && saved < availableDuration - 2) {
					element.currentTime = saved;
					currentTime = saved;
				}
			}
		}}
		onplay={() => (playing = true)}
		onpause={() => { playing = false; persist(); }}
		onended={() => { playing = false; persist(); }}
		ontimeupdate={() => {
			currentTime = element?.currentTime ?? 0;
			if (Math.round(currentTime) % 5 === 0) persist();
		}}
		onerror={() => (errorMessage = 'Lydfilen er ikke tilgængelig lige nu.')}
	></audio>

	<div class="audio-controls">
		<button type="button" class="play" onclick={togglePlayback} aria-label={playing ? 'Sæt lyd på pause' : 'Afspil artikel'}>{playing ? 'Ⅱ' : '▶'}</button>
		<button type="button" class="skip" onclick={() => skip(-15)} aria-label="15 sekunder tilbage">↶ 15</button>
		<input type="range" min="0" max={availableDuration || 0} step="0.1" value={currentTime} aria-label="Afspilningsposition" aria-valuetext={progressLabel} style:--progress={`${percentage}%`} oninput={(event) => seekTo(Number(event.currentTarget.value))} />
		<button type="button" class="skip" onclick={() => skip(15)} aria-label="15 sekunder frem">15 ↷</button>
		<button type="button" class="speed" onclick={changeSpeed} aria-label="Skift afspilningshastighed">{speed}×</button>
	</div>
	<div class="audio-time" aria-live="off"><span>{formatTime(currentTime)}</span><span>{formatTime(availableDuration)}</span></div>
	{#if errorMessage}<p class="audio-error" role="status">{errorMessage}</p>{/if}
</section>

<style>
	.audio-player { margin-top: 1.5rem; padding: 1rem 1.1rem; border: 1px solid color-mix(in srgb, var(--mag-primary, #0b1220) 22%, transparent); border-radius: 0.8rem; background: color-mix(in srgb, var(--mag-primary, #0b1220) 5%, white); }
	.audio-heading, .audio-controls, .audio-time { display: flex; align-items: center; }
	.audio-heading { justify-content: space-between; gap: 1rem; }
	.audio-kicker, .audio-note, .audio-time, .duration { margin: 0; }
	.audio-kicker { font: 700 0.95rem/1.1 var(--font-sans, system-ui); }
	.audio-note, .duration, .audio-time { color: #58616a; font: 0.8rem/1.3 var(--font-sans, system-ui); }
	.audio-controls { gap: 0.45rem; margin-top: 0.85rem; }
	button { min-height: 2.4rem; border: 0; border-radius: 999px; color: #fff; background: var(--mag-primary, #0b1220); cursor: pointer; font: 700 0.78rem/1 var(--font-sans, system-ui); }
	.play { width: 2.4rem; font-size: 1.05rem; }
	.skip, .speed { padding: 0 0.65rem; }
	input[type='range'] { appearance: none; flex: 1; min-width: 3.5rem; height: 0.45rem; border-radius: 999px; background: linear-gradient(to right, var(--mag-primary, #0b1220) var(--progress), #d6dbe0 var(--progress)); cursor: pointer; }
	input[type='range']::-webkit-slider-thumb { appearance: none; width: 0.95rem; height: 0.95rem; border-radius: 50%; background: var(--mag-primary, #0b1220); }
	.audio-time { justify-content: space-between; margin: 0.35rem 5.2rem 0 2.9rem; }
	.audio-error { margin: 0.65rem 0 0; color: #a72525; font-size: 0.86rem; }
	@media (max-width: 430px) { .audio-controls { gap: 0.3rem; } .skip { padding: 0 0.45rem; font-size: 0.7rem; } .speed { padding: 0 0.45rem; } .audio-time { margin-right: 3.6rem; } }
</style>
