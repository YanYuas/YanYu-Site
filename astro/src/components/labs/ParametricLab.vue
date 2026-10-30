<script setup>
import { onBeforeUnmount, onMounted, ref, watch } from "vue";
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import LabShell from "./LabShell.vue";
import { useLabUrl } from "./useLabUrl";

const canvas = ref(null);
const shape = ref("torus");
const R = ref(1.2);
const r = ref(0.42);
const copy = ref("环面：两个半径 R、r 决定胖瘦；沿 u 方向闭合。");
const defaults = { shape: "torus", R: 1.2, r: 0.42 };

useLabUrl({ shape, R, r });

function reset() {
  shape.value = defaults.shape;
  R.value = defaults.R;
  r.value = defaults.r;
}

let renderer;
let scene;
let camera;
let controls;
let group;
let resizeObserver;
let raf = 0;

function parametric(fn, uSeg, vSeg, uMax, vMax) {
  const positions = [];
  const indices = [];
  const stride = vSeg + 1;
  for (let i = 0; i <= uSeg; i += 1) {
    const u = (uMax * i) / uSeg;
    for (let j = 0; j <= vSeg; j += 1) {
      const v = (vMax * j) / vSeg;
      positions.push(...fn(u, v));
    }
  }
  for (let i = 0; i < uSeg; i += 1) {
    for (let j = 0; j < vSeg; j += 1) {
      const a = i * stride + j;
      const b = a + stride;
      indices.push(a, b, a + 1, b, b + 1, a + 1);
    }
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3));
  g.setIndex(indices);
  return g;
}

function geometry() {
  const RR = Number(R.value);
  const rr = Number(r.value);
  if (shape.value === "mobius") {
    return parametric(
      (u, v) => {
        const t = (v - 0.5) * 2 * rr;
        const c = Math.cos(u / 2);
        return [(RR + t * c) * Math.cos(u), t * Math.sin(u / 2), (RR + t * c) * Math.sin(u)];
      },
      160,
      8,
      Math.PI * 2,
      1
    );
  }
  return parametric(
    (u, v) => [(RR + rr * Math.cos(v)) * Math.cos(u), rr * Math.sin(v), (RR + rr * Math.cos(v)) * Math.sin(u)],
    80,
    28,
    Math.PI * 2,
    Math.PI * 2
  );
}

function rebuild() {
  if (!group) return;
  while (group.children.length) {
    const child = group.children.pop();
    child.geometry?.dispose();
    if (Array.isArray(child.material)) child.material.forEach((m) => m.dispose());
    else child.material?.dispose();
  }
  const g = geometry();
  const solid = new THREE.MeshBasicMaterial({
    color: 0xd9bc6a,
    transparent: true,
    opacity: 0.08,
    side: THREE.DoubleSide,
    depthWrite: false,
  });
  const wire = new THREE.MeshBasicMaterial({
    color: 0xd9bc6a,
    wireframe: true,
    transparent: true,
    opacity: 0.5,
    side: THREE.DoubleSide,
  });
  const m = new THREE.Mesh(g, solid);
  const w = new THREE.Mesh(g, wire);
  if (shape.value === "mobius") {
    m.rotation.x = -0.85;
    w.rotation.x = -0.85;
    copy.value = "莫比乌斯环：只有一个面；沿中线走一圈，法向量会反向。";
  } else {
    copy.value = "环面：两个半径 R、r 决定胖瘦；沿 u 方向闭合。";
  }
  group.add(m, w);
}

function setup() {
  const el = canvas.value;
  if (!el) return;
  renderer = new THREE.WebGLRenderer({ canvas: el, alpha: true, antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
  renderer.setClearColor(0x000000, 0);

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
  camera.position.set(4, 3, 5);

  controls = new OrbitControls(camera, el);
  controls.enableDamping = true;
  controls.enablePan = false;
  controls.minDistance = 4;
  controls.maxDistance = 12;
  controls.autoRotate = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  controls.autoRotateSpeed = 0.4;

  const grid = new THREE.GridHelper(6, 12, 0x4a5578, 0x252c44);
  grid.position.y = -2;
  grid.material.transparent = true;
  grid.material.opacity = 0.35;
  scene.add(grid);

  group = new THREE.Group();
  scene.add(group);
  rebuild();

  const resize = () => {
    const parent = el.parentElement;
    const w = parent.clientWidth;
    const h = parent.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  };
  resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(el.parentElement);
  resize();

  const frame = () => {
    controls.update();
    renderer.render(scene, camera);
    raf = requestAnimationFrame(frame);
  };
  frame();
}

watch([shape, R, r], rebuild);
onMounted(setup);
onBeforeUnmount(() => {
  cancelAnimationFrame(raf);
  resizeObserver?.disconnect();
  controls?.dispose();
  renderer?.dispose();
});
</script>

<template>
  <LabShell title="参数曲面" :formula="shape === 'torus' ? 'r(u,v)=(R+r cos v)(cos u, sin u)' : '莫比乌斯参数方程'" :description="copy" @reset="reset">
    <template #stage>
      <canvas ref="canvas" aria-hidden="true"></canvas>
    </template>
    <template #controls>
      <div class="lab__tabs" role="tablist" aria-label="参数曲面">
        <button :class="{ 'is-active': shape === 'torus' }" @click="shape = 'torus'">环面</button>
        <button :class="{ 'is-active': shape === 'mobius' }" @click="shape = 'mobius'">莫比乌斯环</button>
      </div>
      <label class="lab__control">
        <span>大半径 R <b>{{ Number(R).toFixed(2) }}</b></span>
        <input v-model.number="R" type="range" min="0.8" max="1.8" step="0.05" />
      </label>
      <label class="lab__control">
        <span>管径/带宽 r <b>{{ Number(r).toFixed(2) }}</b></span>
        <input v-model.number="r" type="range" min="0.15" max="0.8" step="0.01" />
      </label>
      <p class="lab__hint">拖动旋转 · 滚轮缩放 · 切换拓扑</p>
    </template>
  </LabShell>
</template>
