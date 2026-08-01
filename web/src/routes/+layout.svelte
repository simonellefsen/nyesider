<script lang="ts">
	import { dev } from '$app/environment';
	import { injectAnalytics } from '@vercel/analytics/sveltekit';
	import '$lib/styles/global.css';

	injectAnalytics({ mode: dev ? 'development' : 'production' });

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
	<link rel="icon" href="/favicon.ico" sizes="any" />
	<link rel="apple-touch-icon" href="/favicon-32.png" />
	<meta name="theme-color" content="#0b1220" />
	<meta name="google-site-verification" content="eTmjB_6nbevrnCnUvV35qbc7gH5soFDNsly58ZuMQzk" />
</svelte:head>

{@render children()}
