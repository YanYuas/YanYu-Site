---
hide:
  - navigation
  - toc
  - path
  - footer
title: 首页
---

<!--
  ============================================================
  index.md · 首页（粒子星空 + 史诗背景版）
  ============================================================
  【重要】front matter（上面 --- 包裹的部分）必须在文件最开头！
  前面不能有任何内容（包括注释、空行），否则 MkDocs 不识别。

  【这个页面是干什么的】
    网站首页，访客打开网站第一个看到的页面。
    背景：史诗插画（Ken Burns 缓慢缩放）+ 暖白粒子 + 流星
    布局：Hero 区（问候语 + 名字打字机 + 副标题打字机 + 按钮）→ 三个板块卡片 → 页脚

  【结构说明】
    1. front matter：hide 隐藏导航/目录/路径/页脚，title 浏览器标签页标题
    2. <div class="home">：首页容器
    3. <div class="hero">：Hero 大标题区
       - <p class="greet" id="greet">：问候语，home-greet.js 按时间替换
       - # 衍煜：大标题，particle-bg.js 打字机逐字打出
       - <p class="hero-subtitle">：副标题，打字机效果（带闪烁光标）
       - <div class="hero-buttons">：三个按钮
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

<div class="hero-buttons" markdown>
[数学建模](mathmodel/index.md){ .md-button .md-button--primary }
[数学理论](maththeory/index.md){ .md-button .md-button--primary }
[随笔](blog/index.md){ .md-button }
</div>

</div>

<div class="grid cards" markdown>

-   :material-chart-timeline:{ .lg .middle } __数学建模__

    ---

    建模手的自我修养 · 数学与算法基础 · 竞赛作品 · 论文精解

    [进入](mathmodel/index.md)

-   :material-function-variant:{ .lg .middle } __数学理论__

    ---

    高等代数 · 三领域七模块 · 讲义与习题集

    [进入](maththeory/index.md)

-   :material-pencil:{ .lg .middle } __随笔__

    ---

    日常随笔 · AI实践 · 生活与思考

    [读一读](blog/index.md)

</div>

<div class="home-foot" markdown>
[关于我](about.md) · MkDocs + Material · 全部用 Markdown 写作
</div>

</div>
