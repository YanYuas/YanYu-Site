/* ==================================================================
   mathjax.js · 数学公式渲染配置（配合 pymdownx.arithmatex）
   ------------------------------------------------------------------
   文档中这样写公式：
     行内公式：$x + y = 1$
     独立公式：
       $$
       \max z = c^{T} x
       $$
   ================================================================== */

window.MathJax = {
  tex: {
    // 双轨支持：
    //   ① arithmatex 能识别的公式 → 已转成 \(...\) / \[...\]
    //   ② arithmatex 识别不了的（如写在列表项内的块级公式）→ 保留原始 $...$ / $$...$$
    //      由 MathJax 原生兜底，避免 $ 字面量裸露在页面上。
    inlineMath:  [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,        // 允许用 \$ 转义普通美元符号
    processEnvironments: true,   // 支持 \begin{...} 环境（矩阵、方程组等）

    // 给 \begin{equation} 环境自动编号，效果类似 LaTeX 的 amsmath。
    // 注意：它跟"行内公式换行对齐"无关，那取决于公式自己怎么写。
    tags: "ams"
  },
  options: {
    // 【为什么这样配】
    // MathJax 默认 processHtmlClass="mathjax" 表示「只扫描 mathjax 元素内部」，
    // 但 mkdocs-material 的正文没有这个 class，所以必须放开限制、全页扫描。
    // ignoreHtmlClass 用来排除不该解析的区域（代码块、导航、页脚等）。
    ignoreHtmlClass: "no-mathjax|md-nav|md-header|md-footer|md-search|highlight|md-clipboard",
    processHtmlClass: "md-content__inner"
  },
  startup: {
    // 页面加载完成后立即渲染
    pageReady: function () {
      return MathJax.startup.defaultPageReady();
    }
  }
};
