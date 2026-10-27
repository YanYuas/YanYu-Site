# Phase A Spike Report

- 日期：2026-10-27
- 范围：Astro + Starlight + Vue 3 + Content Collections + KaTeX + Pagefind
- 结论：**GO**（可以进入 Phase B 内容迁移；但先处理下面列出的迁移项）
- 生产站点：仍是 MkDocs；本目录不参与 GitHub Pages 部署

---

## 1. 验证结论

| 项目 | 结果 | 判断 |
|---|---|---|
| Astro build（spike 6 页） | 2.37 s | ✅ |
| Astro build（全量 87 docs 试验） | 93 页 / 16.56 s | ✅ |
| `astro check` | 0 errors / 0 warnings（1 hint） | ✅ |
| KaTeX 全量公式 | 87 文件 / 2,961 公式 / 0 errors | ✅ |
| 全量试构建公式 | 2,966 个 KaTeX 渲染 / 0 个 `katex-error` | ✅ |
| Pagefind 中文检索 | “线性空间” → 2 results | ✅ |
| Vue island（Three.js） | 2 个 canvas 正常渲染 | ✅ |
| Vue island（Canvas 2D） | 圆锥曲线正常渲染 | ✅ |
| 浏览器 console/page error | 0 / 0 | ✅ |
| base path `/YanYu-Site` | 侧边栏、卡片、G1 页面均正确 | ✅ |
| 移动端 390×844 | 实验台上下堆叠，canvas 正常 | ✅ |

---

## 2. 体积与性能

### 实验代码分割

| 产物 | raw | gzip |
|---|---:|---:|
| `QuadricLab.*.js`（Three.js + OrbitControls） | 760,658 B | **190,933 B** |
| `ConicLab.*.js`（纯 Canvas 2D） | 3,805 B | **1,947 B** |
| 首页加载的实验脚本 | 无 | — |
| 实验页加载 | 两个 island 各自独立 chunk | — |

- 首页 HTML 只引用 Starlight 页面脚本和 Search，不加载 QuadricLab/ConicLab；
- 实验页网络请求里同时出现 `QuadricLab` 与 `ConicLab`；
- Three.js 目前是单实验 chunk，gzip 约 191 KB，低于 200 KB 目标，但触发 Vite 500 KB raw 警告。

### 搜索

| 方案 | 索引体积 | 备注 |
|---|---:|---|
| 当前 MkDocs jieba 搜索 | **8.86 MB** 单文件 | 每次构建 9 MB 级索引 |
| Pagefind（spike 6 页） | 约 610 KB | 含 UI 资源 |
| Pagefind（全量 93 页试验） | 约 **563 KB** | 分片、静态 |

中文查询验证：`线性空间` → 2 条结果，标题与摘要正常。

### 构建时间

| 方案 | 92/93 页构建 | 搜索索引 |
|---|---:|---:|
| MkDocs（本地沙箱） | 约 139–186 s | jieba |
| Astro（全量 trial） | **16.56 s** | Pagefind 1.13 s |

> MkDocs 数字来自本机临时关闭 git 插件并行的构建；Astro 数字来自同一台机器。

### 输出体积

- spike 6 页：dist **3.57 MB**（含 692 KB hero 背景图）；
- 全量 trial：dist 20.63 MB（含重复的 `full/` 试验副本和图片），不作为最终指标；
- Pagefind 全量索引从 8.86 MB 降到约 0.56 MB。

---

## 3. 已验证的交互

### 3.1 首页

- Starlight splash + 自定义深色/金色主题；
- 真实 hero 背景图；
- 数据驱动卡片：`src/data/labs.json` + Zod 校验；
- 点击「二次曲面」卡片 → `/YanYu-Site/analytic-geometry/lab/#quadric`。

### 3.2 G1 讲义

- 46300 B 原文迁移；
- 标题、摘要、关键词、侧边栏、TOC 正常；
- MathJax 公式 → KaTeX 渲染；
- `!!! info "模块信息"` 手动转为 `:::note[模块信息]`，渲染为 Starlight aside。

### 3.3 二次曲面 island

- Vue 3 + Three.js；
- 椭球面 / 单叶双曲面 / 马鞍面切换正常；
- 尺度滑杆、OrbitControls、深色网格；
- 截图验证：椭球与单叶双曲面均正确显示。

### 3.4 圆锥曲线 island

- Vue 3 + Canvas 2D；
- 离心率/半通径滑杆；
- 焦点、准线、曲线绘制。

---

## 4. 发现的问题 / Phase B 必做项

### 内容迁移

1. **MkDocs admonitions**：全站 **35** 处 `!!!`；需要转换脚本（`!!! info` → `:::note[标题]`，缩进内容去缩进，补 `:::`）。G1 的 1 处已手动验证。
2. **Material grid cards**：全站 **6** 处 `grid cards` / 图标 / 按钮语法；需要转成 Astro/Vue 组件。
3. **frontmatter title**：全量 trial 中有页面缺 `title`，需要迁移脚本从 H1 自动补；否则 Starlight schema 直接报错。
4. **slug 大小写**：`G1.md` 生成 `/g1/`；侧边栏/链接必须使用 lowercase slug，或给 frontmatter 显式 `slug`。
5. **链接基址**：Starlight 会自动给 sidebar 加 `base`；Markdown/hero 里的绝对链接需要 helper 或手动前缀。Spike 已验证 sidebar 自动前缀、hero 手动前缀。
6. **tags**：MkDocs tags 插件需迁移到 frontmatter + tag 页面。
7. **图片**：`docs/assets` 需要迁到 `src/assets`/`public`，并做体积预算。

### 视觉

- 当前首页是 Starlight splash，不是最终的两栏 Hero + 3D 轮播；Phase D 再移植完整首页。
- 现有 Starry Academic 设计 tokens 只迁移了一部分；需要完整 CSS token 对照。
- G1 页面尚未做 Markdown 内的 Material 卡片/按钮视觉对齐。

### 工程

- 全量 trial 的 `full/` 是临时副本，已删除；切换前需正式内容迁移。
- 未添加 Astro 的 GitHub Actions（Phase D 再加）。
- Starlight 仍有 2 个非阻断 warning：
  - `Entry docs → 404 was not found`（使用内置 404 fallback）；
  - Vite chunk >500 KB（Three.js 单 chunk，gzip 191 KB）；
  - KaTeX 对 `√` 的 strict warn（无 error）。
- `astro check` 目前 0 errors / 0 warnings（1 hint）。

---

## 5. 结论

**GO。**

四个关键风险都已用真实内容验证：

1. **公式**：2,961 个公式 0 KaTeX error；
2. **中文搜索**：Pagefind 可召回；
3. **重型实验**：Three.js/Vue island 正常，独立 chunk，gzip 191 KB；
4. **部署路径**：base `/YanYu-Site` 下页面、侧边栏、卡片可跳转。

下一步进入 **Phase B 内容迁移**：

1. 写 `convert-mkdocs.py`：admonitions、grid cards、titles、tags、图片路径；
2. 迁移全部 87 个 Markdown；
3. 保持 URL parity + redirects；
4. 全量 build + 浏览器回归；
5. 再进入 Phase C 实验迁移与 Phase D 切换。
