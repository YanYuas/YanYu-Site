---
title: 成长之路
hide:
  - toc
tags:
  - 成长
---

<!--
  ============================================================
  journey/index.md · 成长之路页面（三段式过渡版）
  ============================================================
  【核心体验：三段式连续滚动】
    整个页面是一个连续的 sticky 滚动区域，不硬切：
    - 阶段一（滚动 0%→70%）：左1/4信息卡 + 右3/4横向时间线
    - 阶段二（滚动 70%→80%）：过渡动画——左侧扩大到1/3，时间线淡出，简历淡入
    - 阶段三（滚动 80%→100%）：左1/3信息卡 + 右2/3简历

  【结构说明】
    .journey-page
    └── .journey-sticky-wrap        滚动跑道（高度350vh）
        ├── .journey-layout         sticky固定（100vh），左右分栏
        │   ├── .journey-profile    左侧信息卡（宽度CSS变量控制，25%↔33.3%）
        │   └── .journey-content    右侧内容区
        │       ├── .timeline-layer 时间线层（阶段一显示，阶段二淡出）
        │       └── .resume-layer   简历层（阶段二淡入，阶段三显示）
        └── .journey-scroll-hint    滚动提示

  【过渡原理】
    JS 监听滚动进度，到达 70% 时给 html 加 class="journey-phase-resume"。
    CSS 监听到这个类，自动执行：
    - 左侧宽度 25% → 33.3%（0.8秒过渡）
    - 头像 scale 1.0 → 1.15
    - 时间线层 opacity 1 → 0
    - 简历层 opacity 0 → 1
    往回滚到 68% 以下时移除类，恢复时间线。

  【怎么修改】
    - 改头像：.journey-avatar 里的 emoji 换成 <img src="路径">
    - 加时间线卡片：复制 .timeline-card 块
    - 改简历：在 .resume-layer 里增删 .resume-section
    - 改过渡时机：JS 里的 PHASE1_END（默认0.70）
    - 改滚动距离：CSS 里 .journey-sticky-wrap 的 height（默认350vh）
  ============================================================
-->

<div class="journey-page">

<div class="journey-sticky-wrap">

<div class="journey-layout">

<!-- ========== 左侧：个人信息卡（宽度由CSS变量控制） ========== -->
<div class="journey-profile">

<div class="journey-avatar">🌊</div>

<div class="journey-info">

<h2>衍煜</h2>

<p class="journey-tagline">数学与应用数学 · 建模手 · 写作者</p>

<p class="journey-bio">
成都理工大学数学科学学院在读。主攻数学建模与数学理论，业余写小说、作曲、折腾网站。
相信"做过的才是自己的"。
</p>

<div class="journey-links">
<a href="https://github.com/YanYuas" target="_blank">🐙 GitHub</a>
<a href="mailto:2562696772@qq.com">📧 邮箱</a>
<a href="https://maps.google.com/?q=Chengdu" target="_blank">📍 成都</a>
</div>

</div>
</div>

<!-- ========== 右侧内容区：时间线层 + 简历层（叠加） ========== -->
<div class="journey-content">

<!-- ===== 时间线层（阶段一显示） ===== -->
<div class="timeline-layer">

<div class="journey-timeline-header">
<h2>成长之路</h2>
<p>那些走过的路、踩过的坑、拿到的结果 ↓ 向下滚动，时间线向右推进</p>
</div>

<div class="journey-progress-bar">
<div class="journey-progress-fill"></div>
</div>

<div class="journey-timeline">

<!-- 时间线卡片模板：复制下面这块修改即可
<div class="timeline-card">
  <div class="card-date">YYYY.MM</div>
  <h3>事件标题</h3>
  <p class="card-org">颁发机构 / 相关方</p>
  <span class="card-badge gold">等级标签</span>
  <p class="card-note">一句话描述</p>
  <div class="card-index">01</div>
</div>
-->

<!-- 2025.09 入学 -->
<div class="timeline-card important">
<div class="card-date">2025.09</div>
<h3>入学成都理工大学</h3>
<p class="card-org">数学科学学院 · 数学与应用数学专业</p>
<span class="card-badge gold">里程碑</span>
<p class="card-note">一切的起点。从资阳到成都，开始正经学数学。</p>
<div class="card-index">01</div>
</div>

<!-- 2025.09 高等代数体系 -->
<div class="timeline-card">
<div class="card-date">2025.09</div>
<h3>高等代数知识体系搭建</h3>
<p class="card-org">个人学习项目</p>
<span class="card-badge blue">学习</span>
<p class="card-note">不满足于课堂内容，用"几何锚定"的方式重新组织高等代数。三领域七模块，21个模块配讲义和习题集。</p>
<div class="card-index">02</div>
</div>

<!-- 2026.03 最小覆盖圆 -->
<div class="timeline-card important">
<div class="card-date">2026.03</div>
<h3>最小覆盖圆算法研究</h3>
<p class="card-org">独立科研 · Dynamic MEC-IST</p>
<span class="card-badge gold">科研</span>
<p class="card-note">研究动态点集最小覆盖圆的增量维护算法。论文v9.9.0、代码v9.8.3、软著V1.3。三个提速模块：1.49x / 1.50x / 1.30x。</p>
<div class="card-index">03</div>
</div>

<!-- 2026.05 电工杯 -->
<div class="timeline-card">
<div class="card-date">2026.05</div>
<h3>电工杯数学建模竞赛</h3>
<p class="card-org">中国电机工程学会</p>
<span class="card-badge green">省级三等奖</span>
<p class="card-note">第一次参加数学建模竞赛，建模手初体验。从那以后一发不可收拾，半年打了五场。</p>
<div class="card-index">04</div>
</div>

<!-- 2026.07 华数杯 -->
<div class="timeline-card">
<div class="card-date">2026.07</div>
<h3>华数杯数学建模竞赛</h3>
<p class="card-org">中国工业与应用数学学会</p>
<span class="card-badge gray">待公布</span>
<p class="card-note">第二场，开始找到团队配合的节奏。</p>
<div class="card-index">05</div>
</div>

<!-- 2026.08 五一 -->
<div class="timeline-card">
<div class="card-date">2026.08</div>
<h3>五一数学建模联赛</h3>
<p class="card-org">中国矿业大学等</p>
<span class="card-badge gray">待公布</span>
<p class="card-note">第三场，暑假留校比赛，天气很热但状态不错。</p>
<div class="card-index">06</div>
</div>

<!-- 2026.09 网站上线 -->
<div class="timeline-card">
<div class="card-date">2026.09</div>
<h3>个人网站 YanYu-Site 上线</h3>
<p class="card-org">Astro + Starlight · GitHub Pages</p>
<span class="card-badge blue">项目</span>
<p class="card-note">从零开始自学搭建。2026.10 迁移到 Astro，首页、实验台、标签页和搜索全部重做。</p>
<div class="card-index">07</div>
</div>

<!-- 2026.09 国赛 -->
<div class="timeline-card important">
<div class="card-date">2026.09</div>
<h3>高教社杯全国大学生数学建模竞赛</h3>
<p class="card-org">中国工业与应用数学学会 · 国家级赛事</p>
<span class="card-badge gold">国赛</span>
<p class="card-note">第五场，也是最重要的一场。B题，建模手位置，三天三夜。结果待公布。</p>
<div class="card-index">08</div>
</div>

<!-- 2026.10 亚太杯 -->
<div class="timeline-card">
<div class="card-date">2026.10</div>
<h3>亚太杯数学建模竞赛</h3>
<p class="card-org">APMCM · 国际赛事</p>
<span class="card-badge blue">进行中</span>
<p class="card-note">亚太杯，目标拿个好成绩。英文论文，对写作能力也是考验。</p>
<div class="card-index">09</div>
</div>

<!-- 未完待续 -->
<div class="timeline-card">
<div class="card-date">未完待续</div>
<h3>旅程还在继续</h3>
<p class="card-org">—</p>
<span class="card-badge gray">To Be Continued</span>
<p class="card-note">继续向下滚动，看看完整的我 ↓</p>
<div class="card-index">∞</div>
</div>

</div>
<!-- /.journey-timeline -->

<div class="journey-timeline-axis"></div>

</div>
<!-- /.timeline-layer -->

<!-- ===== 简历层（阶段二淡入，阶段三显示） ===== -->
<div class="resume-layer">

<h2>个人简历</h2>

<!-- 教育背景 -->
<div class="resume-section">
<h3>🎓 教育背景</h3>
<div class="resume-item">
<div class="resume-item-title">成都理工大学 · 数学与应用数学 · 本科</div>
<div class="resume-item-meta">2025.09 - 至今 · 数学科学学院</div>
<div class="resume-item-desc">
核心课程：数学分析、高等代数、解析几何、概率论与数理统计、常微分方程
</div>
</div>
</div>

<!-- 科研经历 -->
<div class="resume-section">
<h3>🔬 科研经历</h3>
<div class="resume-item">
<div class="resume-item-title">动态点集最小覆盖圆增量维护算法（Dynamic MEC-IST）</div>
<div class="resume-item-meta">独立研究 · 2026.03 - 至今 · 论文v9.9.0 / 代码v9.8.3 / 软著V1.3</div>
<div class="resume-item-desc">
基于Welzl算法优化，研究动态点集下最小覆盖圆的增量维护。提出三个提速模块：
<ul>
<li>预测模块：只跟踪支撑点速度，提速 1.49 倍</li>
<li>连续性量化：支撑点漂移超阈值才更新，提速 1.50 倍</li>
<li>增量验证：局部重构后只验证变化点附近，提速 1.30 倍</li>
</ul>
目标期刊：冲二区（CGTA / Adv Comput Math），保底三区（Math Probl Eng）。
</div>
</div>
</div>

<!-- 竞赛经历 -->
<div class="resume-section">
<h3>🏆 竞赛经历</h3>
<div class="resume-item">
<div class="resume-item-title">数学建模竞赛 · 建模手</div>
<div class="resume-item-meta">2026.05 - 至今 · 多场参赛</div>
<div class="resume-item-desc">
<ul>
<li>2026 高教社杯全国大学生数学建模竞赛（国家级，B题）</li>
<li>2026 亚太杯数学建模竞赛（国际级，进行中）</li>
<li>2026 华数杯全国大学生数学建模竞赛</li>
<li>2026 五一数学建模联赛</li>
<li>2026 电工杯数学建模竞赛 · 省级三等奖</li>
</ul>
主攻优化模型，技术栈 MATLAB（主力）+ Python（数据/ML）+ Lingo。
</div>
</div>
</div>

<!-- 技能栈 -->
<div class="resume-section">
<h3>💻 技能栈</h3>
<div class="skill-tags">
<span class="skill-tag core">数学分析</span>
<span class="skill-tag core">高等代数</span>
<span class="skill-tag core">数学建模</span>
<span class="skill-tag core">MATLAB</span>
<span class="skill-tag">Python</span>
<span class="skill-tag">FastAPI</span>
<span class="skill-tag">Vue3</span>
<span class="skill-tag">JavaScript</span>
<span class="skill-tag">Astro</span>
<span class="skill-tag">Starlight</span>
<span class="skill-tag">Git</span>
<span class="skill-tag">Lingo</span>
<span class="skill-tag">R</span>
<span class="skill-tag">GeoGebra</span>
<span class="skill-tag">Blender</span>
</div>
</div>

<!-- 个人作品 -->
<div class="resume-section">
<h3>📝 个人作品</h3>

<div class="resume-item">
<div class="resume-item-title">YanYu-Site 个人网站</div>
<div class="resume-item-meta">Astro + Starlight · GitHub Pages · 2026.09 初版 / 2026.10 迁移</div>
<div class="resume-item-desc">从零自学搭建，现为 Astro 静态站，含首页 3D 轮播、解析几何实验台、Pagefind 搜索和标签聚合。</div>
</div>

<div class="resume-item">
<div class="resume-item-title">高等代数知识体系</div>
<div class="resume-item-meta">三领域七模块 · 21个模块讲义 + 习题集 · 2025.09 启动</div>
<div class="resume-item-desc">用"几何锚定"的方式重新组织高等代数，让每个概念都能落到几何直觉上。</div>
</div>

<div class="resume-item">
<div class="resume-item-title">辞煜卡片引擎</div>
<div class="resume-item-meta">FastAPI + Vue3 · 全栈项目</div>
<div class="resume-item-desc">卡片式内容管理引擎，Vibe Coding模式开发。</div>
</div>

<div class="resume-item">
<div class="resume-item-title">智能竞品分析系统</div>
<div class="resume-item-meta">FastAPI + Vue3 · 全栈项目</div>
<div class="resume-item-desc">电商竞品数据采集与分析系统，商科赛事配套项目。</div>
</div>
</div>

<!-- 联系方式 -->
<div class="resume-section">
<h3>📧 联系方式</h3>
<div class="resume-item-desc">
<ul>
<li><strong>邮箱</strong>：2562696772@qq.com</li>
<li><strong>GitHub</strong>：<a href="https://github.com/YanYuas">github.com/YanYuas</a></li>
<li><strong>所在地</strong>：四川成都</li>
</ul>
</div>
</div>

</div>
<!-- /.resume-layer -->

</div>
<!-- /.journey-content -->

</div>
<!-- /.journey-layout -->

<!-- 滚动提示 -->
<div class="journey-scroll-hint">
↓ 向下滚动<br>时间线向右推进
</div>

</div>
<!-- /.journey-sticky-wrap -->

</div>
<!-- /.journey-page -->
