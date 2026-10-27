<script setup>
import { onBeforeUnmount, onMounted, ref, watch } from "vue";
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const canvas = ref(null);
const shape = ref("ellipsoid");
const scale = ref(1.2);
const copy = ref("三个主方向都被缩放；拖动旋转可以看到椭球的三个半轴。");

let renderer;
let scene;
let camera;
let controls;
let group;
let resizeObserver;
let raf = 0;

const LABELS = {
  ellipsoid: "椭球面",
  hyperboloid: "单叶双曲面",
  saddle: "马鞍面",
};

const COPY = {
  ellipsoid: "三个主方向都被缩放；拖动旋转可以看到椭球的三个半轴。",
  hyperboloid: "x² + y² − z² = 1；沿 z 轴无限延伸，颈部最细。",
  saddle: "z = x² − y²；两个主方向曲率相反，典型的鞍点几何。",
};

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
  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3));
  geometry.setIndex(indices);
  return geometry;
}

function geometryFor() {
  const a = scale.value;
  if (shape.value === "hyperboloid") {
    return parametric(
      (u, v) => {
        const t = (v - 0.5) * 2.4;
        const r = Math.sqrt(1 + t * t);
        return [1.05 * a * r * Math.cos(u), 1.1 * a * t, 1.05 * a * r * Math.sin(u)];
      },
      64,
      36,
      Math.PI * 2,
      1
    );
  }
  if (shape.value === "saddle") {
    return parametric(
      (u, v) => {
        const r = v * 1.22 * a;
        const x = r * Math.cos(u);
        const z = r * Math.sin(u);
        return [x, 0.78 * (x * x - z * z), z];
      },
      64,
      32,
      Math.PI * 2,
      1
    );
  }
  return parametric(
    (u, v) => {
      const s = Math.sin(v);
      return [1.45 * a * s * Math.cos(u), 0.98 * a * Math.cos(v), 1.08 * a * s * Math.sin(u)];
    },
    64,
    40,
    Math.PI * 2,
    Math.PI
  );
}

function clear() {
  if (!group) return;
  while (group.children.length) {
    const child = group.children.pop();
    child.geometry?.dispose();
    if (Array.isArray(child.material)) child.material.forEach((m) => m.dispose());
    else child.material?.dispose();
  }
}

function rebuild() {
  if (!group) return;
  clear();
  const geometry = geometryFor();
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
    opacity: 0.55,
    side: THREE.DoubleSide,
  });
  group.add(new THREE.Mesh(geometry, solid));
  group.add(new THREE.Mesh(geometry, wire));
  copy.value = COPY[shape.value];
}

function setup() {
  const el = canvas.value;
  if (!el) return;
  renderer = new THREE.WebGLRenderer({ canvas: el, alpha: true, antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
  renderer.setClearColor(0x000000, 0);

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
  camera.position.set(3.8, 2.8, 4.6);

  controls = new OrbitControls(camera, el);
  controls.enableDamping = true;
  controls.enablePan = false;
  controls.minDistance = 3;
  controls.maxDistance = 10;
  controls.autoRotate = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  controls.autoRotateSpeed = 0.45;

  const grid = new THREE.GridHelper(6, 12, 0x4a5578, 0x252c44);
  grid.position.y = -1.7;
  grid.material.transparent = true;
  grid.material.opacity = 0.35;
  scene.add(grid);

  const axes = new THREE.AxesHelper(2.2);
  axes.position.y = -1.7;
  axes.material.transparent = true;
  axes.material.opacity = 0.55;
  scene.add(axes);

  group = new THREE.Group();
  scene.add(group);
  rebuild();

  const resize = () => {
    const parent = el.parentElement;
    const width = parent.clientWidth;
    const height = parent.clientHeight;
    if (!width || !height) return;
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
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

watch([shape, scale], rebuild);

onMounted(setup);

onBeforeUnmount(() => {
  cancelAnimationFrame(raf);
  resizeObserver?.disconnect();
  clear();
  controls?.dispose();
  renderer?.dispose();
});
</script>

<template>
  <div class="lab" id="quadric">
    <div class="lab__stage">
      <canvas ref="canvas"></canvas>
    </div>
    <aside class="lab__panel">
      <div class="lab__tabs" role="tablist" aria-label="曲面类型">
        <button
          v-for="[key, label] in Object.entries(LABELS)"
          :key="key"
          :class="{ 'is-active': shape === key }"
          @click="shape = key"
        >
          {{ label }}
        </button>
      </div>
      <label class="lab__control">
        <span>尺度 a <b>{{ scale.toFixed(2) }}</b></span>
        <input v-model.number="scale" type="range" min="0.6" max="1.8" step="0.05" />
      </label>
      <p class="lab__desc">{{ copy }}</p>
      <p class="lab__hint">拖动旋转 · 滚轮缩放 · 切换曲面</p>
    </aside>
  </div>
</template>
