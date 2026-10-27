// ============================================================
// home-3d.js · 首页 Hero 三维点缀的加载器
// ============================================================
// 只在满足这些条件时加载 Three.js 包：
//   1. 当前页面有 #hero-3d 画布（只有首页有）
//   2. 视口宽度 > 1000px（手机/平板不加载，省流量和电量）
//   3. 浏览器支持 WebGL
// 加载发生在首屏渲染之后的空闲时间，不阻塞标题/按钮。
// 真正的场景代码在 vendor/hero-3d.bundle.js（由 visual/ 源码打包）。
// ============================================================

(function () {
  "use strict";

  const canvas = document.getElementById("hero-3d");
  if (!canvas) return;

  const desktop = window.matchMedia("(min-width: 1001px)");
  if (!desktop.matches) return;

  const canWebGL =
    typeof WebGLRenderingContext !== "undefined" ||
    typeof WebGL2RenderingContext !== "undefined";
  if (!canWebGL) return;

  const wrapper = canvas.parentElement;
  let started = false;

  async function load() {
    if (started) return;
    started = true;
    try {
      const { initHero3D } = await import("./vendor/hero-3d.bundle.js");
      initHero3D(canvas);
      wrapper.classList.add("is-ready");
    } catch (error) {
      // WebGL 初始化失败时静默降级：保留背景图与文字，不显示空白画布
      wrapper.classList.add("is-failed");
      console.warn("Hero 3D disabled:", error);
    }
  }

  if ("requestIdleCallback" in window) {
    requestIdleCallback(load, { timeout: 2500 });
  } else {
    window.setTimeout(load, 1200);
  }
})();
