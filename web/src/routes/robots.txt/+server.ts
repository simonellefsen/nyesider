import { SITE_URL } from '$lib/seo';

export const prerender = true;

export function GET() {
	const body = `# Nye Sider — https://nyesider.vercel.app
# Production *.vercel.app allows bots. Preview deployments are noindex by Vercel.

User-agent: *
Allow: /

# Static assets / downloads are fine to crawl
Allow: /content/

Sitemap: ${SITE_URL}/sitemap.xml
`;

	return new Response(body, {
		headers: {
			'Content-Type': 'text/plain; charset=utf-8',
			'Cache-Control': 'public, max-age=86400'
		}
	});
}
