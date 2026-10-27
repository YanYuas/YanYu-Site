import {
  Scene,
  PerspectiveCamera,
  WebGLRenderer,
  Group,
  Mesh,
  MeshBasicMaterial,
  BufferGeometry,
  Float32BufferAttribute,
  Color,
  DoubleSide,
  SRGBColorSpace,
  GridHelper,
  AxesHelper,
  PlaneGeometry,
  ArrowHelper,
  Vector3,
} from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const DEFAULTS = {
  ellipsoid: 1.2,
  hyperboloid: 1.2,
  saddle: 1.2,
};

const COPY = {
  ellipsoid: "x²/a² + y²/b² + z²/c² = 1；三个主方向都被缩放，拖动旋转可以看到三个半轴。",
  hyperboloid: "x² + y² − z² = 1；单叶双曲面，沿 z 轴无限延伸，颈部最细。",
  saddle: "z = x² − y²；两个主方向曲率相反，是典型的鞍点几何。",
  plane: "Ax + By + Cz = D；法向量 n=(A,B,C) 决定平面的朝向，箭头就是 n。",
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

  const geometry = new BufferGeometry();
  geometry.setAttribute("position", new Float32BufferAttribute(positions, 3));
  geometry.setIndex(indices);
  return geometry;
}

function quadricGeometry(key, a) {
  if (key === "ellipsoid") {
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

  if (key === "hyperboloid") {
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

export function initAnalyticLab() {
  const canvas = document.getElementById("geo-canvas");
  if (!canvas) return;

  const fallback = document.getElementById("geo-fallback");
  const desc = document.getElementById("geo-desc");
  const slider = document.getElementById("geo-a");
  const sliderWrap = slider ? slider.closest(".geo-lab__control") : null;
  const tabs = Array.from(document.querySelectorAll(".geo-lab__tabs button"));

  let renderer;
  try {
    renderer = new WebGLRenderer({
      canvas,
      alpha: true,
      antialias: true,
      powerPreference: "high-performance",
    });
  } catch (error) {
    canvas.hidden = true;
    if (fallback) fallback.hidden = false;
    console.warn("Analytic lab WebGL unavailable:", error);
    return;
  }

  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
  renderer.setClearColor(0x000000, 0);
  renderer.outputColorSpace = SRGBColorSpace;

  const scene = new Scene();
  const camera = new PerspectiveCamera(42, 1, 0.1, 100);
  camera.position.set(3.8, 2.8, 4.6);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.enablePan = false;
  controls.minDistance = 3;
  controls.maxDistance = 10;
  controls.autoRotate = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  controls.autoRotateSpeed = 0.45;

  const accent =
    getComputedStyle(document.body).getPropertyValue("--sa-gold").trim() || "#d9bc6a";
  const gold = new Color(accent);

  const grid = new GridHelper(6, 12, 0x4a5578, 0x252c44);
  grid.position.y = -1.7;
  grid.material.transparent = true;
  grid.material.opacity = 0.35;
  scene.add(grid);

  const axes = new AxesHelper(2.2);
  axes.position.y = -1.7;
  axes.material.transparent = true;
  axes.material.opacity = 0.55;
  scene.add(axes);

  const group = new Group();
  scene.add(group);

  let current = "ellipsoid";
  let currentA = DEFAULTS.ellipsoid;

  function clearGroup() {
    while (group.children.length) {
      const child = group.children.pop();
      child.geometry?.dispose();
      if (Array.isArray(child.material)) {
        child.material.forEach((material) => material.dispose());
      } else {
        child.material?.dispose();
      }
    }
  }

  function makePlane() {
    const geometry = new PlaneGeometry(4.2, 4.2, 10, 10);
    const solid = new MeshBasicMaterial({
      color: gold,
      transparent: true,
      opacity: 0.1,
      side: DoubleSide,
    });
    const wire = new MeshBasicMaterial({
      color: gold,
      wireframe: true,
      transparent: true,
      opacity: 0.5,
      side: DoubleSide,
    });
    const mesh = new Mesh(geometry, solid);
    const wireMesh = new Mesh(geometry, wire);

    const normal = new Vector3(0.55, 1, 0.32).normalize();
    // PlaneGeometry 默认在 XY 平面、法向 +Z；把它转到目标法向
    mesh.quaternion.setFromUnitVectors(new Vector3(0, 0, 1), normal);
    wireMesh.quaternion.copy(mesh.quaternion);

    group.add(mesh, wireMesh);
    group.add(new ArrowHelper(normal, new Vector3(0, 0, 0), 1.7, gold, 0.16, 0.1));
  }

  function render() {
    clearGroup();
    if (current === "plane") {
      makePlane();
    } else {
      const geometry = quadricGeometry(current, currentA);
      const solid = new MeshBasicMaterial({
        color: gold,
        transparent: true,
        opacity: 0.08,
        side: DoubleSide,
        depthWrite: false,
      });
      const wire = new MeshBasicMaterial({
        color: gold,
        wireframe: true,
        transparent: true,
        opacity: 0.55,
        side: DoubleSide,
      });
      group.add(new Mesh(geometry, solid));
      group.add(new Mesh(geometry, wire));
    }

    if (desc) desc.textContent = COPY[current];
    if (sliderWrap) sliderWrap.classList.toggle("is-disabled", current === "plane");
    if (slider) slider.disabled = current === "plane";
  }

  function setShape(key) {
    current = key;
    currentA = DEFAULTS[key] || 1.2;
    if (slider) slider.value = String(currentA);
    tabs.forEach((tab) => {
      const active = tab.dataset.geo === key;
      tab.classList.toggle("is-active", active);
      tab.setAttribute("aria-selected", String(active));
    });
    render();
  }

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => setShape(tab.dataset.geo));
  });

  if (slider) {
    slider.addEventListener("input", () => {
      currentA = Number.parseFloat(slider.value) || 1.2;
      if (current !== "plane") render();
    });
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

  const resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(canvas.parentElement);
  resize();

  let visible = true;
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(([entry]) => {
      visible = entry.isIntersecting;
    }).observe(canvas);
  }

  let raf = 0;
  function frame() {
    controls.update();
    if (visible && !document.hidden) renderer.render(scene, camera);
    raf = requestAnimationFrame(frame);
  }

  render();
  frame();

  return () => {
    cancelAnimationFrame(raf);
    resizeObserver.disconnect();
    clearGroup();
    controls.dispose();
    renderer.dispose();
  };
}
