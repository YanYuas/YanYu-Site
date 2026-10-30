---
title: "解析几何"
tags:
  - 数学理论
  - 解析几何
---

> 坐标把几何翻译成代数，向量把代数翻译回几何。
> 这里不是一章教材，而是一套可以逐层展开、并且能在浏览器里做实验的解析几何体系。

---

## 这套体系怎么组织

解析几何的核心不是「背方程」，而是三件事的往返翻译：

1. **对象 → 坐标**：点、直线、平面、曲线、曲面写成方程；
2. **坐标 → 结构**：用向量、内积、外积、二次型读出角度、距离、曲率与分类；
3. **结构 → 变换**：换坐标、刚体变换、仿射变换下，哪些量变了，哪些量不变。

按这三步，体系分成三个相对独立、又互相咬合的领域：

| 领域 | 模块 | 关注的问题 |
|---|---|---|
| **一 · 坐标与向量** | A1 坐标系与坐标变换 · A2 向量代数与度量 | 空间如何被坐标化，长度/角度/面积如何被计算 |
| **二 · 曲线与曲面** | B1 直线与平面 · B2 圆锥曲线 · B3 二次曲面 · B4 参数曲线与曲面 | 方程如何变成图形，图形如何被分类 |
| **三 · 变换与分类** | C1 等距与仿射变换 · C2 二次型与分类 | 换一个坐标系/变换之后，什么保持不变 |

> 和高等代数的关系：领域一对应 G1–G3（空间、基、内积），
> 领域二对应 G5/G7（解析几何嵌入、二次型与曲面），
> 领域三对应 T2–T5（矩阵表示、特征理论、对角化）。

---

## 模块导航

### 领域一 · 坐标与向量

- [A1 · 坐标系与坐标变换](/YanYu-Site/maththeory/analytic-geometry/coordinates/a1-coordinate-frame/)
  —— 仿射坐标系、基变换、坐标变换公式与不变量
- [A2 · 向量代数与度量](/YanYu-Site/maththeory/analytic-geometry/coordinates/a2-vector-metric/)
  —— 点积、叉积、混合积；长度、角度、面积、体积

### 领域二 · 曲线与曲面

- [B1 · 直线与平面](/YanYu-Site/maththeory/analytic-geometry/curves-surfaces/b1-line-plane/)
  —— 点向式、一般式、位置关系、距离与夹角
- [B2 · 圆锥曲线](/YanYu-Site/maththeory/analytic-geometry/curves-surfaces/b2-conic/)
  —— 焦点—准线、离心率、极坐标统一方程
- [B3 · 二次曲面](/YanYu-Site/maththeory/analytic-geometry/curves-surfaces/b3-quadric/)
  —— 二次型标准形、椭球/双曲/抛物/柱面/锥面
- [B4 · 参数曲线与曲面](/YanYu-Site/maththeory/analytic-geometry/curves-surfaces/b4-parametric/)
  —— 参数表示、切向量、弧长、环面与莫比乌斯环

### 领域三 · 变换与分类

- [C1 · 等距与仿射变换](/YanYu-Site/maththeory/analytic-geometry/transformations/c1-isometry-affine/)
  —— 平移、旋转、反射、伸缩、剪切与它们的矩阵
- [C2 · 二次型与分类](/YanYu-Site/maththeory/analytic-geometry/transformations/c2-classification/)
  —— 合同变换、惯性定理、二次曲面的不变量分类

---

## 实验台

- [解析几何实验台](/YanYu-Site/maththeory/analytic-geometry/lab/) —— 3D 二次曲面/参数曲面、2D 圆锥曲线、2D 线性变换，
  可拖动、可调参数，全部在浏览器里实时计算。
- 实验台与模块对应关系：
  - B2 ↔ 圆锥曲线实验（离心率、半通径）
  - B3 ↔ 二次曲面实验（椭球/双曲面/马鞍面）
  - B4 ↔ 参数曲面实验（环面/莫比乌斯环）
  - C1 ↔ 线性变换实验（2×2 矩阵、网格、单位圆）

---

## 延伸资源

**3Blue1Brown（3b1b）** 的线性代数系列适合建立几何直觉：

- [Essence of Linear Algebra 官方专题页](https://www.3blue1brown.com/topics/linear-algebra)
- [3b1b/videos：视频动画源码](https://github.com/3b1b/videos)
  —— 内容采用 **CC BY-NC-SA 4.0**，非商业使用需署名并以相同方式共享；
- [3b1b/manim：动画引擎](https://github.com/3b1b/manim)
  —— **MIT** 许可，可以用来生成自己的数学动画。

本站的三维实验使用 Three.js 实时计算；Manim 版本适合做「讲解动画」，
两者分工：**Manim 负责叙事，Three.js 负责交互**。

---

## 建议学习路径

1. A1 → A2：先把「坐标化 + 向量计算」练成肌肉记忆；
2. B1 → B2：从直线/平面进入圆锥曲线，抓住离心率这条主线；
3. B3 → B4：把二次方程升级为二次曲面，再看参数曲面；
4. C1 → C2：用变换和不变量回看前面所有对象；
5. 最后回到高等代数 G5/G7，把具体结论接到抽象结构上。
