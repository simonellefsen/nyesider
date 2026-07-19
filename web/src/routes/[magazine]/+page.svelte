<script lang="ts">
	let { data } = $props();
	const colors = $derived(data.magazine.colors);
</script>

<svelte:head>
	<title>{data.magazine.name} — Nye Sider</title>
	<meta name="description" content={data.magazine.tagline} />
</svelte:head>

<div
	style:--mag-primary={colors.primary ?? '#0b1220'}
	style:--mag-accent={colors.accent ?? '#2a6f97'}
	style:--mag-highlight={colors.highlight ?? '#c9842f'}
>
	<header class="site-header">
		<a class="brand" href="/">Nye <span>Sider</span></a>
		<nav class="site-nav" aria-label="Primær">
			<a href="/{data.magazine.slug}">{data.magazine.name}</a>
		</nav>
	</header>

	<main class="page">
		<section class="mag-hero">
			{#if data.issues[0]?.cover}
				<div class="cover">
					<a href="/{data.magazine.slug}/{data.issues[0].slug}">
						<img
							src={data.issues[0].cover}
							alt="Seneste forside: {data.issues[0].title}"
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
					<p style="margin:0;font-size:0.9rem;color:var(--ink-muted);max-width:36rem">
						{data.magazine.audience}
					</p>
				{/if}
			</div>
		</section>

		<section aria-labelledby="arkiv-heading">
			<h2 id="arkiv-heading" style="font-size:1.1rem;margin:0 0 0.75rem">Numre</h2>
			<ul class="issue-list">
				{#each data.issues as issue (issue.slug)}
					<li>
						<a href="/{data.magazine.slug}/{issue.slug}">
							{#if issue.cover}
								<img src={issue.cover} alt="" width="56" height="75" />
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

	<footer class="site-footer">
		<p><a href="/">← Alle titler</a></p>
	</footer>
</div>
