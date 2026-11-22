---
title: "解析几何"
description: "解析几何：25 个模块的系统讲义与习题，坐标、向量、曲线曲面、变换与交互实验。"
tags:
  - 数学理论
  - 解析几何
---

> 坐标把几何翻译成代数，向量把代数翻译回几何。
> 这里不是一章教材，而是一套可以逐层展开、并且能在浏览器里做实验的解析几何体系。

---

## 主教材层

解析几何的主体是 **25 个模块的系统讲义**，每个模块都配一份习题集：

<div class="card-grid">
<a class="card" href="/YanYu-Site/maththeory/analytic-geometry/notes/"><strong>系统讲义总览</strong><span>25 模块 · 50 篇讲义与习题</span></a>
<a class="card" href="/YanYu-Site/maththeory/analytic-geometry/notes/frames-metric/"><strong>领域一 · 标架与度量</strong><span>E1–E7 · 向量、坐标、内积、外积、坐标系</span></a>
<a class="card" href="/YanYu-Site/maththeory/analytic-geometry/notes/shapes-equations/"><strong>领域二 · 形体与方程</strong><span>S1–S7 · 平面、直线、距离、曲面、空间曲线</span></a>
<a class="card" href="/YanYu-Site/maththeory/analytic-geometry/notes/transforms-classification/"><strong>领域三 · 变换与分类</strong><span>V1–V7 · 二次曲线、二次曲面、变换群</span></a>
<a class="card" href="/YanYu-Site/maththeory/analytic-geometry/notes/extensions/"><strong>领域四 · 延伸模块</strong><span>X1–X4 · 曲率、射影、公理、计算几何</span></a>
<a class="card" href="/YanYu-Site/maththeory/analytic-geometry/notes/terminology/"><strong>用语与约定</strong><span>标架、位置向量、二次曲线、合同变换的统一写法</span></a>
</div>

系统讲义和数学分析、高等代数同级：

- 每个模块有完整定义、定理、证明思路与反例；
- 每个模块配 A/B/C/D 分层习题与解答；
- 先读定义与边界，再读证明，最后用习题检验；
- 原「快速导览」八篇已并入对应模块的「入门速览」一节。

---

## 结构

| 领域 | 模块 | 关注的问题 |
|---|---|---|
| 一 · 标架与度量 | E1–E7 | 向量、分解、标架、坐标、内积、外积、坐标系家族 |
| 二 · 形体与方程 | S1–S7 | 轨迹、平面、空间直线、距离与角、柱锥旋、二次曲面、空间曲线 |
| 三 · 变换与分类 | V1–V7 | 坐标变换、二次曲线、切线与极线、直径与主方向、分类、变换群 |
| 四 · 延伸模块 | X1–X4 | 曲率与挠率、射影几何、公理体系、计算几何接口 |

---

## 快速导览并入了哪里

| 旧页面 | 并入 |
|---|---|
| A1 坐标系与坐标变换 | E3 标架与坐标 |
| A2 向量代数与度量 | E4 内积与投影 |
| B1 直线与平面 | S3 空间直线 |
| B2 圆锥曲线 | V2 二次曲线与直线 |
| B3 二次曲面 | S6 二次曲面标准形 |
| B4 参数曲线与曲面 | S5 柱锥旋 |
| C1 等距与仿射变换 | V1 平面直角坐标变换 |
| C2 二次型与分类 | V6 二次曲面的一般理论 |

旧链接通过跳转表指到新位置，不会 404。

---

## 实验台

- [解析几何实验台](/YanYu-Site/maththeory/analytic-geometry/lab/) —— 3D 二次曲面、参数曲面、2D 圆锥曲线、2D 线性变换。
- 可拖动、可调参数，全部在浏览器里实时计算。
- 实验台与模块的关系：
  - V2 ↔ 二次曲线实验
  - S6 ↔ 二次曲面实验
  - S5 ↔ 参数曲面实验
  - V1 ↔ 线性变换实验

---

## 建议学习路径

1. E1 → E3：把向量、分解、标架和坐标分开；
2. E4 → E7：内积、外积、坐标系、位置向量；
3. S1 → S4：平面、直线、距离与角；
4. S5 → S7：柱锥旋、二次曲面、空间曲线；
5. V1 → V7：用变换和不变量回看整门课；
6. X1–X4 按兴趣选读。

---

## 延伸资源

3Blue1Brown 的线性代数系列适合建立几何直觉：

- [Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)
- [3b1b/videos](https://github.com/3b1b/videos)（CC BY-NC-SA 4.0）
- [3b1b/manim](https://github.com/3b1b/manim)（MIT）

本站的三维实验用 Three.js 实时计算；Manim 适合做讲解动画，两者分工不同。
