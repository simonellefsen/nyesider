#!/usr/bin/env node
/**
 * Copy images + PDFs from ../content into static/content so they are
 * served as static files on Vercel (and locally via Vite).
 * Skips _extract intermediate dumps.
 */
import { cpSync, existsSync, mkdirSync, readdirSync, rmSync, statSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const webRoot = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const contentRoot = path.resolve(webRoot, '../content');
const outRoot = path.join(webRoot, 'static/content');

const ASSET_EXT = new Set(['.png', '.jpg', '.jpeg', '.webp', '.avif', '.gif', '.svg', '.pdf']);

function shouldSkip(name) {
	return name.startsWith('.') || name === '_extract' || name === 'node_modules';
}

function walkCopy(srcDir, destDir) {
	if (!existsSync(srcDir)) return;
	for (const name of readdirSync(srcDir)) {
		if (shouldSkip(name)) continue;
		const src = path.join(srcDir, name);
		const dest = path.join(destDir, name);
		const st = statSync(src);
		if (st.isDirectory()) {
			walkCopy(src, dest);
		} else if (ASSET_EXT.has(path.extname(name).toLowerCase())) {
			mkdirSync(path.dirname(dest), { recursive: true });
			cpSync(src, dest);
		}
	}
}

if (existsSync(outRoot)) {
	rmSync(outRoot, { recursive: true, force: true });
}
mkdirSync(outRoot, { recursive: true });
walkCopy(contentRoot, outRoot);
console.log(`Synced content assets → ${path.relative(webRoot, outRoot)}`);
