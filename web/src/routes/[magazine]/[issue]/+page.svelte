<script lang="ts">
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import Seo from '$lib/components/Seo.svelte';
	import { absoluteUrl, pageTitle, publicationIssueJsonLd } from '$lib/seo';

	let { data } = $props();
	const colors = $derived(data.magazine.colors);
	const path = $derived(`/${data.magazine.slug}/${data.issue.slug}`);
	const description = $derived(
		data.issue.issueTheme
			? `${data.issue.title} — ${data.issue.issueTheme}. Læs indholdsfortegnelsen og hent PDF-udgaven.`
			: `${data.issue.title}. Læs indholdsfortegnelsen og hent PDF-udgaven hos Nye Sider.`
	);
</script>

<Seo
	title={pageTitle([data.issue.title, data.magazine.name])}
	description={description}
	path={path}
	image={data.issue.cover}
	jsonLd={publicationIssueJsonLd({
		name: data.issue.title,
		url: absoluteUrl(path),
		description: data.issue.issueTheme,
		issueNumber: data.issue.number,
		datePublished: data.issue.published,
		image: data.issue.cover,
		periodicalName: data.magazine.name,
		periodicalUrl: absoluteUrl(`/${data.magazine.slug}`)
	})}
/>

<div
	style:--mag-primary={colors.primary ?? '#0b1220'}
	style:--mag-accent={colors.accent ?? '#2a6f97'}
	style:--mag-highlight={colors.highlight ?? '#c9842f'}
>
	<header class="site-header">
		<Breadcrumb
			crumbs={[
				{ label: 'Nye Sider', href: '/' },
				{ label: data.magazine.name, href: `/${data.magazine.slug}` },
				{ label: `Nr. ${data.issue.number}` }
			]}
		/>
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
			<a class="pdf-link" href={data.issue.pdf} download> ↓ Hent PDF-udgaven </a>
		{/if}

		{#if data.issue.cover}
			<figure class="issue-cover" style="margin-top:1.25rem">
				<img
					src={data.issue.cover}
					alt="Forside: {data.issue.title}"
					width="360"
					height="480"
				/>
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
