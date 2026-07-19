<script lang="ts">
	type Crumb = { label: string; href?: string };
	let { crumbs }: { crumbs: Crumb[] } = $props();
</script>

<nav class="breadcrumb" aria-label="Brødkrumme">
	{#each crumbs as crumb, i (crumb.label)}
		{#if i > 0}<span class="sep" aria-hidden="true">/</span>{/if}
		{#if crumb.href}
			<a href={crumb.href}>{crumb.label}</a>
		{:else}
			<span aria-current="page">{crumb.label}</span>
		{/if}
	{/each}
</nav>
