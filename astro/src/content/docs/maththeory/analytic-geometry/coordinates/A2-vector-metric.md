---
title: "A2 · 向量代数与度量"
description: "点积管角度，叉积管面积，混合积管体积"
tags:
  - 数学理论
  - 解析几何
---

> 点积管角度，叉积管面积，混合积管体积。三个积把「度量几何」压缩成三行代数。

## 摘要

有了坐标以后，长度、角度、面积、体积都可以由向量运算得到。本模块把三个基本积
（点积、叉积、混合积）放进同一个几何框架：点积是投影，叉积是法向面积，混合积是
有向体积。由此得到夹角公式、点到直线距离、点到平面距离、平行六面体体积等常用结论。

**关键词**：点积；投影；叉积；混合积；右手系；Gram 行列式

---

## 1 点积：角度与投影

$$
\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta
=a_1b_1+a_2b_2+a_3b_3.
$$

- $\vec a\cdot\vec b=0$ ⇔ 垂直；
- $\vec b$ 在 $\vec a$ 上的投影长度为 $\dfrac{\vec a\cdot\vec b}{|\vec a|}$；
- $\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$。

**几何锚定**：点积是「$\vec b$ 在 $\vec a$ 方向上的影子长度 × $\vec a$ 的长度」。
影子有正负，所以点积可以为负。

---

## 2 叉积：法向与面积

$$
\vec a\times\vec b=
\begin{vmatrix}
e_1&e_2&e_3\\
a_1&a_2&a_3\\
b_1&b_2&b_3
\end{vmatrix},
\qquad
|\vec a\times\vec b|=|\vec a||\vec b|\sin\theta.
$$

- 方向：右手系，同时垂直于 $\vec a,\vec b$；
- 长度：以 $\vec a,\vec b$ 为邻边的平行四边形面积；
- $\vec a\times\vec b=0$ ⇔ 共线。

叉积是「法向量机器」：平面方程、空间直线方向、曲面法向都靠它。

---

## 3 混合积：有向体积

$$
[\vec a,\vec b,\vec c]=(\vec a\times\vec b)\cdot\vec c
=
\begin{vmatrix}
a_1&a_2&a_3\\
b_1&b_2&b_3\\
c_1&c_2&c_3
\end{vmatrix}.
$$

其绝对值是三个向量张成的平行六面体体积；符号给出定向。
$[\vec a,\vec b,\vec c]=0$ ⇔ 三向量共面。

---

## 4 常用度量公式

- 点到平面 $Ax+By+Cz+D=0$ 的距离：
  $$d=\frac{|Ax_0+By_0+Cz_0+D|}{\sqrt{A^2+B^2+C^2}};$$
- 两条异面直线的距离：$d=\dfrac{|(\vec a\times\vec b)\cdot\vec{AB}|}{|\vec a\times\vec b|}$；
- 平面夹角：用法向量点积；直线与平面夹角：用方向向量与法向量点积后取余角。

---

## 5 和高等代数的连接

点积是 G3 内积空间在 $\mathbb R^3$ 上的具体实现；叉积是三维特有的「李代数式」运算；
混合积则是行列式（F3）的几何解释。三者共同说明：**度量结论都有行列式/内积背景**。

---

## 6 练习

1. 已知 $\vec a=(1,2,2),\vec b=(2,-1,0)$，求 $\vec a\cdot\vec b$、$\vec a\times\vec b$ 与夹角。
2. 证明 $|\vec a\times\vec b|^2=|\vec a|^2|\vec b|^2-(\vec a\cdot\vec b)^2$（Lagrange 恒等式）。
3. 求点 $(1,2,3)$ 到平面 $2x-y+2z-4=0$ 的距离。
4. 证明三个向量共面当且仅当混合积为零，并用体积语言解释。

> 实验对应：[解析几何实验台](/YanYu-Site/maththeory/analytic-geometry/lab/) 的「二次曲面」与「线性变换」模式可以观察法向、网格与体积缩放。
