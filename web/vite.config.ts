import adapter from '@sveltejs/adapter-vercel';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.dirname(fileURLToPath(import.meta.url));
const contentDir = path.resolve(root, '../content');

export default defineConfig({
	plugins: [
		sveltekit({
			compilerOptions: {
				runes: ({ filename }) =>
					filename.split(/[/\\]/).includes('node_modules') ? undefined : true
			},
			adapter: adapter({
				// Local Node may be newer than Vercel's supported runtimes;
				// pin an LTS runtime for serverless fallbacks (site is fully prerendered).
				runtime: 'nodejs22.x'
			})
		})
	],
	server: {
		fs: {
			allow: [root, contentDir]
		}
	},
	// Make content available during SSR/prerender
	ssr: {
		external: []
	}
});
