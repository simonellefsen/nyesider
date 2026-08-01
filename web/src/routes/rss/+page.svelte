<script lang="ts">
	import Seo from '$lib/components/Seo.svelte';
	import SiteFooter from '$lib/components/SiteFooter.svelte';
	import SiteHeader from '$lib/components/SiteHeader.svelte';
	import { pageTitle } from '$lib/seo';

	let { data } = $props();

	const description =
		'Følg Nye Sider med RSS — få besked om nye magasinernumre i din læser-app. Ingen konto, ingen app fra os.';

	function feedScheme(url: string): string {
		return `feed://${url.replace(/^https?:\/\//, '')}`;
	}
	function feedlyUrl(url: string): string {
		return `https://feedly.com/i/subscription/feed/${encodeURIComponent(url)}`;
	}
	function inoreaderUrl(url: string): string {
		return `https://www.inoreader.com/?add_feed=${encodeURIComponent(url)}`;
	}
	function newsblurUrl(url: string): string {
		return `https://newsblur.com/?url=${encodeURIComponent(url)}`;
	}

	async function copyFeed(url: string, event: MouseEvent) {
		await navigator.clipboard.writeText(url);
		const btn = event.currentTarget as HTMLButtonElement;
		const original = btn.textContent;
		btn.textContent = 'Kopieret ✓';
		setTimeout(() => (btn.textContent = original), 1500);
	}
</script>

<Seo
	title={pageTitle(['RSS'])}
	description={description}
	path="/rss"
/>

<SiteHeader magazines={data.navMagazines} />

<main class="page page-rss">
	<section class="kiosk-hero">
		<p class="eyebrow">Abonnement uden konto</p>
		<h1>RSS — nye numre i din læser</h1>
		<p>
			Vil du have besked, når vi udgiver et nyt magasinnummer — uden notifikationer, login eller
			nyhedsbrev? Brug <strong>RSS</strong>. Det er en åben feed-adresse, du tilføjer i en app
			<em>du</em> vælger. Vi gemmer ikke dig som abonnent.
		</p>
	</section>

	<section class="rss-card" aria-labelledby="feeds-heading">
		<h2 id="feeds-heading" class="section-heading">Vores feeds</h2>
		<p class="rss-lead">
			Kopiér adressen ind i din RSS-app, eller åbn linket og lad appen genkende feedet.
		</p>

		<ul class="rss-feed-list">
			<li class="rss-feed-item rss-feed-item--primary">
				<div>
					<strong>Alle magasiner</strong>
					<p>Nye numre på tværs af Nye Sider (anbefalet start).</p>
					<code class="rss-url">{data.siteFeedUrl}</code>
				</div>
				<div class="rss-feed-actions">
					<a class="btn btn-primary" href={feedScheme(data.siteFeedUrl)}>Åbn i app</a>
					<a class="btn btn-ghost" href={feedlyUrl(data.siteFeedUrl)} target="_blank" rel="noopener"
						>Feedly</a
					>
					<a
						class="btn btn-ghost"
						href={inoreaderUrl(data.siteFeedUrl)}
						target="_blank"
						rel="noopener">Inoreader</a
					>
					<a class="btn btn-ghost" href={newsblurUrl(data.siteFeedUrl)} target="_blank" rel="noopener"
						>NewsBlur</a
					>
					<button
						class="btn btn-ghost"
						type="button"
						onclick={(e) => copyFeed(data.siteFeedUrl, e)}
					>
						Kopiér adresse
					</button>
				</div>
			</li>
			{#each data.magazines as mag (mag.slug)}
				<li class="rss-feed-item" id={mag.slug}>
					<div>
						<strong>{mag.name}</strong>
						<p>{mag.tagline}</p>
						<code class="rss-url">{mag.feedUrl}</code>
					</div>
					<div class="rss-feed-actions">
						<a class="btn btn-ghost" href={feedScheme(mag.feedUrl)}>Åbn i app</a>
						<a class="btn btn-ghost" href={feedlyUrl(mag.feedUrl)} target="_blank" rel="noopener"
							>Feedly</a
						>
						<button class="btn btn-ghost" type="button" onclick={(e) => copyFeed(mag.feedUrl, e)}>
							Kopiér
						</button>
					</div>
				</li>
			{/each}
		</ul>
	</section>

	<section class="rss-how" aria-labelledby="how-heading">
		<h2 id="how-heading" class="section-heading">Sådan bruger du det</h2>
		<ol class="rss-steps">
			<li>
				<strong>Vælg en RSS-app</strong>
				<p>
					Gratis eller billige læsere: NetNewsWire (Mac/iOS), Reeder, Feedly, Inoreader,
					NewsBlur, FreshRSS (selvhostet) m.fl. Mange e-mail- og “read later”-apps kan også
					abonnere på RSS.
				</p>
			</li>
			<li>
				<strong>Tilføj feed-adressen</strong>
				<p>
					I appen: “Add feed”, “Abonnér” eller “+”, og indsæt fx
					<code>{data.siteFeedUrl}</code>. Nogle browsere viser også et RSS-ikon, når de
					ser feedet.
				</p>
			</li>
			<li>
				<strong>Læs når det passer dig</strong>
				<p>
					Når vi udgiver et nyt nummer og sitet opdateres, dukker det op som ulæst i din app
					— typisk inden for minutter til et par timer, afhængigt af hvor ofte appen tjekker.
					Tryk på emnet, og du lander på nummeret her på Nye Sider.
				</p>
			</li>
		</ol>
	</section>

	<section class="rss-faq" aria-labelledby="faq-heading">
		<h2 id="faq-heading" class="section-heading">Kort fortalt</h2>
		<dl class="rss-dl">
			<div>
				<dt>Skal jeg oprette en konto hos Nye Sider?</dt>
				<dd>Nej. Kun i din RSS-app, hvis den kræver det (mange gør ikke).</dd>
			</div>
			<div>
				<dt>Ser I, at jeg abonnerer?</dt>
				<dd>
					Vi har ingen abonnentliste. Din app henter bare den offentlige feed-fil, ligesom en
					browser henter en side.
				</dd>
			</div>
			<div>
				<dt>Er det det samme som push-notifikationer?</dt>
				<dd>
					Nej. RSS er “hent selv når det passer”. Din app kan give dig en badge eller
					notifikation, men det er <em>appens</em> indstilling — ikke noget vi sender til din
					telefon direkte.
				</dd>
			</div>
			<div>
				<dt>Hvad kommer i feedet?</dt>
				<dd>
					Nye <strong>magasinernumre</strong> (titel, kort indholdsoversigt, link). Ikke hver
					enkelt artikel som separat støj — du åbner nummeret og læser videre på sitet.
				</dd>
			</div>
		</dl>
		<p class="rss-note">
			Tip: Føj også gerne webappen til hjemmeskærmen, så du nemt kan fortsætte læsningen dér,
			hvor du slap. RSS fortæller dig, at der er noget nyt; hjemmeskærmen er til at læse det.
		</p>
	</section>
</main>

<SiteFooter magazines={data.navMagazines} />
