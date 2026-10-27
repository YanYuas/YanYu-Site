// ============================================================
// analytic-geometry.js · 解析几何专题的实验台加载器
// ============================================================
// 只有页面里存在 #geo-canvas 时才加载 Three.js bundle。
// 依赖 browser WebGL；失败时显示静态说明，不阻塞正文阅读。
// ============================================================

(function () {
  "use strict";

  const canvas = document.getElementById("geo-canvas");
  if (!canvas) return;

  const fallback = document.getElementById("geo-fallback");

  const canWebGL =
    typeof WebGLRenderingContext !== "undefined" ||
    typeof WebGL2RenderingContext !== "undefined";

  if (!canWebGL) {
    canvas.hidden = true;
    if (fallback) fallback.hidden = false;
    return;
  }

  let started = false;
  async function load() {
    if (started) return;
    started = true;
    try {
      const { initAnalyticLab } = await import("./vendor/analytic-geometry.bundle.js");
      initAnalyticLab();
    } catch (error) {
      canvas.hidden = true;
      if (fallback) fallback.hidden = false;
      console.warn("Analytic geometry lab unavailable:", error);
    }
  }

  if ("requestIdleCallback" in window) {
    requestIdleCallback(load, { timeout: 800 });
  } else {
    window.setTimeout(load, 300);
  }
})();
