<script setup>
import { onBeforeUnmount, onMounted, ref, watch } from "vue";
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import LabShell from "./LabShell.vue";
import { useLabUrl } from "./useLabUrl";

const canvas = ref(null);
const tilt = ref(35);
const azimuth = ref(30);
const lineAngle = ref(20);
const angleText = ref("");
const defaults = { tilt: 35, azimuth: 30, lineAngle: 20 };
const presets = [
  { label: "水平面", values: { tilt: 5, azimuth: 30, lineAngle: 20 } },
  { label: "倾斜面", values: { tilt: 35, azimuth: 30, lineAngle: 20 } },
  { label: "竖直面", values: { tilt: 85, azimuth: 30, lineAngle: 20 } },
];

useLabUrl({ tilt, azimuth, lineAngle });

function applyPreset(preset) {
  tilt.value = preset.values.tilt;
  azimuth.value = preset.values.azimuth;
  lineAngle.value = preset.values.lineAngle;
}

function reset() {
  tilt.value = defaults.tilt;
  azimuth.value = defaults.azimuth;
  lineAngle.value = defaults.lineAngle;
}

let renderer;
let scene;
let camera;
let controls;
let group;
let resizeObserver;
let raf = 0;

function normalVector() {
  const t = (Number(tilt.value) * Math.PI) / 180;
  const p = (Number(azimuth.value) * Math.PI) / 180;
  return new THREE.Vector3(Math.sin(t) * Math.cos(p), Math.cos(t), Math.sin(t) * Math.sin(p)).normalize();
}

function rebuild() {
  if (!group) return;
  while (group.children.length) {
    const child = group.children.pop();
    child.geometry?.dispose();
    if (Array.isArray(child.material)) child.material.forEach((m) => m.dispose());
    else child.material?.dispose();
  }

  const n = normalVector();
  const planeGeo = new THREE.PlaneGeometry(4.2, 4.2, 8, 8);
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
    opacity: 0.35,
    side: THREE.DoubleSide,
  });
  const mesh = new THREE.Mesh(planeGeo, solid);
  const wireMesh = new THREE.Mesh(planeGeo, wire);
  mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 0, 1), n);
  wireMesh.quaternion.copy(mesh.quaternion);
  group.add(mesh, wireMesh, new THREE.ArrowHelper(n, new THREE.Vector3(0, 0, 0), 1.8, 0xd9bc6a, 0.16, 0.1));

  const a = (Number(lineAngle.value) * Math.PI) / 180;
  const d = new THREE.Vector3(Math.cos(a), 0, Math.sin(a)).normalize();
  const lineGeo = new THREE.BufferGeometry().setFromPoints([
    d.clone().multiplyScalar(-2.5),
    d.clone().multiplyScalar(2.5),
  ]);
  group.add(new THREE.Line(lineGeo, new THREE.LineBasicMaterial({ color: 0x8fb7ff, linewidth: 2 })));
  group.add(new THREE.ArrowHelper(d, new THREE.Vector3(0, 0, 0), 2.2, 0x8fb7ff, 0.16, 0.1));

  const sinTheta = Math.abs(d.dot(n));
  angleText.value = (Math.asin(Math.min(1, sinTheta)) * 180 / Math.PI).toFixed(1);
}

function setup() {
  const el = canvas.value;
  if (!el) return;
  renderer = new THREE.WebGLRenderer({ canvas: el, alpha: true, antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
  renderer.setClearColor(0x000000, 0);

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
  camera.position.set(4, 3.2, 5);

  controls = new OrbitControls(camera, el);
  controls.enableDamping = true;
  controls.enablePan = false;
  controls.minDistance = 4;
  controls.maxDistance = 12;
  controls.autoRotate = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  controls.autoRotateSpeed = 0.3;

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

watch([tilt, azimuth, lineAngle], rebuild);
onMounted(setup);
onBeforeUnmount(() => {
  cancelAnimationFrame(raf);
  resizeObserver?.disconnect();
  controls?.dispose();
  renderer?.dispose();
});
</script>

<template>
  <LabShell title="直线与平面" formula="sin θ = |s · n| / (|s||n|)" description="法向量 n 决定平面朝向；方向向量 s 与它的互余角决定线面角。" @reset="reset">
    <template #stage>
      <canvas ref="canvas" aria-hidden="true"></canvas>
    </template>
    <template #controls>
      <label class="lab__control">
        <span>法向倾角 <b>{{ Number(tilt).toFixed(0) }}°</b></span>
        <input v-model.number="tilt" type="range" min="5" max="85" step="1" />
      </label>
      <label class="lab__control">
        <span>法向方位 <b>{{ Number(azimuth).toFixed(0) }}°</b></span>
        <input v-model.number="azimuth" type="range" min="0" max="360" step="1" />
      </label>
      <label class="lab__control">
        <span>直线方向 <b>{{ Number(lineAngle).toFixed(0) }}°</b></span>
        <input v-model.number="lineAngle" type="range" min="0" max="360" step="1" />
      </label>
      <div class="lab__presets" role="group" aria-label="平面朝向预设">
        <span>预设</span>
        <button v-for="preset in presets" :key="preset.label" type="button" @click="applyPreset(preset)">
          {{ preset.label }}
        </button>
      </div>
      <div class="lab__readout">
        <span>线面角 θ = <b>{{ angleText }}°</b></span>
      </div>
      <p class="lab__hint">金色平面 + 法向 n · 蓝色直线方向 s</p>
    </template>
  </LabShell>
</template>
