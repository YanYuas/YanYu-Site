// ============================================================
// analytic-2d.js · 解析几何实验台的 2D 模块
// ============================================================
// 两个独立的 Canvas 2D 实验：
//   1. 圆锥曲线：离心率 e + 半通径 p，焦点/准线实时显示
//   2. 线性变换：2×2 矩阵滑杆，网格/单位圆/基向量实时变换
// 不依赖 Three.js，页面里没有对应 canvas 时直接退出。
// ============================================================

(function () {
  "use strict";

  const conicCanvas = document.getElementById("conic-canvas");
  const transformCanvas = document.getElementById("transform-canvas");
  if (!conicCanvas && !transformCanvas) return;

  const colors = () => {
    const css = getComputedStyle(document.body);
    return {
      gold: css.getPropertyValue("--sa-gold").trim() || "#d9bc6a",
      text: css.getPropertyValue("--sa-text-mid").trim() || "#dcd9d2",
      low: css.getPropertyValue("--sa-text-low").trim() || "#9e9c95",
      line: css.getPropertyValue("--sa-line").trim() || "rgba(150,150,150,.3)",
      bg: css.getPropertyValue("--sa-bg-2").trim() || "#1e2236",
    };
  };

  function prepare(canvas) {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const width = canvas.parentElement.clientWidth;
    const height = canvas.parentElement.clientHeight;
    if (!width || !height) return null;
    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    const ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx, width, height };
  }

  function drawAxes(ctx, width, height, scale) {
    const c = colors();
    ctx.strokeStyle = c.line;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, height / 2);
    ctx.lineTo(width, height / 2);
    ctx.moveTo(width / 2, 0);
    ctx.lineTo(width / 2, height);
    ctx.stroke();

    ctx.fillStyle = c.low;
    ctx.font = "11px monospace";
    ctx.fillText("x", width - 14, height / 2 - 6);
    ctx.fillText("y", width / 2 + 6, 14);
  }

  function drawGrid(ctx, width, height, scale) {
    const c = colors();
    ctx.strokeStyle = c.line;
    ctx.globalAlpha = 0.35;
    ctx.lineWidth = 0.6;
    const cx = width / 2;
    const cy = height / 2;
    for (let k = -6; k <= 6; k += 1) {
      const x = cx + k * scale;
      const y = cy + k * scale;
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
  }

  function pointToScreen(x, y, width, height, scale, z = 0) {
    return [width / 2 + x * scale, height / 2 - y * scale];
  }

  // ------------------------------------------------------------
  // 1. 圆锥曲线
  // ------------------------------------------------------------
  function initConic(canvas) {
    const eInput = document.getElementById("conic-e");
    const pInput = document.getElementById("conic-p");
    const desc = document.getElementById("conic-desc");
    const eValue = document.getElementById("conic-e-value");
    const pValue = document.getElementById("conic-p-value");
    let plot = null;

    function draw() {
      if (!plot) return;
      const { ctx, width, height } = plot;
      const scale = Math.min(width, height) / 7.5;
      const e = Number.parseFloat(eInput?.value || "0.6");
      const p = Number.parseFloat(pInput?.value || "1.5");
      const c = colors();

      ctx.clearRect(0, 0, width, height);
      drawGrid(ctx, width, height, scale);
      drawAxes(ctx, width, height, scale);

      // 极坐标 r = p / (1 + e cosθ)，焦点在原点
      const rMax = 30;
      const branches = [];
      const n = 600;
      if (e < 1 - 1e-6) {
        const pts = [];
        for (let i = 0; i <= n; i += 1) {
          const th = (Math.PI * 2 * i) / n;
          const r = p / (1 + e * Math.cos(th));
          pts.push([r * Math.cos(th), r * Math.sin(th)]);
        }
        branches.push(pts);
      } else if (e <= 1 + 1e-6) {
        // 抛物线，避开 θ=π 的渐近方向
        const pts = [];
        for (let i = 0; i <= n; i += 1) {
          const th = -Math.PI + (Math.PI * 2 * i) / n;
          if (Math.abs(Math.cos(th) + 1) < 1e-4) continue;
          const r = p / (1 + Math.cos(th));
          if (r > rMax) continue;
          pts.push([r * Math.cos(th), r * Math.sin(th)]);
        }
        branches.push(pts);
      } else {
        // 双曲线两支：分母变号处断开
        const th0 = Math.acos(-1 / e);
        for (const [a, b] of [
          [-th0, th0],
          [th0, Math.PI * 2 - th0],
        ]) {
          const pts = [];
          for (let i = 0; i <= n; i += 1) {
            const th = a + ((b - a) * i) / n;
            const den = 1 + e * Math.cos(th);
            if (Math.abs(den) < 1e-5) continue;
            const r = p / den;
            if (Math.abs(r) > rMax) continue;
            pts.push([r * Math.cos(th), r * Math.sin(th)]);
          }
          branches.push(pts);
        }
      }

      ctx.strokeStyle = c.gold;
      ctx.lineWidth = 2;
      for (const pts of branches) {
        if (pts.length < 2) continue;
        ctx.beginPath();
        pts.forEach(([x, y], i) => {
          const [sx, sy] = pointToScreen(x, y, width, height, scale);
          if (i === 0) ctx.moveTo(sx, sy);
          else ctx.lineTo(sx, sy);
        });
        ctx.stroke();
      }

      // 焦点
      ctx.fillStyle = c.gold;
      ctx.beginPath();
      ctx.arc(width / 2, height / 2, 4, 0, Math.PI * 2);
      ctx.fill();

      // 准线 x = p/e
      if (e > 1e-3) {
        const [dx] = pointToScreen(p / e, 0, width, height, scale);
        ctx.strokeStyle = c.text;
        ctx.globalAlpha = 0.55;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(dx, 0);
        ctx.lineTo(dx, height);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.globalAlpha = 1;
        ctx.fillStyle = c.low;
        ctx.font = "11px monospace";
        ctx.fillText("准线 x=p/e", dx + 5, 14);
      }

      if (eValue) eValue.textContent = e.toFixed(2);
      if (pValue) pValue.textContent = p.toFixed(2);
      if (desc) {
        if (e < 1 - 1e-6) desc.textContent = `e=${e.toFixed(2)} < 1：椭圆，焦点在原点，准线在右侧。`;
        else if (Math.abs(e - 1) < 1e-6) desc.textContent = "e=1：抛物线，焦点到准线的距离与到定点的距离相等。";
        else desc.textContent = `e=${e.toFixed(2)} > 1：双曲线，出现两支，分母变号处断开。`;
      }

      // 图例
      ctx.fillStyle = c.low;
      ctx.font = "11px monospace";
      ctx.fillText("r = p / (1 + e cos θ)", 12, height - 12);
    }

    function resize() {
      plot = prepare(canvas);
      draw();
    }

    eInput?.addEventListener("input", draw);
    pInput?.addEventListener("input", draw);
    window.addEventListener("resize", resize);
    if ("ResizeObserver" in window) new ResizeObserver(resize).observe(canvas.parentElement);
    resize();
  }

  // ------------------------------------------------------------
  // 2. 线性变换
  // ------------------------------------------------------------
  function initTransform(canvas) {
    const inputs = {
      a: document.getElementById("mat-a"),
      b: document.getElementById("mat-b"),
      c: document.getElementById("mat-c"),
      d: document.getElementById("mat-d"),
    };
    const desc = document.getElementById("mat-desc");
    const vals = {
      a: document.getElementById("mat-a-value"),
      b: document.getElementById("mat-b-value"),
      c: document.getElementById("mat-c-value"),
      d: document.getElementById("mat-d-value"),
    };
    let plot = null;

    function matrix() {
      return {
        a: Number.parseFloat(inputs.a?.value || "1"),
        b: Number.parseFloat(inputs.b?.value || "0"),
        c: Number.parseFloat(inputs.c?.value || "0"),
        d: Number.parseFloat(inputs.d?.value || "1"),
      };
    }

    function apply(m, x, y) {
      return [m.a * x + m.b * y, m.c * x + m.d * y];
    }

    function draw() {
      if (!plot) return;
      const { ctx, width, height } = plot;
      const scale = Math.min(width, height) / 10;
      const m = matrix();
      const c = colors();
      const det = m.a * m.d - m.b * m.c;

      ctx.clearRect(0, 0, width, height);
      drawGrid(ctx, width, height, scale);
      drawAxes(ctx, width, height, scale);

      // 原网格（弱）
      ctx.strokeStyle = c.line;
      ctx.globalAlpha = 0.45;
      ctx.lineWidth = 0.7;
      for (let k = -4; k <= 4; k += 1) {
        const p1 = pointToScreen(k, -4, width, height, scale);
        const p2 = pointToScreen(k, 4, width, height, scale);
        ctx.beginPath();
        ctx.moveTo(...p1);
        ctx.lineTo(...p2);
        ctx.stroke();
        const p3 = pointToScreen(-4, k, width, height, scale);
        const p4 = pointToScreen(4, k, width, height, scale);
        ctx.beginPath();
        ctx.moveTo(...p3);
        ctx.lineTo(...p4);
        ctx.stroke();
      }
      ctx.globalAlpha = 1;

      // 变换后的网格（金色）
      ctx.strokeStyle = c.gold;
      ctx.globalAlpha = 0.72;
      ctx.lineWidth = 1.1;
      for (let k = -4; k <= 4; k += 0.5) {
        const pts1 = [apply(m, k, -4), apply(m, k, 4)];
        const pts2 = [apply(m, -4, k), apply(m, 4, k)];
        for (const pts of [pts1, pts2]) {
          const s = pts.map(([x, y]) => pointToScreen(x, y, width, height, scale));
          ctx.beginPath();
          ctx.moveTo(...s[0]);
          ctx.lineTo(...s[1]);
          ctx.stroke();
        }
      }
      ctx.globalAlpha = 1;

      // 单位圆 → 椭圆
      ctx.strokeStyle = c.text;
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      for (let i = 0; i <= 180; i += 1) {
        const t = (Math.PI * 2 * i) / 180;
        const [x, y] = apply(m, Math.cos(t), Math.sin(t));
        const [sx, sy] = pointToScreen(x, y, width, height, scale);
        if (i === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // 基向量
      ctx.strokeStyle = c.gold;
      ctx.lineWidth = 2.4;
      for (const [x, y] of [
        [1, 0],
        [0, 1],
      ]) {
        const [tx, ty] = apply(m, x, y);
        const [sx, sy] = pointToScreen(tx, ty, width, height, scale);
        ctx.beginPath();
        ctx.moveTo(width / 2, height / 2);
        ctx.lineTo(sx, sy);
        ctx.stroke();
      }

      if (desc) desc.textContent = `det(A)=${det.toFixed(2)}；网格随矩阵实时变换，单位圆变成椭圆。`;
      Object.entries(vals).forEach(([k, el]) => {
        if (el) el.textContent = m[k].toFixed(1);
      });
    }

    function resize() {
      plot = prepare(canvas);
      draw();
    }

    Object.values(inputs).forEach((el) => el?.addEventListener("input", draw));
    window.addEventListener("resize", resize);
    if ("ResizeObserver" in window) new ResizeObserver(resize).observe(canvas.parentElement);
    resize();
  }

  if (conicCanvas) initConic(conicCanvas);
  if (transformCanvas) initTransform(transformCanvas);
})();
