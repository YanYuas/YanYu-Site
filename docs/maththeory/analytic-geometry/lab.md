---
tags:
  - 数学理论
  - 解析几何
---

# 解析几何实验台

> 这一页不是「看动画」，而是把方程交给浏览器实时计算：
> 改变参数，图形立刻响应；每个实验都对应一个模块里的定义或定理。

> 所有计算都在本地完成，不上传任何数据；源码在 `visual/src/` 与
> `docs/javascripts/analytic-2d.js`，可以自行修改、复用。

---

## 一、三维曲面实验台

对应模块：[B3 · 二次曲面](curves-surfaces/B3-quadric.md) 与 [B4 · 参数曲线与曲面](curves-surfaces/B4-parametric.md)。

<div class="geo-lab" id="geo-lab">
  <div class="geo-lab__stage">
    <canvas id="geo-canvas"></canvas>
    <div class="geo-lab__fallback" id="geo-fallback" hidden>
      当前浏览器无法启用 WebGL。换用支持 WebGL 的桌面浏览器即可看到交互曲面。
    </div>
  </div>
  <aside class="geo-lab__panel">
    <div class="geo-lab__tabs" role="tablist" aria-label="曲面类型">
      <button class="is-active" data-geo="ellipsoid" role="tab" aria-selected="true">椭球面</button>
      <button data-geo="hyperboloid" role="tab" aria-selected="false">单叶双曲面</button>
      <button data-geo="saddle" role="tab" aria-selected="false">马鞍面</button>
      <button data-geo="plane" role="tab" aria-selected="false">平面</button>
      <button data-geo="torus" role="tab" aria-selected="false">环面</button>
      <button data-geo="mobius" role="tab" aria-selected="false">莫比乌斯环</button>
    </div>

    <label class="geo-lab__control">
      <span>尺度 a <b id="geo-a-value">1.20</b></span>
      <input id="geo-a" type="range" min="0.6" max="1.8" step="0.05" value="1.2" />
    </label>

    <p class="geo-lab__desc" id="geo-desc">
      三个主方向都被缩放；拖动旋转可以看到椭球的三个半轴。
    </p>
    <p class="geo-lab__hint">拖动旋转 · 滚轮缩放 · 切换标签看不同曲面</p>
  </aside>
</div>

---

## 二、圆锥曲线实验台

对应模块：[B2 · 圆锥曲线](curves-surfaces/B2-conic.md)。

统一方程

$$
r=\frac{p}{1+e\cos\theta}
$$

以焦点为极点。拖动 $e$ 与 $p$，观察 $e<1$、$e=1$、$e>1$ 时曲线如何从椭圆过渡到抛物线再到双曲线。

<div class="geo-lab geo-lab--2d" id="conic-lab">
  <div class="geo-lab__stage">
    <canvas id="conic-canvas"></canvas>
  </div>
  <aside class="geo-lab__panel">
    <label class="geo-lab__control">
      <span>离心率 e <b id="conic-e-value">0.60</b></span>
      <input id="conic-e" type="range" min="0.2" max="1.8" step="0.01" value="0.6" />
    </label>
    <label class="geo-lab__control">
      <span>半通径 p <b id="conic-p-value">1.50</b></span>
      <input id="conic-p" type="range" min="0.5" max="3" step="0.05" value="1.5" />
    </label>
    <p class="geo-lab__desc" id="conic-desc">
      拖动离心率，观察椭圆 → 抛物线 → 双曲线的连续变化。
    </p>
    <p class="geo-lab__hint">焦点在原点 · 虚线为准线 · 坐标单位为 1</p>
  </aside>
</div>

---

## 三、线性变换实验台

对应模块：[C1 · 等距与仿射变换](transformations/C1-isometry-affine.md)。

矩阵

$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}
$$

把平面上的每个点 $\vec x$ 送到 $A\vec x$。拖动四个滑杆，观察网格、单位圆和基向量如何变化；
行列式给出面积缩放因子。

<div class="geo-lab geo-lab--2d" id="transform-lab">
  <div class="geo-lab__stage">
    <canvas id="transform-canvas"></canvas>
  </div>
  <aside class="geo-lab__panel">
    <label class="geo-lab__control">
      <span>a <b id="mat-a-value">1.0</b></span>
      <input id="mat-a" type="range" min="-2" max="2" step="0.1" value="1" />
    </label>
    <label class="geo-lab__control">
      <span>b <b id="mat-b-value">0.0</b></span>
      <input id="mat-b" type="range" min="-2" max="2" step="0.1" value="0" />
    </label>
    <label class="geo-lab__control">
      <span>c <b id="mat-c-value">0.0</b></span>
      <input id="mat-c" type="range" min="-2" max="2" step="0.1" value="0" />
    </label>
    <label class="geo-lab__control">
      <span>d <b id="mat-d-value">1.0</b></span>
      <input id="mat-d" type="range" min="-2" max="2" step="0.1" value="1" />
    </label>
    <p class="geo-lab__desc" id="mat-desc">
      det(A)=1；网格随矩阵实时变换，单位圆变成椭圆。
    </p>
    <p class="geo-lab__hint">拖动滑杆 · 观察基向量与单位圆</p>
  </aside>
</div>

---

## 实验与定理的对应

| 实验 | 观察到的现象 | 对应定理 |
|---|---|---|
| 3D 二次曲面 | 特征值符号 → 封闭/张开/鞍形 | 惯性定理、正交对角化 |
| 3D 参数曲面 | 环面与莫比乌斯环的拓扑差异 | 可定向性 |
| 2D 圆锥曲线 | $e$ 连续变化，曲线类型突变 | 焦点—准线统一定义 |
| 2D 线性变换 | 网格随矩阵变形，单位圆变椭圆 | 矩阵的几何意义、行列式 |

## 开放与复用

- 三维：Three.js + Rollup，源码 [visual/src/analytic.js](https://github.com/YanYuas/YanYu-Site/blob/main/visual/src/analytic.js)（仓库根目录 `visual/`）；
- 二维：原生 Canvas 2D，源码 [docs/javascripts/analytic-2d.js](../../javascripts/analytic-2d.js)；
- 所有实验都是纯前端、无后端；可以单独抽出 `visual/` 作为独立演示项目；
- 如果你更想做「讲解动画」而不是交互，`D:\MathWorks\AdvancedAlgebra` 里的 Manim/Plotly
  示例可以作为另一条路线：Manim 生成 MP4，Plotly 生成可交互 HTML。
