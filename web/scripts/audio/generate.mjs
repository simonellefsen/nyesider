#!/usr/bin/env node
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, resolve, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import { audioObjectParams, calibrationText, contentHash, joinMp3, mp3DurationSeconds, spokenText, splitForTts } from './lib.mjs';
import { synthesizeSpeech } from './providers.mjs';

const scriptDir = dirname(fileURLToPath(import.meta.url));
const webRoot = resolve(scriptDir, '../..');
const repoRoot = resolve(webRoot, '..');
loadDotEnv(resolve(repoRoot, '.env.local'));

function loadDotEnv(file) {
	if (!existsSync(file)) return;
	for (const line of readFileSync(file, 'utf8').split(/\r?\n/)) {
		const match = line.match(/^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)\s*$/);
		if (!match || process.env[match[1]] !== undefined) continue;
		const raw = match[2];
		process.env[match[1]] = raw.replace(/^("|')|("|')$/g, '');
	}
}

function fail(message) { console.error(`Fejl: ${message}`); process.exitCode = 1; }

function requireEnv(...keys) {
	const missing = keys.filter((key) => !process.env[key]);
	if (missing.length) throw new Error(`mangler ${missing.join(', ')} i .env.local`);
}

function arg(name) {
	const index = process.argv.indexOf(name);
	return index >= 0 ? process.argv[index + 1] : undefined;
}

function has(name) { return process.argv.includes(name); }

async function synthesize(provider, voice, text) {
	return synthesizeSpeech({
		provider, voice, text,
		apiKey: provider === 'openai' ? process.env.OPENAI_API_KEY : process.env.XAI_API_KEY
	});
}

async function render(provider, voice, text) {
	const parts = splitForTts(text);
	const chunks = [];
	for (const [index, part] of parts.entries()) {
		console.log(`  ${provider}/${voice}: del ${index + 1}/${parts.length}`);
		chunks.push(await synthesize(provider, voice, part));
	}
	const audio = joinMp3(chunks);
	const durationSeconds = mp3DurationSeconds(audio);
	if (!durationSeconds) throw new Error('kunne ikke aflæse MP3-varighed');
	return { audio, durationSeconds };
}

function getArticle(magazine, issueSlug, articleSlug) {
	const issueFile = resolve(repoRoot, 'content', magazine, 'issues', issueSlug, 'issue.json');
	const issue = JSON.parse(readFileSync(issueFile, 'utf8'));
	const article = issue.articles.find((item) => item.slug === articleSlug);
	if (!article) throw new Error(`ukendt artikel ${magazine}/${issueSlug}/${articleSlug}`);
	const markdown = readFileSync(resolve(dirname(issueFile), article.file), 'utf8');
	return { issueFile, issue, article, text: spokenText({ title: article.title, standfirst: article.standfirst, markdown }) };
}

function r2Client() {
	requireEnv('CLOUDFLARE_S3_ACCESS_KEY_ID', 'CLOUDFLARE_S3_SECRET_ACCESS_KEY', 'CLOUDFLARE_S3_API_ENDPOINT');
	const bucket = process.env.CLOUDFLARE_R2_BUCKET || 'nyesider-voice';
	const endpointUrl = new URL(process.env.CLOUDFLARE_S3_API_ENDPOINT);
	endpointUrl.pathname = endpointUrl.pathname.replace(new RegExp(`/${bucket}/?$`), '') || '/';
	return {
		bucket,
		client: new S3Client({
			region: 'auto', endpoint: endpointUrl.toString().replace(/\/$/, ''), forcePathStyle: true,
			credentials: { accessKeyId: process.env.CLOUDFLARE_S3_ACCESS_KEY_ID, secretAccessKey: process.env.CLOUDFLARE_S3_SECRET_ACCESS_KEY }
		})
	};
}

function publicBase() {
	const value = arg('--public-url') || process.env.CLOUDFLARE_R2_PUBLIC_URL;
	if (!value) throw new Error('mangler CLOUDFLARE_R2_PUBLIC_URL eller --public-url');
	if (new URL(value).hostname.endsWith('.r2.dev') && !has('--allow-dev-url')) {
		throw new Error('r2.dev er kun til prøver; brug custom domain eller tilføj --allow-dev-url eksplicit');
	}
	return value.replace(/\/$/, '');
}

async function upload({ audio, key, hash, provider, voice }) {
	const { client, bucket } = r2Client();
	await client.send(new PutObjectCommand(audioObjectParams({ bucket, key, audio, hash, provider, voice })));
}

function writeAudioMeta({ issueFile, issue, article, key, hash, durationSeconds, provider, voice }) {
	const base = publicBase();
	article.audio = {
		url: `${base}/${key}`, durationSeconds, contentHash: hash,
		generation: `nyesider-tts-v1:${provider}:${voice}`
	};
	writeFileSync(issueFile, `${JSON.stringify(issue, null, 2)}\n`);
}

async function renderArticle(magazine, issueSlug, articleSlug) {
	const provider = arg('--provider') || 'openai';
	const voice = arg('--voice') || (provider === 'xai' ? 'carina' : 'coral');
	const record = getArticle(magazine, issueSlug, articleSlug);
	const hash = contentHash(record.text);
	console.log(`${magazine}/${issueSlug}/${articleSlug} — ${record.text.length} tegn, ${hash.slice(0, 12)}`);
	if (has('--dry-run')) return;
	const result = await render(provider, voice, record.text);
	const out = resolve(repoRoot, 'artifacts/audio-preview', magazine, issueSlug, `${articleSlug}-${hash.slice(0, 12)}.mp3`);
	mkdirSync(dirname(out), { recursive: true });
	writeFileSync(out, result.audio);
	console.log(`  preview: ${relative(repoRoot, out)} (${result.durationSeconds}s)`);
	if (has('--upload')) {
		const key = `articles/${magazine}/${issueSlug}/${articleSlug}/${hash}.mp3`;
		await upload({ audio: result.audio, key, hash, provider, voice });
		console.log(`  uploaded: ${key}`);
		if (has('--write')) {
			writeAudioMeta({ ...record, key, hash, durationSeconds: result.durationSeconds, provider, voice });
			console.log('  article metadata updated');
		}
	}
}

async function samples() {
	const variants = [
		{ label: 'A', provider: 'openai', voice: 'coral' },
		{ label: 'B', provider: 'openai', voice: 'shimmer' },
		{ label: 'C', provider: 'xai', voice: 'carina' },
		{ label: 'D', provider: 'xai', voice: 'luna' }
	];
	const out = resolve(repoRoot, 'artifacts/audio-samples');
	mkdirSync(out, { recursive: true });
	for (const variant of variants) {
		console.log(`Prøve ${variant.label}`);
		const result = await render(variant.provider, variant.voice, calibrationText);
		writeFileSync(resolve(out, `${variant.label}.mp3`), result.audio);
	}
	writeFileSync(resolve(out, 'README.txt'), 'A–D er blindmærkede lydprøver. Lyt efter naturlig dansk udtale, tal, forkortelser og rolig magasinrytme.\n');
	console.log(`Prøver klar i ${relative(repoRoot, out)}`);
}

async function issue() {
	const [magazine, issueSlug] = process.argv.slice(3).filter((value) => !value.startsWith('--'));
	if (!magazine || !issueSlug) throw new Error('brug: audio:issue -- <magasin> <nummer> [--upload --write]');
	const issue = JSON.parse(readFileSync(resolve(repoRoot, 'content', magazine, 'issues', issueSlug, 'issue.json'), 'utf8'));
	const limit = Number(arg('--limit') || 1);
	if (!Number.isInteger(limit) || limit < 1) throw new Error('--limit skal være et positivt heltal');
	let processed = 0;
	for (const article of issue.articles) {
		if (article.audio && !has('--force')) continue;
		await renderArticle(magazine, issueSlug, article.slug);
		processed += 1;
		if (processed >= limit) break;
	}
	console.log(`${processed} artikel/artikler behandlet; kør samme kommando igen for resten.`);
}

async function main() {
	const command = process.argv[2];
	if (command === 'samples') return samples();
	if (command === 'article') {
		const [magazine, issueSlug, articleSlug] = process.argv.slice(3).filter((value) => !value.startsWith('--'));
		if (!magazine || !issueSlug || !articleSlug) throw new Error('brug: audio:article -- <magasin> <nummer> <artikel> [--upload --write]');
		return renderArticle(magazine, issueSlug, articleSlug);
	}
	if (command === 'issue') return issue();
	throw new Error('brug: audio:samples | audio:article | audio:issue');
}

main().catch((error) => fail(error instanceof Error ? error.message : String(error)));
