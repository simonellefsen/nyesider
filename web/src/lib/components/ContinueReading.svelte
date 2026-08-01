<script lang="ts">
	import { onMount } from 'svelte';
	import { getContinueReading, type ReadingEntry } from '$lib/readingState';

	let entry = $state<ReadingEntry | null>(null);

	onMount(() => {
		entry = getContinueReading();
	});

	function label(e: ReadingEntry) {
		const pct = Math.round(e.progress);
		if (e.finished) return 'Læs igen';
		if (pct < 8) return 'Fortsæt';
		return `Fortsæt · ${pct} %`;
	}
</script>

{#if entry}
	<section class="continue-reading" aria-labelledby="continue-heading">
		<div class="continue-reading-inner">
			<div>
				<p id="continue-heading" class="continue-kicker">Fortsæt hvor du slap</p>
				<p class="continue-title">
					<a href={entry.path}>{entry.title}</a>
				</p>
				<p class="continue-meta">
					{entry.magazine}
					{#if entry.progress > 0}
						· {Math.round(entry.progress)} % læst
					{/if}
				</p>
			</div>
			<a class="btn btn-primary" href={entry.path}>{label(entry)}</a>
		</div>
		<p class="continue-hint">
			Tip: <strong>Føj til hjemmeskærmen</strong>, så er fremskridtet let at finde igen efter en
			genstart.
		</p>
	</section>
{/if}
