<script lang="ts">
	import { onMount } from 'svelte';
	import {
		dismissInstallBanner,
		isInstallBannerDismissed,
		isStandaloneDisplay
	} from '$lib/readingState';

	let visible = $state(false);
	let isIos = $state(false);
	let deferredPrompt: BeforeInstallPromptEvent | null = $state(null);

	type BeforeInstallPromptEvent = Event & {
		prompt: () => Promise<void>;
		userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
	};

	onMount(() => {
		if (isStandaloneDisplay() || isInstallBannerDismissed()) return;

		const ua = navigator.userAgent || '';
		isIos = /iPad|iPhone|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);

		// Chromium install event
		const onBip = (e: Event) => {
			e.preventDefault();
			deferredPrompt = e as BeforeInstallPromptEvent;
			visible = true;
		};
		window.addEventListener('beforeinstallprompt', onBip);

		// iOS / browsers without BIP: still show educational banner after a short delay
		const t = window.setTimeout(() => {
			if (!isStandaloneDisplay() && !isInstallBannerDismissed()) {
				visible = true;
			}
		}, 1800);

		return () => {
			window.removeEventListener('beforeinstallprompt', onBip);
			window.clearTimeout(t);
		};
	});

	function close() {
		visible = false;
		dismissInstallBanner();
	}

	async function install() {
		if (!deferredPrompt) return;
		await deferredPrompt.prompt();
		try {
			await deferredPrompt.userChoice;
		} catch {
			/* ignore */
		}
		deferredPrompt = null;
		close();
	}
</script>

{#if visible}
	<aside class="install-banner" role="region" aria-label="Føj til hjemmeskærm">
		<div class="install-banner-inner">
			<div class="install-banner-text">
				<strong>Føj Nye Sider til hjemmeskærmen</strong>
				<p>
					Så har du magasinerne som en app — og vi husker <em>hvor du slap</em> og hvad du har
					læst, også efter du lukker og åbner igen (gemmes på denne enhed).
				</p>
				{#if isIos && !deferredPrompt}
					<p class="install-how">
						På iPhone/iPad: tryk <span class="kbd">Del</span> i Safari, vælg
						<strong>Føj til hjemmeskærm</strong>.
					</p>
				{:else if !deferredPrompt}
					<p class="install-how">
						I browserens menu: <strong>Installér app</strong> eller
						<strong>Føj til startskærm</strong>.
					</p>
				{/if}
			</div>
			<div class="install-banner-actions">
				{#if deferredPrompt}
					<button type="button" class="btn btn-primary" onclick={install}>Installér</button>
				{/if}
				<button type="button" class="btn btn-ghost" onclick={close}>Ikke nu</button>
			</div>
		</div>
	</aside>
{/if}
