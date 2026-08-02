export async function synthesizeSpeech({ provider, voice, text, apiKey, fetchImpl = fetch }) {
	if (!apiKey) throw new Error(`mangler API-nøgle til ${provider}`);
	if (provider === 'openai') {
		const response = await fetchImpl('https://api.openai.com/v1/audio/speech', {
			method: 'POST',
			headers: { Authorization: `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
			body: JSON.stringify({
				model: 'gpt-4o-mini-tts', voice, input: text, response_format: 'mp3',
				instructions: 'Tal på klart, naturligt dansk med rolig, varm og professionel kvindelig fortællerstil. Udtal tal, forkortelser og egennavne tydeligt.'
			})
		});
		if (!response.ok) throw new Error(`OpenAI TTS svarede ${response.status}: ${await response.text()}`);
		return Buffer.from(await response.arrayBuffer());
	}
	if (provider === 'xai') {
		const response = await fetchImpl('https://api.x.ai/v1/tts', {
			method: 'POST',
			headers: { Authorization: `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
			body: JSON.stringify({ text, voice_id: voice, language: 'auto', text_normalization: true })
		});
		if (!response.ok) throw new Error(`xAI TTS svarede ${response.status}: ${await response.text()}`);
		return Buffer.from(await response.arrayBuffer());
	}
	throw new Error(`ukendt provider: ${provider}`);
}
