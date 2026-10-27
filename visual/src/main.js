import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const canvas = document.querySelector("#scene");
const fallback = document.querySelector("#fallback");
const hint = document.querySelector("#hint");
const buttons = [...document.querySelectorAll(".mode")];

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const GOLD = 0xd8b25c;

let renderer;
try {
  renderer = new THREE.WebGLRenderer({
    canvas,
    antialias: true,
    alpha: true,
    powerPreference: "high-performance",
  });
} catch (error) {
  canvas.hidden = true;
  fallback.hidden = false;
  hint.textContent = "WebGL 不可用";
  console.warn("WebGL unavailable:", error);
}

if (renderer) {
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
  camera.position.set(3.4, 2.5, 4.3);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.enablePan = false;
  controls.minDistance = 2.6;
  controls.maxDistance = 9;
  controls.autoRotate = !reduceMotion;
  controls.autoRotateSpeed = 0.55;

  scene.add(new THREE.AmbientLight(0x8492b8, 1.4));
  const key = new THREE.DirectionalLight(0xffd9a0, 2.4);
  key.position.set(5, 7, 4);
  scene.add(key);
  const rim = new THREE.PointLight(0x7c9cff, 18, 24, 2);
  rim.position.set(-4, -2, -5);
  scene.add(rim);

  // 背景里少量金色星点，和站点首页的粒子/星空语言一致
  scene.add(makeStars());

  const group = new THREE.Group();
  scene.add(group);

  const solidMaterial = new THREE.MeshPhysicalMaterial({
    color: GOLD,
    metalness: 0.25,
    roughness: 0.3,
    transparent: true,
    opacity: 0.1,
    side: THREE.DoubleSide,
    depthWrite: false,
  });

  const wireMaterial = new THREE.MeshBasicMaterial({
    color: GOLD,
    wireframe: true,
    transparent: true,
    opacity: 0.62,
    side: THREE.DoubleSide,
  });

  const surfaces = {
    ellipsoid: {
      label: "椭球面",
      uMax: Math.PI * 2,
      vMax: Math.PI,
      uSeg: 72,
      vSeg: 44,
      point(u, v) {
        const s = Math.sin(v);
        return [1.55 * s * Math.cos(u), 1.02 * Math.cos(v), 1.12 * s * Math.sin(u)];
      },
    },
    hyperboloid: {
      label: "单叶双曲面",
      uMax: Math.PI * 2,
      vMax: 1,
      uSeg: 72,
      vSeg: 36,
      point(u, v) {
        const t = (v - 0.5) * 2.4;
        const r = Math.sqrt(1 + t * t);
        return [1.1 * r * Math.cos(u), 1.15 * t, 1.1 * r * Math.sin(u)];
      },
    },
    paraboloid: {
      label: "双曲抛物面",
      uMax: Math.PI * 2,
      vMax: 1,
      uSeg: 72,
      vSeg: 36,
      point(u, v) {
        const r = v * 1.28;
        const x = r * Math.cos(u);
        const z = r * Math.sin(u);
        return [x, 0.82 * (x * x - z * z) - 0.35, z];
      },
    },
  };

  let currentKey = "ellipsoid";

  function makeGeometry(surface) {
    const positions = [];
    const indices = [];
    const stride = surface.vSeg + 1;

    for (let i = 0; i <= surface.uSeg; i += 1) {
      const u = (surface.uMax * i) / surface.uSeg;
      for (let j = 0; j <= surface.vSeg; j += 1) {
        const v = (surface.vMax * j) / surface.vSeg;
        positions.push(...surface.point(u, v));
      }
    }

    for (let i = 0; i < surface.uSeg; i += 1) {
      for (let j = 0; j < surface.vSeg; j += 1) {
        const a = i * stride + j;
        const b = a + stride;
        indices.push(a, b, a + 1, b, b + 1, a + 1);
      }
    }

    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3));
    geometry.setIndex(indices);
    geometry.computeVertexNormals();
    return geometry;
  }

  function setSurface(key) {
    const surface = surfaces[key];
    if (!surface) return;
    currentKey = key;

    while (group.children.length) {
      const child = group.children.pop();
      child.geometry?.dispose();
    }

    const geometry = makeGeometry(surface);
    group.add(new THREE.Mesh(geometry, solidMaterial));
    group.add(new THREE.Mesh(geometry, wireMaterial));

    buttons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.surface === key);
      button.setAttribute("aria-pressed", String(button.dataset.surface === key));
    });
  }

  function makeStars() {
    const count = 260;
    const positions = new Float32Array(count * 3);
    for (let i = 0; i < count; i += 1) {
      const r = 6 + Math.random() * 7;
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos(2 * Math.random() - 1);
      positions[i * 3] = r * Math.sin(phi) * Math.cos(theta);
      positions[i * 3 + 1] = r * Math.cos(phi);
      positions[i * 3 + 2] = r * Math.sin(phi) * Math.sin(theta);
    }
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    return new THREE.Points(
      geometry,
      new THREE.PointsMaterial({
        color: GOLD,
        size: 0.035,
        transparent: true,
        opacity: 0.5,
        sizeAttenuation: true,
      })
    );
  }

  function resize() {
    const parent = canvas.parentElement;
    const width = parent.clientWidth;
    const height = parent.clientHeight;
    if (!width || !height) return;
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
  }

  function animate() {
    controls.update();
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }

  buttons.forEach((button) => {
    button.addEventListener("click", () => setSurface(button.dataset.surface));
  });

  window.addEventListener("resize", resize);
  if ("ResizeObserver" in window) {
    new ResizeObserver(resize).observe(canvas.parentElement);
  }

  if (reduceMotion) {
    hint.textContent = "已按系统设置关闭自动旋转 · 可手动拖动";
  }
  window.matchMedia("(prefers-reduced-motion: reduce)").addEventListener?.("change", (event) => {
    controls.autoRotate = !event.matches;
  });

  setSurface(currentKey);
  resize();
  animate();

  // 给控制台一个方便调试的入口，也方便后续接入 MkDocs 时复用
  window.__VISUAL_LAB__ = { scene, camera, renderer, setSurface, surfaces, currentKey };
}
