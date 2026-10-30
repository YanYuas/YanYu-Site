---
title: "领域二 · 曲线与曲面"
tags:
  - 数学理论
  - 解析几何
---

> 方程是几何对象的「身份证」：看出方程的类型，就看出图形的骨架。
> 这个领域从最简的直线/平面出发，逐级升到圆锥曲线、二次曲面和参数曲面。

## 领域结构

- **B1 直线与平面**：一次方程对应的几何对象，位置关系全部由点积/叉积决定；
- **B2 圆锥曲线**：二次方程在平面上的三类解，统一在「焦点—准线—离心率」框架下；
- **B3 二次曲面**：二次型在三维中的标准形，主方向由对称矩阵的特征向量给出；
- **B4 参数曲线与曲面**：从隐式方程转向参数表示，为计算机图形学/交互实验铺路。

## 模块

| 模块 | 核心问题 | 实验 |
|---|---|---|
| [B1 · 直线与平面](/YanYu-Site/maththeory/analytic-geometry/curves-surfaces/b1-line-plane/) | 点向式/一般式、夹角、距离、平面束 | — |
| [B2 · 圆锥曲线](/YanYu-Site/maththeory/analytic-geometry/curves-surfaces/b2-conic/) | 离心率如何统一椭圆/抛物线/双曲线 | 2D 圆锥曲线实验 |
| [B3 · 二次曲面](/YanYu-Site/maththeory/analytic-geometry/curves-surfaces/b3-quadric/) | 特征值符号如何决定曲面类型 | 3D 二次曲面实验 |
| [B4 · 参数曲线与曲面](/YanYu-Site/maththeory/analytic-geometry/curves-surfaces/b4-parametric/) | 参数方程、切向量、环面、莫比乌斯环 | 3D 参数曲面实验 |

## 学习建议

先把 B1 的「法向量」和「方向向量」用熟；B2 只抓一条主线——离心率 $e$；
B3 把二次型矩阵的特征值符号与曲面类型对应起来；B4 则从「方程」切换到「映射」，
为实验台的实时渲染做准备。
