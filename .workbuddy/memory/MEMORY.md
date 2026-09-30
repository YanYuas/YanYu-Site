# YanYuas 站点 · 项目备忘

> 长期约定与关键技术细节。日常进展见 `YYYY-MM-DD.md`。

## 项目性质

MkDocs + Material 搭建的个人学术站点。文件即真源，`site/` 是构建产物（已 gitignore）。
站点定位：数学与应用数学本科生的数学建模、数学理论与随笔。

## 站点的公式机制（重要）

**双轨设计**，改公式相关配置前必读：

1. `pymdownx.arithmatex`（`generic: true`）在解析期把 `$...$` / `$$...$$`
   转成 `\(...\)` / `\[...\]`。
2. `docs/javascripts/mathjax.js` 里 MathJax 同时配置了这两组定界符，
   **另外还开了原生 `$` / `$$` 识别**，用于兜底 arithmatex 处理不了的情况
   （典型：写在列表项内部的块级公式）。

**已知约束**：arithmatex 的块级公式要求公式**不在列表上下文内**，且前后有空行。
题库里大量公式写在 `- **解答**：` 的缩进续行中，属于结构性冲突，
目前靠 MathJax 原生 `$$` 兜底渲染，不做 md 结构改写。

**风险点**：开启 `$` 行内识别后，正文中成对出现的普通 `$`（如金额）会被误当公式。
新增内容若含此类字符，需写成 `\$` 转义。

## MathJax 本地化

`docs/javascripts/vendor/tex-mml-chtml.js`（MathJax 3，约 1.12MB）为本地副本。
**不要改回 CDN** —— 曾用的字节跳动镜像
`lf26-cdn-tos.bytecdntp.com` 与 `lf3-...` 均已 404，会导致全站公式失效。

升级方式：重新下载 `https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js`
覆盖 vendor 目录下同名文件。

## 目录约定

```
docs/
  index.md                    首页
  mathmodel/                  数学建模（导览 + kb + works）
  maththeory/
    index.md                  数学理论导览
    advanced-algebra/         高等代数
      index.md                总览
      theory/                 方法论与研究论文
      matrix-basis/           F1-F7 领域一
      linear-space/           G1-G7 领域二
      linear-transform/       T1-T7 领域三
  blog/                       随笔
  stylesheets/                主题样式
  javascripts/                脚本（vendor/ 存第三方库）
tools/                        项目维护脚本
```

题库模块目录命名：`{代号}-{中文名}`，内含单一文件 `习题集.md`。
导航里的显示名用「代号 · 中文名」形式。

**写索引页的铁律**：模块清单必须写成链接形态（表格或列表都行），
不能只写加粗文本。曾因把 21 个模块写成 `- **F1** 基底与坐标` 纯文本，
导致用户从总览页完全点不进去。

**预览服务会掉**：后台 `mkdocs serve` 在会话间隙会被回收，
用户隔天访问就是 502。交付时要逐一 curl 验证关键页面返回 200，
并明确告知用户当前可用端口（默认 8000）。

## tools/ 脚本

| 脚本 | 作用 | 何时用 |
|---|---|---|
| `check_site.py` | 全站验收：页面数、题量、讲义、公式、内链 | 改动后 |
| `html2md.py` | 奶油糖果风讲义 HTML → Markdown | 有 HTML 讲义要转换 |
| `fix_block_formula.py` | 缩进 `$$...$$` 顶格化 | 新导入 md 时 |
| `fix_matrix_brackets.py` | 矩阵字面量 `[[a,b],[c,d]]` 加反引号 | 新导入 md 时 |
| `fix_bracket_paren.py` | 算式 `[x](y)` 转义方括号 | 新导入 md 时 |
| `gen_nav.py` | 生成 mkdocs.yml 的 nav 块 | 增删模块后 |
| `gen_index.py` | 生成总览 + 三领域索引页 | 增删模块后 |

新导入 Markdown 题库的**标准顺序**：
`fix_block_formula.py` → `fix_matrix_brackets.py` → `fix_bracket_paren.py`
→ `mkdocs build` → `check_site.py`

转换 HTML 讲义的标准顺序：
`html2md.py` → `fix_matrix_brackets.py` → `fix_bracket_paren.py`
→ `gen_nav.py`（更新 nav）→ `gen_index.py`（更新索引）→ `mkdocs build` → `check_site.py`

**注意**：`fix_bracket_paren.py` 不可重复执行（会产生双反斜杠）。

## HTML 讲义的两个特性（与题库 md 不同）

1. **不含 LaTeX**：公式全是 Unicode 数学字符，转换时无需处理定界符。
2. **易踩的 Markdown 陷阱**：
   - `[[a,b],[c,d]]` 矩阵字面量 → 被当链接
   - `[算式](算式)` 形态 → 被当链接
   两者都需转义处理。

## 样式

- `starry-academic.css`：当前生效主题（`starry` 深色 / `parchment` 浅色）
- `cream-candy.css`：奶油糖果风，**未被 mkdocs.yml 引用**（孤儿文件）。
  其 scheme 名为 `cream`，与 mkdocs.yml 中的 `parchment` 不一致。
  若要启用需同步改 `theme.palette` 的 scheme 值。
- `home.css`：首页版式，必须排在 `starry-academic.css` 之后

## 内容边界（作者明确划定，不要动）

**数模竞赛作品的规划结构不要擅自修改**。
`docs/mathmodel/works/index.md` 里有 5 个作品条目，
其中 02_EEMCM / 03_HSMCM / 04_CUMCM / 05_APMCM **尚未创建**，
链接会 404 并在构建时产生 4 条 WARNING —— 这是作者有意保留的占位，
等后续逐个补完。不要「修复」成非链接或删掉。

`tools/check_site.py` 顶部有 `PLANNED_MARKERS` 白名单，
把这 4 条归到「规划中」而非「失效」。建好页面后删掉对应代号。

## 工作流约定

- `site/`、`.venv/` 不入库
- `文档/` 与 `手册/` 为个人学习文档，不入库
  （目录 2026-09 从「文档」改名为「手册」，gitignore 两条都保留）
- `.vscode/settings.json` 例外入库（存 YAML 标签白名单）
- **默认构建不要用 `--strict`**：那 4 条规划链接必然产生警告，
  strict 模式会直接中止构建。tasks.json 里已拆成
  「构建站点」（非 strict）与「严格检查（发布前）」两个任务。
- 提交前建议跑 `tools/check_site.py`
