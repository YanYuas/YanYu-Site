---
hide:
  - navigation
  - toc
  - path
  - footer
title: 首页
---

<!-- markdownlint-disable MD025 -->
<!-- 首页有多个一级标题（# 衍煜 等），这是首页特殊布局，故意为之 -->

<!--
  ============================================================
  index.md · 首页（粒子星空 + 史诗背景）
  ============================================================
  【重要】front matter（上面 --- 包裹的部分）必须在文件最开头！
  前面不能有任何内容（包括注释、空行），否则 MkDocs 不识别。

  【这个页面是干什么的】
    首页，访客打开网站第一个看到的页面。
    背景：史诗插画（Ken Burns 缓慢缩放，已去掉 AI 水印）+ 暖白粒子 + 流星
    布局：Hero 区（左侧问候/名字/副标题/按钮/数据 + 右侧 Three.js 二次型线框）
          → 三个板块卡片 → 页脚

  【结构说明】
    1. front matter：hide 隐藏导航/目录/路径/页脚，title 浏览器标签页标题
    2. <div class="home">：首页容器
    3. <div class="hero">：两栏 Hero（桌面）；手机上退回单列
       - <p class="greet" id="greet">：问候语，home-greet.js 按时间替换
       - # 衍煜：大标题，particle-bg.js 打字机逐字打出
       - <p class="hero-subtitle">：副标题，打字机效果（带闪烁光标）
       - <p class="hero-note">：一句内容说明
       - <div class="hero-buttons">：三个按钮
       - <div class="hero-stats">：21 模块 / 672 题 / 46 万字
       - <div class="hero-visual">：Three.js 画布，home-3d.js 懒加载
    4. <div class="grid cards">：三个板块卡片（玻璃态 + 金色主题）
    5. <div class="home-foot">：页脚小字

  【怎么修改】
    - 改名字：把 "# 衍煜" 改成你的名字
    - 改副标题：修改 <p class="hero-subtitle"> 里的文字
    - 改按钮：修改 [文字](路径)，.md-button--primary 是实心金色按钮
    - 改卡片：修改每个 - 块里的图标、标题、描述、链接
    - 图标语法：:material-xxx:
  ============================================================
-->

<div class="home" markdown>

<div class="hero" markdown>

<p class="greet" id="greet">你好，我是</p>

# 衍煜

<p class="hero-subtitle">数学与应用数学 · 建模手 · 写作者</p>

<p class="hero-note">把做过的、想过的、踩过的坑，整理成可复用的知识。</p>

<div class="hero-buttons" markdown>
[数学建模](mathmodel/index.md){ .md-button .md-button--primary }
[数学理论](maththeory/index.md){ .md-button .md-button--primary }
[随笔](blog/index.md){ .md-button }
</div>

<div class="hero-stats">
  <span><strong>21</strong>高代模块</span>
  <span><strong>672</strong>精编习题</span>
  <span><strong>46</strong>万字讲义</span>
</div>

<p class="hero-link">
  <a href="maththeory/analytic-geometry/">探索解析几何专题 →</a>
</p>

<div class="hero-visual" aria-hidden="true">
  <canvas id="hero-3d"></canvas>
  <div class="hero-visual__hud">
    <span class="hero-visual__no" id="hero-3d-no">01</span>
    <span class="hero-visual__name" id="hero-3d-name">椭球面</span>
    <span class="hero-visual__formula" id="hero-3d-formula">xᵀAx = 1</span>
  </div>
  <div class="hero-visual__dots" id="hero-3d-dots"></div>
</div>

</div>

<div class="grid cards" markdown>

-   :material-chart-timeline:{ .lg .middle } __数学建模__

    ---

    建模手复盘 · 优化模型 · 竞赛记录

    [进入](mathmodel/index.md)

-   :material-function-variant:{ .lg .middle } __数学理论__

    ---

    高等代数 · 21 模块 / 672 题 · 几何锚定

    [进入](maththeory/index.md)

-   :material-pencil:{ .lg .middle } __随笔__

    ---

    日常随笔 · AI 实践 · 持续更新

    [读一读](blog/index.md)

</div>

<div class="home-foot" markdown>
[关于我](about.md) · [GitHub](https://github.com/YanYuas) · © 2026 衍煜
</div>

</div>
