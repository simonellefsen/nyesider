/** Editorial formats that deliberately do not receive AI narration. */
const EXCLUDED_SECTION_PREFIXES = ['leder', 'ordbogen', 'rygtebørsen'];

export function isNarratableArticle(section: string | undefined | null): boolean {
	const normalized = section?.trim().toLocaleLowerCase('da-DK') ?? '';
	return !EXCLUDED_SECTION_PREFIXES.some(
		(prefix) => normalized === prefix || normalized.startsWith(`${prefix} `) || normalized.startsWith(`${prefix}/`)
	);
}
