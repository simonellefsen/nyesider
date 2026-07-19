<script lang="ts">
	import { onMount } from 'svelte';
	import Seo from '$lib/components/Seo.svelte';
	import { absoluteUrl, articleJsonLd, pageTitle } from '$lib/seo';

	let { data } = $props();
	const colors = $derived(data.magazine.colors);
	const useDropcap = $derived(
		!['Leder', 'Rygtebørsen', 'Sjov & Spil', 'Kort & Watt', 'Vandrehistorier fra vagtstuen'].includes(
			data.article.section
		) && data.article.order > 1
	);
	const path = $derived(
		`/${data.magazine.slug}/${data.issue.slug}/${data.article.slug}`
	);
	const description = $derived(
		data.article.standfirst ||
			`${data.article.title} — ${data.article.section} i ${data.magazine.name}. Af ${data.article.byline}.`
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

	let tocDialog: HTMLDialogElement | undefined = $state();
	function openToc() {
		tocDialog?.showModal();
	}
	function closeToc() {
		tocDialog?.close();
	}
</script>

<Seo
	title={pageTitle([data.article.title, data.magazine.name])}
	description={description}
	path={path}
	image={data.article.image}
	type="article"
	publishedTime={data.issue.published}
	author={data.article.byline}
	jsonLd={articleJsonLd({
		headline: data.article.title,
		url: absoluteUrl(path),
		description: data.article.standfirst,
		image: data.article.image,
		datePublished: data.issue.published,
		authorName: data.article.byline,
		section: data.article.section,
		magazineName: data.magazine.name,
		issueName: data.issue.title
	})}
/>

<div
	style:--mag-primary={colors.primary ?? '#0b1220'}
	style:--mag-accent={colors.accent ?? '#2a6f97'}
	style:--mag-highlight={colors.highlight ?? '#c9842f'}
>
	<div class="reading-bar">
		<div class="reading-bar-inner">
			<div class="crumb">
				<a href="/">Nye Sider</a>
				<span class="sep" aria-hidden="true">/</span>
				<a href="/{data.magazine.slug}">{data.magazine.name}</a>
			</div>
			<span class="section-label">{data.article.section}</span>
			<div class="reading-bar-actions">
				<span class="position">{data.nav.position.index}/{data.nav.position.total}</span>
				<button type="button" class="toc-toggle" onclick={openToc}>Indhold</button>
			</div>
		</div>
		<div class="progress" aria-hidden="true">
			<span style:width="{progress}%"></span>
		</div>
	</div>

	<dialog
		bind:this={tocDialog}
		class="toc-sheet"
		onclick={(e) => {
			if (e.target === tocDialog) closeToc();
		}}
	>
		<div class="toc-sheet-head">
			<p>{data.issue.title}</p>
			<button type="button" onclick={closeToc} aria-label="Luk indholdsfortegnelse">✕</button>
		</div>
		<ol>
			{#each data.articles as a (a.slug)}
				<li class:current={a.slug === data.article.slug}>
					<a href={a.href} onclick={closeToc}>
						<span class="section">{a.section}</span>
						<span class="title"
							><span class="num">{String(a.order).padStart(2, '0')}</span>{a.title}</span
						>
					</a>
				</li>
			{/each}
		</ol>
	</dialog>

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
				<img
					src={data.article.image}
					alt=""
					width="800"
					height="450"
					loading="eager"
				/>
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
			{:else}
				<a href={data.nav.tocHref}>
					<span class="label">Sidste artikel</span>
					<span class="title">Til forsiden af {data.issue.title}</span>
				</a>
			{/if}
			<a class="toc-link" href={data.nav.tocHref}>Til indholdet</a>
		</nav>

		{#if !data.nav.next}
			<section class="backcover" aria-labelledby="backcover-heading">
				<p id="backcover-heading" class="eyebrow">Det var {data.issue.title}</p>
				{#if data.issue.pdf}
					<a class="pdf-link" href={data.issue.pdf} download>↓ Hent PDF-udgaven</a>
				{/if}
				{#if data.otherMagazines.length}
					<div class="also-reading">
						<p>Læs også</p>
						{#each data.otherMagazines as m (m.slug)}
							<a class="mag-card-mini" href={m.issueHref}>
								{#if m.cover}
									<img src={m.cover} alt="" width="64" height="85" loading="lazy" />
								{/if}
								<span>
									<strong>{m.name}</strong>
									<small>{m.tagline}</small>
								</span>
							</a>
						{/each}
					</div>
				{/if}
			</section>
		{/if}
	</article>
</div>
