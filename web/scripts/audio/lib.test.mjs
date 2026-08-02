import test from 'node:test';
import assert from 'node:assert/strict';
import { audioObjectParams, contentHash, spokenText, splitForTts } from './lib.mjs';
import { synthesizeSpeech } from './providers.mjs';

test('spokenText keeps article prose but removes figures, sources, URLs, tables and footnotes', () => {
	const script = spokenText({
		title: 'En titel', standfirst: 'En kort introduktion.',
		markdown: `---\ntitle: Ignoreres\n---\n# Mellemoverskrift\n\nEn [relevant tekst](https://example.com) med [^1].\n\n[FIGUR 1]\n\n| År | Tal |\n|---|---|\n| 2026 | 33 |\n\n[^1]: https://sources.example/kilde\n`
	});
	assert.match(script, /En titel\n\nEn kort introduktion\./);
	assert.match(script, /Mellemoverskrift/);
	assert.match(script, /relevant tekst/);
	assert.doesNotMatch(script, /example\.com|FIGUR|\| År/);
});

test('splitForTts keeps every character and prefers sentence boundaries', () => {
	const text = 'Første sætning. Anden sætning er længere. Tredje sætning.';
	const chunks = splitForTts(text, 30);
	assert.ok(chunks.length > 1);
	assert.equal(chunks.join(' ').replace(/\s+/g, ' ').replace(/ \./g, '.'), text.replace(/\s+/g, ' '));
});

test('content hashes change when the spoken script changes', () => {
	assert.equal(contentHash('samme'), contentHash('samme'));
	assert.notEqual(contentHash('samme'), contentHash('ændret'));
});

test('R2 upload has immutable MP3 headers and provenance', () => {
	const params = audioObjectParams({ bucket: 'nyesider-voice', key: 'articles/a.mp3', audio: Buffer.from('mp3'), hash: 'a'.repeat(64), provider: 'openai', voice: 'coral' });
	assert.equal(params.ContentType, 'audio/mpeg');
	assert.equal(params.CacheControl, 'public, max-age=31536000, immutable');
	assert.equal(params.Metadata['content-hash'], 'a'.repeat(64));
	assert.equal(params.Metadata.generation, 'nyesider-tts-v1');
});

test('provider adapters send the expected OpenAI and xAI requests', async () => {
	const calls = [];
	const fetchImpl = async (url, init) => {
		calls.push({ url, init });
		return new Response(new Uint8Array([1, 2, 3]), { status: 200 });
	};
	await synthesizeSpeech({ provider: 'openai', voice: 'coral', text: 'Hej', apiKey: 'test', fetchImpl });
	await synthesizeSpeech({ provider: 'xai', voice: 'carina', text: 'Hej', apiKey: 'test', fetchImpl });
	assert.equal(calls[0].url, 'https://api.openai.com/v1/audio/speech');
	assert.equal(JSON.parse(calls[0].init.body).model, 'gpt-4o-mini-tts');
	assert.equal(calls[1].url, 'https://api.x.ai/v1/tts');
	assert.equal(JSON.parse(calls[1].init.body).language, 'auto');
});
