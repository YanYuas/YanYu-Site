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

/**
 * 首页 hero 的三维点缀：一个缓慢旋转的二次型线框 + 星点。
 * 只负责渲染，不处理布局；加载时机由 docs/javascripts/home-3d.js 控制。
 */
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
    getComputedStyle(document.body).getPropertyValue("--sa-gold").trim() ||
    "#d9bc6a";
  const gold = new Color(accent);

  const group = new Group();
  group.rotation.set(-0.22, -0.5, 0);
  scene.add(group);

  const surfaceMaterial = new MeshBasicMaterial({
    color: gold,
    wireframe: true,
    transparent: true,
    opacity: 0.62,
    side: DoubleSide,
  });

  // 椭球面：二次型 xᵀAx = 1 的典型形状
  const geometry = new BufferGeometry();
  const positions = [];
  const indices = [];
  const uSeg = 54;
  const vSeg = 34;
  const stride = vSeg + 1;

  for (let i = 0; i <= uSeg; i += 1) {
    const u = (Math.PI * 2 * i) / uSeg;
    for (let j = 0; j <= vSeg; j += 1) {
      const v = (Math.PI * j) / vSeg;
      const s = Math.sin(v);
      positions.push(1.55 * s * Math.cos(u), 1.02 * Math.cos(v), 1.12 * s * Math.sin(u));
    }
  }
  for (let i = 0; i < uSeg; i += 1) {
    for (let j = 0; j < vSeg; j += 1) {
      const a = i * stride + j;
      const b = a + stride;
      indices.push(a, b, a + 1, b, b + 1, a + 1);
    }
  }
  geometry.setAttribute("position", new Float32BufferAttribute(positions, 3));
  geometry.setIndex(indices);

  group.add(new Mesh(geometry, surfaceMaterial));

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

  let raf = 0;
  function frame() {
    if (visible && !document.hidden) {
      group.rotation.y += 0.0018;
      group.rotation.x = MathUtils.lerp(group.rotation.x, -0.22 + pointer.y * 0.1, 0.04);
      group.rotation.z = MathUtils.lerp(group.rotation.z, pointer.x * 0.05, 0.04);
      stars.rotation.y -= 0.0004;
      renderer.render(scene, camera);
    }
    raf = requestAnimationFrame(frame);
  }

  // 减少动效时不启动循环，只渲染一帧静态画面
  if (reduceMotion) {
    renderer.render(scene, camera);
  } else {
    frame();
  }

  return () => {
    cancelAnimationFrame(raf);
    resizeObserver.disconnect();
    window.removeEventListener("pointermove", onPointerMove);
    geometry.dispose();
    surfaceMaterial.dispose();
    starGeometry.dispose();
    stars.material.dispose();
    renderer.dispose();
  };
}
