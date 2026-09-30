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
    // arithmatex 会把行内公式包成 \(...\)，独立公式包成 \[...\]
    inlineMath:  [["\<inline_LaTeX_Formula>", "\<\inline_LaTeX_Formula>"], ["\\[", "\\]"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,        // 允许用 \$ 转义普通美元符号
    processEnvironments: true,   // 支持 \begin{...} 环境（矩阵、方程组等）

    // 行内公式中也允许自动换行的对齐环境
    tags: "ams"                  // 自动给 \begin{equation} 编号（可选）
  },
  options: {
    ignoreHtmlClass: ".*|no-mathjax",
    processHtmlClass: "arithmatex"
  },
  startup: {
    // 页面加载完成后立即渲染
    pageReady: function () {
      return MathJax.startup.defaultPageReady();
    }
  }
};
