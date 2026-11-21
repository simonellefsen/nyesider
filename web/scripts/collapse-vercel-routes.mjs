#!/usr/bin/env node
/**
 * adapter-vercel writes two routes per prerendered page: a rewrite to the
 * trailing-slash path, and a 308 back to the canonical path. Vercel rejects
 * a deployment above 2048 routes. The 308s are identical, so one anchored
 * pattern replaces them. Vercel itself adds ^ and $ when src has neither.
 * The per-page rewrites stay; the canonical URL is still served as before.
 */
import { readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const webRoot = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const configPath = path.join(webRoot, '.vercel/output/config.json');

const config = JSON.parse(readFileSync(configPath, 'utf8'));
const routes = config.routes;
if (!Array.isArray(routes)) {
	console.error('collapse-vercel-routes: config.routes is missing');
	process.exit(1);
}

const slashRedirect = {
	src: '/(.+)/',
	status: 308,
	headers: { Location: '/$1' }
};

let twins = 0;
const kept = [];
let placed = false;

for (const route of routes) {
	const location = route?.headers?.Location;
	const keys = Object.keys(route?.headers ?? {});
	const isTwin =
		route?.status === 308 &&
		typeof location === 'string' &&
		route.src === `${location}/` &&
		keys.length === 1 &&
		keys[0] === 'Location';

	if (!isTwin) {
		kept.push(route);
		continue;
	}

	twins += 1;
	if (!placed) {
		kept.push(slashRedirect);
		placed = true;
	}
}

if (twins === 0) {
	console.error('collapse-vercel-routes: no trailing-slash redirects found');
	process.exit(1);
}

config.routes = kept;
writeFileSync(configPath, JSON.stringify(config, null, '\t') + '\n');
console.log(`collapse-vercel-routes: ${routes.length} -> ${kept.length} (${twins} slash redirects)`);
