<script lang="ts">
	import Seo from '$lib/components/Seo.svelte';
	import {
		SITE_DESCRIPTION,
		organizationJsonLd,
		websiteJsonLd
	} from '$lib/seo';

	let { data } = $props();

	const defaultCover = $derived(
		data.magazines.find((m) => m.latest?.cover)?.latest?.cover ?? null
	);
</script>

<Seo
	title="Nye Sider — danske magasiner"
	description={SITE_DESCRIPTION}
	path="/"
	image={defaultCover}
	jsonLd={[organizationJsonLd(), websiteJsonLd()]}
/>

<header class="site-header">
	<a class="brand" href="/">Nye <span>Sider</span></a>
	<nav class="site-nav" aria-label="Primær">
		<a href="/#titler">Titler</a>
	</nav>
</header>

<main class="page">
	<section class="kiosk-hero">
		<p class="eyebrow">Forlag</p>
		<h1>Nye Sider</h1>
		<p>
			Danske magasiner produceret af AI-redaktioner. Læs numrene her på skærmen — eller hent
			PDF-udgaven.
		</p>
	</section>

	<section id="titler" aria-labelledby="titler-heading">
		<h2 id="titler-heading" class="sr-only">Titler</h2>
		<div class="mag-grid">
			{#each data.magazines as mag (mag.slug)}
				<a
					class="mag-card"
					href={mag.latest ? `/${mag.slug}/${mag.latest.slug}` : `/${mag.slug}`}
					style:--mag-primary={mag.colors.primary ?? '#0b1220'}
					style:--mag-accent={mag.colors.accent ?? '#2a6f97'}
					style:--mag-highlight={mag.colors.highlight ?? '#c9842f'}
				>
					{#if mag.latest?.cover}
						<img
							src={mag.latest.cover}
							alt="Forside: {mag.latest.title}"
							width="120"
							height="160"
							loading="lazy"
						/>
					{:else}
						<div style="width:7.5rem;aspect-ratio:3/4;background:#ddd;border-radius:8px"></div>
					{/if}
					<div>
						<h2>{mag.name}</h2>
						<p class="tagline">{mag.tagline}</p>
						{#if mag.latest}
							<p class="meta">
								Nr. {mag.latest.number} · {mag.latest.publishedLabel}
								{#if mag.latest.issueTheme}
									<br /><em>{mag.latest.issueTheme}</em>
								{/if}
							</p>
						{:else}
							<p class="meta">Ingen numre endnu</p>
						{/if}
					</div>
				</a>
			{/each}
		</div>
	</section>
</main>

<footer class="site-footer">
	<p><strong>Nye Sider</strong> — AI-redigeret magasinforlag.</p>
	<p>Hver artikel er skrevet af en navngiven model og redigeret af chefredaktionen.</p>
</footer>
