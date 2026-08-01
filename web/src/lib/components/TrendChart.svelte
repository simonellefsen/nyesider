<script lang="ts">
	import type { ChartSpec } from '$lib/types';

	let { chart }: { chart: ChartSpec } = $props();

	const pad = { top: 16, right: 16, bottom: 36, left: 44 };
	const W = 640;
	const H = 280;
	const innerW = W - pad.left - pad.right;
	const innerH = H - pad.top - pad.bottom;

	const palette = ['#E3A008', '#4EC9B0', '#5B8DEF', '#c45c26', '#8b5cf6', '#64748b'];

	const allValues = $derived(chart.series.flatMap((s) => s.values));
	const yMin = $derived(Math.min(0, ...allValues));
	const yMax = $derived(Math.max(...allValues) * 1.08 || 1);

	function xPos(i: number): number {
		const n = chart.years.length;
		if (n <= 1) return pad.left + innerW / 2;
		return pad.left + (i / (n - 1)) * innerW;
	}

	function yPos(v: number): number {
		const t = (v - yMin) / (yMax - yMin || 1);
		return pad.top + innerH * (1 - t);
	}

	function pathFor(values: number[]): string {
		return values
			.map((v, i) => `${i === 0 ? 'M' : 'L'} ${xPos(i).toFixed(1)} ${yPos(v).toFixed(1)}`)
			.join(' ');
	}

	function colorFor(i: number, explicit?: string): string {
		return explicit || palette[i % palette.length];
	}

	let hover = $state<{
		i: number;
		x: number;
		points: { name: string; value: number; color: string }[];
	} | null>(null);

	function onMove(e: MouseEvent, svg: SVGSVGElement) {
		const rect = svg.getBoundingClientRect();
		const mx = ((e.clientX - rect.left) / rect.width) * W;
		let best = 0;
		let bestDist = Infinity;
		for (let i = 0; i < chart.years.length; i++) {
			const d = Math.abs(xPos(i) - mx);
			if (d < bestDist) {
				bestDist = d;
				best = i;
			}
		}
		hover = {
			i: best,
			x: xPos(best),
			points: chart.series.map((s, si) => ({
				name: s.name,
				value: s.values[best] ?? 0,
				color: colorFor(si, s.color)
			}))
		};
	}

	function onLeave() {
		hover = null;
	}

	function fmt(v: number): string {
		if (Number.isInteger(v)) return String(v);
		return v.toLocaleString('da-DK', { maximumFractionDigits: 1 });
	}

	const yTicks = $derived(
		[0, 0.25, 0.5, 0.75, 1].map((t) => yMin + t * (yMax - yMin))
	);
</script>

<figure class="trend-chart">
	{#if chart.title}
		<figcaption class="trend-chart-title">{chart.title}</figcaption>
	{/if}

	<svg
		class="trend-chart-svg"
		viewBox="0 0 {W} {H}"
		role="img"
		aria-label={chart.title || 'Tendensdiagram'}
		onmousemove={(e) => onMove(e, e.currentTarget)}
		onmouseleave={onLeave}
	>
		<!-- grid -->
		{#each yTicks as tick}
			<line
				class="grid"
				x1={pad.left}
				x2={pad.left + innerW}
				y1={yPos(tick)}
				y2={yPos(tick)}
			/>
			<text class="axis" x={pad.left - 8} y={yPos(tick) + 4} text-anchor="end"
				>{fmt(tick)}{chart.unit === '%' ? '' : ''}</text
			>
		{/each}

		<!-- x labels (first, mid, last + some) -->
		{#each chart.years as year, i}
			{#if i === 0 || i === chart.years.length - 1 || i % Math.ceil(chart.years.length / 6) === 0}
				<text class="axis" x={xPos(i)} y={H - 10} text-anchor="middle">{year}</text>
			{/if}
		{/each}

		<!-- series -->
		{#each chart.series as s, si}
			<path
				class="line"
				d={pathFor(s.values)}
				stroke={colorFor(si, s.color)}
				fill="none"
			/>
			{#each s.values as v, i}
				<circle
					class="dot"
					cx={xPos(i)}
					cy={yPos(v)}
					r={hover?.i === i ? 5 : 3}
					fill={colorFor(si, s.color)}
				/>
			{/each}
		{/each}

		{#if hover}
			<line
				class="hover-line"
				x1={hover.x}
				x2={hover.x}
				y1={pad.top}
				y2={pad.top + innerH}
			/>
		{/if}
	</svg>

	{#if hover}
		<div class="trend-tooltip" style:--tx="{((hover.x / W) * 100).toFixed(1)}%">
			<strong>{chart.years[hover.i]}</strong>
			<ul>
				{#each hover.points as p}
					<li>
						<span class="swatch" style:background={p.color}></span>
						{p.name}:
						<strong
							>{fmt(p.value)}{chart.unit ? `\u00a0${chart.unit}` : ''}</strong
						>
					</li>
				{/each}
			</ul>
		</div>
	{:else}
		<p class="trend-hint">Hold musen over diagrammet for årstal og værdier.</p>
	{/if}

	<ul class="trend-legend">
		{#each chart.series as s, si}
			<li>
				<span class="swatch" style:background={colorFor(si, s.color)}></span>
				{s.name}
			</li>
		{/each}
	</ul>

	{#if chart.note || chart.source}
		<p class="trend-source">
			{#if chart.note}{chart.note}
				{#if chart.source}·{/if}
			{/if}
			{#if chart.source}
				Kilde:
				{#if chart.sourceUrl}
					<a href={chart.sourceUrl} rel="noopener noreferrer" target="_blank"
						>{chart.source}</a
					>
				{:else}
					{chart.source}
				{/if}
			{/if}
		</p>
	{/if}
</figure>
