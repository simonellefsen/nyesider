<script lang="ts">
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';

	type NavMag = { slug: string; name: string };
	type Crumb = { label: string; href?: string };

	let {
		magazines,
		currentSlug = null,
		crumbs = null
	}: {
		magazines: NavMag[];
		currentSlug?: string | null;
		crumbs?: Crumb[] | null;
	} = $props();
</script>

<header class="site-header" class:site-header--with-crumbs={!!crumbs?.length}>
	<div class="site-header-row">
		<a class="brand" href="/">Nye <span>Sider</span></a>
		<nav class="site-nav" aria-label="Primær">
			{#each magazines as mag (mag.slug)}
				<a
					href="/{mag.slug}"
					class:is-current={currentSlug === mag.slug}
					aria-current={currentSlug === mag.slug ? 'page' : undefined}
				>
					{mag.name}
				</a>
			{/each}
		</nav>
	</div>
	{#if crumbs?.length}
		<div class="site-header-crumbs">
			<Breadcrumb {crumbs} />
		</div>
	{/if}
</header>
