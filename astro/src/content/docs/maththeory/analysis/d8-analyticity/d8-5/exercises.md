---
title: "D8-5 最大模原理与调和函数 · 习题集"
description: "领域 ：D8 解析"
tags:
  - "数学理论"
  - "分析学"
  - "D8 解析"
---

> 领域 ：D8 解析

---

## 第一层 · L0 初等直觉（4题）

### 题 1 ★ 基础
**题目**：用"地形"的直觉解释最大模原理：为什么解析函数的模不能在区域内部有"山峰"？以 $f(z)=z^2$ 在单位圆盘内为例，说明最大值确实在边界上。

**对应知识点**：最大模原理的几何直觉——解析函数的模是次调和函数，不能在内部取得最大值。

**解答**：
把 $|f(z)|$ 看作复平面上的"地形高度"。最大模原理说这个地形不能有内部的"山峰"——最高点一定在"边缘"（边界）上。

以 $f(z)=z^2$ 为例，$|f(z)|=|z|^2$。在单位圆盘 $|z|<1$ 内，$|z|^2<1$，而在边界 $|z|=1$ 上 $|z|^2=1$。所以最大值 1 在边界上取得，内部任何点的模都严格小于 1。

为什么解析函数不能有内部山峰？因为解析函数满足平均值原理：$f(z_0)$ 等于周围圆周上 $f$ 的平均值。如果 $|f(z_0)|$ 是最大值 $M$，那么圆周上所有点的 $|f|$ 都必须等于 $M$（否则平均值会严格小于 $M$），从而 $|f|\equiv M$ 在邻域内成立，由唯一性定理 $f$ 为常数。所以非常数解析函数不可能在内部取得最大值。

**一句话点评**：解析函数的"地形"只有"斜坡"和"鞍部"，没有"山峰"——最高点一定在边缘。

---

### 题 2 ★ 基础
**题目**：用"稳态温度"的直觉解释调和函数的平均值原理：为什么调和函数在一点的值等于周围圆周上的平均值？

**对应知识点**：调和函数的物理直觉——稳态温度分布、无旋无源场。

**解答**：
调和函数描述稳态的物理场，比如稳定的温度分布。在稳态下，一点的温度等于周围圆周上温度的平均值——因为如果中心温度高于周围平均，热量会从中心流向周围，温度会下降，直到达到平衡；如果中心温度低于周围平均，热量会流入，温度上升。只有当中心温度等于周围平均时，热量流入等于流出，系统达到稳态。

数学上，Laplace 方程 $\Delta u=u_{xx}+u_{yy}=0$ 意味着函数在各个方向上的"弯曲"之和为零——不能在任何方向上过度凸起或凹陷，所以中心值必须等于周围平均。

**一句话点评**：调和函数就是"稳态温度"——中心温度等于周围平均，没有热源也没有冷源。

---

### 题 3 ★ 基础
**题目**：验证 $u(x,y)=x^2-y^2$ 是调和函数，并验证它在原点处满足平均值原理（取半径 $r=1$ 的圆周）。

**对应知识点**：调和函数的定义验证 + 平均值原理的直接验证。

**解答**：
$u_x=2x$，$u_{xx}=2$；$u_y=-2y$，$u_{yy}=-2$。
$\Delta u=u_{xx}+u_{yy}=2-2=0$，所以 $u$ 是调和函数。

在原点处 $u(0,0)=0$。
半径 $r=1$ 的圆周上，$z=e^{i\theta}=(\cos\theta,\sin\theta)$，$u(\cos\theta,\sin\theta)=\cos^2\theta-\sin^2\theta=\cos 2\theta$。
圆周平均值：$\frac{1}{2\pi}\int_0^{2\pi}\cos 2\theta\,d\theta=0=u(0,0)$。平均值原理成立。

（$u=x^2-y^2$ 是 $f(z)=z^2$ 的实部，所以自然是调和函数。）

**一句话点评**：$x^2-y^2$ 是最经典的调和函数之一——它是 $z^2$ 的实部。

---

### 题 4 ★ 基础
**题目**：用 Schwarz 引理的直觉判断：以下哪个函数可能是单位圆盘到自身的解析映射且满足 $f(0)=0$？
(a) $f(z)=2z$　(b) $f(z)=z^2$　(c) $f(z)=\frac{z}{2}$　(d) $f(z)=e^z-1$

**对应知识点**：Schwarz 引理——$|f(z)|\leq|z|$，等号成立时为旋转。

**解答**：
Schwarz 引理要求 $|f(z)|\leq|z|$ 对所有 $|z|<1$ 成立。

(a) $f(z)=2z$：$|f(z)|=2|z|>|z|$，违反 Schwarz 引理。实际上 $f(1/2)=1$，在边界上达到 1，但 $f(0.6)=1.2>1$，超出单位圆盘。**不可能**。

(b) $f(z)=z^2$：$|f(z)|=|z|^2\leq|z|$（因为 $|z|<1$），满足。$f(0)=0$。**可能**。

(c) $f(z)=z/2$：$|f(z)|=|z|/2\leq|z|$，满足。**可能**。

(d) $f(z)=e^z-1$：$f(0)=0$，但 $|f(z)|=|e^z-1|$。取 $z=0.9$，$e^{0.9}-1\approx1.46>0.9$，违反 $|f(z)|\leq|z|$。实际上 $e^z-1$ 在单位圆盘内无界（$z\to1$ 时 $e^z-1\to e-1\approx1.718>1$）。**不可能**。

**一句话点评**：Schwarz 引理是单位圆盘自映射的"速度限制"——从原点出发，不能比恒等映射更快。

---

## 第二层 · L1 数学分析（12题）

> **引导语**：L1层按基础到进阶到研究递进。基础题建立最小模原理和Poisson核；进阶题训练Schwarz引理和调和函数性质；研究题触及Harnack不等式。

## 题 5 ★ 基础
**题目**：证明最小模原理：若 $f(z)$ 在有界区域 $D$ 内解析且 $f(z)\neq0$，则 $|f(z)|$ 的最小值在边界上取得。

**对应知识点**：最小模原理——最大模原理对 $1/f$ 的应用。

**解答**：
因为 $f(z)\neq0$ 在 $D$ 内，所以 $g(z)=\frac{1}{f(z)}$ 在 $D$ 内解析。

由最大模原理，$|g(z)|=\frac{1}{|f(z)|}$ 的最大值在边界上取得。

设 $|g(z)|$ 的最大值为 $M_g$，在边界上取得。则 $\frac{1}{|f(z)|}\leq M_g$，即 $|f(z)|\geq\frac{1}{M_g}$。

等号在 $|g(z)|=M_g$ 处取得，即在边界上取得。所以 $|f(z)|$ 的最小值 $\frac{1}{M_g}$ 在边界上取得。

如果 $|f(z)|$ 在内部取得最小值，则 $|g(z)|$ 在内部取得最大值，由最大模原理 $g(z)$ 为常数，从而 $f(z)$ 为常数。

**一句话点评**：最小模原理是最大模原理的"倒数版本"——但需要额外假设 $f\neq0$。

---

### 题 6 ★★ 进阶
**题目**：用最大模原理证明代数基本定理：$n$ 次多项式 $P(z)=a_nz^n+\cdots+a_0$（$a_n\neq0$）至少有一个复根。

**对应知识点**：最大模原理 → 代数基本定理。

**解答**：
反证法。假设 $P(z)$ 没有复根，则 $f(z)=\frac{1}{P(z)}$ 是整函数（在整个复平面解析）。

当 $|z|\to\infty$ 时，$|P(z)|\sim|a_n||z|^n\to\infty$，所以 $|f(z)|=\frac{1}{|P(z)|}\to0$。

取足够大的 $R$，使得在 $|z|=R$ 上 $|f(z)|<|f(0)|=\frac{1}{|a_0|}$（假设 $a_0\neq0$；若 $a_0=0$ 则 $z=0$ 已是根）。

由最大模原理，$|f(z)|$ 在 $|z|\leq R$ 上的最大值在边界 $|z|=R$ 上取得。但边界上 $|f(z)|<|f(0)|$，而 $f(0)$ 在内部，矛盾。

所以 $P(z)$ 至少有一个复根。

（更直接：如果 $P$ 无根，则 $1/P$ 是有界整函数，由 Liouville 定理为常数，矛盾。最大模原理给出了有界性的证明。）

**一句话点评**：代数基本定理可以用最大模原理一行证明——无零点的多项式的倒数会在内部"冒尖"。

---

### 题 7 ★★ 进阶
**题目**：证明 Schwarz 引理，并说明等号成立时 $f(z)=e^{i\theta}z$。

**对应知识点**：Schwarz 引理的完整证明。

**解答**：
设 $f(z)$ 在 $|z|<1$ 内解析，$f(0)=0$，$|f(z)|\leq1$。

定义 $g(z)=\frac{f(z)}{z}$（$z\neq0$），$g(0)=f'(0)$。因为 $f(0)=0$，$z=0$ 是 $g(z)$ 的可去奇点，补充定义后 $g(z)$ 在单位圆盘内解析。

对任意 $r<1$，在 $|z|=r$ 上，$|g(z)|=\frac{|f(z)|}{|z|}\leq\frac{1}{r}$。

由最大模原理，$|g(z)|\leq\frac{1}{r}$ 在 $|z|\leq r$ 内成立。令 $r\to1$，得 $|g(z)|\leq1$ 在单位圆盘内成立，即 $|f(z)|\leq|z|$。

特别地，$|g(0)|=|f'(0)|\leq1$。

**等号情形**：如果在某点 $z_0\neq0$ 处 $|f(z_0)|=|z_0|$，则 $|g(z_0)|=1$，即 $g(z)$ 在内部取得最大模 1。由最大模原理，$g(z)$ 为常数 $e^{i\theta}$，所以 $f(z)=e^{i\theta}z$。

如果 $|f'(0)|=1$，则 $|g(0)|=1$，同样由最大模原理 $g(z)\equiv e^{i\theta}$，$f(z)=e^{i\theta}z$。

**一句话点评**：Schwarz 引理的证明核心是构造 $g=f/z$，然后用最大模原理"压制"它。

---

### 题 8 ★★ 进阶
**题目**：设 $f(z)$ 在单位圆盘内解析且 $|f(z)|\leq1$，$f(0)=0$。用 Schwarz 引理证明 $|f'(0)|\leq1$，并求 $f(z)=\frac{z+a}{1+\bar{a}z}$（Möbius 变换）在 $f(0)=0$ 时的形式。

**对应知识点**：Schwarz 引理的推论 + Möbius 变换。

**解答**：
由 Schwarz 引理，$|f(z)|\leq|z|$，所以 $\left|\frac{f(z)-f(0)}{z-0}\right|=\left|\frac{f(z)}{z}\right|\leq1$。令 $z\to0$，得 $|f'(0)|\leq1$。

对于 Möbius 变换 $f(z)=\frac{z+a}{1+\bar{a}z}$，要求 $f(0)=0$，则 $f(0)=\frac{a}{1}=a=0$。所以 $a=0$，$f(z)=z$（恒等映射）。

更一般地，单位圆盘的全纯自同构（到自身的一一解析映射）形式为 $f(z)=e^{i\theta}\frac{z-a}{1-\bar{a}z}$，其中 $|a|<1$。当 $f(0)=0$ 时，$a=0$，所以 $f(z)=e^{i\theta}z$——这正是 Schwarz 引理等号情形的结论。

**一句话点评**：Schwarz 引理的等号情形恰好刻画了固定原点的单位圆盘自同构——只能是旋转。

---

### 题 9 ★ 基础
**题目**：验证 Poisson 核 $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$ 的归一性：$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=1$。

**对应知识点**：Poisson 核的归一性——可以通过 Fourier 级数或留数定理验证。

**解答**：
Poisson 核的 Fourier 级数展开：
$$P_r(\theta)=\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$$

验证：$\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+\sum_{n=1}^{\infty}r^n e^{in\theta}+\sum_{n=1}^{\infty}r^n e^{-in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

而 $\frac{1-r^2}{1-2r\cos\theta+r^2}=\text{Re}\left(\frac{1+re^{i\theta}}{1-re^{i\theta}}\right)=\text{Re}\left(1+2\sum_{n=1}^{\infty}r^n e^{in\theta}\right)=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

所以积分：
$$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=\frac{1}{2\pi}\int_0^{2\pi}\left(1+2\sum_{n=1}^{\infty}r^n\cos n\theta\right)d\theta$$
$$=\frac{1}{2\pi}\left(2\pi+2\sum_{n=1}^{\infty}r^n\cdot0\right)=1$$

（因为 $\int_0^{2\pi}\cos n\theta\,d\theta=0$ 对 $n\geq1$。）

**一句话点评**：Poisson 核是一个"概率分布"——积分等于 1，非负，且在 $r\to1$ 时趋近于 Dirac delta。

---

### 题 10 ★★ 进阶
**题目**：用 Poisson 积分公式求单位圆盘内的调和函数 $u(re^{i\theta})$，已知边界值 $u(e^{i\phi})=\cos\phi$。

**对应知识点**：Poisson 积分公式的直接应用。

**解答**：
边界值 $u(e^{i\phi})=\cos\phi=\frac{e^{i\phi}+e^{-i\phi}}{2}$，其 Fourier 系数为 $c_1=c_{-1}=\frac{1}{2}$，其余为 0。

调和函数的 Fourier 展开在内部为：
$$u(re^{i\theta})=\sum_{n=-\infty}^{\infty}c_n r^{|n|}e^{in\theta}=\frac{1}{2}r e^{i\theta}+\frac{1}{2}r e^{-i\theta}=r\cos\theta$$

用 Poisson 积分公式验证：
$$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\cos\phi\cdot P_r(\theta-\phi)d\phi$$
代入 $P_r=\sum r^{|n|}e^{in(\theta-\phi)}$，只有 $n=\pm1$ 项与 $\cos\phi$ 配对非零，结果为 $r\cos\theta$。

注意 $u(re^{i\theta})=r\cos\theta=x$，这是线性函数，自然是调和函数（$\Delta x=0$）。

**一句话点评**：Poisson 积分公式把边界值"扩散"到内部——$\cos\phi$ 的边界值给出 $x=r\cos\theta$ 的内部调和延拓。

---

### 题 11 ★★ 进阶
**题目**：证明调和函数的最大值原理：非常数调和函数不能在区域内部取得最大值或最小值。

**对应知识点**：调和函数最大值原理的证明——利用平均值原理。

**解答**：
设 $u$ 在有界区域 $D$ 内调和，在 $\bar{D}$ 上连续。假设 $u$ 在 $z_0\in D$ 处取得最大值 $M$。

对任意小的 $r$（使闭圆盘在 $D$ 内），由平均值原理：
$$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})d\theta\leq\frac{1}{2\pi}\int_0^{2\pi}M d\theta=M$$

因为 $u(z_0)=M$，等号成立，所以 $u(z_0+re^{i\theta})=M$ 对所有 $\theta$ 成立（否则积分严格小于 $M$）。

由于 $r$ 可以任意小，$u\equiv M$ 在 $z_0$ 的一个邻域内成立。由调和函数的唯一性定理（或解析函数的唯一性定理，因为 $u$ 局部是解析函数的实部），$u\equiv M$ 在整个 $D$ 内成立。

所以非常数调和函数不能在内部取得最大值。最小值原理对 $-u$ 应用最大值原理即得。

**一句话点评**：调和函数的最大值原理和解析函数的最大模原理证明思路完全一样——都是平均值原理 + 连通性。

---

### 题 12 ★★ 进阶
**题目**：证明平均值原理的逆定理：如果连续函数 $u$ 在区域 $D$ 内满足平均值原理（对所有足够小的圆周），则 $u$ 是调和函数。

**对应知识点**：平均值原理的逆定理——连续性 + 平均值原理 = 调和性。

**解答**：
设 $u$ 连续且满足平均值原理。取任意闭圆盘 $\bar{D}(z_0,R)\subset D$。

设 $v$ 是圆盘内的调和函数，在边界上与 $u$ 相等（由 Poisson 积分公式，这样的 $v$ 存在）。

考虑 $w=u-v$。$w$ 在圆盘内连续，在边界上 $w=0$。

$w$ 满足平均值原理吗？$u$ 满足（假设），$v$ 满足（调和函数），所以 $w$ 也满足。

由最大值原理（满足平均值原理的连续函数也满足最大值原理，证明与调和函数相同），$w$ 的最大值和最小值都在边界上取得。但边界上 $w=0$，所以 $w\equiv0$，即 $u=v$ 在圆盘内。

因为 $v$ 是调和函数，所以 $u$ 在圆盘内调和。由于圆盘任意，$u$ 在整个 $D$ 内调和。

**一句话点评**：平均值原理不仅是调和函数的性质，更是它的等价定义——只需要连续性，不需要假设可导！

---

### 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 9 ★ 基础
**题目**：验证 Poisson 核 $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$ 的归一性：$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=1$。

**对应知识点**：Poisson 核的归一性——可以通过 Fourier 级数或留数定理验证。

**解答**：
Poisson 核的 Fourier 级数展开：
$$P_r(\theta)=\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$$

验证：$\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+\sum_{n=1}^{\infty}r^n e^{in\theta}+\sum_{n=1}^{\infty}r^n e^{-in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

而 $\frac{1-r^2}{1-2r\cos\theta+r^2}=\text{Re}\left(\frac{1+re^{i\theta}}{1-re^{i\theta}}\right)=\text{Re}\left(1+2\sum_{n=1}^{\infty}r^n e^{in\theta}\right)=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

所以积分：
$$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=\frac{1}{2\pi}\int_0^{2\pi}\left(1+2\sum_{n=1}^{\infty}r^n\cos n\theta\right)d\theta$$
$$=\frac{1}{2\pi}\left(2\pi+2\sum_{n=1}^{\infty}r^n\cdot0\right)=1$$

（因为 $\int_0^{2\pi}\cos n\theta\,d\theta=0$ 对 $n\geq1$。）

**一句话点评**：Poisson 核是一个"概率分布"——积分等于 1，非负，且在 $r\to1$ 时趋近于 Dirac delta。

---

### 题 10 ★★ 进阶
**题目**：用 Poisson 积分公式求单位圆盘内的调和函数 $u(re^{i\theta})$，已知边界值 $u(e^{i\phi})=\cos\phi$。

**对应知识点**：Poisson 积分公式的直接应用。

**解答**：
边界值 $u(e^{i\phi})=\cos\phi=\frac{e^{i\phi}+e^{-i\phi}}{2}$，其 Fourier 系数为 $c_1=c_{-1}=\frac{1}{2}$，其余为 0。

调和函数的 Fourier 展开在内部为：
$$u(re^{i\theta})=\sum_{n=-\infty}^{\infty}c_n r^{|n|}e^{in\theta}=\frac{1}{2}r e^{i\theta}+\frac{1}{2}r e^{-i\theta}=r\cos\theta$$

用 Poisson 积分公式验证：
$$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\cos\phi\cdot P_r(\theta-\phi)d\phi$$
代入 $P_r=\sum r^{|n|}e^{in(\theta-\phi)}$，只有 $n=\pm1$ 项与 $\cos\phi$ 配对非零，结果为 $r\cos\theta$。

注意 $u(re^{i\theta})=r\cos\theta=x$，这是线性函数，自然是调和函数（$\Delta x=0$）。

**一句话点评**：Poisson 积分公式把边界值"扩散"到内部——$\cos\phi$ 的边界值给出 $x=r\cos\theta$ 的内部调和延拓。

---

### 题 11 ★★ 进阶
**题目**：证明调和函数的最大值原理：非常数调和函数不能在区域内部取得最大值或最小值。

**对应知识点**：调和函数最大值原理的证明——利用平均值原理。

**解答**：
设 $u$ 在有界区域 $D$ 内调和，在 $\bar{D}$ 上连续。假设 $u$ 在 $z_0\in D$ 处取得最大值 $M$。

对任意小的 $r$（使闭圆盘在 $D$ 内），由平均值原理：
$$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})d\theta\leq\frac{1}{2\pi}\int_0^{2\pi}M d\theta=M$$

因为 $u(z_0)=M$，等号成立，所以 $u(z_0+re^{i\theta})=M$ 对所有 $\theta$ 成立（否则积分严格小于 $M$）。

由于 $r$ 可以任意小，$u\equiv M$ 在 $z_0$ 的一个邻域内成立。由调和函数的唯一性定理（或解析函数的唯一性定理，因为 $u$ 局部是解析函数的实部），$u\equiv M$ 在整个 $D$ 内成立。

所以非常数调和函数不能在内部取得最大值。最小值原理对 $-u$ 应用最大值原理即得。

**一句话点评**：调和函数的最大值原理和解析函数的最大模原理证明思路完全一样——都是平均值原理 + 连通性。

---

### 题 12 ★★ 进阶
**题目**：证明平均值原理的逆定理：如果连续函数 $u$ 在区域 $D$ 内满足平均值原理（对所有足够小的圆周），则 $u$ 是调和函数。

**对应知识点**：平均值原理的逆定理——连续性 + 平均值原理 = 调和性。

**解答**：
设 $u$ 连续且满足平均值原理。取任意闭圆盘 $\bar{D}(z_0,R)\subset D$。

设 $v$ 是圆盘内的调和函数，在边界上与 $u$ 相等（由 Poisson 积分公式，这样的 $v$ 存在）。

考虑 $w=u-v$。$w$ 在圆盘内连续，在边界上 $w=0$。

$w$ 满足平均值原理吗？$u$ 满足（假设），$v$ 满足（调和函数），所以 $w$ 也满足。

由最大值原理（满足平均值原理的连续函数也满足最大值原理，证明与调和函数相同），$w$ 的最大值和最小值都在边界上取得。但边界上 $w=0$，所以 $w\equiv0$，即 $u=v$ 在圆盘内。

因为 $v$ 是调和函数，所以 $u$ 在圆盘内调和。由于圆盘任意，$u$ 在整个 $D$ 内调和。

**一句话点评**：平均值原理不仅是调和函数的性质，更是它的等价定义——只需要连续性，不需要假设可导！

---

### 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 6 ★★ 进阶
**题目**：用最大模原理证明代数基本定理：$n$ 次多项式 $P(z)=a_nz^n+\cdots+a_0$（$a_n\neq0$）至少有一个复根。

**对应知识点**：最大模原理 → 代数基本定理。

**解答**：
反证法。假设 $P(z)$ 没有复根，则 $f(z)=\frac{1}{P(z)}$ 是整函数（在整个复平面解析）。

当 $|z|\to\infty$ 时，$|P(z)|\sim|a_n||z|^n\to\infty$，所以 $|f(z)|=\frac{1}{|P(z)|}\to0$。

取足够大的 $R$，使得在 $|z|=R$ 上 $|f(z)|<|f(0)|=\frac{1}{|a_0|}$（假设 $a_0\neq0$；若 $a_0=0$ 则 $z=0$ 已是根）。

由最大模原理，$|f(z)|$ 在 $|z|\leq R$ 上的最大值在边界 $|z|=R$ 上取得。但边界上 $|f(z)|<|f(0)|$，而 $f(0)$ 在内部，矛盾。

所以 $P(z)$ 至少有一个复根。

（更直接：如果 $P$ 无根，则 $1/P$ 是有界整函数，由 Liouville 定理为常数，矛盾。最大模原理给出了有界性的证明。）

**一句话点评**：代数基本定理可以用最大模原理一行证明——无零点的多项式的倒数会在内部"冒尖"。

---

### 题 7 ★★ 进阶
**题目**：证明 Schwarz 引理，并说明等号成立时 $f(z)=e^{i\theta}z$。

**对应知识点**：Schwarz 引理的完整证明。

**解答**：
设 $f(z)$ 在 $|z|<1$ 内解析，$f(0)=0$，$|f(z)|\leq1$。

定义 $g(z)=\frac{f(z)}{z}$（$z\neq0$），$g(0)=f'(0)$。因为 $f(0)=0$，$z=0$ 是 $g(z)$ 的可去奇点，补充定义后 $g(z)$ 在单位圆盘内解析。

对任意 $r<1$，在 $|z|=r$ 上，$|g(z)|=\frac{|f(z)|}{|z|}\leq\frac{1}{r}$。

由最大模原理，$|g(z)|\leq\frac{1}{r}$ 在 $|z|\leq r$ 内成立。令 $r\to1$，得 $|g(z)|\leq1$ 在单位圆盘内成立，即 $|f(z)|\leq|z|$。

特别地，$|g(0)|=|f'(0)|\leq1$。

**等号情形**：如果在某点 $z_0\neq0$ 处 $|f(z_0)|=|z_0|$，则 $|g(z_0)|=1$，即 $g(z)$ 在内部取得最大模 1。由最大模原理，$g(z)$ 为常数 $e^{i\theta}$，所以 $f(z)=e^{i\theta}z$。

如果 $|f'(0)|=1$，则 $|g(0)|=1$，同样由最大模原理 $g(z)\equiv e^{i\theta}$，$f(z)=e^{i\theta}z$。

**一句话点评**：Schwarz 引理的证明核心是构造 $g=f/z$，然后用最大模原理"压制"它。

---

### 题 8 ★★ 进阶
**题目**：设 $f(z)$ 在单位圆盘内解析且 $|f(z)|\leq1$，$f(0)=0$。用 Schwarz 引理证明 $|f'(0)|\leq1$，并求 $f(z)=\frac{z+a}{1+\bar{a}z}$（Möbius 变换）在 $f(0)=0$ 时的形式。

**对应知识点**：Schwarz 引理的推论 + Möbius 变换。

**解答**：
由 Schwarz 引理，$|f(z)|\leq|z|$，所以 $\left|\frac{f(z)-f(0)}{z-0}\right|=\left|\frac{f(z)}{z}\right|\leq1$。令 $z\to0$，得 $|f'(0)|\leq1$。

对于 Möbius 变换 $f(z)=\frac{z+a}{1+\bar{a}z}$，要求 $f(0)=0$，则 $f(0)=\frac{a}{1}=a=0$。所以 $a=0$，$f(z)=z$（恒等映射）。

更一般地，单位圆盘的全纯自同构（到自身的一一解析映射）形式为 $f(z)=e^{i\theta}\frac{z-a}{1-\bar{a}z}$，其中 $|a|<1$。当 $f(0)=0$ 时，$a=0$，所以 $f(z)=e^{i\theta}z$——这正是 Schwarz 引理等号情形的结论。

**一句话点评**：Schwarz 引理的等号情形恰好刻画了固定原点的单位圆盘自同构——只能是旋转。

---

### 题 9 ★ 基础
**题目**：验证 Poisson 核 $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$ 的归一性：$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=1$。

**对应知识点**：Poisson 核的归一性——可以通过 Fourier 级数或留数定理验证。

**解答**：
Poisson 核的 Fourier 级数展开：
$$P_r(\theta)=\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$$

验证：$\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+\sum_{n=1}^{\infty}r^n e^{in\theta}+\sum_{n=1}^{\infty}r^n e^{-in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

而 $\frac{1-r^2}{1-2r\cos\theta+r^2}=\text{Re}\left(\frac{1+re^{i\theta}}{1-re^{i\theta}}\right)=\text{Re}\left(1+2\sum_{n=1}^{\infty}r^n e^{in\theta}\right)=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

所以积分：
$$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=\frac{1}{2\pi}\int_0^{2\pi}\left(1+2\sum_{n=1}^{\infty}r^n\cos n\theta\right)d\theta$$
$$=\frac{1}{2\pi}\left(2\pi+2\sum_{n=1}^{\infty}r^n\cdot0\right)=1$$

（因为 $\int_0^{2\pi}\cos n\theta\,d\theta=0$ 对 $n\geq1$。）

**一句话点评**：Poisson 核是一个"概率分布"——积分等于 1，非负，且在 $r\to1$ 时趋近于 Dirac delta。

---

### 题 10 ★★ 进阶
**题目**：用 Poisson 积分公式求单位圆盘内的调和函数 $u(re^{i\theta})$，已知边界值 $u(e^{i\phi})=\cos\phi$。

**对应知识点**：Poisson 积分公式的直接应用。

**解答**：
边界值 $u(e^{i\phi})=\cos\phi=\frac{e^{i\phi}+e^{-i\phi}}{2}$，其 Fourier 系数为 $c_1=c_{-1}=\frac{1}{2}$，其余为 0。

调和函数的 Fourier 展开在内部为：
$$u(re^{i\theta})=\sum_{n=-\infty}^{\infty}c_n r^{|n|}e^{in\theta}=\frac{1}{2}r e^{i\theta}+\frac{1}{2}r e^{-i\theta}=r\cos\theta$$

用 Poisson 积分公式验证：
$$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\cos\phi\cdot P_r(\theta-\phi)d\phi$$
代入 $P_r=\sum r^{|n|}e^{in(\theta-\phi)}$，只有 $n=\pm1$ 项与 $\cos\phi$ 配对非零，结果为 $r\cos\theta$。

注意 $u(re^{i\theta})=r\cos\theta=x$，这是线性函数，自然是调和函数（$\Delta x=0$）。

**一句话点评**：Poisson 积分公式把边界值"扩散"到内部——$\cos\phi$ 的边界值给出 $x=r\cos\theta$ 的内部调和延拓。

---

### 题 11 ★★ 进阶
**题目**：证明调和函数的最大值原理：非常数调和函数不能在区域内部取得最大值或最小值。

**对应知识点**：调和函数最大值原理的证明——利用平均值原理。

**解答**：
设 $u$ 在有界区域 $D$ 内调和，在 $\bar{D}$ 上连续。假设 $u$ 在 $z_0\in D$ 处取得最大值 $M$。

对任意小的 $r$（使闭圆盘在 $D$ 内），由平均值原理：
$$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})d\theta\leq\frac{1}{2\pi}\int_0^{2\pi}M d\theta=M$$

因为 $u(z_0)=M$，等号成立，所以 $u(z_0+re^{i\theta})=M$ 对所有 $\theta$ 成立（否则积分严格小于 $M$）。

由于 $r$ 可以任意小，$u\equiv M$ 在 $z_0$ 的一个邻域内成立。由调和函数的唯一性定理（或解析函数的唯一性定理，因为 $u$ 局部是解析函数的实部），$u\equiv M$ 在整个 $D$ 内成立。

所以非常数调和函数不能在内部取得最大值。最小值原理对 $-u$ 应用最大值原理即得。

**一句话点评**：调和函数的最大值原理和解析函数的最大模原理证明思路完全一样——都是平均值原理 + 连通性。

---

### 题 12 ★★ 进阶
**题目**：证明平均值原理的逆定理：如果连续函数 $u$ 在区域 $D$ 内满足平均值原理（对所有足够小的圆周），则 $u$ 是调和函数。

**对应知识点**：平均值原理的逆定理——连续性 + 平均值原理 = 调和性。

**解答**：
设 $u$ 连续且满足平均值原理。取任意闭圆盘 $\bar{D}(z_0,R)\subset D$。

设 $v$ 是圆盘内的调和函数，在边界上与 $u$ 相等（由 Poisson 积分公式，这样的 $v$ 存在）。

考虑 $w=u-v$。$w$ 在圆盘内连续，在边界上 $w=0$。

$w$ 满足平均值原理吗？$u$ 满足（假设），$v$ 满足（调和函数），所以 $w$ 也满足。

由最大值原理（满足平均值原理的连续函数也满足最大值原理，证明与调和函数相同），$w$ 的最大值和最小值都在边界上取得。但边界上 $w=0$，所以 $w\equiv0$，即 $u=v$ 在圆盘内。

因为 $v$ 是调和函数，所以 $u$ 在圆盘内调和。由于圆盘任意，$u$ 在整个 $D$ 内调和。

**一句话点评**：平均值原理不仅是调和函数的性质，更是它的等价定义——只需要连续性，不需要假设可导！

---

### 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 7 ★★ 进阶
**题目**：证明 Schwarz 引理，并说明等号成立时 $f(z)=e^{i\theta}z$。

**对应知识点**：Schwarz 引理的完整证明。

**解答**：
设 $f(z)$ 在 $|z|<1$ 内解析，$f(0)=0$，$|f(z)|\leq1$。

定义 $g(z)=\frac{f(z)}{z}$（$z\neq0$），$g(0)=f'(0)$。因为 $f(0)=0$，$z=0$ 是 $g(z)$ 的可去奇点，补充定义后 $g(z)$ 在单位圆盘内解析。

对任意 $r<1$，在 $|z|=r$ 上，$|g(z)|=\frac{|f(z)|}{|z|}\leq\frac{1}{r}$。

由最大模原理，$|g(z)|\leq\frac{1}{r}$ 在 $|z|\leq r$ 内成立。令 $r\to1$，得 $|g(z)|\leq1$ 在单位圆盘内成立，即 $|f(z)|\leq|z|$。

特别地，$|g(0)|=|f'(0)|\leq1$。

**等号情形**：如果在某点 $z_0\neq0$ 处 $|f(z_0)|=|z_0|$，则 $|g(z_0)|=1$，即 $g(z)$ 在内部取得最大模 1。由最大模原理，$g(z)$ 为常数 $e^{i\theta}$，所以 $f(z)=e^{i\theta}z$。

如果 $|f'(0)|=1$，则 $|g(0)|=1$，同样由最大模原理 $g(z)\equiv e^{i\theta}$，$f(z)=e^{i\theta}z$。

**一句话点评**：Schwarz 引理的证明核心是构造 $g=f/z$，然后用最大模原理"压制"它。

---

### 题 8 ★★ 进阶
**题目**：设 $f(z)$ 在单位圆盘内解析且 $|f(z)|\leq1$，$f(0)=0$。用 Schwarz 引理证明 $|f'(0)|\leq1$，并求 $f(z)=\frac{z+a}{1+\bar{a}z}$（Möbius 变换）在 $f(0)=0$ 时的形式。

**对应知识点**：Schwarz 引理的推论 + Möbius 变换。

**解答**：
由 Schwarz 引理，$|f(z)|\leq|z|$，所以 $\left|\frac{f(z)-f(0)}{z-0}\right|=\left|\frac{f(z)}{z}\right|\leq1$。令 $z\to0$，得 $|f'(0)|\leq1$。

对于 Möbius 变换 $f(z)=\frac{z+a}{1+\bar{a}z}$，要求 $f(0)=0$，则 $f(0)=\frac{a}{1}=a=0$。所以 $a=0$，$f(z)=z$（恒等映射）。

更一般地，单位圆盘的全纯自同构（到自身的一一解析映射）形式为 $f(z)=e^{i\theta}\frac{z-a}{1-\bar{a}z}$，其中 $|a|<1$。当 $f(0)=0$ 时，$a=0$，所以 $f(z)=e^{i\theta}z$——这正是 Schwarz 引理等号情形的结论。

**一句话点评**：Schwarz 引理的等号情形恰好刻画了固定原点的单位圆盘自同构——只能是旋转。

---

### 题 9 ★ 基础
**题目**：验证 Poisson 核 $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$ 的归一性：$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=1$。

**对应知识点**：Poisson 核的归一性——可以通过 Fourier 级数或留数定理验证。

**解答**：
Poisson 核的 Fourier 级数展开：
$$P_r(\theta)=\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$$

验证：$\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+\sum_{n=1}^{\infty}r^n e^{in\theta}+\sum_{n=1}^{\infty}r^n e^{-in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

而 $\frac{1-r^2}{1-2r\cos\theta+r^2}=\text{Re}\left(\frac{1+re^{i\theta}}{1-re^{i\theta}}\right)=\text{Re}\left(1+2\sum_{n=1}^{\infty}r^n e^{in\theta}\right)=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

所以积分：
$$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=\frac{1}{2\pi}\int_0^{2\pi}\left(1+2\sum_{n=1}^{\infty}r^n\cos n\theta\right)d\theta$$
$$=\frac{1}{2\pi}\left(2\pi+2\sum_{n=1}^{\infty}r^n\cdot0\right)=1$$

（因为 $\int_0^{2\pi}\cos n\theta\,d\theta=0$ 对 $n\geq1$。）

**一句话点评**：Poisson 核是一个"概率分布"——积分等于 1，非负，且在 $r\to1$ 时趋近于 Dirac delta。

---

### 题 10 ★★ 进阶
**题目**：用 Poisson 积分公式求单位圆盘内的调和函数 $u(re^{i\theta})$，已知边界值 $u(e^{i\phi})=\cos\phi$。

**对应知识点**：Poisson 积分公式的直接应用。

**解答**：
边界值 $u(e^{i\phi})=\cos\phi=\frac{e^{i\phi}+e^{-i\phi}}{2}$，其 Fourier 系数为 $c_1=c_{-1}=\frac{1}{2}$，其余为 0。

调和函数的 Fourier 展开在内部为：
$$u(re^{i\theta})=\sum_{n=-\infty}^{\infty}c_n r^{|n|}e^{in\theta}=\frac{1}{2}r e^{i\theta}+\frac{1}{2}r e^{-i\theta}=r\cos\theta$$

用 Poisson 积分公式验证：
$$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\cos\phi\cdot P_r(\theta-\phi)d\phi$$
代入 $P_r=\sum r^{|n|}e^{in(\theta-\phi)}$，只有 $n=\pm1$ 项与 $\cos\phi$ 配对非零，结果为 $r\cos\theta$。

注意 $u(re^{i\theta})=r\cos\theta=x$，这是线性函数，自然是调和函数（$\Delta x=0$）。

**一句话点评**：Poisson 积分公式把边界值"扩散"到内部——$\cos\phi$ 的边界值给出 $x=r\cos\theta$ 的内部调和延拓。

---

### 题 11 ★★ 进阶
**题目**：证明调和函数的最大值原理：非常数调和函数不能在区域内部取得最大值或最小值。

**对应知识点**：调和函数最大值原理的证明——利用平均值原理。

**解答**：
设 $u$ 在有界区域 $D$ 内调和，在 $\bar{D}$ 上连续。假设 $u$ 在 $z_0\in D$ 处取得最大值 $M$。

对任意小的 $r$（使闭圆盘在 $D$ 内），由平均值原理：
$$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})d\theta\leq\frac{1}{2\pi}\int_0^{2\pi}M d\theta=M$$

因为 $u(z_0)=M$，等号成立，所以 $u(z_0+re^{i\theta})=M$ 对所有 $\theta$ 成立（否则积分严格小于 $M$）。

由于 $r$ 可以任意小，$u\equiv M$ 在 $z_0$ 的一个邻域内成立。由调和函数的唯一性定理（或解析函数的唯一性定理，因为 $u$ 局部是解析函数的实部），$u\equiv M$ 在整个 $D$ 内成立。

所以非常数调和函数不能在内部取得最大值。最小值原理对 $-u$ 应用最大值原理即得。

**一句话点评**：调和函数的最大值原理和解析函数的最大模原理证明思路完全一样——都是平均值原理 + 连通性。

---

### 题 12 ★★ 进阶
**题目**：证明平均值原理的逆定理：如果连续函数 $u$ 在区域 $D$ 内满足平均值原理（对所有足够小的圆周），则 $u$ 是调和函数。

**对应知识点**：平均值原理的逆定理——连续性 + 平均值原理 = 调和性。

**解答**：
设 $u$ 连续且满足平均值原理。取任意闭圆盘 $\bar{D}(z_0,R)\subset D$。

设 $v$ 是圆盘内的调和函数，在边界上与 $u$ 相等（由 Poisson 积分公式，这样的 $v$ 存在）。

考虑 $w=u-v$。$w$ 在圆盘内连续，在边界上 $w=0$。

$w$ 满足平均值原理吗？$u$ 满足（假设），$v$ 满足（调和函数），所以 $w$ 也满足。

由最大值原理（满足平均值原理的连续函数也满足最大值原理，证明与调和函数相同），$w$ 的最大值和最小值都在边界上取得。但边界上 $w=0$，所以 $w\equiv0$，即 $u=v$ 在圆盘内。

因为 $v$ 是调和函数，所以 $u$ 在圆盘内调和。由于圆盘任意，$u$ 在整个 $D$ 内调和。

**一句话点评**：平均值原理不仅是调和函数的性质，更是它的等价定义——只需要连续性，不需要假设可导！

---

### 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 8 ★★ 进阶
**题目**：设 $f(z)$ 在单位圆盘内解析且 $|f(z)|\leq1$，$f(0)=0$。用 Schwarz 引理证明 $|f'(0)|\leq1$，并求 $f(z)=\frac{z+a}{1+\bar{a}z}$（Möbius 变换）在 $f(0)=0$ 时的形式。

**对应知识点**：Schwarz 引理的推论 + Möbius 变换。

**解答**：
由 Schwarz 引理，$|f(z)|\leq|z|$，所以 $\left|\frac{f(z)-f(0)}{z-0}\right|=\left|\frac{f(z)}{z}\right|\leq1$。令 $z\to0$，得 $|f'(0)|\leq1$。

对于 Möbius 变换 $f(z)=\frac{z+a}{1+\bar{a}z}$，要求 $f(0)=0$，则 $f(0)=\frac{a}{1}=a=0$。所以 $a=0$，$f(z)=z$（恒等映射）。

更一般地，单位圆盘的全纯自同构（到自身的一一解析映射）形式为 $f(z)=e^{i\theta}\frac{z-a}{1-\bar{a}z}$，其中 $|a|<1$。当 $f(0)=0$ 时，$a=0$，所以 $f(z)=e^{i\theta}z$——这正是 Schwarz 引理等号情形的结论。

**一句话点评**：Schwarz 引理的等号情形恰好刻画了固定原点的单位圆盘自同构——只能是旋转。

---

### 题 9 ★ 基础
**题目**：验证 Poisson 核 $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$ 的归一性：$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=1$。

**对应知识点**：Poisson 核的归一性——可以通过 Fourier 级数或留数定理验证。

**解答**：
Poisson 核的 Fourier 级数展开：
$$P_r(\theta)=\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$$

验证：$\sum_{n=-\infty}^{\infty}r^{|n|}e^{in\theta}=1+\sum_{n=1}^{\infty}r^n e^{in\theta}+\sum_{n=1}^{\infty}r^n e^{-in\theta}=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

而 $\frac{1-r^2}{1-2r\cos\theta+r^2}=\text{Re}\left(\frac{1+re^{i\theta}}{1-re^{i\theta}}\right)=\text{Re}\left(1+2\sum_{n=1}^{\infty}r^n e^{in\theta}\right)=1+2\sum_{n=1}^{\infty}r^n\cos n\theta$。

所以积分：
$$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)d\theta=\frac{1}{2\pi}\int_0^{2\pi}\left(1+2\sum_{n=1}^{\infty}r^n\cos n\theta\right)d\theta$$
$$=\frac{1}{2\pi}\left(2\pi+2\sum_{n=1}^{\infty}r^n\cdot0\right)=1$$

（因为 $\int_0^{2\pi}\cos n\theta\,d\theta=0$ 对 $n\geq1$。）

**一句话点评**：Poisson 核是一个"概率分布"——积分等于 1，非负，且在 $r\to1$ 时趋近于 Dirac delta。

---

### 题 10 ★★ 进阶
**题目**：用 Poisson 积分公式求单位圆盘内的调和函数 $u(re^{i\theta})$，已知边界值 $u(e^{i\phi})=\cos\phi$。

**对应知识点**：Poisson 积分公式的直接应用。

**解答**：
边界值 $u(e^{i\phi})=\cos\phi=\frac{e^{i\phi}+e^{-i\phi}}{2}$，其 Fourier 系数为 $c_1=c_{-1}=\frac{1}{2}$，其余为 0。

调和函数的 Fourier 展开在内部为：
$$u(re^{i\theta})=\sum_{n=-\infty}^{\infty}c_n r^{|n|}e^{in\theta}=\frac{1}{2}r e^{i\theta}+\frac{1}{2}r e^{-i\theta}=r\cos\theta$$

用 Poisson 积分公式验证：
$$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\cos\phi\cdot P_r(\theta-\phi)d\phi$$
代入 $P_r=\sum r^{|n|}e^{in(\theta-\phi)}$，只有 $n=\pm1$ 项与 $\cos\phi$ 配对非零，结果为 $r\cos\theta$。

注意 $u(re^{i\theta})=r\cos\theta=x$，这是线性函数，自然是调和函数（$\Delta x=0$）。

**一句话点评**：Poisson 积分公式把边界值"扩散"到内部——$\cos\phi$ 的边界值给出 $x=r\cos\theta$ 的内部调和延拓。

---

### 题 11 ★★ 进阶
**题目**：证明调和函数的最大值原理：非常数调和函数不能在区域内部取得最大值或最小值。

**对应知识点**：调和函数最大值原理的证明——利用平均值原理。

**解答**：
设 $u$ 在有界区域 $D$ 内调和，在 $\bar{D}$ 上连续。假设 $u$ 在 $z_0\in D$ 处取得最大值 $M$。

对任意小的 $r$（使闭圆盘在 $D$ 内），由平均值原理：
$$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})d\theta\leq\frac{1}{2\pi}\int_0^{2\pi}M d\theta=M$$

因为 $u(z_0)=M$，等号成立，所以 $u(z_0+re^{i\theta})=M$ 对所有 $\theta$ 成立（否则积分严格小于 $M$）。

由于 $r$ 可以任意小，$u\equiv M$ 在 $z_0$ 的一个邻域内成立。由调和函数的唯一性定理（或解析函数的唯一性定理，因为 $u$ 局部是解析函数的实部），$u\equiv M$ 在整个 $D$ 内成立。

所以非常数调和函数不能在内部取得最大值。最小值原理对 $-u$ 应用最大值原理即得。

**一句话点评**：调和函数的最大值原理和解析函数的最大模原理证明思路完全一样——都是平均值原理 + 连通性。

---

### 题 12 ★★ 进阶
**题目**：证明平均值原理的逆定理：如果连续函数 $u$ 在区域 $D$ 内满足平均值原理（对所有足够小的圆周），则 $u$ 是调和函数。

**对应知识点**：平均值原理的逆定理——连续性 + 平均值原理 = 调和性。

**解答**：
设 $u$ 连续且满足平均值原理。取任意闭圆盘 $\bar{D}(z_0,R)\subset D$。

设 $v$ 是圆盘内的调和函数，在边界上与 $u$ 相等（由 Poisson 积分公式，这样的 $v$ 存在）。

考虑 $w=u-v$。$w$ 在圆盘内连续，在边界上 $w=0$。

$w$ 满足平均值原理吗？$u$ 满足（假设），$v$ 满足（调和函数），所以 $w$ 也满足。

由最大值原理（满足平均值原理的连续函数也满足最大值原理，证明与调和函数相同），$w$ 的最大值和最小值都在边界上取得。但边界上 $w=0$，所以 $w\equiv0$，即 $u=v$ 在圆盘内。

因为 $v$ 是调和函数，所以 $u$ 在圆盘内调和。由于圆盘任意，$u$ 在整个 $D$ 内调和。

**一句话点评**：平均值原理不仅是调和函数的性质，更是它的等价定义——只需要连续性，不需要假设可导！

---

### 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 10 ★★ 进阶
**题目**：用 Poisson 积分公式求单位圆盘内的调和函数 $u(re^{i\theta})$，已知边界值 $u(e^{i\phi})=\cos\phi$。

**对应知识点**：Poisson 积分公式的直接应用。

**解答**：
边界值 $u(e^{i\phi})=\cos\phi=\frac{e^{i\phi}+e^{-i\phi}}{2}$，其 Fourier 系数为 $c_1=c_{-1}=\frac{1}{2}$，其余为 0。

调和函数的 Fourier 展开在内部为：
$$u(re^{i\theta})=\sum_{n=-\infty}^{\infty}c_n r^{|n|}e^{in\theta}=\frac{1}{2}r e^{i\theta}+\frac{1}{2}r e^{-i\theta}=r\cos\theta$$

用 Poisson 积分公式验证：
$$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\cos\phi\cdot P_r(\theta-\phi)d\phi$$
代入 $P_r=\sum r^{|n|}e^{in(\theta-\phi)}$，只有 $n=\pm1$ 项与 $\cos\phi$ 配对非零，结果为 $r\cos\theta$。

注意 $u(re^{i\theta})=r\cos\theta=x$，这是线性函数，自然是调和函数（$\Delta x=0$）。

**一句话点评**：Poisson 积分公式把边界值"扩散"到内部——$\cos\phi$ 的边界值给出 $x=r\cos\theta$ 的内部调和延拓。

---

### 题 11 ★★ 进阶
**题目**：证明调和函数的最大值原理：非常数调和函数不能在区域内部取得最大值或最小值。

**对应知识点**：调和函数最大值原理的证明——利用平均值原理。

**解答**：
设 $u$ 在有界区域 $D$ 内调和，在 $\bar{D}$ 上连续。假设 $u$ 在 $z_0\in D$ 处取得最大值 $M$。

对任意小的 $r$（使闭圆盘在 $D$ 内），由平均值原理：
$$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})d\theta\leq\frac{1}{2\pi}\int_0^{2\pi}M d\theta=M$$

因为 $u(z_0)=M$，等号成立，所以 $u(z_0+re^{i\theta})=M$ 对所有 $\theta$ 成立（否则积分严格小于 $M$）。

由于 $r$ 可以任意小，$u\equiv M$ 在 $z_0$ 的一个邻域内成立。由调和函数的唯一性定理（或解析函数的唯一性定理，因为 $u$ 局部是解析函数的实部），$u\equiv M$ 在整个 $D$ 内成立。

所以非常数调和函数不能在内部取得最大值。最小值原理对 $-u$ 应用最大值原理即得。

**一句话点评**：调和函数的最大值原理和解析函数的最大模原理证明思路完全一样——都是平均值原理 + 连通性。

---

### 题 12 ★★ 进阶
**题目**：证明平均值原理的逆定理：如果连续函数 $u$ 在区域 $D$ 内满足平均值原理（对所有足够小的圆周），则 $u$ 是调和函数。

**对应知识点**：平均值原理的逆定理——连续性 + 平均值原理 = 调和性。

**解答**：
设 $u$ 连续且满足平均值原理。取任意闭圆盘 $\bar{D}(z_0,R)\subset D$。

设 $v$ 是圆盘内的调和函数，在边界上与 $u$ 相等（由 Poisson 积分公式，这样的 $v$ 存在）。

考虑 $w=u-v$。$w$ 在圆盘内连续，在边界上 $w=0$。

$w$ 满足平均值原理吗？$u$ 满足（假设），$v$ 满足（调和函数），所以 $w$ 也满足。

由最大值原理（满足平均值原理的连续函数也满足最大值原理，证明与调和函数相同），$w$ 的最大值和最小值都在边界上取得。但边界上 $w=0$，所以 $w\equiv0$，即 $u=v$ 在圆盘内。

因为 $v$ 是调和函数，所以 $u$ 在圆盘内调和。由于圆盘任意，$u$ 在整个 $D$ 内调和。

**一句话点评**：平均值原理不仅是调和函数的性质，更是它的等价定义——只需要连续性，不需要假设可导！

---

### 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 11 ★★ 进阶
**题目**：证明调和函数的最大值原理：非常数调和函数不能在区域内部取得最大值或最小值。

**对应知识点**：调和函数最大值原理的证明——利用平均值原理。

**解答**：
设 $u$ 在有界区域 $D$ 内调和，在 $\bar{D}$ 上连续。假设 $u$ 在 $z_0\in D$ 处取得最大值 $M$。

对任意小的 $r$（使闭圆盘在 $D$ 内），由平均值原理：
$$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})d\theta\leq\frac{1}{2\pi}\int_0^{2\pi}M d\theta=M$$

因为 $u(z_0)=M$，等号成立，所以 $u(z_0+re^{i\theta})=M$ 对所有 $\theta$ 成立（否则积分严格小于 $M$）。

由于 $r$ 可以任意小，$u\equiv M$ 在 $z_0$ 的一个邻域内成立。由调和函数的唯一性定理（或解析函数的唯一性定理，因为 $u$ 局部是解析函数的实部），$u\equiv M$ 在整个 $D$ 内成立。

所以非常数调和函数不能在内部取得最大值。最小值原理对 $-u$ 应用最大值原理即得。

**一句话点评**：调和函数的最大值原理和解析函数的最大模原理证明思路完全一样——都是平均值原理 + 连通性。

---

### 题 12 ★★ 进阶
**题目**：证明平均值原理的逆定理：如果连续函数 $u$ 在区域 $D$ 内满足平均值原理（对所有足够小的圆周），则 $u$ 是调和函数。

**对应知识点**：平均值原理的逆定理——连续性 + 平均值原理 = 调和性。

**解答**：
设 $u$ 连续且满足平均值原理。取任意闭圆盘 $\bar{D}(z_0,R)\subset D$。

设 $v$ 是圆盘内的调和函数，在边界上与 $u$ 相等（由 Poisson 积分公式，这样的 $v$ 存在）。

考虑 $w=u-v$。$w$ 在圆盘内连续，在边界上 $w=0$。

$w$ 满足平均值原理吗？$u$ 满足（假设），$v$ 满足（调和函数），所以 $w$ 也满足。

由最大值原理（满足平均值原理的连续函数也满足最大值原理，证明与调和函数相同），$w$ 的最大值和最小值都在边界上取得。但边界上 $w=0$，所以 $w\equiv0$，即 $u=v$ 在圆盘内。

因为 $v$ 是调和函数，所以 $u$ 在圆盘内调和。由于圆盘任意，$u$ 在整个 $D$ 内调和。

**一句话点评**：平均值原理不仅是调和函数的性质，更是它的等价定义——只需要连续性，不需要假设可导！

---

### 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 12 ★★ 进阶
**题目**：证明平均值原理的逆定理：如果连续函数 $u$ 在区域 $D$ 内满足平均值原理（对所有足够小的圆周），则 $u$ 是调和函数。

**对应知识点**：平均值原理的逆定理——连续性 + 平均值原理 = 调和性。

**解答**：
设 $u$ 连续且满足平均值原理。取任意闭圆盘 $\bar{D}(z_0,R)\subset D$。

设 $v$ 是圆盘内的调和函数，在边界上与 $u$ 相等（由 Poisson 积分公式，这样的 $v$ 存在）。

考虑 $w=u-v$。$w$ 在圆盘内连续，在边界上 $w=0$。

$w$ 满足平均值原理吗？$u$ 满足（假设），$v$ 满足（调和函数），所以 $w$ 也满足。

由最大值原理（满足平均值原理的连续函数也满足最大值原理，证明与调和函数相同），$w$ 的最大值和最小值都在边界上取得。但边界上 $w=0$，所以 $w\equiv0$，即 $u=v$ 在圆盘内。

因为 $v$ 是调和函数，所以 $u$ 在圆盘内调和。由于圆盘任意，$u$ 在整个 $D$ 内调和。

**一句话点评**：平均值原理不仅是调和函数的性质，更是它的等价定义——只需要连续性，不需要假设可导！

---

### 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 13 ★★ 进阶
**题目**：求 $u(x,y)=e^x\cos y$ 的共轭调和函数 $v(x,y)$，使得 $f(z)=u+iv$ 解析，并验证 $f(z)=e^z$。

**对应知识点**：共轭调和函数的求法——线积分或 C-R 方程。

**解答**：
由 C-R 方程：$u_x=v_y$，$u_y=-v_x$。
$u_x=e^x\cos y$，$u_y=-e^x\sin y$。

所以 $v_y=e^x\cos y$，对 $y$ 积分：$v=e^x\sin y+h(x)$。
又 $v_x=e^x\sin y+h'(x)=-u_y=e^x\sin y$，所以 $h'(x)=0$，$h(x)=C$。

取 $C=0$，$v(x,y)=e^x\sin y$。

验证：$f(z)=u+iv=e^x\cos y+ie^x\sin y=e^x(\cos y+i\sin y)=e^x e^{iy}=e^{x+iy}=e^z$。

**一句话点评**：$e^x\cos y$ 和 $e^x\sin y$ 是共轭调和函数——它们拼起来就是 $e^z$。

---

### 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 题 14 ★★★ 研究
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $|z-z_0|<R$ 内非负调和，则
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0),\quad |z-z_0|=r$$

**对应知识点**：Harnack 不等式——非负调和函数的振荡范围。

**解答**：
由 Poisson 积分公式（平移到 $z_0$，半径 $R$）：
$$u(z)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\phi})\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}d\phi$$

Poisson 核的估计：分母 $R^2-2Rr\cos\alpha+r^2$ 的范围是 $(R-r)^2\leq\text{分母}\leq(R+r)^2$。

所以：
$$\frac{R^2-r^2}{(R+r)^2}\leq P_R(r,\alpha)\leq\frac{R^2-r^2}{(R-r)^2}$$
$$\frac{R-r}{R+r}\leq P_R(r,\alpha)\leq\frac{R+r}{R-r}$$

因为 $u\geq0$，对 Poisson 积分公式两边放缩：
$$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u\,d\phi\leq u(z)\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u\,d\phi$$

由平均值原理，$\frac{1}{2\pi}\int u(z_0+Re^{i\phi})d\phi=u(z_0)$。

所以：
$$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$$

**一句话点评**：Harnack 不等式说非负调和函数不能"变化太快"——离中心越远，允许的振荡范围越大。

---

### 题 15 ★★ 进阶
**题目**：用 Schwarz-Pick 引理的微分形式 $\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$，说明单位圆盘上的双曲度量在解析映射下是"收缩"的。

**对应知识点**：Schwarz-Pick 引理的微分形式——双曲度量的收缩性。

**解答**：
单位圆盘上的双曲度量（Poincaré 度量）为 $ds^2=\frac{4|dz|^2}{(1-|z|^2)^2}$，即双曲长度元 $ds=\frac{2|dz|}{1-|z|^2}$。

Schwarz-Pick 微分形式说：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

两边乘以 2：
$$\frac{2|f'(z)|}{1-|f(z)|^2}\leq\frac{2}{1-|z|^2}$$

即 $ds_{f(z)}\leq ds_z$——像点处的双曲长度元不超过原像处的双曲长度元。

所以解析映射 $f$ 是双曲度量下的"收缩映射"（距离不增）。等号成立时 $f$ 是 Möbius 变换（双曲等距映射）。

这与 Schwarz 引理的几何意义一致：固定原点时 $|f(z)|\leq|z|$（欧氏距离收缩），而 Schwarz-Pick 说更一般的双曲距离收缩。

**一句话点评**：Schwarz-Pick 引理的微分形式就是"解析映射不增加双曲距离"——这是双曲几何与复分析的深刻联系。

---

### 题 16 ★★ 进阶
**题目**：说明调和函数的实解析性：为什么只假设 $C^2$ 且 $\Delta u=0$，就能推出 $u$ 可以展开为收敛幂级数？

**对应知识点**：调和函数的正则性——$C^2$ 自动蕴含实解析。

**解答**：
在单连通区域内，调和函数 $u$ 是某个解析函数 $f=u+iv$ 的实部（共轭调和函数 $v$ 存在）。

解析函数 $f(z)$ 在每一点 $z_0$ 附近可以展开为收敛的复幂级数：
$$f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n$$

将 $z-z_0=(x-x_0)+i(y-y_0)$ 代入，展开后取实部：
$$u(x,y)=\text{Re}\left[\sum_{n=0}^{\infty}a_n((x-x_0)+i(y-y_0))^n\right]$$

这是关于 $(x-x_0)$ 和 $(y-y_0)$ 的二重幂级数，且在某个邻域内收敛（因为复幂级数收敛）。所以 $u$ 是实解析的。

关键在于：调和性保证了共轭调和函数的存在性（在单连通区域内），从而 $u$ 是解析函数的实部，而解析函数有幂级数展开。

这是椭圆型偏微分方程（Laplace 方程）的典型正则性——解在内部自动光滑（甚至实解析），与热方程、波动方程等抛物/双曲型方程形成对比。

**一句话点评**：调和函数的定义只要求 $C^2$，但 Laplace 方程"强迫"它变成实解析——这是椭圆型方程的魔法。

---

## 第三层 · L2 复变函数（2题）

### 题 17 ★★ 进阶
**题目**：设 $f(z)$ 在单位圆盘内解析，$|f(z)|\leq1$，且 $f(0)=a$（$|a|<1$）。用 Schwarz-Pick 引理估计 $|f'(0)|$ 的上界。

**对应知识点**：Schwarz-Pick 引理在非零原点的应用。

**解答**：
Schwarz-Pick 引理的微分形式：
$$\frac{|f'(z)|}{1-|f(z)|^2}\leq\frac{1}{1-|z|^2}$$

在 $z=0$ 处：
$$\frac{|f'(0)|}{1-|f(0)|^2}\leq\frac{1}{1-0}=1$$

所以 $|f'(0)|\leq1-|f(0)|^2=1-|a|^2$。

等号成立时 $f$ 是 Möbius 变换 $f(z)=e^{i\theta}\frac{z+a}{1+\bar{a}z}$（验证：$f(0)=e^{i\theta}a$，调整相位使 $f(0)=a$，则 $f(z)=\frac{z+a}{1+\bar{a}z}$，$f'(0)=\frac{1-|a|^2}{(1+\bar{a}z)^2}\big|_{z=0}=1-|a|^2$）。

当 $a=0$ 时，上界为 1，回到 Schwarz 引理。

**一句话点评**：Schwarz-Pick 把 Schwarz 引理的 $|f'(0)|\leq1$ 推广到 $|f'(0)|\leq1-|a|^2$——像点离原点越远，导数的上界越小。

---

### 题 18 ★★★ 研究
**题目**：证明次调和函数的最大值原理：若 $v$ 是区域 $D$ 内的次调和函数（满足平均值不等式 $v(z_0)\leq\frac{1}{2\pi}\int v(z_0+re^{i\theta})d\theta$），则 $v$ 的最大值在边界上取得。

**对应知识点**：次调和函数的最大值原理——平均值不等式蕴含最大值原理。

**解答**：
设 $v$ 在有界区域 $D$ 内次调和，在 $\bar{D}$ 上连续。假设 $v$ 在 $z_0\in D$ 处取得最大值 $M$。

对任意小的 $r$：
$$v(z_0)\leq\frac{1}{2\pi}\int_0^{2\pi}v(z_0+re^{i\theta})d\theta\leq\frac{1}{2\pi}\int_0^{2\pi}M d\theta=M$$

因为 $v(z_0)=M$，等号成立，所以 $v(z_0+re^{i\theta})=M$ 对所有 $\theta$ 成立（否则积分严格小于 $M$，与 $v(z_0)\leq$ 积分 $\leq M$ 且 $v(z_0)=M$ 矛盾）。

所以 $v\equiv M$ 在 $z_0$ 的邻域内成立。

需要证明 $v\equiv M$ 在整个 $D$ 内成立。设 $E=\{z\in D:v(z)=M\}$。$E$ 是非空开集（上面证明了每一点都是内点）。$E$ 也是闭集（$v$ 连续，$E=v^{-1}(M)$ 是闭集）。因为 $D$ 连通，$E=D$，所以 $v\equiv M$。

因此非常数次调和函数不能在内部取得最大值。

解析函数的模 $|f(z)|$ 是次调和函数（在 $f\neq0$ 处 $\Delta\log|f|=0$，一般地 $|f|^p$ 对 $p>0$ 次调和），所以最大模原理是次调和函数最大值原理的特例。

**一句话点评**：最大模原理的深层原因是 $|f|$ 次调和——次调和函数的最大值原理统一了解析函数和调和函数的极值性质。

---

## 第四层 · L3 实变函数（1题）

### 题 19 ★★★ 研究
**题目**：从位势论（potential theory）的角度理解调和函数与 Dirichlet 问题：为什么边界值完全决定内部的调和函数？这与概率论中的"布朗运动首达边界"有什么联系？

**对应知识点**：调和函数的位势论解释 + 概率解释（Brown 运动）。

**解答**：
**位势论角度**：调和函数描述无旋无源的稳态场（静电势、引力势、稳态温度）。在区域内部没有源（$\Delta u=0$），所以场完全由边界上的"源分布"决定。Poisson 积分公式 $u(z)=\int_{\partial D}u(\zeta)P(z,\zeta)d\sigma(\zeta)$ 中，Poisson 核 $P(z,\zeta)$ 就是边界点 $\zeta$ 对内部点 $z$ 的"影响权重"——这是 Green 函数法向导数的特例。

**概率论角度**：调和函数有一个优美的概率解释。设 $B_t$ 是从 $z$ 出发的二维 Brown 运动，$\tau$ 是首达边界 $\partial D$ 的时间，则：
$$u(z)=\mathbb{E}^z[u(B_\tau)]$$
即调和函数在 $z$ 处的值等于从 $z$ 出发的 Brown 运动首达边界时，边界值的期望。

这个公式的直觉：Brown 运动是"随机游走"的连续极限，在每一步都随机选择方向。调和函数的平均值原理说 $u(z)$ 等于周围圆周的平均值——这正是"随机走一步后取平均"的连续版本。所以调和函数就是"边界值在 Brown 运动下的期望"。

Poisson 核 $P(z,\zeta)$ 恰好是从 $z$ 出发的 Brown 运动首达边界时在 $\zeta$ 附近的概率密度。所以 Poisson 积分公式就是全期望公式：$u(z)=\int u(\zeta)d\mathbb{P}^z(B_\tau\in d\zeta)$。

这是分析与概率的深刻联系——Dirichlet 问题的解可以用 Brown 运动的期望表示，最大值原理对应"期望不超过最大值"，Harnack 不等式对应"不同起点的 Brown 运动首达分布的比较"。

**一句话点评**：调和函数 = 边界值在 Brown 运动下的期望——Poisson 核就是首达边界的概率密度。

---


## 补充基础题（L1 数学分析 / L2 复变函数 / L3 实变函数）

### L1 数学分析基础

### 题 31 ★ 基础
**题目**：叙述调和函数的均值性质：若 $u$ 在区域 $D$ 内调和，则对任意圆盘 $B(z_0,R)\subset D$，$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\theta})d\theta$。

**对应知识点**：调和函数的均值性质——调和函数在圆心的值等于圆周上的平均值。

**解答**：
调和函数 $u$ 满足 Laplace 方程 $\Delta u=0$。
在圆盘 $B(z_0,R)$ 上，$u$ 有共轭调和函数 $v$ 使 $f=u+iv$ 解析（单连通区域上）。
由 Cauchy 积分公式：$f(z_0)=\frac{1}{2\pi i}\oint_{|z-z_0|=R}\frac{f(z)}{z-z_0}dz=\frac{1}{2\pi}\int_0^{2\pi}f(z_0+Re^{i\theta})d\theta$。
取实部：$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\theta})d\theta$。
这就是均值性质（圆盘上的调和函数在圆心的值等于边界上的平均值）。
反过来，满足均值性质的连续函数必调和（Weyl 引理的特例）。

**一句话点评**：均值性质是调和函数的核心特征——圆心值等于圆周平均值，这是 Laplace 方程的"平均值"表述。

---

### 题 32 ★ 基础
**题目**：证明调和函数的最大值原理：若 $u$ 在有界区域 $D$ 内调和、在 $\overline{D}$ 上连续且非常数，则 $u$ 的最大值和最小值都在边界 $\partial D$ 上取得。

**对应知识点**：最大值原理——调和函数不能在内部取得极值（除非常数）。

**解答**：
设 $u$ 在 $D$ 内调和，在 $\overline{D}$ 上连续。
假设 $u$ 在内部 $z_0\in D$ 取得最大值 $M$。
由均值性质，$u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})d\theta$ 对任意小的 $r$。
因为 $u(z_0+re^{i\theta})\leq M=u(z_0)$，且平均值等于 $M$，故 $u(z_0+re^{i\theta})=M$ 对所有 $\theta$（连续函数若处处 $\leq M$ 且平均值为 $M$，则处处等于 $M$）。
故 $u$ 在 $z_0$ 附近恒为 $M$。
由连通性，$u\equiv M$ 在 $D$ 上（与非常数矛盾）。
故最大值不能在内部取得，必在边界上。最小值同理（对 $-u$ 应用最大值原理）。

**一句话点评**：调和函数不能在内部"冒尖"——极值必须在边界上取得，这是椭圆型方程的基本性质。

---

### 题 33 ★ 基础
**题目**：叙述 Poisson 积分公式：单位圆盘上的调和函数由边界值唯一确定，$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta-\phi)u(e^{i\phi})d\phi$，其中 $P_r(t)=\frac{1-r^2}{1-2r\cos t+r^2}$ 是 Poisson 核。

**对应知识点**：Poisson 积分公式——Dirichlet 问题的显式解。

**解答**：
Poisson 积分公式：若 $u$ 在单位圆盘内调和、在闭圆盘上连续，则
$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\frac{1-r^2}{1-2r\cos(\theta-\phi)+r^2}u(e^{i\phi})d\phi$。
Poisson 核 $P_r(t)=\frac{1-r^2}{1-2r\cos t+r^2}$ 满足：
(1) $P_r(t)\geq0$；
(2) $\frac{1}{2\pi}\int_0^{2\pi}P_r(t)dt=1$；
(3) $P_r(t)\to0$（$r\to1$）对 $t\neq0$ 一致，在 $t=0$ 附近形成"尖峰"。
故 $P_r$ 是逼近恒等（approximate identity），$u(re^{i\theta})\to u(e^{i\theta})$（$r\to1$）。
Poisson 公式给出了单位圆盘 Dirichlet 问题的显式解：给定边界值，内部调和函数唯一确定。

**一句话点评**：Poisson 积分公式是 Dirichlet 问题的显式解——边界值通过 Poisson 核"加权平均"得到内部值。

---

### 题 34 ★★ 进阶
**题目**：证明 Harnack 不等式：若 $u$ 在圆盘 $B(0,R)$ 内非负调和，则 $\frac{R-r}{R+r}u(0)\leq u(re^{i\theta})\leq\frac{R+r}{R-r}u(0)$。

**对应知识点**：Harnack 不等式——非负调和函数的局部有界性估计。

**解答**：
由 Poisson 公式（对 $B(0,R)$ 缩放）：
$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\frac{R^2-r^2}{R^2-2Rr\cos(\theta-\phi)+r^2}u(Re^{i\phi})d\phi$。
Poisson 核的估计：$\frac{R-r}{R+r}\leq\frac{R^2-r^2}{R^2-2Rr\cos t+r^2}\leq\frac{R+r}{R-r}$。
因为 $u\geq0$，积分后得：
$\frac{R-r}{R+r}\cdot\frac{1}{2\pi}\int u(Re^{i\phi})d\phi\leq u(re^{i\theta})\leq\frac{R+r}{R-r}\cdot\frac{1}{2\pi}\int u(Re^{i\phi})d\phi$。
由均值性质，$\frac{1}{2\pi}\int u(Re^{i\phi})d\phi=u(0)$。
故 $\frac{R-r}{R+r}u(0)\leq u(re^{i\theta})\leq\frac{R+r}{R-r}u(0)$。

Harnack 不等式是 Harnack 原理（单调调和函数列收敛到调和函数或无穷）的基础，也是椭圆型偏微分方程正则性理论的核心工具。

**一句话点评**：Harnack 不等式说明非负调和函数在局部"不能太不均匀"——这是椭圆型方程的深刻性质。

---

### L2 复变函数基础

### 题 35 ★ 基础
**题目**：叙述最大模原理：若 $f$ 在有界区域 $D$ 内解析、在 $\overline{D}$ 上连续且非常数，则 $|f|$ 的最大值在边界 $\partial D$ 上取得。

**对应知识点**：最大模原理——解析函数的模不能在内部取得最大值。

**解答**：
最大模原理：若 $f$ 在有界区域 $D$ 内解析，在 $\overline{D}$ 上连续，且 $f$ 非常数，则 $|f(z)|<\max_{\partial D}|f|$ 对所有 $z\in D$。

证明：设 $|f|$ 在 $z_0\in D$ 取得最大值 $M$。
若 $f(z_0)=0$，则 $f\equiv0$（常数），矛盾。
若 $f(z_0)\neq0$，在 $z_0$ 附近取 $f$ 的一个解析对数分支 $\log f$（因为 $f(z_0)\neq0$）。
$\text{Re}(\log f)=\log|f|$ 是调和函数，在 $z_0$ 取得最大值 $\log M$。
由调和函数最大值原理，$\log|f|$ 为常数 ⟹ $|f|$ 为常数 ⟹ $f$ 为常数（D8-1-024），矛盾。
故 $|f|$ 的最大值不能在内部取得。

**一句话点评**：最大模原理是解析函数"刚性"的又一体现——模的最大值必须在边界上，不能在内部"冒尖"。

---

### 题 36 ★ 基础
**题目**：叙述 Schwarz 引理：若 $f:\mathbb{D}\to\mathbb{D}$ 解析且 $f(0)=0$，则 $|f(z)|\leq|z|$ 且 $|f'(0)|\leq1$；等号成立当且仅当 $f(z)=e^{i\theta}z$（旋转）。

**对应知识点**：Schwarz 引理——单位圆盘到自身的解析映射的基本估计。

**解答**：
Schwarz 引理：设 $f$ 在单位圆盘 $\mathbb{D}$ 内解析，$|f(z)|<1$，$f(0)=0$。则
(1) $|f(z)|\leq|z|$ 对所有 $z\in\mathbb{D}$；
(2) $|f'(0)|\leq1$；
(3) 若存在 $z_0\neq0$ 使 $|f(z_0)|=|z_0|$，或 $|f'(0)|=1$，则 $f(z)=e^{i\theta}z$（旋转）。

证明：定义 $g(z)=\frac{f(z)}{z}$（$z\neq0$），$g(0)=f'(0)$。$g$ 在 $\mathbb{D}$ 内解析（$z=0$ 是可去奇点）。
对 $|z|<r<1$，由最大模原理，$|g(z)|\leq\max_{|\zeta|=r}\frac{|f(\zeta)|}{r}\leq\frac{1}{r}$。
令 $r\to1$，得 $|g(z)|\leq1$，即 $|f(z)|\leq|z|$。$|f'(0)|=|g(0)|\leq1$。
等号成立时，$g$ 为常数 $e^{i\theta}$，故 $f(z)=e^{i\theta}z$。

**一句话点评**：Schwarz 引理是复分析中最有用的引理之一——它给出了圆盘自映射的精确估计，是双曲几何和 Pick 定理的基础。

---

### 题 37 ★★ 进阶
**题目**：用最大模原理证明代数基本定理：非常数多项式 $p(z)$ 必有复零点。

**对应知识点**：最大模原理的应用——代数基本定理的复分析证明。

**解答**：
设 $p(z)=a_nz^n+\cdots+a_0$（$n\geq1$，$a_n\neq0$）是非常数多项式。
反证：假设 $p(z)\neq0$ 对所有 $z\in\mathbb{C}$。
则 $f(z)=\frac{1}{p(z)}$ 是整函数（在全平面解析）。
当 $|z|\to\infty$ 时，$|p(z)|\sim|a_n||z|^n\to\infty$，故 $|f(z)|\to0$。
取 $R$ 足够大，使 $|f(z)|<|f(0)|=\frac{1}{|a_0|}$ 对 $|z|=R$（假设 $a_0\neq0$；若 $a_0=0$ 则 $z=0$ 已是零点）。
由最大模原理，$|f|$ 在 $|z|\leq R$ 上的最大值在边界 $|z|=R$ 上取得。
但 $|f(0)|=\frac{1}{|a_0|}>\max_{|z|=R}|f(z)|$，矛盾。
故 $p$ 必有零点。

这是代数基本定理最简洁的证明之一，完全基于最大模原理（或 Liouville 定理）。

**一句话点评**：代数基本定理可以用最大模原理一行证明——复分析的"刚性"给出了代数基本定理的最优雅证明。

---

### L3 实变函数基础

### 题 38 ★ 基础
**题目**：证明：若 $u$ 是调和函数且 $u\in L^p(\mathbb{R}^n)$（$1\leq p<\infty$），则 $u\equiv0$。

**对应知识点**：$L^p$ 调和函数必为零——调和函数的 Liouville 型定理。

**解答**：
调和函数满足均值性质：$u(x)=\frac{1}{|B_r(x)|}\int_{B_r(x)}u(y)dy$。
由 Hölder 不等式：
$|u(x)|\leq\frac{1}{|B_r|}\int_{B_r(x)}|u(y)|dy\leq\frac{1}{|B_r|}(\int_{B_r(x)}|u|^p)^{1/p}|B_r|^{1-1/p}$
$=\frac{1}{|B_r|^{1/p}}(\int_{B_r(x)}|u|^p)^{1/p}\leq\frac{\|u\|_p}{|B_r|^{1/p}}$。
$|B_r|\sim r^n\to\infty$（$r\to\infty$），故 $|u(x)|\to0$。
$u(x)=0$ 对所有 $x$。

$p=\infty$ 时，有界调和函数为常数（Liouville 定理），不一定为零。

**一句话点评**：$L^p$ 调和函数必为零——这是调和函数"刚性"的体现，也是解析函数实部的性质。

---

### 题 39 ★★ 进阶
**题目**：叙述 Weyl 引理：若 $u\in L^1_{\text{loc}}$ 满足 $\int u\Delta\phi=0$ 对所有 $\phi\in C_c^\infty$，则 $u$ 几乎处处等于一个调和函数。

**对应知识点**：Weyl 引理——弱解的正则性：分布意义下的调和函数必是光滑调和函数。

**解答**：
Weyl 引理：设 $u\in L^1_{\text{loc}}(\Omega)$，若 $\int_\Omega u\Delta\phi\,dx=0$ 对所有 $\phi\in C_c^\infty(\Omega)$，则存在调和函数 $v\in C^\infty(\Omega)$ 使 $u=v$ a.e.。

这是椭圆型方程正则性理论的基本结果：Laplace 方程的"弱解"（分布意义下的解）自动是光滑的经典解。
证明思路：(1) 用磨光核 $u_\varepsilon=u*\rho_\varepsilon$ 逼近 $u$；(2) $u_\varepsilon$ 光滑且满足 $\Delta u_\varepsilon=0$（因为 $\Delta(u*\rho_\varepsilon)=u*\Delta\rho_\varepsilon=0$，由弱解定义）；(3) 调和函数族 $\{u_\varepsilon\}$ 内闭一致有界（均值性质 + $L^1$ 控制），由 Arzela-Ascoli 取收敛子列；(4) 极限 $v$ 调和且 $u=v$ a.e.。

Weyl 引理说明 Laplace 方程是"亚椭圆"的——弱解自动光滑。这与双曲型方程（如波动方程）形成对比（弱解可能不光滑）。

**一句话点评**：Weyl 引理是椭圆正则性的基石——分布意义下的调和函数自动是光滑的经典解，这是 Laplace 方程"亚椭圆性"的体现。

---

### 题 40 ★★ 进阶
**题目**：叙述 Sobolev 空间中的 Dirichlet 问题：在 $W_0^{1,2}(\Omega)$ 中求 $u$ 使 $\int\nabla u\cdot\nabla\phi=\int f\phi$ 对所有 $\phi\in W_0^{1,2}(\Omega)$，并说明其与经典 Dirichlet 问题的关系。

**对应知识点**：Dirichlet 问题的弱形式——Sobolev 空间中的变分表述。

**解答**：
经典 Dirichlet 问题：$-\Delta u=f$ 在 $\Omega$ 内，$u=0$ 在 $\partial\Omega$ 上。
弱形式：求 $u\in W_0^{1,2}(\Omega)$（Sobolev 空间，零边界值）使
$\int_\Omega\nabla u\cdot\nabla\phi\,dx=\int_\Omega f\phi\,dx$ 对所有 $\phi\in W_0^{1,2}(\Omega)$。
这来自分部积分：$\int(-\Delta u)\phi=\int\nabla u\cdot\nabla\phi$（边界项为零因为 $\phi|_{\partial\Omega}=0$）。

存在唯一性：由 Lax-Milgram 定理（双线性型 $a(u,v)=\int\nabla u\cdot\nabla v$ 连续且强制），对任意 $f\in L^2(\Omega)$，存在唯一弱解 $u\in W_0^{1,2}(\Omega)$。
正则性：若 $\Omega$ 光滑且 $f\in L^2$，则 $u\in W^{2,2}\cap W_0^{1,2}$（椭圆正则性）；若 $f$ 更光滑，则 $u$ 更光滑，最终当 $f\in C^\infty$ 且 $\Omega$ 光滑时，$u\in C^\infty(\overline{\Omega})$（Weyl 引理 + 边界正则性）。

Sobolev 空间方法将偏微分方程从"经典解"推广到"弱解"，大大降低了解的光滑性要求，同时通过正则性理论回到经典解。这是现代偏微分方程理论的标准框架。

**一句话点评**：Sobolev 空间中的 Dirichlet 问题是现代偏微分方程理论的标准范式——先在弱意义下求解，再通过正则性理论提升光滑性。

---


## 第五层 · 跨领域综合题（11题）

### 题 20 ★★★ 经典名题
**题目**：用 Schwarz 引理证明 Liouville 定理：有界整函数必为常数。

**对应知识点**：Schwarz 引理 → Liouville 定理。

**解答**：
设 $f(z)$ 是有界整函数，$|f(z)|\leq M$ 对所有 $z$ 成立。

对任意 $R>0$，考虑 $g(z)=\frac{f(Rz)-f(0)}{2M}$。则 $g(z)$ 在单位圆盘内解析，$g(0)=0$，且
$$|g(z)|=\frac{|f(Rz)-f(0)|}{2M}\leq\frac{|f(Rz)|+|f(0)|}{2M}\leq\frac{M+M}{2M}=1$$

由 Schwarz 引理，$|g(z)|\leq|z|$，即 $\left|\frac{f(Rz)-f(0)}{2M}\right|\leq|z|$。

对任意固定的 $z\neq0$，令 $R\to\infty$（此时 $Rz\to\infty$，但 $f(Rz)$ 有界）：
$$|f(Rz)-f(0)|\leq2M|z|$$
这对任意 $R$ 成立。但我们需要更精确的估计。

实际上，对任意 $z_0$，取 $R>|z_0|$，令 $w=z_0/R$，则 $|w|<1$：
$$\left|\frac{f(z_0)-f(0)}{2M}\right|=|g(w)|\leq|w|=\frac{|z_0|}{R}$$

令 $R\to\infty$，得 $|f(z_0)-f(0)|\leq0$，所以 $f(z_0)=f(0)$。

由于 $z_0$ 任意，$f$ 为常数。

**一句话点评**：Schwarz 引理可以证明 Liouville 定理——在越来越大的圆盘上应用 Schwarz 引理，让"压缩因子"趋于 0。

---

### 题 21 ★★★ 反例与构造
**题目**：构造一个在单位圆盘内解析、在边界上连续、但不满足最大模原理"等号在内部推出常数"的反例（提示：考虑无界区域或不连通区域）。

**对应知识点**：最大模原理的条件——有界区域 + 连通。

**解答**：
最大模原理要求区域是**有界**且**连通**的。反例可以从破坏这两个条件入手。

**反例 1（无界区域）**：$f(z)=e^z$ 在右半平面 $\text{Re}(z)>0$ 内解析。在虚轴（边界）上 $|e^{iy}|=1$，但在内部 $|e^z|=e^{\text{Re}(z)}>1$。所以最大值不在边界上——因为区域无界，函数可以在"无穷远"方向增长。

**反例 2（不连通区域）**：设 $D=D_1\cup D_2$，其中 $D_1=\{|z|<1\}$，$D_2=\{|z-3|<1\}$。定义 $f(z)=z$ 在 $D_1$ 内，$f(z)=3$ 在 $D_2$ 内。$f$ 在 $D$ 内解析（每个连通分支上解析），在 $D_2$ 内部 $|f|=3$ 是常数（最大值），但 $f$ 不是整个 $D$ 上的常数。最大模原理在不连通区域上只能推出"每个连通分支上为常数"，不能推出全局常数。

**反例 3（边界不连续）**：$f(z)=\exp\left(\frac{1+z}{1-z}\right)$ 在单位圆盘内解析，$|f(z)|=\exp\left(\text{Re}\frac{1+z}{1-z}\right)=\exp\left(\frac{1-|z|^2}{|1-z|^2}\right)>1$。当 $z\to1$（边界点）时 $|f(z)|\to\infty$，所以 $f$ 在边界上不连续。最大模原理要求在闭区域上连续，这里不满足。

**一句话点评**：最大模原理的条件缺一不可——有界、连通、闭区域上连续，破坏任何一个都可能出反例。

---

### 题 22 ★★★ 定理串联
**题目**：从 Cauchy 积分公式出发，完整推导最大模原理 → Schwarz 引理 → Schwarz-Pick 引理的逻辑链。

**对应知识点**：Cauchy 积分公式 → 平均值原理 → 最大模原理 → Schwarz 引理 → Schwarz-Pick 引理。

**解答**：

**第一步：Cauchy 积分公式 → 平均值原理**
Cauchy 积分公式：$f(z_0)=\frac{1}{2\pi i}\oint_{|z-z_0|=r}\frac{f(z)}{z-z_0}dz$。
参数化 $z=z_0+re^{i\theta}$，得 $f(z_0)=\frac{1}{2\pi}\int_0^{2\pi}f(z_0+re^{i\theta})d\theta$——平均值原理。

**第二步：平均值原理 → 最大模原理**
若 $|f(z_0)|=M$ 是最大值，则 $M=|f(z_0)|\leq\frac{1}{2\pi}\int|f|d\theta\leq M$，等号成立意味着 $|f|\equiv M$ 在圆周上，由连通性 $f$ 为常数。所以非常数解析函数不能在内部取最大值。

**第三步：最大模原理 → Schwarz 引理**
构造 $g(z)=f(z)/z$（$f(0)=0$），$g$ 解析。在 $|z|=r$ 上 $|g(z)|\leq1/r$，由最大模原理 $|g(z)|\leq1/r$ 在内部，令 $r\to1$ 得 $|g(z)|\leq1$，即 $|f(z)|\leq|z|$。

**第四步：Schwarz 引理 → Schwarz-Pick 引理**
对任意 $a\in D$，构造 Möbius 变换 $\phi_a(z)=\frac{z-a}{1-\bar{a}z}$（将 $a$ 映到 0，单位圆盘自同构）。考虑 $F(z)=\phi_{f(a)}\circ f\circ\phi_a^{-1}(z)$，则 $F(0)=0$，$|F(z)|\leq1$。由 Schwarz 引理 $|F(z)|\leq|z|$。代回 $z=\phi_a(w)$，得 $|\phi_{f(a)}(f(w))|\leq|\phi_a(w)|$，即 Schwarz-Pick 引理。

**逻辑链**：Cauchy 积分公式（积分表示）→ 平均值原理（局部平均）→ 最大模原理（极值在边界）→ Schwarz 引理（圆盘自映射压缩）→ Schwarz-Pick 引理（双曲距离收缩）。

**一句话点评**：整个链条从一个积分公式出发，层层推进到双曲几何——复分析的定理之间是有机联系的。

---

### 题 23 ★★ 基础综合
**题目**：设 $u(x,y)=x^3-3xy^2$。(a) 验证 $u$ 是调和函数；(b) 求共轭调和函数 $v$；(c) 写出对应的解析函数 $f(z)$。

**对应知识点**：调和函数验证 + 共轭调和函数 + 解析函数。

**解答**：
(a) $u_x=3x^2-3y^2$，$u_{xx}=6x$；$u_y=-6xy$，$u_{yy}=-6x$。
$\Delta u=6x-6x=0$，调和。

(b) 由 C-R 方程：$v_y=u_x=3x^2-3y^2$，对 $y$ 积分：$v=3x^2y-y^3+h(x)$。
$v_x=6xy+h'(x)=-u_y=6xy$，所以 $h'(x)=0$，$h(x)=C$。
取 $C=0$，$v=3x^2y-y^3$。

(c) $f(z)=u+iv=(x^3-3xy^2)+i(3x^2y-y^3)=x^3+3ix^2y-3xy^2-iy^3=(x+iy)^3=z^3$。

**一句话点评**：$x^3-3xy^2$ 是 $z^3$ 的实部——所有整系数齐次调和多项式都是 $z^n$ 实部或虚部的线性组合。

---

### 题 24 ★★★ 经典名题
**题目**：用 Poisson 积分公式求解上半平面的 Dirichlet 问题：已知边界值 $u(x,0)=f(x)$，求上半平面内的调和函数 $u(x,y)$。

**对应知识点**：上半平面的 Poisson 积分公式——通过共形映射从圆盘公式推导。

**解答**：
上半平面 $\mathbb{H}=\{z:\text{Im}(z)>0\}$ 到单位圆盘的共形映射：$w=\frac{z-i}{z+i}$（将 $i$ 映到 0，实轴映到单位圆周）。

逆映射：$z=i\frac{1+w}{1-w}$。

在单位圆盘上用 Poisson 公式，再通过共形映射拉回上半平面。边界点 $x\in\mathbb{R}$ 对应 $w=\frac{x-i}{x+i}=e^{i\theta}$，其中 $\theta=2\arctan(1/x)$（或更直接地计算）。

上半平面的 Poisson 核为：
$$P_y(x)=\frac{1}{\pi}\cdot\frac{y}{x^2+y^2}$$

所以上半平面的 Dirichlet 问题解为：
$$u(x,y)=\frac{1}{\pi}\int_{-\infty}^{\infty}f(t)\frac{y}{(x-t)^2+y^2}dt$$

验证 Poisson 核性质：$\frac{1}{\pi}\int_{-\infty}^{\infty}\frac{y}{x^2+y^2}dx=\frac{1}{\pi}[\arctan(x/y)]_{-\infty}^{\infty}=1$，归一性成立。当 $y\to0^+$ 时，$\frac{y}{(x-t)^2+y^2}\to\pi\delta(x-t)$，近似恒等性成立。

**一句话点评**：上半平面的 Poisson 核 $\frac{1}{\pi}\frac{y}{x^2+y^2}$ 是 Cauchy 分布的概率密度——调和函数值就是边界值的 Cauchy 加权平均。

---

### 题 25 ★★ 反例与构造
**题目**：说明 $u(x,y)=\ln(x^2+y^2)$ 在 $\mathbb{R}^2\setminus\{0\}$ 内是调和函数，但在原点处不满足平均值原理（以原点为中心）。这说明了什么？

**对应知识点**：调和函数的区域依赖性——去掉奇点后调和，但在奇点处不满足平均值原理。

**解答**：
$u=\ln(x^2+y^2)=2\ln|z|=2\text{Re}(\log z)$。在 $z\neq0$ 处，$\log z$ 局部解析，所以 $u$ 调和。

直接验证：$u_x=\frac{2x}{x^2+y^2}$，$u_{xx}=\frac{2(y^2-x^2)}{(x^2+y^2)^2}$；$u_y=\frac{2y}{x^2+y^2}$，$u_{yy}=\frac{2(x^2-y^2)}{(x^2+y^2)^2}$。$\Delta u=0$。

但以原点为中心的圆周平均值：
$$\frac{1}{2\pi}\int_0^{2\pi}\ln(r^2)d\theta=\ln(r^2)=2\ln r$$
而 $u(0,0)$ 不存在（$u$ 在原点无定义，且 $\lim_{z\to0}u=-\infty$）。

这说明：
1. 调和函数的定义依赖于区域——$u$ 在 $\mathbb{R}^2\setminus\{0\}$ 内调和，但不能延拓到原点（原点是对数奇点）。
2. 平均值原理要求圆心在区域内且闭圆盘在区域内——以原点为中心的圆盘包含原点（不在区域内），所以平均值原理不适用。
3. $\ln|z|$ 是 Laplace 方程的**基本解**——它在原点有奇点，且 $\Delta\ln|z|=2\pi\delta_0$（分布意义下）。这正是 Green 函数的基础。

**一句话点评**：$\ln|z|$ 是 Laplace 方程的"原子"——它在除原点外调和，在原点处携带 $2\pi$ 的"电荷"。

---

### 题 26 ★★★ 定理串联
**题目**：用 Harnack 收敛定理证明：若 $\{u_n\}$ 是区域 $D$ 内单调递增的调和函数序列，且在某点 $z_0$ 处有界，则 $\{u_n\}$ 在 $D$ 内内闭一致收敛于一个调和函数。

**对应知识点**：Harnack 收敛定理——单调调和函数序列的极限仍调和。

**解答**：
设 $u_n$ 单调递增，$u_n(z_0)\leq M$。令 $v_n=u_n-u_1\geq0$，则 $v_n$ 是非负调和函数序列，单调递增，$v_n(z_0)\leq M-u_1(z_0)$。

对任意紧子集 $K\subset D$，取有限个圆盘覆盖 $K$，每个圆盘的闭包在 $D$ 内。对每个圆盘应用 Harnack 不等式：存在常数 $C$（依赖于圆盘和 $z_0$ 的距离），使得对所有 $z$ 在圆盘内，$v_n(z)\leq C v_n(z_0)\leq C(M-u_1(z_0))$。所以 $v_n$ 在 $K$ 上一致有界。

单调递增且一致有界的序列逐点收敛：$v_n(z)\to v(z)$。

需要证明一致收敛。对任意 $m>n$，$v_m-v_n\geq0$ 是调和函数。由 Harnack 不等式，在紧集 $K$ 上：
$$v_m(z)-v_n(z)\leq C'(v_m(z_0)-v_n(z_0))$$
因为 $v_n(z_0)$ 收敛（单调有界），所以 $v_m(z_0)-v_n(z_0)\to0$（$m,n\to\infty$），从而 $v_m-v_n$ 在 $K$ 上一致趋于 0。所以 $\{v_n\}$ 在 $K$ 上一致收敛。

极限 $v$ 是调和函数：一致收敛的调和函数序列的极限仍调和（因为可以用平均值原理——$v_n$ 满足平均值原理，一致收敛取极限后 $v$ 也满足，由逆定理 $v$ 调和）。

所以 $u_n=v_n+u_1$ 内闭一致收敛于调和函数 $v+u_1$。

**一句话点评**：Harnack 收敛定理是"单调收敛定理"在调和函数中的版本——而且极限自动保持调和性，不需要额外假设。

---

### 题 27 ★★ 基础综合
**题目**：设 $f(z)$ 在单位圆盘内解析且 $|f(z)|\leq1$。用 Schwarz-Pick 引理证明：对任意 $|a|<1$，
$$\left|\frac{f(z)-f(a)}{1-\overline{f(a)}f(z)}\right|\leq\left|\frac{z-a}{1-\bar{a}z}\right|$$

**对应知识点**：Schwarz-Pick 引理的标准形式——伪双曲距离收缩。

**解答**：
定义 Möbius 变换：
$$\phi_a(z)=\frac{z-a}{1-\bar{a}z},\quad \phi_{f(a)}(w)=\frac{w-f(a)}{1-\overline{f(a)}w}$$

这两个变换都是单位圆盘的自同构（将 $a$ 和 $f(a)$ 分别映到 0）。

考虑 $F(z)=\phi_{f(a)}(f(\phi_a^{-1}(z)))$。则：
- $F$ 在单位圆盘内解析（复合解析函数）
- $|F(z)|\leq1$（因为 $f$ 和 Möbius 变换都将单位圆盘映到自身）
- $F(0)=\phi_{f(a)}(f(a))=0$

由 Schwarz 引理，$|F(z)|\leq|z|$。

令 $z=\phi_a(w)$（即 $w=\phi_a^{-1}(z)$），则：
$$|F(\phi_a(w))|=|\phi_{f(a)}(f(w))|\leq|\phi_a(w)|$$

即：
$$\left|\frac{f(w)-f(a)}{1-\overline{f(a)}f(w)}\right|\leq\left|\frac{w-a}{1-\bar{a}w}\right|$$

**一句话点评**：Schwarz-Pick 引理说解析映射不增加伪双曲距离——这是 Schwarz 引理的"坐标不变"版本。

---

### 题 28 ★★★ 经典名题
**题目**：用最大模原理证明 Hadamard 三圆定理：若 $f(z)$ 在圆环 $r_1<|z|<r_2$ 内解析，$M(r)=\max_{|z|=r}|f(z)|$，则 $\log M(r)$ 是 $\log r$ 的凸函数，即
$$\log M(r)\leq\frac{\log(r_2/r)}{\log(r_2/r_1)}\log M(r_1)+\frac{\log(r/r_1)}{\log(r_2/r_1)}\log M(r_2)$$

**对应知识点**：Hadamard 三圆定理——最大模原理在圆环上的应用。

**解答**：
对任意 $\alpha$，考虑 $g(z)=z^\alpha f(z)$（取定一个分支，在圆环内单值）。$|g(z)|=|z|^\alpha|f(z)|=r^\alpha|f(z)|$。

由最大模原理（在圆环上，注意圆环是多连通的，但最大模原理仍适用——最大值在内外边界之一取得）：
$$\max_{r_1\leq|z|\leq r_2}|g(z)|=\max\left(r_1^\alpha M(r_1), r_2^\alpha M(r_2)\right)$$

所以对任意 $r\in(r_1,r_2)$：
$$r^\alpha M(r)\leq\max\left(r_1^\alpha M(r_1), r_2^\alpha M(r_2)\right)$$

选择 $\alpha$ 使得 $r_1^\alpha M(r_1)=r_2^\alpha M(r_2)$，即
$$\alpha\log r_1+\log M(r_1)=\alpha\log r_2+\log M(r_2)$$
$$\alpha=-\frac{\log M(r_2)-\log M(r_1)}{\log r_2-\log r_1}$$

此时 $r^\alpha M(r)\leq r_1^\alpha M(r_1)$，取对数：
$$\alpha\log r+\log M(r)\leq\alpha\log r_1+\log M(r_1)$$
$$\log M(r)\leq\alpha(\log r_1-\log r)+\log M(r_1)$$

代入 $\alpha$ 的表达式，化简即得：
$$\log M(r)\leq\frac{\log(r_2/r)}{\log(r_2/r_1)}\log M(r_1)+\frac{\log(r/r_1)}{\log(r_2/r_1)}\log M(r_2)$$

这说明 $\log M(r)$ 关于 $\log r$ 是凸函数。

**一句话点评**：Hadamard 三圆定理是最大模原理的"对数凸"版本——解析函数在圆环上的最大模满足对数凸性。

---

### 题 29 ★★★ 研究
**题目**：从几何视角总结最大模原理与调和函数的完整体系：最大模原理的"地形"几何、Schwarz引理的"距离压缩"几何、调和函数的"稳态场"几何、Poisson核的"加权平均"几何、Harnack不等式的"振荡范围"几何。

**对应知识点**：最大模原理与调和函数体系的几何全景。

**解答**：

**1. 最大模原理的地形几何**
解析函数的模 $|f(z)|$ 是复平面上的"地形高度"。最大模原理说这个地形不能有内部"山峰"——最高点一定在边缘。深层原因是 $|f|$ 是次调和函数（$\Delta\log|f|\geq0$），次调和函数的最大值在边界上。从开映射定理看：非常数解析函数将开集映为开集，所以内部点的像不可能是模的最大值（否则像集不是开集）。

**2. Schwarz 引理的距离压缩几何**
单位圆盘到自身、固定原点的解析映射不能拉伸任何点到原点的距离——$|f(z)|\leq|z|$。这是"速度限制"：从原点出发，不能比恒等映射更快。等号成立时只能是旋转（保持距离的映射）。Schwarz-Pick 引理推广到双曲距离：解析映射不增加双曲距离。这是双曲几何与复分析的桥梁——单位圆盘上的 Poincaré 度量在解析映射下收缩。

**3. 调和函数的稳态场几何**
调和函数描述稳态物理场（温度、电势、引力势）。平均值原理说中心值等于周围圆周平均——这是"无热源"的稳态条件。最大值原理说不能有内部"热点"或"冷点"——极值一定在边界。调和函数的地形是"鞍形"的——没有山峰也没有山谷，只有斜坡和鞍部。

**4. Poisson 核的加权平均几何**
Poisson 核 $P_r(\theta)$ 是边界值的"概率分布"——对于内部点 $re^{i\theta}$，离它"最近"的边界点权重最大，最远的边界点权重最小。当内部点趋近边界时，权重集中在该边界点附近（近似恒等，趋近 Dirac delta）。Poisson 积分公式就是"边界值的加权平均决定内部值"——这是 Dirichlet 问题的显式解。

**5. Harnack 不等式的振荡范围几何**
非负调和函数在圆盘内的取值被中心值"夹住"：$\frac{R-r}{R+r}u(z_0)\leq u(z)\leq\frac{R+r}{R-r}u(z_0)$。离中心越远，允许的振荡范围越大（系数从 1 趋向 0 和 $\infty$）。这说明非负调和函数不能"突变"——它的变化速度受几何限制。Harnack 收敛定理进一步说单调调和序列的极限仍调和——正则性在极限下保持。

**6. 正则性的几何**
调和函数只需要 $C^2$ 就自动实解析——这是椭圆型方程的"内部光滑性"。从几何上看，Laplace 方程 $\Delta u=0$ 意味着函数在每个方向上的"弯曲"相互抵消，这种强约束迫使函数无限光滑。平均值原理甚至不需要可导性——连续 + 平均值原理就蕴含调和性。

**一句话点评**：最大模原理与调和函数的整个体系是几何的——地形、距离压缩、稳态场、加权平均、振荡范围，每一个概念都有清晰的物理和几何图像。

---

### 题 30 ★★★ 研究
**题目**：比较解析函数的最大模原理与调和函数的最大值原理的异同，并说明为什么解析函数的模只满足最大值原理（最小模需要 $f\neq0$），而调和函数同时满足最大值和最小值原理。

**对应知识点**：最大模原理 vs 调和最大值原理——次调和 vs 调和。

**解答**：

**相同点**：
1. 都由平均值原理推导而来（解析函数的 Cauchy 平均值原理 vs 调和函数的平均值原理）。
2. 都说明非常数函数不能在区域内部取得极值（最大值）。
3. 都蕴含唯一性定理（Dirichlet 问题解唯一）。
4. 证明结构相同：假设内部取最大值 → 平均值原理推出邻域内恒等于最大值 → 连通性推出全局常数。

**不同点**：
1. **对象不同**：最大模原理针对 $|f(z)|$（解析函数的模，非负函数），调和最大值原理针对 $u(x,y)$（调和函数，可正可负）。
2. **最小值原理**：调和函数同时满足最大值和最小值原理（对 $-u$ 应用最大值原理）。解析函数的模 $|f|$ 只满足最大值原理——最小模原理需要额外假设 $f\neq0$（对 $1/f$ 应用最大模原理）。
3. **原因**：$|f(z)|$ 是**次调和**函数（$\Delta|f|\geq0$，在 $f\neq0$ 处 $\Delta\log|f|=0$），次调和函数只满足最大值原理，不满足最小值原理（次调和函数可以在内部取得最小值，例如 $|z|$ 在原点取最小值 0）。而调和函数满足 $\Delta u=0$，同时满足最大和最小值原理。
4. **几何**：$|f|$ 的地形可以有"山谷"（最小值在内部，例如 $|z|$ 在原点），但不能有"山峰"。调和函数的地形既不能有山峰也不能有山谷——只能是鞍形。

**深层联系**：
在 $f\neq0$ 的区域内，$\log|f|$ 是调和函数（因为 $\log|f|=\text{Re}(\log f)$，而 $\log f$ 局部解析）。所以 $\log|f|$ 同时满足最大和最小值原理。但 $|f|=e^{\log|f|}$ 是 $\log|f|$ 的递增凸函数，凸函数保持最大值原理（次调和性），但不保持最小值原理。这就是为什么 $|f|$ 只有最大值原理，而 $\log|f|$ 有最大最小值原理。

**一句话点评**：$|f|$ 次调和所以只有最大值原理，$\log|f|$ 调和所以有最大最小值原理——指数函数把调和变成了次调和。

---

## 附录 · 知识点索引

| 题号 | 核心知识点 | 难度 |
|------|-----------|------|
| 1 | 最大模原理的地形直觉 | ★ |
| 2 | 调和函数的稳态温度直觉 | ★ |
| 3 | 调和函数验证 + 平均值原理 | ★ |
| 4 | Schwarz 引理直觉判别 | ★ |
| 5 | 最小模原理 | ★ |
| 6 | 最大模原理证代数基本定理 | ★★ |
| 7 | Schwarz 引理证明 | ★★ |
| 8 | Schwarz 引理推论 + Möbius 变换 | ★★ |
| 9 | Poisson 核归一性 | ★ |
| 10 | Poisson 积分公式应用 | ★★ |
| 11 | 调和函数最大值原理证明 | ★★ |
| 12 | 平均值原理逆定理 | ★★ |
| 13 | 共轭调和函数求法 | ★★ |
| 14 | Harnack 不等式证明 | ★★★ |
| 15 | Schwarz-Pick 微分形式 + 双曲度量 | ★★ |
| 16 | 调和函数实解析性 | ★★ |
| 17 | Schwarz-Pick 估计导数 | ★★ |
| 18 | 次调和函数最大值原理 | ★★★ |
| 19 | 位势论 + Brown 运动解释 | ★★★ |
| 20 | Schwarz 引理证 Liouville 定理 | ★★★ |
| 21 | 最大模原理反例 | ★★★ |
| 22 | Cauchy→最大模→Schwarz→Schwarz-Pick 链 | ★★★ |
| 23 | 调和函数 + 共轭 + 解析函数 | ★★ |
| 24 | 上半平面 Poisson 公式 | ★★★ |
| 25 | $\ln|z|$ 基本解 | ★★ |
| 26 | Harnack 收敛定理 | ★★★ |
| 27 | Schwarz-Pick 标准形式证明 | ★★ |
| 28 | Hadamard 三圆定理 | ★★★ |
| 29 | 最大模与调和函数的几何全景 | ★★★ |
| 30 | 最大模原理 vs 调和最大值原理比较 | ★★★ |
