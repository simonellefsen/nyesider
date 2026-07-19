<script lang="ts">
	let { data } = $props();
	const colors = $derived(data.magazine.colors);
</script>

<svelte:head>
	<title>{data.issue.title} — {data.magazine.name}</title>
	{#if data.issue.issueTheme}
		<meta name="description" content={data.issue.issueTheme} />
	{/if}
	{#if data.issue.cover}
		<meta property="og:image" content={data.issue.cover} />
	{/if}
</svelte:head>

<div
	style:--mag-primary={colors.primary ?? '#0b1220'}
	style:--mag-accent={colors.accent ?? '#2a6f97'}
	style:--mag-highlight={colors.highlight ?? '#c9842f'}
>
	<header class="site-header">
		<a class="brand" href="/{data.magazine.slug}">{data.magazine.name}</a>
		<nav class="site-nav" aria-label="Primær">
			<a href="/">Nye Sider</a>
		</nav>
	</header>

	<main class="page">
		<p class="eyebrow">
			<a href="/{data.magazine.slug}" style="color:inherit;text-decoration:none"
				>{data.magazine.name}</a
			>
			· Nr. {data.issue.number}
		</p>
		<h1 style="margin:0 0 0.35rem;font-size:clamp(1.6rem,5vw,2.4rem)">{data.issue.title}</h1>
		<p style="margin:0;color:var(--ink-muted)">{data.issue.publishedLabel}</p>
		{#if data.issue.issueTheme}
			<p style="margin:0.5rem 0 0;font-family:var(--font-serif);font-size:1.2rem;font-style:italic">
				{data.issue.issueTheme}
			</p>
		{/if}

		{#if data.issue.pdf}
			<a class="pdf-link" href={data.issue.pdf} download>
				↓ Hent PDF-udgaven
			</a>
		{/if}

		{#if data.issue.cover}
			<figure class="issue-cover" style="margin-top:1.25rem">
				<img src={data.issue.cover} alt="Forside: {data.issue.title}" width="360" height="480" />
			</figure>
		{/if}

		<section aria-labelledby="indhold-heading">
			<h2 id="indhold-heading" style="font-size:1.15rem;margin:1.75rem 0 0.25rem">Indhold</h2>
			<ol class="toc">
				{#each data.articles as article, i (article.slug)}
					<li>
						<a href={article.href}>
							<p class="section">{article.section}</p>
							<h2>
								<span style="color:var(--ink-muted);font-weight:500;margin-right:0.35rem"
									>{String(i + 1).padStart(2, '0')}</span
								>{article.title}
							</h2>
							{#if article.standfirst}
								<p class="standfirst">{article.standfirst}</p>
							{/if}
							<p class="byline">Af {article.byline}</p>
						</a>
					</li>
				{/each}
			</ol>
		</section>
	</main>

	<footer class="site-footer">
		<p><a href="/{data.magazine.slug}">← Alle numre af {data.magazine.name}</a></p>
	</footer>
</div>
