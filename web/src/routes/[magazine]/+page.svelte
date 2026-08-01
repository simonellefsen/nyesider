<script lang="ts">
	import Seo from '$lib/components/Seo.svelte';
	import SiteFooter from '$lib/components/SiteFooter.svelte';
	import SiteHeader from '$lib/components/SiteHeader.svelte';
	import { absoluteUrl, pageTitle, periodicalJsonLd } from '$lib/seo';

	let { data } = $props();
	const colors = $derived(data.magazine.colors);
	const path = $derived(`/${data.magazine.slug}`);
	const cover = $derived(data.issues.find((i) => i.cover)?.cover ?? null);
	const description = $derived(
		data.magazine.tagline +
			(data.magazine.audience ? ` ${data.magazine.audience}.` : '')
	);
	const latest = $derived(data.issues[0] ?? null);
	const feedPath = $derived(`/${data.magazine.slug}/feed.xml`);
</script>

<svelte:head>
	<link
		rel="alternate"
		type="application/rss+xml"
		title="{data.magazine.name} — Nye Sider"
		href={feedPath}
	/>
</svelte:head>

<Seo
	title={pageTitle([data.magazine.name])}
	description={description}
	path={path}
	image={cover}
	jsonLd={periodicalJsonLd({
		name: data.magazine.name,
		url: absoluteUrl(path),
		description: data.magazine.tagline
	})}
/>

<div
	style:--mag-primary={colors.primary ?? '#0b1220'}
	style:--mag-accent={colors.accent ?? '#2a6f97'}
	style:--mag-highlight={colors.highlight ?? '#c9842f'}
>
	<SiteHeader
		magazines={data.navMagazines}
		currentSlug={data.magazine.slug}
		crumbs={[{ label: 'Nye Sider', href: '/' }, { label: data.magazine.name }]}
	/>

	<main class="page">
		<section class="mag-hero">
			{#if cover}
				<div class="cover">
					<a href={latest ? `/${data.magazine.slug}/${latest.slug}` : path}>
						<img
							src={cover}
							alt="Seneste forside: {latest?.title ?? data.magazine.name}"
							width="360"
							height="480"
						/>
					</a>
				</div>
			{/if}
			<div>
				<p class="eyebrow">Magasin</p>
				<h1 style="margin:0 0 0.5rem;font-size:clamp(2rem,6vw,3rem);letter-spacing:0.04em">
					{data.magazine.name}
				</h1>
				<p style="margin:0 0 0.75rem;color:var(--ink-muted);max-width:36rem">
					{data.magazine.tagline}
				</p>
				{#if data.magazine.audience}
					<p style="margin:0 0 1rem;font-size:0.9rem;color:var(--ink-muted);max-width:36rem">
						{data.magazine.audience}
					</p>
				{/if}
				{#if latest}
					<div class="mag-card-actions" style="margin-top:0.25rem">
						<a class="btn btn-primary" href="/{data.magazine.slug}/{latest.slug}">
							Læs nr. {latest.number}
						</a>
						<a class="btn btn-ghost" href="/{data.magazine.slug}/feed.xml" title="RSS for {data.magazine.name}">
							RSS
						</a>
					</div>
				{/if}
			</div>
		</section>

		<section aria-labelledby="arkiv-heading">
			<h2 id="arkiv-heading" class="section-heading">Numre</h2>
			<ul class="issue-list">
				{#each data.issues as issue (issue.slug)}
					<li>
						<a href="/{data.magazine.slug}/{issue.slug}">
							{#if issue.cover}
								<img src={issue.cover} alt="" width="56" height="75" loading="lazy" />
							{:else}
								<div class="issue-thumb-placeholder" aria-hidden="true">
									<span>Nr.&nbsp;{issue.number}</span>
								</div>
							{/if}
							<div>
								<strong>{issue.title}</strong>
								<div style="font-size:0.88rem;color:var(--ink-muted);margin-top:0.2rem">
									{issue.publishedLabel}
									{#if issue.issueTheme}
										· <em>{issue.issueTheme}</em>
									{/if}
									· {issue.articleCount} artikler
								</div>
							</div>
						</a>
					</li>
				{/each}
			</ul>
		</section>
	</main>

	<SiteFooter
		magazines={data.navMagazines}
		note={`Alle numre af ${data.magazine.name} · Nye Sider`}
	/>
</div>
