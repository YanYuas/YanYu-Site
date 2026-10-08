/* ============================================================
   journey.js · 成长之路页面滚动联动脚本（三段式版）
   ============================================================
   【核心：三段式滚动进度】
     整个 sticky 区域高度 350vh，分为三段：
     - 阶段一（进度 0%→70%）：时间线横向滚动
     - 阶段二（进度 70%→80%）：过渡动画（CSS transition 自动处理）
     - 阶段三（进度 80%→100%）：简历展示

   【JS 做什么】
     1. 监听滚动，计算整体进度 (0→1)
     2. 阶段一：把进度的 0→0.7 映射为时间线的 translateX (0→max)
     3. 进度到达 0.7 时：给 html 加 class="journey-phase-resume"
        （CSS 监听到这个类，自动执行宽度过渡+时间线淡出+简历淡入）
     4. 进度低于 0.68 时：移除类（往回滚时恢复时间线）
     5. 更新顶部进度条

   【为什么用 0.7 和 0.68 两个阈值】
     用滞回区间（hysteresis），避免在临界点附近反复切换导致闪烁。
     前进时超过 0.7 才切换，后退时低于 0.68 才切回。
   ============================================================ */

(function () {
  'use strict';

  const timeline = document.querySelector('.journey-timeline');
  if (!timeline) return;

  // ========== 缓存DOM元素 ==========
  const stickyWrap = document.querySelector('.journey-sticky-wrap');
  const progressFill = document.querySelector('.journey-progress-fill');
  const scrollHint = document.querySelector('.journey-scroll-hint');

  // ========== 配置参数 ==========
  const PHASE1_END = 0.70;   // 阶段一结束点（时间线滚完，开始过渡）
  const PHASE1_END_BACK = 0.68; // 回退阈值（往回滚时恢复时间线）
  const SCROLL_RATIO = 1.0;  // 时间线滚动灵敏度

  // ========== 状态变量 ==========
  let ticking = false;
  let maxTranslateX = 0;
  let isResumePhase = false;  // 当前是否在简历阶段

  /**
   * 计算时间线最大横向偏移量
   */
  function calcMaxTranslateX() {
    const container = timeline.parentElement;
    if (!container) return 0;
    return Math.max(0, timeline.scrollWidth - container.clientWidth + 40);
  }

  /**
   * 缓动函数：easeOutCubic
   */
  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  /**
   * 切换到简历阶段
   * 给 html 加类，CSS 自动执行过渡动画
   */
  function enterResumePhase() {
    if (isResumePhase) return;
    isResumePhase = true;
    document.documentElement.classList.add('journey-phase-resume');
  }

  /**
   * 切回时间线阶段（往回滚时）
   */
  function exitResumePhase() {
    if (!isResumePhase) return;
    isResumePhase = false;
    document.documentElement.classList.remove('journey-phase-resume');
  }

  /**
   * 核心更新函数
   */
  function updateTimeline() {
    if (!stickyWrap) return;

    const rect = stickyWrap.getBoundingClientRect();
    const wrapHeight = stickyWrap.offsetHeight;
    const viewportHeight = window.innerHeight;

    // 整体滚动进度 (0→1)
    const totalScroll = wrapHeight - viewportHeight;
    let progress = totalScroll > 0 ? -rect.top / totalScroll : 0;
    progress = Math.max(0, Math.min(1, progress));

    // ===== 阶段判断 =====
    if (progress >= PHASE1_END) {
      enterResumePhase();
    } else if (progress <= PHASE1_END_BACK) {
      exitResumePhase();
    }

    // ===== 时间线横向偏移（只在阶段一内映射） =====
    // 把整体进度的 0→PHASE1_END 映射为 0→1
    let timelineProgress = progress / PHASE1_END;
    timelineProgress = Math.max(0, Math.min(1, timelineProgress));

    // 应用缓动 + 灵敏度
    const easedProgress = easeOutCubic(timelineProgress * SCROLL_RATIO);
    const clampedProgress = Math.min(1, easedProgress);

    const translateX = clampedProgress * maxTranslateX;
    timeline.style.transform = `translateX(-${translateX}px)`;

    // ===== 进度条（显示整体进度） =====
    if (progressFill) {
      progressFill.style.width = `${progress * 100}%`;
    }

    // ===== 滚动提示：开始滚动后隐藏 =====
    if (scrollHint && progress > 0.02) {
      scrollHint.style.opacity = '0';
    }

    ticking = false;
  }

  /**
   * 滚动事件：requestAnimationFrame 节流
   */
  function onScroll() {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(updateTimeline);
    }
  }

  /**
   * 窗口大小改变：重新计算最大偏移量
   */
  function onResize() {
    maxTranslateX = calcMaxTranslateX();
    updateTimeline();
  }

  // ========== 初始化 ==========
  function init() {
    maxTranslateX = calcMaxTranslateX();
    updateTimeline();

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onResize);

    // 1秒后再次计算（确保字体加载完毕）
    setTimeout(() => {
      maxTranslateX = calcMaxTranslateX();
      updateTimeline();
    }, 1000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
