<script lang="ts">
	import Seo from '$lib/components/Seo.svelte';
	import SiteFooter from '$lib/components/SiteFooter.svelte';
	import SiteHeader from '$lib/components/SiteHeader.svelte';
	import { SITE_DESCRIPTION, organizationJsonLd, websiteJsonLd } from '$lib/seo';

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

<SiteHeader magazines={data.navMagazines} />

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
		<h2 id="titler-heading" class="section-heading">Titler</h2>
		<div class="mag-grid">
			{#each data.magazines as mag (mag.slug)}
				<article
					class="mag-card mag-card--panel"
					style:--mag-primary={mag.colors.primary ?? '#0b1220'}
					style:--mag-accent={mag.colors.accent ?? '#2a6f97'}
					style:--mag-highlight={mag.colors.highlight ?? '#c9842f'}
				>
					<a
						class="mag-card-cover"
						href={mag.latest?.href ?? mag.archiveHref}
						aria-label={mag.latest
							? `Læs ${mag.name} nr. ${mag.latest.number}`
							: `Gå til ${mag.name}`}
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
							<div class="mag-card-placeholder" aria-hidden="true">
								<span>{mag.name.slice(0, 1)}</span>
							</div>
						{/if}
					</a>

					<div class="mag-card-body">
						<h2>
							<a href={mag.archiveHref}>{mag.name}</a>
						</h2>
						<p class="tagline">{mag.tagline}</p>

						{#if mag.latest}
							<p class="meta">
								Seneste: Nr. {mag.latest.number} · {mag.latest.publishedLabel}
								{#if mag.latest.issueTheme}
									<br /><em>{mag.latest.issueTheme}</em>
								{/if}
							</p>
							<div class="mag-card-actions">
								<a class="btn btn-primary" href={mag.latest.href}>
									Læs nr. {mag.latest.number}
								</a>
								<a class="btn btn-ghost" href={mag.archiveHref}>
									Alle numre{#if mag.issueCount > 1}
										<span class="count">({mag.issueCount})</span>
									{/if}
								</a>
							</div>
						{:else}
							<p class="meta">Ingen numre endnu</p>
							<div class="mag-card-actions">
								<a class="btn btn-ghost" href={mag.archiveHref}>Gå til magasin</a>
							</div>
						{/if}
					</div>
				</article>
			{/each}
		</div>
	</section>
</main>

<SiteFooter magazines={data.navMagazines} />
