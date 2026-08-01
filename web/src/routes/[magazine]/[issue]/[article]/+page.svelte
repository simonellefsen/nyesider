<script lang="ts">
	import { onMount } from 'svelte';
	import Seo from '$lib/components/Seo.svelte';
	import TrendChart from '$lib/components/TrendChart.svelte';
	import {
		getArticleProgress,
		saveArticleProgress
	} from '$lib/readingState';
	import { absoluteUrl, articleJsonLd, pageTitle } from '$lib/seo';

	let { data } = $props();
	const colors = $derived(data.magazine.colors);
	// Skip drop caps on list/data sections and openers that start with a statistic
	// (Tallet often leads with "30 %" / "324" — ::first-letter would split the number).
	const useDropcap = $derived(
		![
			'Leder',
			'Tallet',
			'Rygtebørsen',
			'Sjov & Spil',
			'Kort & Watt',
			'Vandrehistorier fra vagtstuen'
		].includes(data.article.section) && data.article.order > 1
	);
	const path = $derived(
		`/${data.magazine.slug}/${data.issue.slug}/${data.article.slug}`
	);
	const description = $derived(
		data.article.standfirst ||
			`${data.article.title} — ${data.article.section} i ${data.magazine.name}. Af ${data.article.byline}.`
	);

	let progress = $state(0);

	function persistProgress(pct: number, scrollY: number) {
		saveArticleProgress({
			path: path,
			title: data.article.title,
			magazine: data.magazine.name,
			magazineSlug: data.magazine.slug,
			issueSlug: data.issue.slug,
			articleSlug: data.article.slug,
			progress: pct,
			scrollY
		});
	}

	onMount(() => {
		const articlePath = path;

		// Restore scroll if we left this article mid-read
		const saved = getArticleProgress(articlePath);
		if (saved && saved.scrollY > 80 && saved.progress < 95) {
			requestAnimationFrame(() => {
				window.scrollTo(0, saved.scrollY);
			});
		}

		let lastSaved = 0;
		const onScroll = () => {
			const el = document.documentElement;
			const max = el.scrollHeight - el.clientHeight;
			const pct = max > 0 ? Math.min(100, (el.scrollTop / max) * 100) : 0;
			progress = pct;
			const now = Date.now();
			// Throttle localStorage writes
			if (now - lastSaved > 800) {
				lastSaved = now;
				persistProgress(pct, el.scrollTop);
			}
		};
		onScroll();
		window.addEventListener('scroll', onScroll, { passive: true });

		const onHide = () => {
			const el = document.documentElement;
			const max = el.scrollHeight - el.clientHeight;
			const pct = max > 0 ? Math.min(100, (el.scrollTop / max) * 100) : progress;
			persistProgress(pct, el.scrollTop);
		};
		const onVis = () => {
			if (document.visibilityState === 'hidden') onHide();
		};
		window.addEventListener('pagehide', onHide);
		document.addEventListener('visibilitychange', onVis);

		return () => {
			onHide();
			window.removeEventListener('scroll', onScroll);
			window.removeEventListener('pagehide', onHide);
			document.removeEventListener('visibilitychange', onVis);
		};
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
				<span class="sep" aria-hidden="true">/</span>
				<a href="/{data.magazine.slug}/{data.issue.slug}">Nr. {data.issue.number}</a>
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
				{#if data.article.imageCredit || data.article.imageSource}
					<figcaption class="image-credit">
						{#if data.article.imageSource}
							Kilde:
							<a
								href={data.article.imageSource}
								rel="noopener noreferrer"
								target="_blank"
								>{data.article.imageCredit ?? data.article.imageSource}</a
							>
						{:else}
							Kilde: {data.article.imageCredit}
						{/if}
					</figcaption>
				{/if}
			</figure>
		{/if}

		{#if data.article.body?.length}
			{#each data.article.body as part, i (i)}
				{#if part.type === 'html'}
					<div class="prose" class:dropcap={useDropcap && i === 0}>
						{@html part.html}
					</div>
				{:else if part.type === 'chart'}
					<TrendChart chart={part.chart} />
				{/if}
			{/each}
		{:else}
			<div class="prose" class:dropcap={useDropcap}>
				{@html data.article.html}
			</div>
		{/if}

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
