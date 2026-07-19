<script lang="ts">
	import { onMount } from 'svelte';

	let { data } = $props();
	const colors = $derived(data.magazine.colors);
	const useDropcap = $derived(
		!['Leder', 'Rygtebørsen', 'Sjov & Spil', 'Kort & Watt', 'Vandrehistorier fra vagtstuen'].includes(
			data.article.section
		) && data.article.order > 1
	);

	let progress = $state(0);

	onMount(() => {
		const onScroll = () => {
			const el = document.documentElement;
			const max = el.scrollHeight - el.clientHeight;
			progress = max > 0 ? Math.min(100, (el.scrollTop / max) * 100) : 0;
		};
		onScroll();
		window.addEventListener('scroll', onScroll, { passive: true });
		return () => window.removeEventListener('scroll', onScroll);
	});
</script>

<svelte:head>
	<title>{data.article.title} — {data.magazine.name}</title>
	{#if data.article.standfirst}
		<meta name="description" content={data.article.standfirst} />
	{/if}
	{#if data.article.image}
		<meta property="og:image" content={data.article.image} />
	{/if}
</svelte:head>

<div
	style:--mag-primary={colors.primary ?? '#0b1220'}
	style:--mag-accent={colors.accent ?? '#2a6f97'}
	style:--mag-highlight={colors.highlight ?? '#c9842f'}
>
	<div class="reading-bar">
		<div class="reading-bar-inner">
			<a href="/{data.magazine.slug}">{data.magazine.name}</a>
			<span class="section-label">{data.article.section}</span>
			<a href={data.nav.tocHref}>Indhold</a>
		</div>
		<div class="progress" aria-hidden="true">
			<span style:width="{progress}%"></span>
		</div>
	</div>

	<article class="page-narrow">
		<header class="article-header">
			<p class="eyebrow">{data.article.section}</p>
			<h1>{data.article.title}</h1>
			{#if data.article.standfirst}
				<p class="standfirst">{data.article.standfirst}</p>
			{/if}
			<p class="byline">Af <strong>{data.article.byline}</strong></p>
		</header>

		{#if data.article.image}
			<figure class="article-figure">
				<img src={data.article.image} alt="" width="800" height="450" loading="eager" />
			</figure>
		{/if}

		<div class="prose" class:dropcap={useDropcap}>
			{@html data.article.html}
		</div>

		<nav class="article-nav" aria-label="Artikelnavigation">
			{#if data.nav.prev}
				<a href={data.nav.prev.href}>
					<span class="label">Forrige artikel</span>
					<span class="title">{data.nav.prev.title}</span>
				</a>
			{:else}
				<span></span>
			{/if}
			{#if data.nav.next}
				<a href={data.nav.next.href}>
					<span class="label">Næste artikel</span>
					<span class="title">{data.nav.next.title}</span>
				</a>
			{/if}
			<a class="toc-link" href={data.nav.tocHref}>Til indholdet</a>
		</nav>
	</article>
</div>
