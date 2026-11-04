---
title: "概率论"
description: "从随机试验、事件与概率空间出发，建立概率论的基础语言。"
tags:
  - 数学理论
  - 概率论
---

> 概率论不是“算可能性”的技巧，而是把不确定性写成可推理的对象。
> 先把样本空间、事件和概率空间说清楚，后面的条件概率、独立性和随机变量才有地方落脚。

---

## 这条线怎么组织

这一部分目前是**基础扩充版**，先把最核心的七章搭起来：

| 章节 | 主题 | 解决的问题 |
|---|---|---|
| 01 | 随机试验和随机事件 | 用什么描述一次随机现象？ |
| 02 | 可测空间和概率空间 | 哪些集合可以谈概率？概率怎么公理化？ |
| 03 | 条件概率 | 已知信息后，概率怎么更新？ |
| 04 | 独立事件 | 什么时候“互不影响”可以写成等式？ |
| 05 | 随机变量与分布函数 | 怎样把样本点变成数？ |
| 06 | 数学期望与方差 | 怎样用两个数概括分布？ |
| 07 | 大数定律与中心极限定理 | 平均为什么稳定、波动为什么近似正态？ |

<div class="card-grid">
<a class="card" href="/YanYu-Site/maththeory/probability-theory/概率空间和随机事件/01随机试验和随机事件/"><strong>01 · 随机试验和随机事件</strong><span>样本空间、事件、集合运算</span></a>
<a class="card" href="/YanYu-Site/maththeory/probability-theory/概率空间和随机事件/02可测空间和概率空间/"><strong>02 · 可测空间和概率空间</strong><span>σ-代数、概率测度、三元组</span></a>
<a class="card" href="/YanYu-Site/maththeory/probability-theory/概率空间和随机事件/03条件概率/"><strong>03 · 条件概率</strong><span>乘法公式、全概率、Bayes</span></a>
<a class="card" href="/YanYu-Site/maththeory/probability-theory/概率空间和随机事件/04独立事件/"><strong>04 · 独立事件</strong><span>两两独立、相互独立、Bernoulli 试验</span></a>
<a class="card" href="/YanYu-Site/maththeory/probability-theory/概率空间和随机事件/05随机变量与分布函数/"><strong>05 · 随机变量与分布函数</strong><span>离散型、连续型、常见分布</span></a>
<a class="card" href="/YanYu-Site/maththeory/probability-theory/概率空间和随机事件/06数学期望与方差/"><strong>06 · 数学期望与方差</strong><span>位置、波动、常见分布的数字特征</span></a>
<a class="card" href="/YanYu-Site/maththeory/probability-theory/概率空间和随机事件/07大数定律与中心极限定理/"><strong>07 · 大数定律与中心极限定理</strong><span>样本均值的稳定与正态近似</span></a>
</div>

---

## 先建立三层直觉

### 第一层：随机试验

抛一次硬币、测一次寿命、抽一张牌，都是随机试验。
结果事先不能确定，但所有可能结果的集合是明确的。

### 第二层：事件

事件是“样本空间里的一部分结果”。
例如“点数为偶数”就是样本空间的一个子集。

### 第三层：概率

概率给每个事件分配一个 $[0,1]$ 之间的数，并且满足几条基本规则。
把这三层写成一个三元组，就是**概率空间**：

$$
(\Omega,\ \mathcal{F},\ P)
$$

---

## 学习建议

- **先画样本空间**：不要一上来套公式，先写清楚 $\Omega$ 是什么；
- **事件用集合写**：把“至少一个”“都不”“恰好一个”翻译成并、交、补；
- **概率公理只记四条**：非负、规范、可列可加，以及由此推出的性质；
- **条件概率注意分母**：$P(A\mid B)$ 的分母是 $P(B)$，不是 $P(A)$；
- **独立不等于互斥**：这是最常见的一个混淆点。

:::note[当前范围]
这一部分是基础扩充版：随机变量、分布函数、期望和方差、极限定理已经补上；
数理统计（抽样、估计、检验）后续再补。
:::
