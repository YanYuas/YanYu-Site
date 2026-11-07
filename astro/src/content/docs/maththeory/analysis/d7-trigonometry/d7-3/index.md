---
title: "D7-3 三角恒等式的几何证明——旋转与投影"
description: "领域 ：D7 三角学"
tags:
  - "数学理论"
  - "分析学"
  - "D7 三角学"
---

> 领域 ：D7 三角学

---

## 第一章 三角恒等式的两种证明方式——代数 vs 几何

### 1.1 传统的代数证明

传统教材中，三角恒等式的证明通常采用代数方法：

例如，证明和角公式 $\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$，常见的代数方法是：
1. 先证明 $\cos(\alpha-\beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$（用单位圆上两点间距离公式）
2. 然后用诱导公式 $\sin x = \cos(\pi/2 - x)$ 推导正弦的和角公式
3. 再推导其他公式

这种代数证明虽然逻辑严密，但有一个根本问题：**它没有揭示公式的几何本质**。学生记住了公式，却不理解为什么会有这样的公式——它看起来像是"代数运算的巧合"。

### 1.2 几何证明的方法论

几何证明的核心思想是：**每一个三角恒等式都是一个几何事实**。

具体来说：
- 角度 = 旋转量
- 正弦/余弦 = 单位圆上点的坐标（投影）
- 角度的加法 = 旋转的合成
- 因此，和角公式 = "两次旋转合成后，坐标如何分解为两次旋转各自坐标的组合"

📐 **几何证明方法论**：
1. **画单位圆**：所有三角函数都归结为单位圆上点的坐标
2. **标记旋转**：在单位圆上标记出角 $\alpha$、$\beta$、$\alpha+\beta$ 对应的点
3. **分析坐标**：写出每个点的坐标（$\cos, \sin$）
4. **几何关系**：利用旋转的几何性质（旋转保持距离、旋转矩阵等）建立坐标之间的关系
5. **提取公式**：从坐标关系中提取出三角恒等式

这种方法的优点是：**每一个公式都有清晰的几何图像**，不需要死记硬背。

### 1.3 旋转矩阵——几何证明的核心工具

旋转矩阵是几何证明的核心工具。

> **定义**：平面上绕原点逆时针旋转角 $\theta$ 的变换，可以用矩阵表示：
> $$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
> 即点 $(x, y)$ 旋转后变为：
> $$(x\cos\theta - y\sin\theta, \; x\sin\theta + y\cos\theta)$$

旋转矩阵的性质：
1. **旋转的合成 = 矩阵的乘法**：$R_{\alpha+\beta} = R_\alpha R_\beta$
2. **旋转保持内积**：旋转是正交变换，保持距离和角度
3. **逆旋转 = 转置矩阵**：$R_{-\theta} = R_\theta^T$

几乎所有三角恒等式都可以通过旋转矩阵的乘法来几何地证明。

---

## 第二章 和角公式的几何证明

### 2.1 和角公式

和角公式是三角恒等式中最基本、最重要的公式：

$$\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$$
$$\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$$

### 2.2 几何证明一：旋转矩阵乘法

最简洁的几何证明是利用旋转矩阵的乘法：

先旋转 $\beta$，再旋转 $\alpha$，总效果是旋转 $\alpha+\beta$：
$$R_{\alpha+\beta} = R_\alpha R_\beta$$

计算右边：
$$R_\alpha R_\beta = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix} \begin{pmatrix} \cos\beta & -\sin\beta \\ \sin\beta & \cos\beta \end{pmatrix}$$

$$= \begin{pmatrix} \cos\alpha\cos\beta - \sin\alpha\sin\beta & -\cos\alpha\sin\beta - \sin\alpha\cos\beta \\ \sin\alpha\cos\beta + \cos\alpha\sin\beta & -\sin\alpha\sin\beta + \cos\alpha\cos\beta \end{pmatrix}$$

左边：
$$R_{\alpha+\beta} = \begin{pmatrix} \cos(\alpha+\beta) & -\sin(\alpha+\beta) \\ \sin(\alpha+\beta) & \cos(\alpha+\beta) \end{pmatrix}$$

比较矩阵元素，立即得到：
$$\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$$
$$\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$$

📐 **几何理解**：这个证明的几何本质是"旋转的合成"。先转 $\beta$ 再转 $\alpha$，和直接转 $\alpha+\beta$ 是同一个旋转。旋转矩阵的元素就是"旋转后基向量的坐标"，矩阵乘法就是"两次旋转后基向量坐标的复合"。比较两个矩阵的元素，就得到了和角公式。

### 2.3 几何证明二：单位圆上的投影分解

另一种更直观的几何证明是直接在单位圆上分析投影。

考虑单位圆上的点 $P(\cos(\alpha+\beta), \sin(\alpha+\beta))$。

我们可以通过两次旋转到达 $P$：
1. 从 $(1, 0)$ 旋转 $\beta$，到达点 $Q(\cos\beta, \sin\beta)$
2. 再从 $Q$ 旋转 $\alpha$，到达 $P$

第二步旋转中，点 $Q$ 的坐标 $(\cos\beta, \sin\beta)$ 可以看作是"在旋转 $\alpha$ 后的坐标系中的坐标"。

具体来说，旋转 $\alpha$ 后的新坐标系的基向量是：
- 新 x 轴方向：$(\cos\alpha, \sin\alpha)$
- 新 y 轴方向：$(-\sin\alpha, \cos\alpha)$

点 $Q$ 在新坐标系中的坐标是 $(\cos\beta, \sin\beta)$（因为 $Q$ 是从新 x 轴方向旋转 $\beta$ 得到的）。

所以 $P$ 在原坐标系中的坐标是：
$$P = \cos\beta \cdot (\cos\alpha, \sin\alpha) + \sin\beta \cdot (-\sin\alpha, \cos\alpha)$$

即：
$$x = \cos\alpha\cos\beta - \sin\alpha\sin\beta = \cos(\alpha+\beta)$$
$$y = \sin\alpha\cos\beta + \cos\alpha\sin\beta = \sin(\alpha+\beta)$$

📐 **几何理解**：这个证明的核心是"坐标的投影分解"。点 $P$ 的坐标可以分解为"在旋转 $\alpha$ 后的两个坐标轴上的投影"——在新 x 轴上的投影是 $\cos\beta$，在新 y 轴上的投影是 $\sin\beta$。然后把这两个投影"翻译"回原坐标系，就得到了和角公式。这是"投影的投影"——非常几何化的证明。

### 2.4 几何证明三：向量的旋转与内积

还可以用向量内积来证明余弦的和角公式。

考虑单位向量 $\mathbf{u} = (\cos\alpha, \sin\alpha)$ 和 $\mathbf{v} = (\cos\beta, \sin\beta)$。

它们的夹角是 $|\alpha - \beta|$，所以内积为：
$$\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos(\alpha-\beta) = \cos(\alpha-\beta)$$

另一方面，按坐标计算内积：
$$\mathbf{u} \cdot \mathbf{v} = \cos\alpha\cos\beta + \sin\alpha\sin\beta$$

所以：
$$\cos(\alpha-\beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$$

然后用 $-\beta$ 替换 $\beta$，得到：
$$\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$$

📐 **几何理解**：内积的几何意义是"一个向量在另一个向量方向上的投影长度乘以另一个向量的长度"。对于单位向量，内积就是"投影长度"。两个单位向量的内积等于它们夹角的余弦——这是余弦差角公式的几何本质。

---

## 第三章 差角公式的几何证明

### 3.1 差角公式

$$\sin(\alpha-\beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta$$
$$\cos(\alpha-\beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$$

### 3.2 几何证明

差角公式可以看作是和角公式的特例——用 $-\beta$ 替换 $\beta$：

$$\sin(\alpha-\beta) = \sin(\alpha+(-\beta)) = \sin\alpha\cos(-\beta) + \cos\alpha\sin(-\beta)$$

利用 $\cos(-\beta) = \cos\beta$（余弦是偶函数）和 $\sin(-\beta) = -\sin\beta$（正弦是奇函数），得到：
$$\sin(\alpha-\beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta$$

同理：
$$\cos(\alpha-\beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$$

📐 **几何理解**：差角 = "先旋转 $\alpha$，再反向旋转 $\beta$"。反向旋转就是顺时针旋转，对应的坐标变换是"y 坐标变号"（因为顺时针旋转是逆时针旋转的镜像）。所以差角公式就是和角公式加上"镜像变号"。

也可以用旋转矩阵直接证明：$R_{\alpha-\beta} = R_\alpha R_{-\beta}$，其中 $R_{-\beta}$ 是顺时针旋转 $\beta$ 的矩阵。

---

## 第四章 倍角公式的几何证明

### 4.1 倍角公式

$$\sin 2\alpha = 2\sin\alpha\cos\alpha$$
$$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha$$
$$\tan 2\alpha = \frac{2\tan\alpha}{1 - \tan^2\alpha}$$

### 4.2 几何证明：和角公式的特例

倍角公式是和角公式在 $\beta = \alpha$ 时的特例：

$$\sin 2\alpha = \sin(\alpha+\alpha) = \sin\alpha\cos\alpha + \cos\alpha\sin\alpha = 2\sin\alpha\cos\alpha$$

$$\cos 2\alpha = \cos(\alpha+\alpha) = \cos\alpha\cos\alpha - \sin\alpha\sin\alpha = \cos^2\alpha - \sin^2\alpha$$

利用 $\cos^2\alpha + \sin^2\alpha = 1$，可以得到另外两种形式：
$$\cos 2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha$$

### 4.3 几何理解：旋转 2α 后的投影

📐 **几何理解**：倍角公式的几何本质是"旋转 $2\alpha$ 后的坐标与旋转 $\alpha$ 后的坐标的关系"。

在单位圆上：
- 旋转 $\alpha$ 后的点是 $(\cos\alpha, \sin\alpha)$
- 旋转 $2\alpha$ 后的点是 $(\cos 2\alpha, \sin 2\alpha)$

从 $(\cos\alpha, \sin\alpha)$ 再旋转 $\alpha$，就到达 $(\cos 2\alpha, \sin 2\alpha)$。这个"再旋转 $\alpha$"的过程，就是和角公式在 $\beta=\alpha$ 时的情形。

特别地，$\sin 2\alpha = 2\sin\alpha\cos\alpha$ 有一个优美的几何解释：
- $\sin\alpha$ 是点的纵坐标
- $\cos\alpha$ 是点的横坐标
- $2\sin\alpha\cos\alpha$ 是"以 $\sin\alpha$ 和 $\cos\alpha$ 为边的矩形面积的 2 倍"
- 几何上，这对应于"旋转 $2\alpha$ 后的纵坐标"

---

## 第五章 半角公式的几何证明

### 5.1 半角公式

$$\sin\frac{\alpha}{2} = \pm\sqrt{\frac{1-\cos\alpha}{2}}$$
$$\cos\frac{\alpha}{2} = \pm\sqrt{\frac{1+\cos\alpha}{2}}$$
$$\tan\frac{\alpha}{2} = \pm\sqrt{\frac{1-\cos\alpha}{1+\cos\alpha}} = \frac{\sin\alpha}{1+\cos\alpha} = \frac{1-\cos\alpha}{\sin\alpha}$$

### 5.2 几何证明：从倍角公式反推

半角公式可以从倍角公式反推得到。

由 $\cos 2\theta = 2\cos^2\theta - 1$，令 $\theta = \alpha/2$，得：
$$\cos\alpha = 2\cos^2\frac{\alpha}{2} - 1$$
$$\cos^2\frac{\alpha}{2} = \frac{1+\cos\alpha}{2}$$
$$\cos\frac{\alpha}{2} = \pm\sqrt{\frac{1+\cos\alpha}{2}}$$

同理，由 $\cos 2\theta = 1 - 2\sin^2\theta$，得：
$$\sin\frac{\alpha}{2} = \pm\sqrt{\frac{1-\cos\alpha}{2}}$$

### 5.3 几何理解：半角投影

📐 **几何理解**：半角公式的几何本质是"已知旋转 $\alpha$ 后的坐标，求旋转 $\alpha/2$ 后的坐标"。

在单位圆上，已知点 $P(\cos\alpha, \sin\alpha)$，求角 $\alpha/2$ 对应的点 $Q(\cos(\alpha/2), \sin(\alpha/2))$。

几何上，$Q$ 是弧 $OP$ 的中点（$O$ 是 $(1,0)$）。弧中点的坐标可以通过几何方法求得：
- 弧中点在角 $\alpha/2$ 的射线上
- 弧中点到 $O$ 和 $P$ 的距离相等

半角公式中的正负号由 $\alpha/2$ 所在的象限决定——这又是"坐标符号由象限决定"的几何事实。

特别地，$\tan(\alpha/2) = \frac{\sin\alpha}{1+\cos\alpha}$ 有一个优美的几何解释：
- 在单位圆上，从点 $(-1, 0)$ 到点 $(\cos\alpha, \sin\alpha)$ 的直线的斜率就是 $\tan(\alpha/2)$
- 这是因为"圆周角等于圆心角的一半"——从 $(-1,0)$ 看 $(\cos\alpha, \sin\alpha)$ 的视角是 $\alpha/2$

---

## 第六章 和差化积的几何证明

### 6.1 和差化积公式

$$\sin\alpha + \sin\beta = 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$$
$$\sin\alpha - \sin\beta = 2\cos\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}$$
$$\cos\alpha + \cos\beta = 2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$$
$$\cos\alpha - \cos\beta = -2\sin\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}$$

### 6.2 几何证明：旋转的合成与分解

和差化积公式的几何本质是"两个旋转的合成与分解"。

考虑单位圆上的两个点：
- $P(\cos\alpha, \sin\alpha)$（旋转 $\alpha$）
- $Q(\cos\beta, \sin\beta)$（旋转 $\beta$）

它们的中点 $M$ 的坐标是：
$$M = \left(\frac{\cos\alpha+\cos\beta}{2}, \frac{\sin\alpha+\sin\beta}{2}\right)$$

另一方面，$M$ 也可以用"平均旋转"和"半差旋转"来表示：
- 平均角度：$\gamma = \frac{\alpha+\beta}{2}$
- 半差角度：$\delta = \frac{\alpha-\beta}{2}$
- 则 $\alpha = \gamma+\delta$，$\beta = \gamma-\delta$

点 $P$ 和 $Q$ 关于角 $\gamma$ 的射线对称。它们的中点 $M$ 在角 $\gamma$ 的射线上，且 $|OM| = \cos\delta$（因为 $M$ 是等腰三角形 $OPQ$ 的底边中点，$|OP|=|OQ|=1$，顶角为 $2\delta$）。

所以 $M$ 的坐标是：
$$M = (\cos\delta \cdot \cos\gamma, \; \cos\delta \cdot \sin\gamma) = \left(\cos\frac{\alpha-\beta}{2}\cos\frac{\alpha+\beta}{2}, \; \cos\frac{\alpha-\beta}{2}\sin\frac{\alpha+\beta}{2}\right)$$

与中点坐标比较，得到：
$$\frac{\cos\alpha+\cos\beta}{2} = \cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$$
$$\frac{\sin\alpha+\sin\beta}{2} = \sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$$

即：
$$\cos\alpha + \cos\beta = 2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$$
$$\sin\alpha + \sin\beta = 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$$

📐 **几何理解**：和差化积的几何本质是"两个单位向量的和向量"。两个长度为 1 的向量（对应单位圆上的两个点）的和向量，方向在它们的角平分线上，长度是 $2\cos(\delta)$（其中 $\delta$ 是半差角）。这就是"平行四边形法则"——两个单位向量构成的平行四边形的对角线就是和向量。

对于差向量 $\sin\alpha - \sin\beta$，类似地，它对应于"两个单位向量的差向量"，方向垂直于角平分线，长度是 $2\sin(\delta)$。

---

## 第七章 积化和差的几何证明

### 7.1 积化和差公式

$$\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha-\beta) - \cos(\alpha+\beta)]$$
$$\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha-\beta) + \cos(\alpha+\beta)]$$
$$\sin\alpha\cos\beta = \frac{1}{2}[\sin(\alpha+\beta) + \sin(\alpha-\beta)]$$

### 7.2 几何证明：投影乘积的旋转分解

积化和差公式的几何本质是"两个投影的乘积可以分解为两个旋转的投影之和/差"。

以 $\sin\alpha\cos\beta$ 为例：

$\sin\alpha$ 是点 $(\cos\alpha, \sin\alpha)$ 的纵坐标（y 投影）。
$\cos\beta$ 是点 $(\cos\beta, \sin\beta)$ 的横坐标（x 投影）。

它们的乘积可以通过和角公式来分解：

从和角公式：
$$\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$$
$$\sin(\alpha-\beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta$$

两式相加：
$$\sin(\alpha+\beta) + \sin(\alpha-\beta) = 2\sin\alpha\cos\beta$$

所以：
$$\sin\alpha\cos\beta = \frac{1}{2}[\sin(\alpha+\beta) + \sin(\alpha-\beta)]$$

📐 **几何理解**：积化和差的几何本质是"投影的乘积 = 两个旋转的投影的平均"。

具体来说，$\sin\alpha\cos\beta$ 是"一个点的 y 投影乘以另一个点的 x 投影"。这个乘积可以分解为"旋转 $\alpha+\beta$ 后的 y 投影"和"旋转 $\alpha-\beta$ 后的 y 投影"的平均值。

几何上，这对应于"矩形面积的分解"——以 $\sin\alpha$ 和 $\cos\beta$ 为边的矩形面积，可以分解为两个"旋转后的投影"的平均。

---

## 第八章 万能公式的几何理解

### 8.1 万能公式

令 $t = \tan\frac{\alpha}{2}$，则：
$$\sin\alpha = \frac{2t}{1+t^2}, \quad \cos\alpha = \frac{1-t^2}{1+t^2}, \quad \tan\alpha = \frac{2t}{1-t^2}$$

### 8.2 几何理解：半角正切与全角三角函数

万能公式的几何本质是"半角的正切可以表示全角的所有三角函数"。

从 D7-2 的射影几何视角来看，$t = \tan(\alpha/2)$ 是"从点 $(-1, 0)$ 到点 $(\cos\alpha, \sin\alpha)$ 的直线的斜率"（圆周角定理）。

这条直线的参数方程是：
$$(x, y) = (-1, 0) + s(1, t) = (-1+s, st)$$

与单位圆 $x^2 + y^2 = 1$ 的交点：
$$(-1+s)^2 + (st)^2 = 1$$
$$1 - 2s + s^2 + s^2t^2 = 1$$
$$s(-2 + s(1+t^2)) = 0$$

解得 $s=0$（对应点 $(-1,0)$）或 $s = \frac{2}{1+t^2}$。

所以另一个交点的坐标是：
$$x = -1 + \frac{2}{1+t^2} = \frac{1-t^2}{1+t^2} = \cos\alpha$$
$$y = \frac{2t}{1+t^2} = \sin\alpha$$

这就是万能公式的几何推导！

📐 **几何理解**：万能公式的几何本质是"单位圆的有理参数化"。通过从点 $(-1, 0)$ 作斜率为 $t$ 的直线，与单位圆的另一个交点的坐标可以用 $t$ 的有理函数表示。这就是"万能公式"——它将三角函数（超越函数）转化为有理函数，使得很多三角积分可以用代数方法计算。

从射影几何的角度看，这是"从圆上一点出发的中心投影将圆参数化"的经典例子——圆是射影直线的模型，从一点出发的投影建立了圆（去掉该点）与直线之间的一一对应。

---

## 第九章 Chebyshev 多项式的几何本质

### 9.1 Chebyshev 多项式的定义

> **定义**：第一类 Chebyshev 多项式 $T_n(x)$ 定义为：
> $$T_n(\cos\theta) = \cos(n\theta)$$
> 即 $T_n(x) = \cos(n\arccos x)$。

前几个 Chebyshev 多项式：
- $T_0(x) = 1$
- $T_1(x) = x$
- $T_2(x) = 2x^2 - 1$
- $T_3(x) = 4x^3 - 3x$
- $T_4(x) = 8x^4 - 8x^2 + 1$

### 9.2 几何本质：倍角公式的多项式化

Chebyshev 多项式的几何本质是**倍角公式的多项式化**。

$\cos(n\theta)$ 可以用 $\cos\theta$ 的多项式表示——这是因为：
1. $\cos 2\theta = 2\cos^2\theta - 1$（倍角公式）
2. $\cos 3\theta = \cos(2\theta+\theta) = \cos 2\theta\cos\theta - \sin 2\theta\sin\theta = (2\cos^2\theta-1)\cos\theta - 2\sin\theta\cos\theta\sin\theta = 2\cos^3\theta - \cos\theta - 2\cos\theta(1-\cos^2\theta) = 4\cos^3\theta - 3\cos\theta$
3. 一般地，$\cos(n\theta)$ 是 $\cos\theta$ 的 $n$ 次多项式

递推关系：
$$T_{n+1}(x) = 2xT_n(x) - T_{n-1}(x)$$

这个递推关系来自和角公式：
$$\cos((n+1)\theta) + \cos((n-1)\theta) = 2\cos\theta\cos(n\theta)$$

（这是和差化积公式的特例）

### 9.3 几何理解：旋转的迭代

📐 **几何理解**：Chebyshev 多项式的几何本质是"旋转的迭代"。

在单位圆上：
- 旋转 $\theta$ 后的点是 $(\cos\theta, \sin\theta)$
- 旋转 $n\theta$ 后的点是 $(\cos(n\theta), \sin(n\theta)) = (T_n(\cos\theta), \ldots)$

$T_n(\cos\theta) = \cos(n\theta)$ 意味着"旋转 $n$ 次 $\theta$ 后的横坐标"可以用"旋转一次 $\theta$ 后的横坐标"的多项式表示。

这是一个非常深刻的几何事实——**旋转的迭代在横坐标上表现为多项式映射**。这个性质使得 Chebyshev 多项式在逼近论、数值分析、信号处理等领域有广泛应用。

特别地，Chebyshev 多项式的零点 $\cos\left(\frac{2k-1}{2n}\pi\right)$ 和极值点 $\cos\left(\frac{k\pi}{n}\right)$ 在单位圆上均匀分布——这又是"旋转均匀性"的几何体现。

---

## 第十章 射影几何视角下的三角恒等式

### 10.1 交比与三角恒等式

在 D7-2 中，我们建立了三角函数与射影几何的联系。现在从射影几何的角度重新审视三角恒等式。

**交比公式**：
对于角度 $\alpha, \beta, \gamma, \delta$，有：
$$(\tan\alpha, \tan\beta; \tan\gamma, \tan\delta) = \frac{\sin(\alpha-\gamma)\sin(\beta-\delta)}{\sin(\beta-\gamma)\sin(\alpha-\delta)}$$

这个公式本身就是一个三角恒等式，它的射影几何意义是：**正切函数将角度的差转化为交比**。

许多三角恒等式可以通过交比的性质来证明：
- 交比在射影变换下不变
- 交比的特殊值（0, 1, ∞, -1）对应特殊的几何关系

### 10.2 Möbius 变换与三角恒等式

正切加法公式 $\tan(\alpha+\beta) = \frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$ 对应于 Möbius 变换：
$$t \mapsto \frac{t + \tan\beta}{1 - t\tan\beta}$$

Möbius 变换的复合对应于角度的加法。许多三角恒等式可以通过 Möbius 变换的群性质来证明。

例如，$\tan(\alpha+\beta+\gamma)$ 的公式可以通过两次 Möbius 变换的复合来得到，而不需要记住复杂的公式。

### 10.3 射影直线上的三角函数

从射影几何的角度看，三角函数是"射影直线（圆）上的坐标函数"：
- $\cos\theta, \sin\theta$ 是圆在平面直角坐标系中的坐标
- $\tan\theta$ 是圆在切线坐标系中的坐标（中心投影）
- 不同的坐标系之间的转换关系就是三角恒等式

这个视角揭示了三角恒等式的本质：**它们是同一个几何对象（圆/射影直线）在不同坐标系下的坐标转换公式**。

---

## 第十一章 反直觉结论与常见误区

### 11.1 反直觉结论

**1. 所有三角恒等式都是几何事实，不是代数巧合**：
和角公式、倍角公式、和差化积、积化和差——每一个都有清晰的几何图像（旋转的合成、投影的分解）。

**2. 倍角公式是和角公式的特例**：
$\sin 2\alpha = 2\sin\alpha\cos\alpha$ 不需要单独记忆——它就是 $\sin(\alpha+\alpha)$。

**3. 和差化积是"两个单位向量的和/差向量"**：
$\sin\alpha + \sin\beta = 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}$ 的几何本质是平行四边形法则。

**4. 万能公式是"单位圆的有理参数化"**：
$\sin\alpha = \frac{2t}{1+t^2}, \cos\alpha = \frac{1-t^2}{1+t^2}$ 来自从 $(-1,0)$ 出发的中心投影，是射影几何的经典结果。

**5. Chebyshev 多项式是"旋转迭代的多项式化"**：
$T_n(\cos\theta) = \cos(n\theta)$ 意味着旋转的迭代在横坐标上表现为多项式映射。

**6. 三角恒等式是"射影直线上不同坐标系的转换公式"**：
从射影几何的高度看，所有三角恒等式都是同一个几何对象在不同坐标系下的坐标转换。

### 11.2 常见误区

**误区 1**：三角恒等式需要死记硬背。
- **纠正**：所有恒等式都可以通过旋转和投影的几何图像推导出来。记住"和角公式"和"勾股恒等式"，其他都可以推导。

**误区 2**：和角公式是代数运算的结果。
- **纠正**：和角公式是"两次旋转合成后坐标分解"的几何事实。

**误区 3**：万能公式是"代数技巧"。
- **纠正**：万能公式是"单位圆的有理参数化"，有深刻的射影几何意义。

**误区 4**：Chebyshev 多项式是"人为定义的特殊函数"。
- **纠正**：Chebyshev 多项式是倍角公式的自然推广，几何本质是旋转的迭代。

**误区 5**：积化和差与和差化积是互逆的代数运算。
- **纠正**：它们有不同的几何意义——和差化积是"两个向量的和/差"，积化和差是"投影乘积的旋转分解"。

---

## 第十二章 历史演进

### 12.1 三角恒等式的发展

**古代**：
- 古希腊 Hipparchus（约公元前150年）：编制了弦表，相当于已知的最早的三角函数表
- Ptolemy（约公元150年）：《天文学大成》中给出了和角公式的等价形式（用弦长表示），用于计算行星位置

**中世纪**：
- 印度数学家：发展了正弦和余弦的概念，给出了和角公式
- 阿拉伯数学家：Al-Battani（约公元900年）发现了余弦的和角公式；Abu al-Wafa（约公元980年）给出了正弦的和角公式

**近代**：
- Euler（1748）：《无穷分析引论》中系统整理了所有三角恒等式，引入了现代记号，用 Euler 公式统一了指数函数和三角函数
- Euler 公式 $e^{i\theta} = \cos\theta + i\sin\theta$ 使得所有三角恒等式都可以通过指数运算来证明——这是"代数证明"的巅峰，但也掩盖了几何本质

**射影几何视角**：
- Desargues（1639）：射影几何奠基人
- 19 世纪：三角函数与射影几何的联系被逐渐认识，特别是通过 Möbius 变换和非欧几何的研究
- Chebyshev（1854）：系统研究了 Chebyshev 多项式，发现了其在逼近论中的重要性

### 12.2 关键人物贡献表

| 人物 | 年代 | 贡献 |
|------|------|------|
| Hipparchus | 约公元前190-120年 | 弦表，三角学奠基人 |
| Ptolemy | 约公元100-170年 | 和角公式的等价形式 |
| 印度数学家 | 公元5-12世纪 | 正弦、余弦，和角公式 |
| Al-Battani | 约公元858-929年 | 余弦和角公式 |
| Abu al-Wafa | 公元940-998年 | 正弦和角公式 |
| Euler | 1707-1783 | 系统整理三角恒等式，Euler 公式 |
| Chebyshev | 1821-1894 | Chebyshev 多项式，逼近论 |

---

## 第十三章 五类边

### 13.1 前驱→后继边

- 角与弧度（D7-1）→ 单位圆 → 三角函数定义（D7-2）→ 三角恒等式（D7-3）
- 和角公式 → 倍角公式 → 半角公式 → Chebyshev 多项式
- 和差化积/积化和差 → Fourier 级数（D5-6）
- 万能公式 → 有理函数积分（D4-3）
- 三角恒等式 → Euler 公式（D7-4）→ 复三角函数
- Chebyshev 多项式 → 正交多项式 → 逼近论

### 13.2 类比边

- 和角公式 ⇔ 旋转矩阵的乘法
- 和差化积 ⇔ 平行四边形法则（向量加法）
- 积化和差 ⇔ 投影乘积的旋转分解
- 万能公式 ⇔ 单位圆的有理参数化（射影几何）
- Chebyshev 多项式 ⇔ 旋转的迭代
- 三角恒等式 ⇔ 射影直线上不同坐标系的转换公式

### 13.3 推广边

- 平面三角恒等式 → 球面三角恒等式（D7-6）
- 实三角恒等式 → 复三角恒等式（D7-4）
- 三角函数 → 双曲函数（D7-7，恒等式平行但符号不同）
- 二维旋转 → 三维旋转 → 高维旋转（四元数、Clifford 代数）
- Chebyshev 多项式 → 正交多项式（Legendre、Hermite、Laguerre）

### 13.4 特例边

- $\alpha = \beta$ → 倍角公式
- $\beta = \alpha/2$ → 半角公式
- $\alpha + \beta = \pi/2$ → 余角公式（诱导公式）
- $\beta = 0$ → 平凡恒等式
- $n=2,3,4$ → 低阶 Chebyshev 多项式

### 13.5 反例簇边

- 三角恒等式不是代数巧合，而是几何事实
- 万能公式不是代数技巧，而是射影几何的经典结果
- Chebyshev 多项式不是人为定义，而是倍角公式的自然推广
- $\sin(\alpha+\beta) \neq \sin\alpha + \sin\beta$（非线性！这是最常见的错误）
- 和差化积与积化和差不是简单的互逆运算，有不同的几何意义

---

## 第十四章 学习路径与常见误区

### 14.1 学习路径建议

1. **掌握和角公式**：这是所有三角恒等式的基础。用旋转矩阵乘法或单位圆投影分解来几何地理解它。
2. **推导其他公式**：从和角公式出发，推导差角、倍角、半角公式。不要死记硬背。
3. **理解和差化积**：用"两个单位向量的和/差向量"的几何图像来理解。
4. **理解积化和差**：用"投影乘积的旋转分解"来理解。
5. **掌握万能公式**：理解它是"单位圆的有理参数化"，来自从 $(-1,0)$ 出发的中心投影。
6. **学习 Chebyshev 多项式**：理解它是"倍角公式的多项式化"，几何本质是旋转的迭代。
7. **射影几何视角**：从更高的角度理解——所有三角恒等式都是射影直线上不同坐标系的转换公式。

### 14.2 常见误区

1. **误区**：三角恒等式需要死记硬背。
   - **纠正**：记住和角公式和勾股恒等式，其他都可以推导。

2. **误区**：$\sin(\alpha+\beta) = \sin\alpha + \sin\beta$。
   - **纠正**：正弦不是线性函数！和角公式是 $\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$。

3. **误区**：万能公式是代数技巧。
   - **纠正**：它是单位圆的有理参数化，有深刻的射影几何意义。

4. **误区**：Chebyshev 多项式是特殊函数，与三角学无关。
   - **纠正**：Chebyshev 多项式就是倍角公式的多项式化，$T_n(\cos\theta) = \cos(n\theta)$。

5. **误区**：和差化积与积化和差是互逆的代数运算。
   - **纠正**：它们有不同的几何意义——和差化积是向量的和/差，积化和差是投影乘积的分解。

---

## 第十五章 本章小结

D7-3 作为三角学领域的第三个模块，系统研究了三角恒等式的几何证明，核心是从"代数技巧"到"旋转与投影的几何事实"的范式转换。

**核心内容回顾**：

1. **两种证明方式**：代数证明（逻辑严密但不揭示本质）vs 几何证明（每个公式都有清晰的几何图像）。核心工具：旋转矩阵。
2. **和角公式的几何证明**：三种方法——旋转矩阵乘法、单位圆上的投影分解、向量内积。几何本质：两次旋转合成后坐标的分解。
3. **差角公式**：和角公式加上"镜像变号"（顺时针旋转）。
4. **倍角公式**：和角公式在 $\beta=\alpha$ 时的特例。几何本质：旋转 $2\alpha$ 后的坐标与 $\alpha$ 的关系。
5. **半角公式**：从倍角公式反推。几何本质：已知旋转 $\alpha$ 后的坐标，求旋转 $\alpha/2$ 后的坐标（弧中点）。
6. **和差化积**：几何本质是"两个单位向量的和/差向量"（平行四边形法则）。和向量在角平分线上，长度为 $2\cos(\delta)$。
7. **积化和差**：几何本质是"投影乘积的旋转分解"。两个投影的乘积等于两个旋转的投影的平均。
8. **万能公式**：几何本质是"单位圆的有理参数化"。从 $(-1,0)$ 出发的中心投影将圆参数化为有理函数。射影几何的经典结果。
9. **Chebyshev 多项式**：几何本质是"倍角公式的多项式化"和"旋转的迭代"。$T_n(\cos\theta) = \cos(n\theta)$。
10. **射影几何视角**：所有三角恒等式都是射影直线（圆）上不同坐标系的转换公式。交比、Möbius 变换与三角恒等式的深刻联系。

**核心方法论**：把每个公式翻译成旋转/投影语言，拒绝纯代数推导。记住和角公式和勾股恒等式，其他所有公式都可以通过几何图像推导出来。

**下一个模块 D7-4** 将深入研究欧拉公式与复三角——数学中最反直觉的公式之一。$e^{i\theta} = \cos\theta + i\sin\theta$ 将指数函数（增长/衰减）和三角函数（周期/振荡）统一在一个公式里。它的几何本质是"复平面上的旋转"——$e^{i\theta}$ 不是"指数增长"，而是"单位圆上角度为 $\theta$ 的点"。复三角函数的无界性、复对数的多值性等反直觉结论也将在那里揭示。

---

**D7 三角学领域进度**：3/8 完成（D7-1 ✅、D7-2 ✅、D7-3 ✅、D7-4 ⏳、D7-5 ⏳、D7-6 ⏳、D7-7 ⏳、D7-8 ⏳）。

**总体进度**：46/59（78%）
