<script lang="ts">
	import { dev } from '$app/environment';
	import { injectAnalytics } from '@vercel/analytics/sveltekit';
	import InstallBanner from '$lib/components/InstallBanner.svelte';
	import '$lib/styles/global.css';

	injectAnalytics({ mode: dev ? 'development' : 'production' });

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
	<link rel="icon" href="/favicon.ico" sizes="any" />
	<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
	<link rel="manifest" href="/manifest.webmanifest" />
	<link
		rel="alternate"
		type="application/rss+xml"
		title="Nye Sider — nye numre"
		href="/feed.xml"
	/>
	<meta name="theme-color" content="#0b1220" />
	<meta name="mobile-web-app-capable" content="yes" />
	<meta name="apple-mobile-web-app-capable" content="yes" />
	<meta name="apple-mobile-web-app-status-bar-style" content="default" />
	<meta name="apple-mobile-web-app-title" content="Nye Sider" />
	<meta name="google-site-verification" content="eTmjB_6nbevrnCnUvV35qbc7gH5soFDNsly58ZuMQzk" />
</svelte:head>

{@render children()}

<InstallBanner />
