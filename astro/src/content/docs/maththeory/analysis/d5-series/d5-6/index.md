---
title: "D5-6 正交级数与 Fourier 分析"
description: "领域 ：D5 级数"
tags:
  - "数学理论"
  - "分析学"
  - "D5 级数"
---

> 领域 ：D5 级数

---

## 第一章 内积空间与正交性

### 1.1 内积的定义

在 D6-5 中我们学习了 Lp 空间和 Banach 空间。现在我们引入一个更特殊的结构——内积。

> **定义**：设 $V$ 是实数域（或复数域）上的线性空间。如果对任意 $x, y \in V$，都有一个实数（或复数）$\langle x, y \rangle$ 与之对应，满足：
> 1. **正定性**：$\langle x, x \rangle \geq 0$，且 $\langle x, x \rangle = 0 \Leftrightarrow x = 0$；
> 2. **线性性**（第一变元）：$\langle \alpha x + \beta y, z \rangle = \alpha \langle x, z \rangle + \beta \langle y, z \rangle$；
> 3. **对称性**（实空间）或 **共轭对称性**（复空间）：$\langle x, y \rangle = \overline{\langle y, x \rangle}$。
>
> 则称 $\langle x, y \rangle$ 为 $x$ 与 $y$ 的**内积**，$V$ 称为**内积空间**。

内积诱导出范数 $\|x\| = \sqrt{\langle x, x \rangle}$。完备的内积空间称为 **Hilbert 空间**。

### 1.2 函数空间中的内积

在区间 $[a, b]$ 上的平方可积函数空间 $L^2[a, b]$ 中，可以定义内积：

$$\langle f, g \rangle = \int_a^b f(x) \overline{g(x)} \, dx$$

（实函数时去掉共轭。）

这个内积诱导的范数是 $\|f\|_2 = \sqrt{\int_a^b |f(x)|^2 dx}$，即 L² 范数。

$L^2[a, b]$ 是 Hilbert 空间——它是完备的（D6-5 中证明了 Lp 空间的完备性）。

### 1.3 正交性与正交函数系

> **定义**：在内积空间中，如果 $\langle f, g \rangle = 0$，则称 $f$ 与 $g$ **正交**。

> **定义**：如果函数系 $\{\varphi_n\}_{n=1}^{\infty}$ 中任意两个不同的函数都正交，即 $\langle \varphi_m, \varphi_n \rangle = 0$（$m \neq n$），则称 $\{\varphi_n\}$ 为**正交函数系**。

如果进一步有 $\|\varphi_n\| = 1$ 对所有 $n$，则称为**标准正交函数系**。

📐 **几何理解**：正交性是三维空间中"垂直"概念在无穷维函数空间中的推广。在三维空间中，两个向量垂直当且仅当它们的点积为 0；在函数空间中，两个函数正交当且仅当它们的内积（积分）为 0。正交函数系就像函数空间中的一组"坐标轴"，每个函数都可以表示为这些坐标轴上的投影之和。

### 1.4 正交投影与最佳逼近

> **定理**：设 $\{\varphi_n\}_{n=1}^{N}$ 是标准正交函数系，$f$ 是任意函数。则 $f$ 在 $\text{span}\{\varphi_1, \ldots, \varphi_N\}$ 上的最佳逼近（使 $\|f - g\|$ 最小的 $g$）为：
> $$g = \sum_{n=1}^{N} \langle f, \varphi_n \rangle \varphi_n$$
> 其中 $\langle f, \varphi_n \rangle$ 是 $f$ 在 $\varphi_n$ 方向上的**正交投影**。

这个定理是 Fourier 级数的理论基础——Fourier 系数就是函数在三角函数系各方向上的正交投影，Fourier 级数的部分和就是函数在三角函数系张成的有限维子空间上的最佳逼近。

---

## 第二章 三角函数系的正交性

### 2.1 三角函数系

在区间 $[-\pi, \pi]$ 上，考虑函数系：

$$\{1, \cos x, \sin x, \cos 2x, \sin 2x, \ldots, \cos nx, \sin nx, \ldots\}$$

这就是**三角函数系**。

### 2.2 正交性的验证

利用积化和差公式，可以验证三角函数系的正交性：

$$\int_{-\pi}^{\pi} \cos mx \cos nx \, dx = \begin{cases} 0, & m \neq n \\ 2\pi, & m = n = 0 \\ \pi, & m = n \geq 1 \end{cases}$$

$$\int_{-\pi}^{\pi} \sin mx \sin nx \, dx = \begin{cases} 0, & m \neq n \\ \pi, & m = n \geq 1 \end{cases}$$

$$\int_{-\pi}^{\pi} \cos mx \sin nx \, dx = 0 \quad (\text{对所有 } m, n)$$

所以三角函数系在 $[-\pi, \pi]$ 上是正交函数系。

对应的标准正交函数系为：

$$\left\{\frac{1}{\sqrt{2\pi}}, \frac{\cos x}{\sqrt{\pi}}, \frac{\sin x}{\sqrt{\pi}}, \frac{\cos 2x}{\sqrt{\pi}}, \frac{\sin 2x}{\sqrt{\pi}}, \ldots\right\}$$

### 2.3 复指数形式的三角函数系

利用 Euler 公式 $e^{inx} = \cos nx + i \sin nx$，三角函数系可以等价地表示为复指数函数系：

$$\{e^{inx}\}_{n=-\infty}^{\infty} = \{\ldots, e^{-2ix}, e^{-ix}, 1, e^{ix}, e^{2ix}, \ldots\}$$

这个函数系在 $[-\pi, \pi]$ 上也是正交的：

$$\int_{-\pi}^{\pi} e^{imx} \overline{e^{inx}} \, dx = \int_{-\pi}^{\pi} e^{i(m-n)x} \, dx = \begin{cases} 0, & m \neq n \\ 2\pi, & m = n \end{cases}$$

复指数形式更简洁，在理论推导中更方便。

📐 **几何理解**：复指数函数 $e^{inx}$ 的几何意义是"单位圆上以角速度 $n$ 旋转的点"。当 $m \neq n$ 时，$e^{imx}$ 和 $e^{inx}$ 以不同的角速度旋转，它们的乘积 $e^{i(m-n)x}$ 在一个周期内的积分为 0——因为旋转的对称性，正负贡献相互抵消。这就是正交性的几何本质。

---

## 第三章 Fourier 级数的定义与系数

### 3.1 Fourier 级数的三角形式

设 $f(x)$ 是 $[-\pi, \pi]$ 上的可积函数。定义：

$$a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \, dx$$

$$a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos nx \, dx \quad (n \geq 1)$$

$$b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin nx \, dx \quad (n \geq 1)$$

这些系数称为 $f(x)$ 的 **Fourier 系数**。

对应的级数：

$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$$

称为 $f(x)$ 的 **Fourier 级数**。

注意这里用 $\sim$ 而不是 $=$，因为 Fourier 级数是否收敛到 $f(x)$ 还需要进一步讨论。

### 3.2 Fourier 级数的复指数形式

利用 Euler 公式，Fourier 级数可以写成更简洁的复指数形式：

$$f(x) \sim \sum_{n=-\infty}^{\infty} c_n e^{inx}$$

其中

$$c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} \, dx$$

复指数形式与三角形式的关系：

$$c_0 = \frac{a_0}{2}, \quad c_n = \frac{a_n - i b_n}{2}, \quad c_{-n} = \frac{a_n + i b_n}{2} \quad (n \geq 1)$$

### 3.3 一般周期的 Fourier 级数

如果 $f(x)$ 的周期为 $2L$（而不是 $2\pi$），则 Fourier 级数为：

$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \cos \frac{n\pi x}{L} + b_n \sin \frac{n\pi x}{L}\right)$$

其中

$$a_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos \frac{n\pi x}{L} \, dx, \quad b_n = \frac{1}{L} \int_{-L}^{L} f(x) \sin \frac{n\pi x}{L} \, dx$$

### 3.4 Fourier 系数的几何意义

📐 **几何理解**：Fourier 系数 $c_n$ 是函数 $f(x)$ 在"频率为 $n$ 的复指数方向"上的正交投影。就像三维空间中一个向量在 $x$ 轴上的投影是 $\vec{v} \cdot \vec{e}_x$，函数 $f$ 在 $e^{inx}$ 方向上的投影是 $\langle f, e^{inx} \rangle / \|e^{inx}\|^2 = c_n$。

Fourier 级数就是将函数分解为不同频率的简谐波的叠加——每个 $c_n e^{inx}$ 是一个频率为 $n$、振幅为 $|c_n|$、相位为 $\arg(c_n)$ 的简谐波。这就是"频谱分析"的数学基础。

---

## 第四章 Fourier 级数的收敛性

### 4.1 收敛性的三种类型

Fourier 级数的收敛性是一个复杂而深刻的问题，有三种主要的收敛概念：

1. **逐点收敛**：对每个固定的 $x$，部分和 $S_N(x) \to f(x)$。
2. **一致收敛**：$\sup_x |S_N(x) - f(x)| \to 0$。
3. **L² 收敛**：$\|S_N - f\|_2 \to 0$，即 $\int |S_N(x) - f(x)|^2 dx \to 0$。

这三种收敛性的强度不同：一致收敛 ⇒ 逐点收敛和 L² 收敛；逐点收敛和 L² 收敛之间没有蕴含关系。

### 4.2 Dirichlet 条件与逐点收敛

> **Dirichlet 定理**：如果 $f(x)$ 在 $[-\pi, \pi]$ 上满足 Dirichlet 条件：
> 1. 连续或只有有限个第一类间断点；
> 2. 只有有限个极值点。
>
> 则 $f(x)$ 的 Fourier 级数在每一点 $x$ 处收敛于：
> $$\frac{f(x^+) + f(x^-)}{2}$$
> 即函数在该点的左右极限的平均值。

在连续点处，$f(x^+) = f(x^-) = f(x)$，所以 Fourier 级数收敛于 $f(x)$。在间断点处，收敛于左右极限的平均值（跳跃的中点）。

Dirichlet 条件是一个充分条件，不是必要条件。实际应用中遇到的大多数函数都满足 Dirichlet 条件。

### 4.3 一致收敛的条件

> **定理**：如果 $f(x)$ 是周期为 $2\pi$ 的连续函数，且 $f'(x)$ 分段连续，则 $f(x)$ 的 Fourier 级数在整个实轴上一致收敛于 $f(x)$。

更一般地，如果 $f(x)$ 连续且其 Fourier 系数满足 $\sum (|a_n| + |b_n|) < \infty$，则 Fourier 级数一致收敛（Weierstrass M 判别法）。

### 4.4 L² 收敛与完备性

> **定理（Riesz-Fischer）**：对任意 $f \in L^2[-\pi, \pi]$，其 Fourier 级数在 L² 意义下收敛于 $f$：
> $$\lim_{N \to \infty} \int_{-\pi}^{\pi} \left|f(x) - S_N(x)\right|^2 dx = 0$$

这个定理说明三角函数系在 $L^2[-\pi, \pi]$ 中是**完备的**——它是 $L^2$ 空间的一组标准正交基。任何平方可积函数都可以用三角函数系的线性组合在 L² 意义下任意逼近。

L² 收敛是 Fourier 级数最"可靠"的收敛性——它对所有 $L^2$ 函数都成立，不需要任何额外条件。

📐 **几何理解**：L² 收敛的几何意义是——在无穷维的 $L^2$ 空间中，Fourier 级数的部分和 $S_N$ 是 $f$ 在前 $N$ 个三角函数方向张成的子空间上的正交投影。随着 $N$ 增大，投影子空间越来越大，投影越来越接近 $f$ 本身。L² 收敛就是说这些投影在距离（L² 范数）意义下收敛到 $f$。

---

## 第五章 Gibbs 现象

### 5.1 Gibbs 现象的发现

1899 年，美国物理学家 Josiah Willard Gibbs 在《自然》杂志上发表了一篇短文，指出了一个反直觉的现象：

> 当 Fourier 级数的部分和逼近一个有跳跃间断点的函数时，在间断点附近，部分和会出现"过冲"——超过函数值约 9% 的振荡，而且即使 $N \to \infty$，这个过冲的高度也不会消失，只是过冲的位置越来越靠近间断点。

这个现象被称为 **Gibbs 现象**。

### 5.2 Gibbs 现象的数学描述

以方波函数为例：

$$f(x) = \begin{cases} -1, & -\pi < x < 0 \\ 1, & 0 < x < \pi \end{cases}$$

其 Fourier 级数为：

$$f(x) \sim \frac{4}{\pi} \sum_{k=0}^{\infty} \frac{\sin(2k+1)x}{2k+1}$$

在 $x=0$ 处，$f$ 有一个从 $-1$ 到 $1$ 的跳跃（跳跃量为 2）。

Fourier 级数的部分和 $S_N(x)$ 在 $x = \pi/(2N+1)$ 处达到最大值：

$$\lim_{N \to \infty} S_N\left(\frac{\pi}{2N+1}\right) = \frac{2}{\pi} \int_0^{\pi} \frac{\sin t}{t} dt \approx 1.17898$$

所以过冲量约为 $1.17898 - 1 = 0.17898$，占跳跃量（2）的比例约为 $0.17898/2 \approx 8.95\%$，即约 9%。

### 5.3 Gibbs 现象的本质

Gibbs 现象的本质是：**Fourier 级数的部分和是 L² 意义下的最佳逼近，但不是一致意义下的最佳逼近。**

在 L² 意义下，部分和使 $\int |f - S_N|^2$ 最小。但在间断点附近，为了使积分误差最小，部分和会"牺牲"间断点附近的局部行为——通过一个有限高度的过换来换取更远处的更好逼近。

即使 $N \to \infty$，过冲的高度也不会消失，只是过冲的宽度越来越窄（与 $1/N$ 成正比），所以过冲的"面积"趋于 0，L² 误差仍然趋于 0。

📐 **几何理解**：Gibbs 现象的几何图像是——在间断点附近，Fourier 部分和的图像像一个"试图爬上台阶但总是冲过头"的曲线。随着项数增加，曲线越来越接近台阶，但在台阶边缘总是有一个约 9% 的"小山峰"。这个山峰不会消失，只是越来越窄。这就像用有限波长的波去逼近一个尖锐的跳跃——波无法完全"拐过"这个急转弯，总会有一点过冲。

### 5.4 Gibbs 现象的消除

Gibbs 现象可以通过**求和核**（如 Fejér 核、Cesàro 求和）来消除。Fejér 和是 Fourier 部分和的算术平均：

$$\sigma_N(x) = \frac{1}{N+1} \sum_{k=0}^{N} S_k(x)$$

Fejér 和在连续点处一致收敛于 $f(x)$，不会出现 Gibbs 过冲。但 Fejér 和的收敛速度比 Fourier 部分和慢。

---

## 第六章 Parseval 等式

### 6.1 Parseval 等式

> **Parseval 等式**：对任意 $f \in L^2[-\pi, \pi]$，有
> $$\frac{1}{\pi} \int_{-\pi}^{\pi} |f(x)|^2 dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty} (a_n^2 + b_n^2)$$

复指数形式：

$$\frac{1}{2\pi} \int_{-\pi}^{\pi} |f(x)|^2 dx = \sum_{n=-\infty}^{\infty} |c_n|^2$$

Parseval 等式说明：函数的"能量"（L² 范数的平方）等于其各频率分量的能量之和。

### 6.2 Parseval 等式的几何意义

📐 **几何理解**：Parseval 等式是**勾股定理在无穷维 Hilbert 空间中的推广**。

在三维空间中，一个向量 $\vec{v} = (v_1, v_2, v_3)$ 的长度平方等于各分量平方之和：$\|\vec{v}\|^2 = v_1^2 + v_2^2 + v_3^2$。这是因为三个坐标轴是正交的。

在 $L^2$ 空间中，函数 $f$ 可以分解为在各三角函数方向上的投影之和：$f = \sum c_n e^{inx}$。由于三角函数系是正交的，函数的"长度"平方等于各投影分量的长度平方之和：$\|f\|^2 = \sum |c_n|^2 \|e^{inx}\|^2$。这就是 Parseval 等式。

### 6.3 Parseval 等式的应用

Parseval 等式有许多重要应用：

1. **计算级数的和**：例如，对 $f(x) = x$ 在 $[-\pi, \pi]$ 上，其 Fourier 系数为 $b_n = 2(-1)^{n+1}/n$，由 Parseval 等式：
   $$\frac{1}{\pi} \int_{-\pi}^{\pi} x^2 dx = \sum_{n=1}^{\infty} \frac{4}{n^2}$$
   左边 $= 2\pi^2/3$，所以 $\sum_{n=1}^{\infty} 1/n^2 = \pi^2/6$（Basel 问题的又一证明）。

2. **能量守恒**：在信号处理中，Parseval 等式说明信号在时域的能量等于在频域的能量。

3. **最佳逼近的误差估计**：由 Bessel 不等式（Parseval 等式的部分和版本），可以估计 Fourier 部分和的 L² 逼近误差。

### 6.4 Bessel 不等式

> **Bessel 不等式**：对任意 $f \in L^2$ 和任意标准正交系 $\{\varphi_n\}$，有
> $$\sum_{n=1}^{\infty} |\langle f, \varphi_n \rangle|^2 \leq \|f\|^2$$

Bessel 不等式是 Parseval 等式的"单向版本"——它对任意正交系都成立，而 Parseval 等式只对完备正交系成立（等号成立）。

---

## 第七章 Fourier 级数的运算

### 7.1 逐项积分

> **定理**：如果 $f(x)$ 在 $[-\pi, \pi]$ 上可积，其 Fourier 级数为
> $$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$$
> 则对任意 $x$，有
> $$\int_0^x f(t) dt = \frac{a_0}{2}x + \sum_{n=1}^{\infty} \frac{a_n \sin nx + b_n(1 - \cos nx)}{n}$$

注意：逐项积分后的级数一定收敛，即使原 Fourier 级数不收敛！这是 Fourier 级数一个非常好的性质——积分总是使级数"变好"（系数多除以一个 $n$，收敛更快）。

### 7.2 逐项微分

逐项微分的条件更严格：

> **定理**：如果 $f(x)$ 连续、$f'(x)$ 分段连续，且 $f(-\pi) = f(\pi)$，则 $f'(x)$ 的 Fourier 级数可以由 $f(x)$ 的 Fourier 级数逐项微分得到：
> $$f'(x) \sim \sum_{n=1}^{\infty} n(-a_n \sin nx + b_n \cos nx)$$

注意：逐项微分后的级数系数多乘了一个 $n$，收敛更慢（甚至可能不收敛）。所以微分总是使级数"变坏"。

逐项积分和逐项微分的这种不对称性，反映了积分是"光滑化"操作（使函数更光滑、级数收敛更快），而微分是"粗糙化"操作（使函数更不光滑、级数收敛更慢）。

### 7.3 Fourier 级数的乘法（卷积）

两个周期函数的乘积的 Fourier 系数与各自 Fourier 系数的**卷积**有关：

如果 $f(x) \sim \sum c_n e^{inx}$，$g(x) \sim \sum d_n e^{inx}$，则

$$f(x)g(x) \sim \sum_{n=-\infty}^{\infty} \left(\sum_{k=-\infty}^{\infty} c_k d_{n-k}\right) e^{inx}$$

即乘积的 Fourier 系数是各自 Fourier 系数的卷积。

对应的，两个函数的卷积的 Fourier 系数是各自 Fourier 系数的乘积：

$$\widehat{f * g}(n) = 2\pi \, \hat{f}(n) \hat{g}(n)$$

这就是**卷积定理**，是信号处理和 Fourier 分析的核心定理之一。

---

## 第八章 其他正交级数

### 8.1 正交多项式概览

除了三角函数系，还有许多重要的正交函数系，其中最重要的是各类**正交多项式**。

正交多项式是在某个区间上关于某个权函数正交的多项式系。常见的正交多项式包括：

| 正交多项式 | 区间 | 权函数 | 应用领域 |
|-----------|------|--------|---------|
| Legendre 多项式 | $[-1, 1]$ | $1$ | 球谐函数、量子力学 |
| Chebyshev 多项式（第一类） | $[-1, 1]$ | $1/\sqrt{1-x^2}$ | 数值逼近、滤波器设计 |
| Chebyshev 多项式（第二类） | $[-1, 1]$ | $\sqrt{1-x^2}$ | 数值分析 |
| Laguerre 多项式 | $[0, +\infty)$ | $e^{-x}$ | 量子力学（氢原子） |
| Hermite 多项式 | $(-\infty, +\infty)$ | $e^{-x^2}$ | 量子力学（谐振子）、概率论 |
| Gegenbauer 多项式 | $[-1, 1]$ | $(1-x^2)^{\lambda-1/2}$ | 高维球谐函数 |
| Jacobi 多项式 | $[-1, 1]$ | $(1-x)^\alpha(1+x)^\beta$ | 一般正交多项式 |

### 8.2 Legendre 多项式

Legendre 多项式 $P_n(x)$ 是在 $[-1, 1]$ 上关于权函数 1 正交的多项式：

$$\int_{-1}^{1} P_m(x) P_n(x) dx = \frac{2}{2n+1} \delta_{mn}$$

前几个 Legendre 多项式：

$$P_0(x) = 1, \quad P_1(x) = x, \quad P_2(x) = \frac{3x^2-1}{2}, \quad P_3(x) = \frac{5x^3-3x}{2}$$

Legendre 多项式满足递推关系：

$$(n+1)P_{n+1}(x) = (2n+1)x P_n(x) - n P_{n-1}(x)$$

Legendre 多项式在球谐函数展开、量子力学的角动量理论、电磁学的多极展开中有重要应用。

### 8.3 Hermite 多项式

Hermite 多项式 $H_n(x)$ 是在 $(-\infty, +\infty)$ 上关于权函数 $e^{-x^2}$ 正交的多项式：

$$\int_{-\infty}^{\infty} H_m(x) H_n(x) e^{-x^2} dx = \sqrt{\pi} \, 2^n n! \, \delta_{mn}$$

Hermite 多项式是量子力学中谐振子波函数的空间部分，在概率论（正态分布的累积量）和信号处理（Gabor 变换）中也有重要应用。

### 8.4 Bessel 函数

Bessel 函数 $J_n(x)$ 不是多项式，但它是另一类重要的正交函数系。Bessel 函数满足 Bessel 微分方程：

$$x^2 y'' + x y' + (x^2 - n^2)y = 0$$

Bessel 函数在圆柱坐标系中分离变量时自然出现，在波动方程、热传导方程、电磁学中有广泛应用。

Bessel 函数的零点构成正交系：如果 $\alpha_{mn}$ 是 $J_m(x)$ 的第 $n$ 个正零点，则 $\{J_m(\alpha_{mn} r)\}$ 在 $[0, 1]$ 上关于权函数 $r$ 正交。

### 8.5 正交级数的统一视角

所有这些正交级数都有统一的理论框架：

1. **Sturm-Liouville 理论**：正交函数系通常是某个 Sturm-Liouville 微分算子的特征函数系。微分算子的自伴性保证了特征函数的正交性，特征值的离散性保证了正交系的完备性。

2. **最佳逼近**：正交级数的部分和是函数在有限维子空间上的正交投影（L² 最佳逼近）。

3. **Parseval 等式**：对完备正交系，函数的能量等于各分量能量之和。

4. **收敛性**：正交级数的收敛性取决于函数的光滑性和正交系的性质。

📐 **几何理解**：所有正交级数都是同一个几何思想的不同实现——在无穷维函数空间中选择一组正交的"坐标轴"，将函数投影到这些坐标轴上，得到函数的"坐标"（展开系数），然后用这些坐标的线性组合来表示函数。不同的正交系对应不同的"坐标系"，适用于不同的几何和物理场景（三角函数系适用于周期现象和圆上的分析，Legendre 多项式适用于球面上的分析，Bessel 函数适用于圆柱上的分析，Hermite 多项式适用于高斯加权的全空间分析）。

---

## 第九章 从 Fourier 级数到 Fourier 变换

### 9.1 周期趋于无穷的极限

Fourier 级数适用于周期函数。对于非周期函数，可以将其视为周期趋于无穷的周期函数的极限。

设 $f_L(x)$ 是周期为 $2L$ 的函数，在 $[-L, L]$ 上等于 $f(x)$。其 Fourier 级数为：

$$f_L(x) = \sum_{n=-\infty}^{\infty} c_n e^{i n\pi x/L}$$

其中 $c_n = \frac{1}{2L} \int_{-L}^{L} f(t) e^{-i n\pi t/L} dt$。

令 $\omega_n = n\pi/L$，则相邻频率的间隔为 $\Delta\omega = \pi/L$。当 $L \to \infty$ 时，$\Delta\omega \to 0$，离散的频率 $\omega_n$ 变为连续的频率 $\omega$，求和变为积分：

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \left(\int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt\right) e^{i\omega x} d\omega$$

这就是 **Fourier 变换** 和 **Fourier 逆变换**。

### 9.2 Fourier 变换的定义

> **定义**：对 $f \in L^1(\mathbb{R})$，其 Fourier 变换为
> $$\hat{f}(\omega) = \int_{-\infty}^{\infty} f(x) e^{-i\omega x} dx$$
> Fourier 逆变换为
> $$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \hat{f}(\omega) e^{i\omega x} d\omega$$

Fourier 变换将时域函数 $f(x)$ 转换为频域函数 $\hat{f}(\omega)$，是 Fourier 级数从离散频率到连续频率的推广。

### 9.3 Fourier 变换的基本性质

Fourier 变换有许多优美的性质：

1. **线性性**：$\widehat{af + bg} = a\hat{f} + b\hat{g}$。
2. **平移性质**：$\widehat{f(x-a)}(\omega) = e^{-ia\omega} \hat{f}(\omega)$。
3. **调制性质**：$\widehat{e^{iax} f(x)}(\omega) = \hat{f}(\omega - a)$。
4. **伸缩性质**：$\widehat{f(ax)}(\omega) = \frac{1}{|a|} \hat{f}(\omega/a)$。
5. **微分性质**：$\widehat{f'(x)}(\omega) = i\omega \hat{f}(\omega)$（在适当条件下）。
6. **卷积定理**：$\widehat{f * g} = \hat{f} \cdot \hat{g}$。
7. **Parseval 等式（Plancherel 定理）**：$\int |f(x)|^2 dx = \frac{1}{2\pi} \int |\hat{f}(\omega)|^2 d\omega$。

这些性质使 Fourier 变换成为解决微分方程、信号处理、图像处理等问题的强大工具。

📐 **几何理解**：Fourier 变换的几何意义是——在无穷维的 $L^2(\mathbb{R})$ 空间中，将函数从"时域坐标系"（以 $\delta(x-a)$ 为基）转换到"频域坐标系"（以 $e^{i\omega x}$ 为基）。这是一个无穷维空间中的"坐标旋转"——Fourier 变换是 $L^2(\mathbb{R})$ 上的酉算子（保持内积和范数），就像三维空间中的旋转矩阵保持向量长度一样。

---

## 第十章 反例库

### 10.1 Fourier 级数不收敛的函数

**反例**：du Bois-Reymond 于 1873 年构造了一个连续函数，其 Fourier 级数在某一点发散。
- 意义：连续函数的 Fourier 级数不一定逐点收敛。L² 收敛不蕴含逐点收敛。
- 后续：Carleson 于 1966 年证明了 $L^2$ 函数的 Fourier 级数几乎处处收敛（Carleson 定理），但在个别点仍可能发散。

### 10.2 Gibbs 现象

**反例**：方波函数的 Fourier 级数在间断点附近有约 9% 的过冲。
- 即使 $N \to \infty$，过冲高度也不消失，只是宽度趋于 0。
- 意义：Fourier 部分和是 L² 最佳逼近，不是一致最佳逼近；逐点收敛不蕴含一致收敛。

### 10.3 逐项微分后级数不收敛

**反例**：$f(x) = \sum_{n=1}^{\infty} \sin(n^2 x)/n^2$。
- 原级数一致收敛（Weierstrass M 判别法），$f(x)$ 连续。
- 逐项微分后得到 $\sum n \cos(n^2 x)$，通项不趋于 0，级数发散。
- 意义：逐项微分需要严格条件，不能随意对 Fourier 级数逐项微分。

### 10.4 正交系不完备的例子

**反例**：在 $L^2[-\pi, \pi]$ 中，去掉一个函数（如 $\sin x$）后的三角函数系。
- 仍然是正交系，但不再完备。
- Bessel 不等式严格成立（Parseval 等式不成立）。
- 意义：正交性不蕴含完备性，完备性是更强的条件。

### 10.5 Fourier 系数衰减速度与函数光滑性

**反例对比**：
- 不连续函数：Fourier 系数衰减速度为 $O(1/n)$。
- 连续但导数不连续：$O(1/n^2)$。
- $k$ 阶导数连续：$O(1/n^{k+1})$。
- 解析函数：指数衰减 $O(e^{-cn})$。
- 意义：Fourier 系数的衰减速度反映了函数的光滑性——越光滑的函数，高频分量越少，Fourier 系数衰减越快。

### 10.6 非周期函数不能直接用 Fourier 级数

**反例**：$f(x) = e^{-x^2}$（高斯函数，非周期）。
- 不能直接展开为 Fourier 级数（Fourier 级数只适用于周期函数）。
- 但可以用 Fourier 变换表示：$\hat{f}(\omega) = \sqrt{\pi} e^{-\omega^2/4}$。
- 意义：Fourier 级数是 Fourier 变换在周期情形下的特例，非周期函数需要用 Fourier 变换。

---

## 第十一章 历史演进

### 11.1 Fourier 分析的发展

**d'Alembert 与波动方程（1747）**：
d'Alembert 在研究弦振动方程时，提出了波动方程的通解，引发了关于"任意函数能否表示为三角级数"的争论。

**Euler 与 Bernoulli 的争论（1750s）**：
Daniel Bernoulli 提出弦振动的任意初始位移可以表示为正弦级数的和，但 Euler 和 d'Alembert 对此表示怀疑——他们认为三角级数只能表示周期函数，而"任意函数"不一定是周期的。这场争论持续了几十年。

**Fourier 的工作（1807-1822）**：
Joseph Fourier 在研究热传导方程时，系统地使用了三角级数来表示任意函数。他在 1807 年的论文中提出了 Fourier 级数的方法，但论文被 Lagrange 和 Laplace 评审后未发表（Lagrange 坚持认为三角级数不能表示任意函数）。Fourier 后来在 1822 年的《热的解析理论》中系统阐述了他的方法。

Fourier 虽然没有给出严格的收敛性证明，但他的工作开创了一个全新的领域，对数学和物理学产生了深远影响。

**Dirichlet 的严格化（1829）**：
Peter Gustav Lejeune Dirichlet 给出了 Fourier 级数收敛性的第一个严格证明——Dirichlet 定理，证明了满足 Dirichlet 条件的函数的 Fourier 级数收敛于左右极限的平均值。Dirichlet 还引入了函数的现代定义。

**Riemann 的贡献（1854）**：
Riemann 在他的就职论文中研究了 Fourier 级数，引入了 Riemann 积分的概念，证明了可积函数的 Fourier 系数趋于 0（Riemann-Lebesgue 引理的雏形）。

**Cantor 与集合论（1870s）**：
Georg Cantor 在研究 Fourier 级数的唯一性问题时，引入了集合论的概念——他研究了"在哪些点上级数可以不收敛到函数而唯一性仍然成立"的问题，这导致了点集拓扑和集合论的诞生。

**du Bois-Reymond 的反例（1873）**：
du Bois-Reymond 构造了一个连续函数，其 Fourier 级数在某一点发散，否定了"连续函数的 Fourier 级数处处收敛"的猜想。

**Gibbs 现象（1899）**：
Josiah Willard Gibbs 指出了 Fourier 级数在间断点附近的过冲现象。

**Lebesgue 积分与 L² 理论（1902-1907）**：
Lebesgue 积分的引入使 Fourier 分析建立在更坚实的基础上。Riesz-Fischer 定理（1907）证明了 $L^2$ 函数的 Fourier 级数在 L² 意义下收敛，建立了 $L^2$ 空间与平方可和序列空间的同构。

**Carleson 定理（1966）**：
Lennart Carleson 证明了 $L^2$ 函数的 Fourier 级数几乎处处收敛，解决了这个困扰数学家近一个世纪的问题（Lusin 猜想）。Carleson 的证明极其深刻，被誉为 20 世纪分析学最伟大的成就之一。

### 11.2 关键人物贡献表

| 人物 | 年代 | 贡献 |
|------|------|------|
| d'Alembert | 1717-1783 | 波动方程、三角级数表示的争论 |
| Fourier | 1768-1830 | Fourier 级数的系统应用、《热的解析理论》 |
| Dirichlet | 1805-1859 | Fourier 级数收敛性的第一个严格证明、Dirichlet 条件 |
| Riemann | 1826-1866 | Riemann 积分、Riemann-Lebesgue 引理 |
| Cantor | 1845-1918 | Fourier 级数唯一性、集合论的诞生 |
| du Bois-Reymond | 1831-1889 | 连续函数 Fourier 级数发散的反例 |
| Gibbs | 1839-1903 | Gibbs 现象 |
| Lebesgue | 1875-1941 | Lebesgue 积分、Fourier 分析的现代基础 |
| Riesz & Fischer | 1880-1956 / 1875-1954 | Riesz-Fischer 定理、L² 收敛理论 |
| Carleson | 1928- | Carleson 定理、L² 函数 Fourier 级数几乎处处收敛 |

---

## 第十二章 五类边

### 12.1 前驱→后继边

- 内积空间（D6-5）→ 正交函数系 → Fourier 级数
- 函数项级数一致收敛（D5-2）→ Fourier 级数的一致收敛
- 幂级数（D5-3）→ Fourier 级数（从代数基到三角基）
- Riemann 积分（D4-2）→ Fourier 系数的计算
- Lebesgue 积分（D4-6）→ L² 收敛理论、Riesz-Fischer 定理
- Fourier 级数 → Fourier 变换（离散频率→连续频率）
- Fourier 变换 → 调和分析、小波分析、时频分析

### 12.2 类比边

- 正交函数系 ⇔ 三维空间中的正交坐标系
- Fourier 系数 ⇔ 向量在坐标轴上的投影
- Fourier 级数 ⇔ 向量的坐标分解
- Parseval 等式 ⇔ 勾股定理（无穷维推广）
- L² 最佳逼近 ⇔ 三维空间中点到平面的最短距离
- Fourier 变换 ⇔ 无穷维空间中的坐标旋转（酉变换）
- 卷积定理 ⇔ 频域中的乘法对应时域中的卷积

### 12.3 推广边

- 有限维向量空间 → 无穷维函数空间（Hilbert 空间）
- 有限正交基 → 无穷正交系（完备性）
- 周期函数的 Fourier 级数 → 非周期函数的 Fourier 变换
- 一维 Fourier 分析 → 多维 Fourier 分析
- 三角函数系 → 一般正交函数系（Legendre/Bessel/Hermite 等）
- Fourier 分析 → 抽象调和分析（拓扑群上的 Fourier 分析）
- 经典 Fourier 分析 → 小波分析、时频分析

### 12.4 特例边

- 方波函数的 Fourier 级数是 Gibbs 现象的经典特例
- $f(x)=x$ 的 Fourier 级数是计算 Basel 问题的特例
- 高斯函数的 Fourier 变换仍是高斯函数（Fourier 变换的特征函数）
- $\delta$ 函数的 Fourier 变换是常数（广义函数意义下）
- 纯音 $e^{i\omega_0 x}$ 的 Fourier 变换是 $\delta(\omega-\omega_0)$

### 12.5 反例簇边

- du Bois-Reymond 函数：连续但 Fourier 级数在某点发散
- Gibbs 现象：逐点收敛但不一致收敛，过冲不消失
- 逐项微分后级数发散：微分使级数"变坏"
- 不完备正交系：Bessel 不等式严格成立
- Fourier 系数衰减慢：函数不光滑
- 非周期函数：不能直接用 Fourier 级数，需要 Fourier 变换

---

## 第十三章 学习路径与常见误区

### 13.1 学习路径建议

1. **先掌握内积空间和正交性**：这是 Fourier 级数的理论基础。理解正交投影和最佳逼近。
2. **验证三角函数系的正交性**：亲手计算几个积分，理解正交性的来源。
3. **掌握 Fourier 系数的计算**：熟练计算 $a_n$、$b_n$、$c_n$，理解奇偶函数的简化。
4. **理解三种收敛性**：逐点收敛、一致收敛、L² 收敛的区别和联系。
5. **掌握 Dirichlet 定理**：理解 Fourier 级数在连续点和间断点处的收敛行为。
6. **理解 Gibbs 现象**：这是 Fourier 级数最反直觉的现象，理解其本质是 L² 最佳逼近而非一致最佳逼近。
7. **掌握 Parseval 等式**：理解其几何意义（勾股定理的推广）和应用（计算级数的和）。
8. **了解其他正交级数**：Legendre、Bessel、Hermite 等，理解正交级数的统一框架。
9. **理解 Fourier 变换**：从 Fourier 级数到 Fourier 变换的过渡，掌握基本性质。

### 13.2 常见误区

1. **误区**：Fourier 级数一定收敛到函数本身。
   - **纠正**：Fourier 级数的收敛性需要条件。在连续点处（满足 Dirichlet 条件）收敛到函数值；在间断点处收敛到左右极限的平均值；在某些点（即使对连续函数）可能发散。

2. **误区**：Fourier 级数的部分和一致收敛到函数。
   - **纠正**：只有在函数足够光滑（连续且导数分段连续）时才一致收敛。对于有间断点的函数，即使逐点收敛，也不一致收敛（Gibbs 现象）。

3. **误区**：Gibbs 现象的过冲会随着项数增加而消失。
   - **纠正**：过冲的高度（约跳跃量的 9%）不会消失，只是过冲的宽度越来越窄。这是 Fourier 部分和作为 L² 最佳逼近的固有特性。

4. **误区**：可以随意对 Fourier 级数逐项微分。
   - **纠正**：逐项微分需要严格条件（函数连续、导数分段连续、端点值相等）。微分使 Fourier 系数多乘一个 $n$，收敛更慢，甚至可能不收敛。

5. **误区**：正交系一定是完备的。
   - **纠正**：正交性和完备性是不同的概念。正交系不一定完备（如去掉一个函数的三角函数系）。完备性需要单独证明。

6. **误区**：Fourier 级数只适用于周期函数，非周期函数不能用 Fourier 分析。
   - **纠正**：非周期函数可以用 Fourier 变换（周期趋于无穷的极限）。Fourier 变换是 Fourier 级数从离散频率到连续频率的推广。

7. **误区**：Fourier 系数的计算只需要记住公式。
   - **纠正**：Fourier 系数的本质是函数在三角函数方向上的正交投影。理解这个几何本质比记住公式更重要——它解释了为什么 Fourier 级数是最佳逼近，为什么 Parseval 等式成立。

---

## 第十四章 本章小结

D5-6 作为级数领域的第六个模块，系统研究了正交函数系与 Fourier 分析，这是级数理论中最具应用价值的部分，连接了分析学、物理学和工程学。

**核心内容回顾**：

1. **内积空间与正交性**：内积的定义、函数空间中的内积、正交函数系、正交投影与最佳逼近。
2. **三角函数系的正交性**：三角函数系在 $[-\pi, \pi]$ 上的正交性、复指数形式、正交性的几何本质。
3. **Fourier 级数的定义与系数**：三角形式和复指数形式、一般周期的 Fourier 级数、Fourier 系数的几何意义（频率轴上的坐标）。
4. **Fourier 级数的收敛性**：逐点收敛、一致收敛、L² 收敛三种类型；Dirichlet 定理；Riesz-Fischer 定理与完备性。
5. **Gibbs 现象**：间断点附近约 9% 的过冲、过冲高度不消失的本质、Fejér 求和消除过冲。
6. **Parseval 等式**：能量守恒、勾股定理在无穷维空间的推广、Bessel 不等式、应用（计算级数的和）。
7. **Fourier 级数的运算**：逐项积分（总是收敛）、逐项微分（需要条件）、卷积定理。
8. **其他正交级数**：Legendre、Chebyshev、Laguerre、Hermite、Bessel 等正交函数系、Sturm-Liouville 理论的统一框架。
9. **从 Fourier 级数到 Fourier 变换**：周期趋于无穷的极限、Fourier 变换的定义和基本性质、Fourier 变换的几何意义（坐标旋转）。
10. **几何视角**：函数空间中的投影与最佳逼近、圆上的调和分析、Fourier 系数是频率轴上的坐标、Parseval 等式是勾股定理的推广。

**下一个模块 D5-7** 将是级数领域的收束模块——级数的蜕变图谱，系统梳理从初等数列到数学分析、复变函数、实变函数中级数概念的蜕变与推演，建立级数理论的全局视图。

---

**D5 级数领域进度**：6/7 完成（D5-1 从数列到级数 ✅、D5-2 函数项级数与一致收敛 ✅、D5-3 幂级数与 Taylor 级数 ✅、D5-4 无穷乘积 ✅、D5-5 复级数与 Laurent 展开 ✅、D5-6 正交级数与 Fourier 分析 ✅、D5-7 级数的蜕变图谱 ⏳）。
