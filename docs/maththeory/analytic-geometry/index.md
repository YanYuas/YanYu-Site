---
tags:
  - 数学理论
  - 解析几何
---

# 解析几何

> 用坐标把几何问题翻译成代数问题，再用向量把代数结果翻译回几何直觉。
> 这一页是「解析几何」专题的起点：先建立坐标与向量的语言，再进入曲面和交互实验。

---

## 为什么单独做一个专题

高等代数里的「几何锚定」需要一个具体落点：基、坐标、线性变换和二次型，最终都要能在
平面/空间里画出来。解析几何正好提供这套画布：

- **坐标**：把点变成有序数组，把几何关系变成方程；
- **向量**：把方向、长度、夹角变成可计算的对象；
- **二次型**：把椭圆、双曲线、抛物面、马鞍面统一成 $x^{\mathsf T}Ax=1$ 的分类问题；
- **参数方程**：把曲线/曲面变成可采样、可渲染的对象——这也是三维交互的入口。

它和高等代数不是两门课，而是同一套结构在「具体几何」和「抽象空间」两端的两次表述。

---

## 一、坐标与向量

在选定原点 $O$ 和基 $\{e_1,e_2,e_3\}$ 之后，空间中每个点 $P$ 都对应唯一坐标
$(x,y,z)$，每个向量 $\vec v$ 也对应唯一坐标。几何里的「平移、伸缩、投影」因此变成
坐标里的加法、数乘和点积。

三个最基本的结构：

$$
\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta,\qquad
\vec a\times\vec b=
\begin{vmatrix}
e_1&e_2&e_3\\
a_1&a_2&a_3\\
b_1&b_2&b_3
\end{vmatrix}
$$

- 点积负责「角度与投影」；
- 叉积负责「法向与面积」；
- 混合积负责「体积与共面判定」。

---

## 二、直线与平面

空间直线用「点 + 方向」表示：

$$
\frac{x-x_0}{m}=\frac{y-y_0}{n}=\frac{z-z_0}{p}
$$

空间平面用「点 + 法向量」表示：

$$
Ax+By+Cz+D=0,\qquad \vec n=(A,B,C)
$$

平面与直线的关系，本质上就是**法向量与方向向量的点积**：
平行、垂直、相交、距离，都可以化成一个点积或一个叉积。这是「几何翻译成代数」最直接的例子。

---

## 三、二次曲线与二次曲面

二次型 $x^{\mathsf T}Ax=1$ 在三维里给出三类典型二次曲面：

| 方程 | 名称 | 主方向的符号 |
|---|---|---|
| $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}+\dfrac{z^2}{c^2}=1$ | 椭球面 | 三个正 |
| $x^2+y^2-z^2=1$ | 单叶双曲面 | 两正一负 |
| $z=x^2-y^2$ | 双曲抛物面（马鞍面） | 一正一负 |

再加一个非定向曲面作为对照：**莫比乌斯环**。它不能用「一个二次方程」描述，但可以用参数方程
$(R+v\cos\frac u2)\cos u,\ v\sin\frac u2,\ (R+v\cos\frac u2)\sin u$ 生成——这正是交互实验里
四种形状的来源。

> 二次曲面的分类，最终由矩阵 $A$ 的特征值符号决定；这和你高代里学的「合同标准形」是同一件事。

---

## 四、三维交互实验

下面这个画布把「方程—曲面」的对应关系做成可以拖动、缩放的对象。
切换标签看不同曲面，拖动滑杆改变尺度；平面模式会显示法向量。

<div class="geo-lab" id="geo-lab">
  <div class="geo-lab__stage">
    <canvas id="geo-canvas"></canvas>
    <div class="geo-lab__fallback" id="geo-fallback" hidden>
      当前浏览器无法启用 WebGL。你仍然可以阅读本页的公式与说明；<br>
      换用支持 WebGL 的桌面浏览器即可看到交互曲面。
    </div>
  </div>
  <aside class="geo-lab__panel">
    <div class="geo-lab__tabs" role="tablist" aria-label="曲面类型">
      <button class="is-active" data-geo="ellipsoid" role="tab" aria-selected="true">椭球面</button>
      <button data-geo="hyperboloid" role="tab" aria-selected="false">单叶双曲面</button>
      <button data-geo="saddle" role="tab" aria-selected="false">马鞍面</button>
      <button data-geo="plane" role="tab" aria-selected="false">平面</button>
    </div>

    <label class="geo-lab__control">
      <span>尺度 a</span>
      <input id="geo-a" type="range" min="0.6" max="1.8" step="0.05" value="1.2" />
    </label>

    <p class="geo-lab__desc" id="geo-desc">
      三个主方向都被缩放；拖动旋转可以看到椭球的三个半轴。
    </p>
    <p class="geo-lab__hint">拖动旋转 · 滚轮缩放 · 悬停暂停自动巡游</p>
  </aside>
</div>

---

## 五、和高等代数的连接

- [G5 · 解析几何嵌入](../advanced-algebra/linear-space/G5-解析几何嵌入/讲义.md)
  —— 点、向量、直线/平面如何嵌入线性空间；
- [G7 · 二次型与曲面](../advanced-algebra/linear-space/G7-二次型与曲面/讲义.md)
  —— 二次型的合同标准形与二次曲面分类；
- [高等代数总览](../advanced-algebra/index.md)
  —— 三领域 × 七模块的完整入口。

---

## 六、延伸资源

**3Blue1Brown（3b1b）** 的线性代数系列适合建立几何直觉：

- [Essence of Linear Algebra 官方专题页](https://www.3blue1brown.com/topics/linear-algebra)
- [3b1b/videos：视频动画源码](https://github.com/3b1b/videos)
  —— 内容采用 **CC BY-NC-SA 4.0**，非商业使用需署名并以相同方式共享；
- [3b1b/manim：动画引擎](https://github.com/3b1b/manim)
  —— **MIT** 许可，可以用它生成自己的数学动画。

> 这里只做链接与学习路径推荐，不直接搬运视频或动画源码；如果你想用 Manim
> 生成属于本站的解析几何动画，可以作为下一阶段的独立项目。

---

## 七、学习路径（建议）

1. 先把「点/向量/坐标」的对应关系写熟；
2. 再用点积、叉积推导直线与平面的位置关系；
3. 进入二次型：用合同变换把方程化成标准形；
4. 对照交互实验，把参数变化和曲面形状对应起来；
5. 最后回到高等代数，看 G5 / G7 里的抽象定义如何落回这些具体对象。
