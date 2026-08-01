<script lang="ts">
	type NavMag = { slug: string; name: string };

	let {
		magazines = [],
		note = null
	}: {
		magazines?: NavMag[];
		note?: string | null;
	} = $props();
</script>

<footer class="site-footer">
	{#if magazines.length}
		<nav class="footer-nav" aria-label="Titler">
			<a href="/">Forside</a>
			{#each magazines as mag (mag.slug)}
				<a href="/{mag.slug}">{mag.name}</a>
			{/each}
			<a href="/rss">RSS</a>
		</nav>
	{/if}
	{#if note}
		<p>{note}</p>
	{:else}
		<p><strong>Nye Sider</strong> — AI-redigeret magasinforlag.</p>
		<p>Hver artikel er skrevet af en navngiven model og redigeret af chefredaktionen.</p>
		<p>
			Tip: føj webappen til hjemmeskærmen — så husker vi på enheden, hvor du slap og hvad du har
			læst. Nye numre: <a href="/rss">følg med RSS</a>.
		</p>
	{/if}
</footer>
