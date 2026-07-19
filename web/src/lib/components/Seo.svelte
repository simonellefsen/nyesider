<script lang="ts">
	import {
		SITE_LOCALE,
		SITE_NAME,
		absoluteUrl,
		absoluteAssetUrl,
		jsonLdScript
	} from '$lib/seo';

	type Props = {
		title: string;
		description: string;
		/** Path starting with / */
		path?: string;
		/** Relative or absolute image URL */
		image?: string | null;
		type?: 'website' | 'article';
		publishedTime?: string | null;
		author?: string | null;
		noindex?: boolean;
		jsonLd?: object | object[] | null;
	};

	let {
		title,
		description,
		path = '/',
		image = null,
		type = 'website',
		publishedTime = null,
		author = null,
		noindex = false,
		jsonLd = null
	}: Props = $props();

	const canonical = $derived(absoluteUrl(path));
	const ogImage = $derived(absoluteAssetUrl(image));
	const robots = $derived(noindex ? 'noindex, nofollow' : 'index, follow, max-image-preview:large');
</script>

<svelte:head>
	<title>{title}</title>
	<meta name="description" content={description} />
	<meta name="robots" content={robots} />
	<link rel="canonical" href={canonical} />

	<meta property="og:site_name" content={SITE_NAME} />
	<meta property="og:locale" content={SITE_LOCALE} />
	<meta property="og:type" content={type} />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta property="og:url" content={canonical} />
	{#if ogImage}
		<meta property="og:image" content={ogImage} />
		<meta property="og:image:alt" content={title} />
	{/if}

	<meta name="twitter:card" content={ogImage ? 'summary_large_image' : 'summary'} />
	<meta name="twitter:title" content={title} />
	<meta name="twitter:description" content={description} />
	{#if ogImage}
		<meta name="twitter:image" content={ogImage} />
	{/if}

	{#if type === 'article' && publishedTime}
		<meta property="article:published_time" content={publishedTime} />
	{/if}
	{#if type === 'article' && author}
		<meta property="article:author" content={author} />
	{/if}

	{#if jsonLd}
		{@html `<script type="application/ld+json">${jsonLdScript(jsonLd)}</script>`}
	{/if}
</svelte:head>
