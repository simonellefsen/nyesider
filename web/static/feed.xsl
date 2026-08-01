<?xml version="1.0" encoding="UTF-8"?>
<!--
  Renders /feed.xml (and /<magazine>/feed.xml) as a readable page when a
  human opens the raw feed URL directly — e.g. tapping "Feed (XML)" on an
  iPhone, which has no built-in RSS reader and otherwise just dumps XML.
  RSS readers ignore this <?xml-stylesheet?> entirely and parse the feed
  as before; this file changes nothing about what they see.

  Must be served as text/xml or application/xml (never application/rss+xml
  — WebKit does not apply XSLT to that MIME type, which would silently
  break this page). See vercel.json for the explicit content-type rule.
-->
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:atom="http://www.w3.org/2005/Atom">
	<xsl:output method="html" encoding="UTF-8" indent="no" />

	<xsl:template match="/rss/channel">
		<xsl:variable name="feedUrl" select="atom:link/@href" />
		<xsl:variable name="feedUrlNoScheme" select="substring-after($feedUrl, '://')" />

		<html lang="da">
			<head>
				<meta charset="utf-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1" />
				<title><xsl:value-of select="title" /></title>
				<meta name="robots" content="noindex" />
				<style>
					:root {
						--bg: #f7f4ef;
						--bg-elevated: #fffcf7;
						--ink: #1a1a1a;
						--ink-muted: #5c5c5c;
						--line: rgba(26, 26, 26, 0.12);
						--accent: #0b1220;
						--font-sans: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
						--font-serif: 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif;
					}
					@media (prefers-color-scheme: dark) {
						:root {
							--bg: #0f1419;
							--bg-elevated: #171d24;
							--ink: #f0ebe3;
							--ink-muted: #a8a29a;
							--line: rgba(240, 235, 227, 0.12);
							--accent: #e7ded0;
						}
					}
					* { box-sizing: border-box; }
					body {
						margin: 0;
						background: var(--bg);
						color: var(--ink);
						font-family: var(--font-sans);
						line-height: 1.5;
					}
					main {
						max-width: 640px;
						margin: 0 auto;
						padding: clamp(1.25rem, 5vw, 3rem) 1.25rem 4rem;
					}
					.eyebrow {
						text-transform: uppercase;
						letter-spacing: 0.08em;
						font-size: 0.75rem;
						color: var(--ink-muted);
						margin: 0 0 0.5rem;
					}
					h1 {
						font-family: var(--font-serif);
						font-size: clamp(1.5rem, 5vw, 2.1rem);
						margin: 0 0 0.75rem;
					}
					.lede {
						color: var(--ink-muted);
						margin: 0 0 1.75rem;
					}
					.card {
						background: var(--bg-elevated);
						border: 1px solid var(--line);
						border-radius: 14px;
						padding: 1.25rem;
						margin-bottom: 1.5rem;
					}
					.card h2 {
						margin: 0 0 0.9rem;
						font-size: 1rem;
					}
					.actions {
						display: flex;
						flex-wrap: wrap;
						gap: 0.5rem;
					}
					.btn {
						display: inline-flex;
						align-items: center;
						gap: 0.4rem;
						padding: 0.55rem 0.95rem;
						border-radius: 999px;
						font-size: 0.88rem;
						font-weight: 600;
						text-decoration: none;
						border: 1px solid var(--line);
						color: var(--ink);
						background: transparent;
						cursor: pointer;
						font-family: inherit;
					}
					.btn-primary {
						background: var(--accent);
						color: var(--bg-elevated);
						border-color: transparent;
					}
					.url-row {
						display: flex;
						align-items: center;
						gap: 0.5rem;
						margin-top: 1rem;
						flex-wrap: wrap;
					}
					code {
						font-size: 0.82rem;
						background: var(--bg);
						border: 1px solid var(--line);
						border-radius: 8px;
						padding: 0.3rem 0.55rem;
						word-break: break-all;
					}
					.hint {
						font-size: 0.85rem;
						color: var(--ink-muted);
						margin-top: 0.9rem;
					}
					.items { list-style: none; margin: 0; padding: 0; }
					.items li {
						padding: 0.9rem 0;
						border-top: 1px solid var(--line);
					}
					.items li:first-child { border-top: none; }
					.items a {
						color: var(--ink);
						font-weight: 600;
						text-decoration: none;
					}
					.items a:hover { text-decoration: underline; }
					.items time {
						display: block;
						font-size: 0.78rem;
						color: var(--ink-muted);
						margin-bottom: 0.2rem;
					}
					footer {
						margin-top: 2.5rem;
						font-size: 0.8rem;
						color: var(--ink-muted);
					}
					footer a { color: inherit; }
				</style>
			</head>
			<body>
				<main>
					<p class="eyebrow">RSS-feed</p>
					<h1><xsl:value-of select="title" /></h1>
					<p class="lede"><xsl:value-of select="description" /></p>

					<section class="card">
						<h2>Abonnér i en app</h2>
						<div class="actions">
							<a class="btn btn-primary" href="{concat('feed://', $feedUrlNoScheme)}">
								Åbn i installeret app
							</a>
							<a class="btn" href="{concat('https://feedly.com/i/subscription/feed/', $feedUrl)}" target="_blank" rel="noopener">
								Feedly
							</a>
							<a class="btn" href="{concat('https://www.inoreader.com/?add_feed=', $feedUrl)}" target="_blank" rel="noopener">
								Inoreader
							</a>
							<a class="btn" href="{concat('https://newsblur.com/?url=', $feedUrl)}" target="_blank" rel="noopener">
								NewsBlur
							</a>
						</div>
						<div class="url-row">
							<code id="feed-url"><xsl:value-of select="$feedUrl" /></code>
							<button class="btn" type="button" onclick="navigator.clipboard.writeText(document.getElementById('feed-url').textContent);this.textContent='Kopieret ✓';">
								Kopiér
							</button>
						</div>
						<p class="hint">
							Har du ikke en RSS-app endnu? <strong>NetNewsWire</strong> (gratis, iOS/Mac) eller
							<strong>Reeder</strong> er gode steder at starte — søg navnet i App Store, og indsæt
							adressen ovenfor.
						</p>
					</section>

					<section>
						<h2 class="eyebrow" style="margin-bottom:0.75rem;">Seneste i feedet</h2>
						<ul class="items">
							<xsl:for-each select="item">
								<li>
									<time><xsl:value-of select="pubDate" /></time>
									<a href="{link}"><xsl:value-of select="title" /></a>
								</li>
							</xsl:for-each>
						</ul>
					</section>

					<footer>
						<p>
							Dette er en RSS-feed-fil, vist som en side fordi din browser (eller app) åbnede
							den direkte. En rigtig RSS-læser viser i stedet nye numre i din egen app.
							<a href="/rss">Læs mere om RSS på Nye Sider →</a>
						</p>
					</footer>
				</main>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>
