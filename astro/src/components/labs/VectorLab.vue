<script setup>
import { onBeforeUnmount, onMounted, ref, watch } from "vue";
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import LabShell from "./LabShell.vue";
import { useLabUrl } from "./useLabUrl";

const canvas = ref(null);
const lenA = ref(1.6);
const lenB = ref(1.3);
const angle = ref(55);
const dot = ref("");
const crossLen = ref("");
const crossValue = ref("");
const defaults = { lenA: 1.6, lenB: 1.3, angle: 55 };
const presets = [
  { label: "垂直", values: { lenA: 1.6, lenB: 1.3, angle: 90 } },
  { label: "平行", values: { lenA: 1.6, lenB: 1.3, angle: 0 } },
  { label: "60°", values: { lenA: 1.6, lenB: 1.3, angle: 60 } },
];

useLabUrl({ lenA, lenB, angle });

function applyPreset(preset) {
  lenA.value = preset.values.lenA;
  lenB.value = preset.values.lenB;
  angle.value = preset.values.angle;
}

function reset() {
  lenA.value = defaults.lenA;
  lenB.value = defaults.lenB;
  angle.value = defaults.angle;
}

let renderer;
let scene;
let camera;
let controls;
let group;
let resizeObserver;
let raf = 0;

function rebuild() {
  if (!group) return;
  while (group.children.length) {
    const child = group.children.pop();
    child.geometry?.dispose();
    if (Array.isArray(child.material)) child.material.forEach((m) => m.dispose());
    else child.material?.dispose();
  }

  const rad = (Number(angle.value) * Math.PI) / 180;
  const a = new THREE.Vector3(Number(lenA.value), 0, 0);
  const b = new THREE.Vector3(Math.cos(rad) * Number(lenB.value), Math.sin(rad) * Number(lenB.value), 0);
  const cross = a.clone().cross(b);

  group.add(new THREE.ArrowHelper(a.clone().normalize(), new THREE.Vector3(0, 0, 0), a.length(), 0xd9bc6a, 0.16, 0.1));
  group.add(new THREE.ArrowHelper(b.clone().normalize(), new THREE.Vector3(0, 0, 0), b.length(), 0x8fb7ff, 0.16, 0.1));
  if (cross.length() > 0.001) {
    group.add(new THREE.ArrowHelper(cross.clone().normalize(), new THREE.Vector3(0, 0, 0), Math.min(cross.length(), 2.2), 0xff9a9a, 0.14, 0.09));
  }

  const pts = [
    new THREE.Vector3(0, 0, 0),
    a,
    a.clone().add(b),
    b,
    new THREE.Vector3(0, 0, 0),
  ];
  group.add(new THREE.Line(
    new THREE.BufferGeometry().setFromPoints(pts),
    new THREE.LineBasicMaterial({ color: 0xd9bc6a, transparent: true, opacity: 0.35 })
  ));

  dot.value = a.dot(b).toFixed(2);
  crossLen.value = cross.length().toFixed(2);
  crossValue.value = cross.z.toFixed(2);
}

function setup() {
  const el = canvas.value;
  if (!el) return;
  renderer = new THREE.WebGLRenderer({ canvas: el, alpha: true, antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
  renderer.setClearColor(0x000000, 0);

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
  camera.position.set(3.2, 2.4, 4);

  controls = new OrbitControls(camera, el);
  controls.enableDamping = true;
  controls.enablePan = false;
  controls.minDistance = 3;
  controls.maxDistance = 12;
  controls.autoRotate = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  controls.autoRotateSpeed = 0.35;

  const grid = new THREE.GridHelper(6, 12, 0x5a6588, 0x2c3450);
  grid.position.y = -1.6;
  grid.material.transparent = true;
  grid.material.opacity = 0.5;
  scene.add(grid);
  const axes = new THREE.AxesHelper(2.4);
  axes.material.transparent = true;
  axes.material.opacity = 0.65;
  scene.add(axes);

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

watch([lenA, lenB, angle], rebuild);
onMounted(setup);
onBeforeUnmount(() => {
  cancelAnimationFrame(raf);
  resizeObserver?.disconnect();
  controls?.dispose();
  renderer?.dispose();
});
</script>

<template>
  <LabShell title="向量与度量" formula="a · b, |a × b|" description="点积管角度，叉积管面积；拖动旋转看第三个方向。" @reset="reset">
    <template #stage>
      <canvas ref="canvas" aria-hidden="true"></canvas>
    </template>
    <template #controls>
      <label class="lab__control">
        <span>|a| <b>{{ Number(lenA).toFixed(2) }}</b></span>
        <input v-model.number="lenA" type="range" min="0.4" max="2.5" step="0.05" />
      </label>
      <label class="lab__control">
        <span>|b| <b>{{ Number(lenB).toFixed(2) }}</b></span>
        <input v-model.number="lenB" type="range" min="0.4" max="2.5" step="0.05" />
      </label>
      <label class="lab__control">
        <span>夹角 θ <b>{{ Number(angle).toFixed(0) }}°</b></span>
        <input v-model.number="angle" type="range" min="0" max="180" step="1" />
      </label>
      <div class="lab__presets" role="group" aria-label="向量参数预设">
        <span>预设</span>
        <button v-for="preset in presets" :key="preset.label" type="button" @click="applyPreset(preset)">
          {{ preset.label }}
        </button>
      </div>
      <div class="lab__readout">
        <span>a · b = <b>{{ dot }}</b></span>
        <span>|a × b| = <b>{{ crossLen }}</b></span>
        <span>(a × b)ᶻ = <b>{{ crossValue }}</b></span>
      </div>
      <p class="lab__hint">金色 a · 蓝色 b · 红色叉积</p>
    </template>
  </LabShell>
</template>
