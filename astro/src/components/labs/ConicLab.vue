<script setup>
import { onBeforeUnmount, onMounted, ref, watch } from "vue";
import LabShell from "./LabShell.vue";

const canvas = ref(null);
const e = ref(0.6);
const p = ref(1.5);
const copy = ref("拖动离心率，观察椭圆 → 抛物线 → 双曲线的连续变化。");

let plot = null;
let resizeObserver;

function draw() {
  if (!plot) return;
  const { ctx, width, height } = plot;
  const scale = Math.min(width, height) / 7.5;
  const ev = Number(e.value);
  const pv = Number(p.value);
  ctx.clearRect(0, 0, width, height);

  // 网格
  ctx.strokeStyle = "rgba(150,150,170,.22)";
  ctx.lineWidth = 0.6;
  for (let k = -6; k <= 6; k += 1) {
    const x = width / 2 + k * scale;
    const y = height / 2 + k * scale;
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, height);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(width, y);
    ctx.stroke();
  }

  // 坐标轴
  ctx.strokeStyle = "rgba(180,180,200,.45)";
  ctx.beginPath();
  ctx.moveTo(0, height / 2);
  ctx.lineTo(width, height / 2);
  ctx.moveTo(width / 2, 0);
  ctx.lineTo(width / 2, height);
  ctx.stroke();

  const toScreen = (x, y) => [width / 2 + x * scale, height / 2 - y * scale];
  const branches = [];
  const n = 600;
  const rMax = 30;

  if (ev < 1 - 1e-6) {
    const pts = [];
    for (let i = 0; i <= n; i += 1) {
      const th = (Math.PI * 2 * i) / n;
      const r = pv / (1 + ev * Math.cos(th));
      pts.push([r * Math.cos(th), r * Math.sin(th)]);
    }
    branches.push(pts);
  } else if (ev <= 1 + 1e-6) {
    const pts = [];
    for (let i = 0; i <= n; i += 1) {
      const th = -Math.PI + (Math.PI * 2 * i) / n;
      if (Math.abs(Math.cos(th) + 1) < 1e-4) continue;
      const r = pv / (1 + Math.cos(th));
      if (r > rMax) continue;
      pts.push([r * Math.cos(th), r * Math.sin(th)]);
    }
    branches.push(pts);
  } else {
    const th0 = Math.acos(-1 / ev);
    for (const [a, b] of [
      [-th0, th0],
      [th0, Math.PI * 2 - th0],
    ]) {
      const pts = [];
      for (let i = 0; i <= n; i += 1) {
        const th = a + ((b - a) * i) / n;
        const den = 1 + ev * Math.cos(th);
        if (Math.abs(den) < 1e-5) continue;
        const r = pv / den;
        if (Math.abs(r) > rMax) continue;
        pts.push([r * Math.cos(th), r * Math.sin(th)]);
      }
      branches.push(pts);
    }
  }

  ctx.strokeStyle = "#d9bc6a";
  ctx.lineWidth = 2;
  for (const pts of branches) {
    if (pts.length < 2) continue;
    ctx.beginPath();
    pts.forEach(([x, y], i) => {
      const [sx, sy] = toScreen(x, y);
      if (i === 0) ctx.moveTo(sx, sy);
      else ctx.lineTo(sx, sy);
    });
    ctx.stroke();
  }

  // 焦点
  ctx.fillStyle = "#d9bc6a";
  ctx.beginPath();
  ctx.arc(width / 2, height / 2, 4, 0, Math.PI * 2);
  ctx.fill();

  // 准线
  if (ev > 1e-3) {
    const dx = toScreen(pv / ev, 0)[0];
    ctx.strokeStyle = "rgba(220,220,230,.55)";
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(dx, 0);
    ctx.lineTo(dx, height);
    ctx.stroke();
    ctx.setLineDash([]);
  }

  // 图例
  ctx.fillStyle = "rgba(200,200,215,.8)";
  ctx.font = "11px monospace";
  ctx.fillText("r = p / (1 + e cos θ)", 12, height - 12);

  if (ev < 1 - 1e-6) copy.value = `e=${ev.toFixed(2)} < 1：椭圆，焦点在原点，准线在右侧。`;
  else if (Math.abs(ev - 1) < 1e-6) copy.value = "e=1：抛物线，焦点到定点的距离等于到准线的距离。";
  else copy.value = `e=${ev.toFixed(2)} > 1：双曲线，出现两支。`;
}

function resize() {
  const el = canvas.value;
  if (!el) return;
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const width = el.parentElement.clientWidth;
  const height = el.parentElement.clientHeight;
  if (!width || !height) return;
  el.width = Math.round(width * dpr);
  el.height = Math.round(height * dpr);
  el.style.width = width + "px";
  el.style.height = height + "px";
  const ctx = el.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  plot = { ctx, width, height };
  draw();
}

watch([e, p], draw);
onMounted(() => {
  resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(canvas.value.parentElement);
  resize();
});
onBeforeUnmount(() => {
  resizeObserver?.disconnect();
});
</script>

<template>
  <LabShell title="圆锥曲线" formula="r = p / (1 + e cos θ)" :description="copy">
    <template #stage>
      <canvas ref="canvas" aria-hidden="true"></canvas>
    </template>
    <template #controls>
      <label class="lab__control">
        <span>离心率 e <b>{{ Number(e).toFixed(2) }}</b></span>
        <input v-model.number="e" type="range" min="0.2" max="1.8" step="0.01" />
      </label>
      <label class="lab__control">
        <span>半通径 p <b>{{ Number(p).toFixed(2) }}</b></span>
        <input v-model.number="p" type="range" min="0.5" max="3" step="0.05" />
      </label>
      <p class="lab__hint">焦点在原点 · 虚线为准线 · 坐标单位为 1</p>
    </template>
  </LabShell>
</template>
