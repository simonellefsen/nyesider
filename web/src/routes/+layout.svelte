<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import '$lib/styles/global.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<meta name="description" content="Nye Sider — danske AI-redigerede magasiner til skærmen." />
</svelte:head>

{@render children()}
