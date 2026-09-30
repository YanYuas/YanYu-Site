/* ==================================================================
   mathjax.js · 数学公式渲染配置（零基础自学版 · 完整版）
   ------------------------------------------------------------------
   【这个脚本是干什么的】
     配置 MathJax——一个在网页上渲染 LaTeX 数学公式的库。
     你的 Markdown 里写的 $x + y = 1$ 和 $$...$$ 公式，
     最终就是由 MathJax 变成漂亮的数学符号的。

   【支持的 LaTeX 功能】
     ✅ 行内公式：$...$ 或 \(...\)
     ✅ 块级公式：$$...$$ 或 \[...\]
     ✅ 矩阵、方程组：\begin{matrix}、\begin{cases} 等
     ✅ 自动编号：\begin{equation} 自动编号
     ✅ 交叉引用：\label{eq:xxx} + \ref{eq:xxx} 或 \eqref{eq:xxx}
     ✅ 自定义宏：常用命令简写（如 \R → 实数集符号）
     ✅ 自动加载扩展：需要什么包自动加载（amsmath、amssymb 等）
     ✅ 转义：\$ 显示普通美元符号

   【工作流程】
     1. MkDocs 构建时，pymdownx.arithmatex 扩展把 $...$ 转成 \(...\)
     2. 页面加载时，MathJax 扫描页面，把 \(...\) 和 \[...\] 渲染成公式
     3. 如果 arithmatex 没转成功（比如公式写在列表里），
        MathJax 也能直接识别原始的 $...$ 和 $$...$$（兜底）

   【文档中这样写公式】
     行内公式：$x + y = 1$          → 显示在文字中间
     独立公式：
       $$
       \max z = c^{T} x
       $$                             → 单独占一行，居中

     带编号的公式：
       $$
       \begin{equation}
       \label{eq:example}
       E = mc^2
       \end{equation}
       $$
     引用公式：见公式 \eqref{eq:example}

   【为什么 MathJax 本体在本地】
     javascripts/vendor/tex-mml-chtml.js 是 MathJax 库本体（1.1MB）。
     原先用的字节跳动 CDN 已失效（404），会导致全站公式完全不渲染。
     下载到本地后既快又稳定，离线也能用。
   ================================================================== */

// window.MathJax 是 MathJax 的全局配置对象
// 必须在加载 MathJax 本体之前设置，否则配置不生效
window.MathJax = {

  // ================================================================
  // TeX（LaTeX）输入配置
  // ================================================================
  tex: {

    // ---- 公式定界符 ----
    // 行内公式的左右包裹符号
    // 双轨支持：
    //   ① arithmatex 能识别的公式 → 已转成 \(...\)
    //   ② arithmatex 识别不了的（如写在列表项内的块级公式）→ 保留原始 $...$
    //      由 MathJax 原生兜底，避免 $ 字面量裸露在页面上。
    inlineMath:  [["\\(", "\\)"], ["$", "$"]],

    // 独立（块级）公式的定界符
    //   ① \[...\] 是 arithmatex 转换后的格式
    //   ② $$...$$ 是原始 Markdown 格式（兜底）
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],

    // ---- 基础选项 ----
    processEscapes: true,        // 允许用 \$ 转义普通美元符号（写"100$"时不会被当成公式）
    processEnvironments: true,   // 支持 \begin{...} 环境（矩阵、方程组等）
    processRefs: true,           // 处理 \ref 和 \eqref 引用

    // ---- 自动编号 ----
    // 给 \begin{equation} 环境自动编号，效果类似 LaTeX 的 amsmath 包。
    // "ams" = 像 AMS（美国数学会）格式那样编号：(1) (2) (3)
    // "all" = 所有块级公式都编号（包括 $$...$$）
    // "none" = 不自动编号
    tags: "ams",

    // 编号的侧边：right = 编号在右边（LaTeX 默认），left = 编号在左边
    tagSide: "right",

    // 编号和公式的缩进
    tagIndent: "0.8em",

    // ---- 标签格式 ----
    // 控制 \eqref 引用时显示的格式
    tagformat: {
      number: function (n) { return n; },           // 编号本身：直接显示数字
      tag:    function (n) { return '(' + n + ')'; }, // 公式旁边的标签：(1)
      eqref:  function (n) { return '(' + n + ')'; }  // \eqref 引用时的显示：(1)
    },

    // ---- 自动加载扩展 ----
    // MathJax 把很多不常用的功能拆成了扩展，需要时才加载。
    // 这里配置哪些命令对应哪个扩展，MathJax 遇到时自动加载。
    // （本地 tex-mml-chtml.js 已包含所有扩展，不需要联网下载）
    autoload: {
      // amsmath 扩展：align、gather、multline 等对齐环境
      align: ['amsmath'],
      alignat: ['amsmath'],
      gather: ['amsmath'],
      multline: ['amsmath'],
      flalign: ['amsmath'],
      // cases 扩展：大括号方程组
      cases: ['amsmath'],
      // 矩阵扩展
      matrix: ['amsmath'],
      pmatrix: ['amsmath'],
      bmatrix: ['amsmath'],
      vmatrix: ['amsmath'],
      Vmatrix: ['amsmath'],
      // 其他常用环境
      equation: ['amsmath'],
      eqnarray: ['amsmath'],
      // amssymb 扩展：更多数学符号（\mathbb、\mathcal 等）
      mathbb: ['amssymb'],
      mathcal: ['amssymb'],
      mathfrak: ['amssymb'],
      mathscr: ['amssymb'],
      // 颜色扩展
      color: ['color'],
      textcolor: ['color'],
      // 新定义扩展
      newcommand: ['newcommand'],
      // 文本扩展
      text: ['text'],
      // 上划线/下划线扩展
      cancel: ['cancel'],
      // 化学公式扩展（如果需要写化学式）
      ce: ['mhchem']
    },

    // ---- 自定义宏 ----
    // 这里定义常用命令的简写，写公式时可以直接用。
    // 格式："命令名": ["替换内容", 参数个数]
    // 比如 \R 会被替换成 \mathbb{R}（实数集符号）
    macros: {
      // 数集符号
      R:  ['\\mathbb{R}', 0],   // 实数集
      N:  ['\\mathbb{N}', 0],   // 自然数集
      Z:  ['\\mathbb{Z}', 0],   // 整数集
      Q:  ['\\mathbb{Q}', 0],   // 有理数集
      C:  ['\\mathbb{C}', 0],   // 复数集
      // 常用算子
      dim:    ['\\operatorname{dim}', 0],    // 维度
      rank:   ['\\operatorname{rank}', 0],   // 秩
      ker:    ['\\operatorname{ker}', 0],    // 核
      im:     ['\\operatorname{im}', 0],     // 像
      tr:     ['\\operatorname{tr}', 0],     // 迹
      det:    ['\\operatorname{det}', 0],    // 行列式
      // 向量符号（箭头）
      vec:    ['\\boldsymbol{#1}', 1],       // 加粗向量（覆盖默认箭头）
      // 常用括号
      abs:    ['\\left|#1\\right|', 1],      // 绝对值
      norm:   ['\\left\\|#1\\right\\|', 1],  // 范数
      // 常用符号
      iff:    ['\\Longleftrightarrow', 0],   // 当且仅当
      implies:['\\Longrightarrow', 0],       // 蕴含
      empty:  ['\\varnothing', 0],           // 空集
      // 分段函数
      piecewise: ['\\begin{cases}#1\\end{cases}', 1]
    },

    // ---- 已加载的包（不需要自动加载，直接启用）----
    packages: { '[+]': ['noerrors', 'noundefined'] }
    // noerrors：公式出错时显示原始 LaTeX 代码，而不是报错信息
    // noundefined：未定义的命令显示为红色，而不是报错
  },

  // ================================================================
  // 选项配置
  // ================================================================
  options: {
    // 【为什么这样配】
    // MathJax 默认 processHtmlClass="mathjax" 表示「只扫描 mathjax 元素内部」，
    // 但 mkdocs-material 的正文没有这个 class，所以必须放开限制、全页扫描。
    // ignoreHtmlClass 用来排除不该解析的区域（代码块、导航、页脚等）。

    // 不解析这些区域里的内容（避免代码里的 $ 被当成公式）
    ignoreHtmlClass: "no-mathjax|md-nav|md-header|md-footer|md-search|highlight|md-clipboard",

    // 只解析正文内容区（md-content__inner 是 Material 包裹文章的容器）
    processHtmlClass: "md-content__inner",

    // 渲染前跳过的元素类型
    skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"],

    // 公式渲染完成后的回调（可以在这里加自定义逻辑）
    renderActions: {
      // 默认为空，不需要额外操作
    }
  },

  // ================================================================
  // 输出配置（CHTML = 通用 HTML 输出）
  // ================================================================
  chtml: {
    // 公式字体大小（相对于正文的比例，1 = 一样大）
    scale: 1,
    // 最小字体大小（防止嵌套公式太小看不清）
    minScale: 0.5,
    // 匹配容器高度（让公式和文字基线对齐）
    matchFontHeight: true
  },

  // ================================================================
  // 启动配置
  // ================================================================
  startup: {
    // 页面加载完成后立即渲染公式
    pageReady: function () {
      // 调用默认的 pageReady 函数（执行标准初始化流程）
      return MathJax.startup.defaultPageReady();
    },
    // 启动时需要加载的类型
    typeset: true
  },

  // ================================================================
  // 文档级配置
  // ================================================================
  // 当页面内容动态变化时（比如 SPA 切换页面），是否重新渲染公式
  // MkDocs 是静态网站，不需要这个，但加上无害
  document: {
    // 公式渲染完成后的回调
    onRender: function (doc) {
      // 默认为空
    }
  }
};
