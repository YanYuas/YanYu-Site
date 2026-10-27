import {
  Scene,
  PerspectiveCamera,
  WebGLRenderer,
  Group,
  Mesh,
  MeshBasicMaterial,
  BufferGeometry,
  Float32BufferAttribute,
  Points,
  PointsMaterial,
  Color,
  DoubleSide,
  SRGBColorSpace,
  MathUtils,
} from "three";

// ------------------------------------------------------------
// 四种曲面 / 曲面的展示顺序
// 每个形状都在同一个中心、同一相机下建模，切换时只做淡入淡出 +
// 轻微缩放，不做“形变”，避免拓扑不一致时出现穿模。
// ------------------------------------------------------------
const SURFACES = [
  {
    key: "ellipsoid",
    no: "01",
    name: "椭球面",
    formula: "xᵀAx = 1",
    dwell: 8000,
    build: () =>
      parametric(
        (u, v) => {
          const s = Math.sin(v);
          return [1.55 * s * Math.cos(u), 1.02 * Math.cos(v), 1.12 * s * Math.sin(u)];
        },
        64,
        40,
        Math.PI * 2,
        Math.PI
      ),
  },
  {
    key: "hyperboloid",
    no: "02",
    name: "单叶双曲面",
    formula: "x² + y² − z² = 1",
    dwell: 8000,
    build: () =>
      parametric(
        (u, v) => {
          const t = (v - 0.5) * 2.4;
          const r = Math.sqrt(1 + t * t);
          return [1.12 * r * Math.cos(u), 1.2 * t, 1.12 * r * Math.sin(u)];
        },
        64,
        36,
        Math.PI * 2,
        1
      ),
  },
  {
    key: "saddle",
    no: "03",
    name: "马鞍面",
    formula: "z = x² − y²",
    dwell: 8000,
    build: () =>
      parametric(
        (u, v) => {
          const r = v * 1.3;
          const x = r * Math.cos(u);
          const z = r * Math.sin(u);
          return [x, 0.8 * (x * x - z * z), z];
        },
        64,
        32,
        Math.PI * 2,
        1
      ),
  },
  {
    key: "mobius",
    no: "04",
    name: "莫比乌斯环",
    formula: "只有一个面 · 非定向",
    dwell: 9000,
    build: () =>
      parametric(
        (u, v) => {
          const t = (v - 0.5) * 0.96; // 带宽
          const c = Math.cos(u / 2);
          return [
            (1.28 + t * c) * Math.cos(u),
            t * Math.sin(u / 2),
            (1.28 + t * c) * Math.sin(u),
          ];
        },
        180,
        8,
        Math.PI * 2,
        1
      ),
  },
];

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

function easeInOutCubic(t) {
  return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

export function initHero3D(canvas) {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const renderer = new WebGLRenderer({
    canvas,
    alpha: true,
    antialias: true,
    powerPreference: "high-performance",
  });

  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
  renderer.setClearColor(0x000000, 0);
  renderer.outputColorSpace = SRGBColorSpace;

  const scene = new Scene();
  const camera = new PerspectiveCamera(38, 1, 0.1, 100);
  camera.position.set(0, 0.15, 5.4);

  const accent =
    getComputedStyle(document.body).getPropertyValue("--sa-gold").trim() || "#d9bc6a";
  const gold = new Color(accent);

  const group = new Group();
  group.rotation.set(-0.22, -0.5, 0);
  scene.add(group);

  const materialOptions = {
    color: gold,
    wireframe: true,
    transparent: true,
    opacity: 0.62,
    side: DoubleSide,
  };

  // 背景星点
  const starCount = 220;
  const starPositions = new Float32Array(starCount * 3);
  for (let i = 0; i < starCount; i += 1) {
    const r = 4.2 + Math.random() * 3.2;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(2 * Math.random() - 1);
    starPositions[i * 3] = r * Math.sin(phi) * Math.cos(theta);
    starPositions[i * 3 + 1] = r * Math.cos(phi);
    starPositions[i * 3 + 2] = r * Math.sin(phi) * Math.sin(theta);
  }
  const starGeometry = new BufferGeometry();
  starGeometry.setAttribute("position", new Float32BufferAttribute(starPositions, 3));
  const stars = new Points(
    starGeometry,
    new PointsMaterial({
      color: gold,
      size: 0.032,
      transparent: true,
      opacity: 0.55,
      sizeAttenuation: true,
    })
  );
  scene.add(stars);

  // HUD：01 / 椭球面 / xᵀAx = 1
  const noEl = document.getElementById("hero-3d-no");
  const nameEl = document.getElementById("hero-3d-name");
  const formulaEl = document.getElementById("hero-3d-formula");
  const dotsEl = document.getElementById("hero-3d-dots");
  const dots = [];

  if (dotsEl) {
    SURFACES.forEach((surface, index) => {
      const dot = document.createElement("span");
      dot.dataset.index = String(index);
      if (index === 0) dot.classList.add("is-active");
      dotsEl.appendChild(dot);
      dots.push(dot);
    });
  }

  function setHUD(index) {
    const surface = SURFACES[index];
    if (noEl) noEl.textContent = surface.no;
    if (nameEl) nameEl.textContent = surface.name;
    if (formulaEl) formulaEl.textContent = surface.formula;
    dots.forEach((dot, dotIndex) => {
      dot.classList.toggle("is-active", dotIndex === index);
    });
  }

  function makeObject(index) {
    const surface = SURFACES[index];
    const geometry = surface.build();
    const material = new MeshBasicMaterial({ ...materialOptions });
    const mesh = new Mesh(geometry, material);
    if (surface.key === "mobius") {
      // 莫比乌斯环的带面在 xz 平面上，稍微立起来才能看到扭转
      mesh.rotation.x = -0.9;
    }
    group.add(mesh);
    return { surface, mesh, geometry, material };
  }

  let current = makeObject(0);
  let transition = null;
  let currentIndex = 0;
  let paused = false;
  let nextSwitchAt = performance.now() + SURFACES[0].dwell;
  setHUD(0);

  const wrapper = canvas.parentElement;
  const onEnter = () => {
    paused = true;
  };
  const onLeave = () => {
    paused = false;
    // 离开时重新给当前形状一个完整停留时间，避免立刻切换
    nextSwitchAt = performance.now() + current.surface.dwell;
  };
  if (!reduceMotion) {
    wrapper.addEventListener("pointerenter", onEnter);
    wrapper.addEventListener("pointerleave", onLeave);
  }

  const pointer = { x: 0, y: 0 };
  const onPointerMove = (event) => {
    pointer.x = (event.clientX / window.innerWidth - 0.5) * 2;
    pointer.y = (event.clientY / window.innerHeight - 0.5) * 2;
  };
  if (!reduceMotion) {
    window.addEventListener("pointermove", onPointerMove, { passive: true });
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

  const resizeObserver = new ResizeObserver(() => {
    resize();
    if (reduceMotion) renderer.render(scene, camera);
  });
  resizeObserver.observe(canvas.parentElement);
  resize();

  let visible = true;
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(([entry]) => {
      visible = entry.isIntersecting;
    }).observe(canvas);
  }

  function startTransition(index, now) {
    if (transition) return;
    const next = makeObject(index);
    next.material.opacity = 0;
    next.mesh.scale.setScalar(0.94);
    transition = {
      from: current,
      to: next,
      start: now,
      duration: 760,
    };
    current = next;
    currentIndex = index;
    nextSwitchAt = now + next.surface.dwell;
    setHUD(index);
  }

  let raf = 0;
  function frame() {
    const now = performance.now();

    if (!reduceMotion && !transition && visible && !document.hidden && !paused && now >= nextSwitchAt) {
      startTransition((currentIndex + 1) % SURFACES.length, now);
    }

    if (transition) {
      const t = Math.min(1, (now - transition.start) / transition.duration);
      const eased = easeInOutCubic(t);
      transition.from.material.opacity = materialOptions.opacity * (1 - eased);
      transition.from.mesh.scale.setScalar(1 + 0.04 * eased);
      transition.to.material.opacity = materialOptions.opacity * eased;
      transition.to.mesh.scale.setScalar(0.94 + 0.06 * eased);

      if (t >= 1) {
        group.remove(transition.from.mesh);
        transition.from.geometry.dispose();
        transition.from.material.dispose();
        transition = null;
      }
    }

    if (visible && !document.hidden) {
      group.rotation.y += 0.0016;
      group.rotation.x = MathUtils.lerp(group.rotation.x, -0.22 + pointer.y * 0.1, 0.04);
      group.rotation.z = MathUtils.lerp(group.rotation.z, pointer.x * 0.05, 0.04);
      stars.rotation.y -= 0.0004;
      renderer.render(scene, camera);
    }

    raf = requestAnimationFrame(frame);
  }

  if (reduceMotion) {
    renderer.render(scene, camera);
  } else {
    frame();
  }

  return () => {
    cancelAnimationFrame(raf);
    resizeObserver.disconnect();
    window.removeEventListener("pointermove", onPointerMove);
    wrapper.removeEventListener("pointerenter", onEnter);
    wrapper.removeEventListener("pointerleave", onLeave);
    if (transition) {
      transition.to.geometry.dispose();
      transition.to.material.dispose();
      transition = null;
    }
    current.geometry.dispose();
    current.material.dispose();
    starGeometry.dispose();
    stars.material.dispose();
    renderer.dispose();
  };
}
