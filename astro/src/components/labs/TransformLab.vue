<script setup>
import { onBeforeUnmount, onMounted, ref, watch } from "vue";
import LabShell from "./LabShell.vue";
import { useLabUrl } from "./useLabUrl";

const canvas = ref(null);
const a = ref(1);
const b = ref(0.5);
const c = ref(0.2);
const d = ref(1);
const det = ref("1.00");
const defaults = { a: 1, b: 0.5, c: 0.2, d: 1 };
const presets = [
  { label: "旋转 90°", values: { a: 0, b: -1, c: 1, d: 0 } },
  { label: "剪切", values: { a: 1, b: 1, c: 0, d: 1 } },
  { label: "缩放", values: { a: 1.4, b: 0, c: 0, d: 0.7 } },
  { label: "奇异", values: { a: 1, b: 1, c: 1, d: 1 } },
];

useLabUrl({ a, b, c, d });

function applyPreset(preset) {
  a.value = preset.values.a;
  b.value = preset.values.b;
  c.value = preset.values.c;
  d.value = preset.values.d;
}

function reset() {
  a.value = defaults.a;
  b.value = defaults.b;
  c.value = defaults.c;
  d.value = defaults.d;
}

let ctx = null;
let width = 0;
let height = 0;
let resizeObserver;

function draw() {
  if (!ctx || !width || !height) return;
  const s = Math.min(width, height) / 9;
  const cx = width / 2;
  const cy = height / 2;
  const A = { a: Number(a.value), b: Number(b.value), c: Number(c.value), d: Number(d.value) };
  const D = A.a * A.d - A.b * A.c;
  det.value = D.toFixed(2);

  ctx.clearRect(0, 0, width, height);
  ctx.strokeStyle = "rgba(140,140,170,.25)";
  ctx.lineWidth = 0.7;
  for (let k = -4; k <= 4; k += 1) {
    ctx.beginPath();
    ctx.moveTo(cx + k * s, 0);
    ctx.lineTo(cx + k * s, height);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(0, cy + k * s);
    ctx.lineTo(width, cy + k * s);
    ctx.stroke();
  }

  ctx.strokeStyle = "rgba(210,210,230,.45)";
  ctx.beginPath();
  ctx.moveTo(0, cy);
  ctx.lineTo(width, cy);
  ctx.moveTo(cx, 0);
  ctx.lineTo(cx, height);
  ctx.stroke();

  const P = (x, y) => [cx + x * s, cy - y * s];
  const T = (x, y) => [A.a * x + A.b * y, A.c * x + A.d * y];

  ctx.strokeStyle = "rgba(217,188,106,.75)";
  ctx.lineWidth = 1.2;
  for (let k = -4; k <= 4; k += 0.5) {
    for (const pts of [
      [T(k, -4), T(k, 4)],
      [T(-4, k), T(4, k)],
    ]) {
      const p1 = P(...pts[0]);
      const p2 = P(...pts[1]);
      ctx.beginPath();
      ctx.moveTo(...p1);
      ctx.lineTo(...p2);
      ctx.stroke();
    }
  }

  ctx.strokeStyle = "rgba(230,230,240,.9)";
  ctx.lineWidth = 1.8;
  ctx.beginPath();
  for (let i = 0; i <= 180; i += 1) {
    const t = (Math.PI * 2 * i) / 180;
    const p = P(...T(Math.cos(t), Math.sin(t)));
    if (i === 0) ctx.moveTo(...p);
    else ctx.lineTo(...p);
  }
  ctx.stroke();

  ctx.strokeStyle = "#d9bc6a";
  ctx.lineWidth = 2.6;
  for (const [x, y] of [[1, 0], [0, 1]]) {
    const p = P(...T(x, y));
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(...p);
    ctx.stroke();
  }

  ctx.fillStyle = "rgba(190,190,210,.8)";
  ctx.font = "11px monospace";
  ctx.fillText(`A = [[${A.a}, ${A.b}], [${A.c}, ${A.d}]]`, 12, height - 12);
}

function resize() {
  const el = canvas.value;
  if (!el) return;
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  width = el.parentElement.clientWidth;
  height = el.parentElement.clientHeight;
  if (!width || !height) return;
  el.width = Math.round(width * dpr);
  el.height = Math.round(height * dpr);
  el.style.width = width + "px";
  el.style.height = height + "px";
  ctx = el.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  draw();
}

watch([a, b, c, d], draw);
onMounted(() => {
  resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(canvas.value.parentElement);
  resize();
});
onBeforeUnmount(() => resizeObserver?.disconnect());
</script>

<template>
  <LabShell title="线性变换" formula="x ↦ Ax" :description="`det(A)=${det}；单位圆变成椭圆，网格随矩阵实时变形。`" @reset="reset">
    <template #stage>
      <canvas ref="canvas" aria-hidden="true"></canvas>
    </template>
    <template #controls>
      <label class="lab__control">
        <span>a <b>{{ Number(a).toFixed(1) }}</b></span>
        <input v-model.number="a" type="range" min="-2" max="2" step="0.1" />
      </label>
      <label class="lab__control">
        <span>b <b>{{ Number(b).toFixed(1) }}</b></span>
        <input v-model.number="b" type="range" min="-2" max="2" step="0.1" />
      </label>
      <label class="lab__control">
        <span>c <b>{{ Number(c).toFixed(1) }}</b></span>
        <input v-model.number="c" type="range" min="-2" max="2" step="0.1" />
      </label>
      <label class="lab__control">
        <span>d <b>{{ Number(d).toFixed(1) }}</b></span>
        <input v-model.number="d" type="range" min="-2" max="2" step="0.1" />
      </label>
      <div class="lab__presets" aria-label="线性变换预设">
        <span>预设</span>
        <button v-for="preset in presets" :key="preset.label" type="button" @click="applyPreset(preset)">
          {{ preset.label }}
        </button>
      </div>
      <div class="lab__readout">
        <span>det(A) = <b>{{ det }}</b></span>
      </div>
      <p class="lab__hint">拖动滑杆 · 观察基向量与单位圆</p>
    </template>
  </LabShell>
</template>
