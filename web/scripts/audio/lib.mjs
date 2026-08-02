import { createHash } from 'node:crypto';

const FRONTMATTER = /^---\s*\n[\s\S]*?\n---\s*\n/;
const FOOTNOTE_DEFINITION = /^\s*\[\^[^\]]+\]:.*(?:\n {2,}.*)*$/gm;
const TABLE_ROW = /^\s*\|.*\|\s*$/gm;

/** Produce the editorial script: headings and prose only, never references or visual-only content. */
export function spokenText({ title, standfirst, markdown }) {
	const body = markdown
		.replace(FRONTMATTER, '')
		.replace(FOOTNOTE_DEFINITION, '')
		.replace(/^\s*\[(?:FIGUR\s*\d*|CHART\s+[a-z0-9_-]+)\]\s*$/gim, '')
		.replace(TABLE_ROW, '')
		.replace(/!\[[^\]]*\]\([^)]*\)/g, '')
		.replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
		.replace(/\[\^([^\]]+)\]/g, '')
		.replace(/^\s{0,3}#{1,6}\s+/gm, '')
		.replace(/^\s*>\s?/gm, '')
		.replace(/`([^`]+)`/g, '$1')
		.replace(/<[^>]+>/g, ' ')
		.replace(/https?:\/\/[^\s)\]]+/gi, '')
		.replace(/\*{1,3}|_{1,3}/g, '')
		.replace(/\n{3,}/g, '\n\n')
		.trim();
	return [title.trim(), standfirst?.trim(), body]
		.filter(Boolean)
		.join('\n\n')
		.replace(/[ \t]+\n/g, '\n')
		.replace(/[ \t]{2,}/g, ' ')
		.trim();
}

export function contentHash(text) {
	return createHash('sha256').update(text, 'utf8').digest('hex');
}

/** Split on paragraph/sentence boundaries before falling back to a hard character limit. */
export function splitForTts(text, maxChars = 3400) {
	if (text.length <= maxChars) return [text];
	const units = text.split(/\n{2,}/).flatMap((paragraph) => {
		if (paragraph.length <= maxChars) return [paragraph];
		return paragraph.match(/[^.!?]+[.!?]+(?:\s|$)|[^.!?]+$/g)?.map((s) => s.trim()) ?? [paragraph];
	});
	const chunks = [];
	let current = '';
	for (const unit of units) {
		if (!unit) continue;
		if (unit.length > maxChars) {
			if (current) chunks.push(current);
			for (let start = 0; start < unit.length; start += maxChars) chunks.push(unit.slice(start, start + maxChars));
			current = '';
		} else if (!current) {
			current = unit;
		} else if (current.length + unit.length + 2 <= maxChars) {
			current += `\n\n${unit}`;
		} else {
			chunks.push(current);
			current = unit;
		}
	}
	if (current) chunks.push(current);
	return chunks;
}

/** Concatenated MP3 frames are valid in browsers and avoid a native ffmpeg dependency. */
export function joinMp3(chunks) {
	return Buffer.concat(chunks.map((chunk) => Buffer.from(chunk)));
}

/** Measure common MPEG Layer III streams from frame headers; returns 0 for an unknown stream. */
export function mp3DurationSeconds(buffer) {
	let pos = 0;
	if (buffer.subarray(0, 3).toString('ascii') === 'ID3' && buffer.length >= 10) {
		const size = ((buffer[6] & 0x7f) << 21) | ((buffer[7] & 0x7f) << 14) | ((buffer[8] & 0x7f) << 7) | (buffer[9] & 0x7f);
		pos = 10 + size;
	}
	const bitratesV1 = [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320];
	const bitratesV2 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160];
	const sampleRates = { 3: [44100, 48000, 32000], 2: [22050, 24000, 16000], 0: [11025, 12000, 8000] };
	let seconds = 0;
	while (pos + 4 <= buffer.length) {
		if (buffer[pos] !== 0xff || (buffer[pos + 1] & 0xe0) !== 0xe0) { pos += 1; continue; }
		const version = (buffer[pos + 1] >> 3) & 0x03;
		const layer = (buffer[pos + 1] >> 1) & 0x03;
		const bitrateIndex = (buffer[pos + 2] >> 4) & 0x0f;
		const sampleRateIndex = (buffer[pos + 2] >> 2) & 0x03;
		const padding = (buffer[pos + 2] >> 1) & 0x01;
		const sampleRate = sampleRates[version]?.[sampleRateIndex];
		const bitrate = (version === 3 ? bitratesV1 : bitratesV2)[bitrateIndex];
		if (layer !== 1 || !sampleRate || !bitrate) { pos += 1; continue; }
		const frameLength = Math.floor((version === 3 ? 144 : 72) * bitrate * 1000 / sampleRate) + padding;
		if (frameLength <= 4 || pos + frameLength > buffer.length) break;
		seconds += (version === 3 ? 1152 : 576) / sampleRate;
		pos += frameLength;
	}
	return Math.round(seconds * 10) / 10;
}

export function audioObjectParams({ bucket, key, audio, hash, provider, voice }) {
	return {
		Bucket: bucket,
		Key: key,
		Body: audio,
		ContentType: 'audio/mpeg',
		CacheControl: 'public, max-age=31536000, immutable',
		Metadata: { 'content-hash': hash, provider, voice, generation: 'nyesider-tts-v1' }
	};
}

export const calibrationText = `Nye Sider tester en rolig, varm dansk oplæser. En aluminiumsdåse på 33 centiliter begynder som bauxit, men ender først som emballage, når metal, lak og logistik passer sammen. I HumaNerd møder 1X, Figure og Boston Dynamics den samme prøve: Kan en robot udføre en nyttig opgave sikkert gennem et helt arbejdsskift? Prøven rummer tal, forkortelser og navne, fordi en god oplæsning skal være tydelig — også når stoffet er teknisk.`;
