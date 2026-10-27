// ============================================================
// home-motion.js · 首页滚动/数字动效
// ============================================================
// 两个增强，都是渐进式的：
//   1. 数据条数字从 0 递增到目标值（21 / 672 / 46）
//   2. 首屏之外的卡片滚动进场
// 关闭 JS、开启减少动效时，页面仍显示完整内容（不会隐藏）。
// ============================================================

(function () {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) return;

  const home = document.querySelector(".home");
  if (!home) return;

  // ---------- 数据条数字递增 ----------
  // 数据条本身有 2.4s 的淡入延迟，数字递增也等到那时再开始，
  // 否则数字会在不可见状态下就涨完。
  window.setTimeout(() => {
    document.querySelectorAll(".hero-stats strong").forEach((element) => {
      const target = Number.parseInt(element.textContent, 10);
      if (!Number.isFinite(target)) return;
      const duration = 900;
      const start = performance.now();
      element.textContent = "0";

      function tick(now) {
        const progress = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - progress, 3);
        element.textContent = String(Math.round(target * eased));
        if (progress < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  }, 2200);

  // ---------- 首屏之外的卡片滚动进场 ----------
  const cards = Array.from(document.querySelectorAll(".home .grid.cards > ul > li"));
  if (!cards.length || !("IntersectionObserver" in window)) return;

  const viewportHeight = window.innerHeight;
  const pending = cards.filter((card) => card.getBoundingClientRect().top > viewportHeight * 0.92);
  if (!pending.length) return;

  home.classList.add("reveal-enabled");
  pending.forEach((card) => card.classList.add("will-reveal"));

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
  );

  pending.forEach((card) => observer.observe(card));
})();
