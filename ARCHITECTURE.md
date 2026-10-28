# 站点长期架构决策（ADR）

- 状态：Accepted（2026-10-27）
- 决策：**迁移到 Astro + Starlight，Vue 3 islands，内容数据源用 Content Collections + YAML**
- 迁移策略：**strangler（逐步替换）**；Phase A–D 已完成，生产已切换为 Astro
- 当前状态：**Phase D 完成，生产站点 = Astro**；代码在 `astro/`，报告见 [astro/PHASE_D_REPORT.md](astro/PHASE_D_REPORT.md)；MkDocs 通过 `deploy-mkdocs.yml` 手动回滚

### Phase A 结果摘要

- Astro build：spike 6 页 2.37 s；全量 87 docs 试验 93 页 16.56 s；
- KaTeX：2,961 个公式 0 error；全量试构建 2,966 个 KaTeX 渲染 0 error；
- Pagefind 中文检索可用（“线性空间” 2 条结果）；
- Three.js island 760,658 B raw / 190,933 B gzip，与 Canvas 2D island 分开 chunk；
- base path `/YanYu-Site` 下侧边栏、卡片、内容页跳转正常；
- 浏览器 console/page error 0；移动端 390×844 正常；
- 待处理：35 处 MkDocs admonitions、6 处 grid cards、缺 title 的页面、slug 大小写、图片迁移、完整首页移植。

### Phase B 结果摘要

- 85 个内容页迁入 Astro，保留自定义首页与实验台；87 个 sitemap URL 新旧均可访问；
- `astro check` 0/0/0，内部链接 0 broken，KaTeX 2,951 个渲染 0 error；
- 35 处 admonitions、4 处 grid cards、105 个 `.md` 链接已转换；
- 侧边栏由 `mkdocs.yml` nav 生成并折叠；redirects 生成；
- Pagefind 562.7 KB，中文搜索可用；
- 已知：大小写 alias 页面当前返回完整内容，dist raw 偏大；Phase D 优化；
- 下一步：Phase C 实验迁移、Phase D 完整首页/切换。

### Phase C 结果摘要

- LabShell / LabExplorer / labs.json 注册表；
- 6 个实验：向量、直线与平面、圆锥曲线、二次曲面、参数曲面、线性变换；
- 每实验独立 async chunk；Three 共享 chunk gzip 约 189 KB；
- `astro check` 0/0/0，内部链接 0 broken，旧/新 87/87 URL 200；
- Ubuntu Astro Check workflow 通过。

### Phase D 结果摘要

- 自定义 Starlight Hero：两栏首页 + 三入口 + 6 实验卡片 + 页脚；
- 首页 Three.js 四曲面轮播/HUD，桌面懒加载、移动端隐藏；
- 生产 workflow 切换为 Astro（`deploy.yml`），MkDocs 回滚 workflow 保留；
- 线上首页、实验台、搜索、旧 URL、sitemap/robots 验证通过；
- 旧 redirect 的 base 前缀修复。

---

---

## 1. 背景

当前站点是 MkDocs 1.6 + Material 9.7：

- 87 个 Markdown，构建 92 个页面；
- 21 篇高等代数讲义 + 672 道题，公式约 2,712 处；
- 自定义 CSS/JS、MathJax 本地化、Three.js 首页、解析几何实验台；
- 搜索索引约 9 MB，MathJax 每页约 1.17 MB（未压缩）；
- 后续会加入**非常多的重型交互实验**（三维、Canvas、Manim/Plotly、参数化对象、可视化算法等）。

MkDocs 的优势是内容写作和文档导航，但它没有组件模型、没有按页 code-splitting、没有内容 schema；
当实验数量增长到几十个时，继续用「手写 script 标签 + 全局 bundle + 手写 nav」会让维护成本超线性上升。

因此需要一次长期架构决策，而不是继续在 MkDocs 上叠胶水。

---

## 2. 决策

### 2.1 目标架构

```
Astro（当前稳定版）+ Starlight
├── Content Collections + Zod        # 内容/数据 schema，构建期校验
├── Vue 3 islands                    # 每个重型实验一个独立 island
├── Three.js / Canvas 2D             # 实验内部实现，共享 runtime
├── KaTeX（构建期）                  # 公式默认预渲染，减少客户端负担
├── Pagefind                         # 静态搜索；中文召回率需 spike 验证
├── GitHub Pages                     # 部署方式不变
└── 保留现有 URL + redirects         # 不破坏外部链接
```

### 2.2 为什么是 Astro + Starlight

| 需求 | Astro + Starlight 的回答 |
|---|---|
| 很多重型实验 | islands + `client:visible`/`client:idle`，每个实验独立 chunk，按页懒加载 |
| 实验需要 Vue/React 组件 | Astro 官方支持 Vue/React/Svelte islands；选 Vue 3（与现有项目经验一致） |
| 内容数据源 | Content Collections + Zod；YAML/JSON 与 Markdown 同源校验 |
| 导航/索引不再手写 | Starlight sidebar 可从内容结构生成；作品/模块索引由数据渲染 |
| 搜索 | Pagefind 静态搜索，索引分片，不再有 9 MB 单文件 |
| 公式 | KaTeX 构建期渲染；不支持的宏可退回 MathJax（按页） |
| 首页/视觉 | Starlight 可覆盖组件；自定义首页用 Astro 页面，保留现有设计语言 |
| 部署 | 继续 GitHub Pages，无服务器依赖 |

### 2.3 不做的事

- **不继续留在 MkDocs 上堆实验胶水**：少量实验可以，几十个不行。
- **不做 iframe 实验农场**：样式、路由、SEO、通信都会变成新的维护债。
- **不迁 Next/Nuxt 全家桶**：对静态学术站过重，SSR 能力用不上。
- **暂不做题库自测/数据化**（第 4 项，按要求暂缓）。

---

## 3. 目标目录与内容数据源

```
astro/
├── astro.config.mjs
├── src/
│   ├── content.config.ts          # Zod schema：docs / labs / works / modules
│   ├── content/
│   │   └── docs/                  # Markdown/MDX 正文（从 docs/ 迁移）
│   ├── data/
│   │   ├── profile.yml            # 姓名/邮箱/GitHub/简介
│   │   ├── works.yml              # 竞赛：日期/题目/角色/结果/链接
│   │   ├── modules.yml            # 高代/解析几何模块清单与顺序
│   │   └── labs.yml               # 实验注册表：slug/标题/组件/公式/状态
│   ├── components/
│   │   ├── labs/                  # 每个实验一个 Vue SFC
│   │   ├── ui/                    # Slider、Formula、LabShell、卡片
│   │   └── data/                  # WorksTable、ModuleGrid（由 YAML 渲染）
│   ├── layouts/
│   ├── pages/                     # 首页/自定义页/索引页
│   └── styles/
└── public/
```

### 3.1 单一数据源规则

- 作品事实只写在 `works.yml`；作品表、首页卡片、成长之路时间线都从这里渲染。
- 模块顺序/标题/描述只写在 `modules.yml`；侧边栏、总览卡片、上一页/下一页都从它生成。
- 实验元信息只写在 `labs.yml`；实验卡片、路由、组件懒加载都从它生成。
- 个人常量只写在 `profile.yml`；关于页/首页/页脚引用同一份。
- 构建时用 Zod 校验；字段缺失/类型错误直接失败。

### 3.2 实验契约

每个实验是一个独立 Vue island：

```vue
<!-- src/components/labs/QuadricLab.vue -->
<LabShell title="二次曲面" :formula="...">
  <canvas ref="canvas" />
</LabShell>
```

- 通过 `client:visible` 或 `client:idle` 挂载；
- 共享 `src/components/labs/three/` 的 renderer/resize/dispose/主题工具；
- 每个实验独立 chunk，禁止把多个重型实验打进同一个 global bundle；
- 无 WebGL / reduced-motion / 移动端有降级；
- 单实验 gzip 预算：目标 < 200 KB；单页实验总量目标 < 350 KB。

---

## 4. 迁移策略（strangler）

**MkDocs 继续线上服务，Astro 版在 `astro-migration` 分支（或仓库内 `astro/` 目录）开发，不切流量。**

### Phase A · 技术 spike（2–3 天）

目标：验证风险，不追求全站。

1. 在 `astro/` 搭 Starlight + Vue；
2. 迁移首页 + 解析几何实验室（2 个实验即可）；
3. 迁移 2 个代表性内容页：一篇 G1 讲义、一篇带表格/链接的索引页；
4. 验证：
   - KaTeX 对现有 2,712 处公式的兼容性；
   - Pagefind 中文召回率（用「线性空间」「特征值」「二次曲面」测试）；
   - Three.js/Vue island 的构建与代码分割；
   - 自定义 Starry Academic 视觉的可迁移性；
   - GitHub Pages 子路径 `/YanYu-Site/` 的 base/链接；
5. 输出：构建产物大小、构建时间、需要的手工迁移清单。

**Spike 通过后才继续。**

### Phase B · 内容迁移（1–2 周）

- 批量迁移 `docs/**/*.md` 到 `src/content/docs/**`；
- 转换 MkDocs/Material 特有语法：
  - `!!! note` → Starlight aside / 组件；
  - `grid cards`、Material 图标、`{ .md-button }` → Astro/Vue 组件；
  - `markdown` 属性 HTML 块 → MDX 组件；
  - tags → frontmatter + tag 页面；
- 保留 URL：文件路径尽量不变；改名用 redirects 表；
- 图片迁移到 `src/assets` 或 `public`，加尺寸/压缩预算。

### Phase C · 实验迁移（约 1 周）

- 把 `analytic.js` 拆成独立 lab islands：二次曲面/参数曲面/圆锥曲线/线性变换；
- 建立 `labs.yml` 注册表与 `LabShell`；
- 旧实验的全局 loader 删除，改为按页 import；
- 增加“实验元信息”卡片：公式、参数、相关模块。

### Phase D · 切换（2–3 天）

- GitHub Actions 改为 Astro build + Pages；
- 验证 sitemap、robots、canonical、404、redirects；
- 旧 MkDocs 分支保留 1–2 个版本作为回滚；
- 观察 1 周后归档 MkDocs 配置。

**总工期估计：3–4 周（按业余时间并行内容工作）。**

---

## 5. 持续维护（已确认要做）

### CI 必须项

- `astro check` / TypeScript 检查；
- Content Collections schema 校验；
- 内链 + 锚点检查（Starlight links validator 或自建）；
- 构建期 KaTeX 错误检查；
- 实验 bundle 预算检查（单实验/单页）；
- 图片体积检查（单图 ≤ 300 KB，优先 WebP/AVIF）；
- Lighthouse/移动端基线（可选，先记录不阻断）。

### 依赖与仓库

- Node/pnpm 版本锁定；Dependabot 或 Renovate 每月检查；
- 大文件（视频/PDF/数据集）放 GitHub Releases 或对象存储，不进 git 历史；
- 仓库体积季度检查；历史清理仍用 `git filter-repo` + bundle 备份；
- 所有 URL 变更必须走 `redirects` 表，不允许裸删。

### 文档

- 本 ADR 作为架构基线；
- `README` 只保留运行/维护入口，细节放 `docs` 或 `手册`；
- 数据 schema、实验契约、发布流程各有单一说明页。

---

## 6. 风险与缓解

| 风险 | 缓解 |
|---|---|
| KaTeX 不支持部分 MathJax 宏 | Spike 用全量公式做兼容性检查；不支持的页面保留 MathJax 客户端渲染 |
| Pagefind 中文召回差 | Spike 对比「Pagefind / jieba 预构建索引 / Orama」；必要时保留 jieba 方案 |
| Material 语法迁移遗漏 | 写转换脚本 + 逐页对比渲染结果；链接检查兜底 |
| 视觉还原成本 | 先迁移设计 tokens 与 LabShell，再做页面级 CSS；首页最后迁移 |
| DSH 沙箱无法跑 Astro 构建 | Spike 以 GitHub Actions 为构建验证环境；本地只做源码/类型检查 |
| 迁移期间双维护 | 冻结 MkDocs 新功能；只修 P0；Astro 完成后一次性切换 |
| 实验数量继续增长 | 实验注册表 + 独立 chunk；每个实验必须声明预算和降级策略 |

---

## 7. 验收标准（切换前）

- 所有现有 URL 200 或有 redirect；
- 87 个页面内容齐全，公式渲染无回归；
- 搜索能召回中文关键词；
- 首页/实验台视觉与交互不低于当前版本；
- 单页实验 JS 预算达标；
- GitHub Actions 构建稳定，失败可回滚；
- 移动端关键页面可用。

---

## 8. 下一步

1. 搭建 Astro spike（Phase A）；
2. 用真实内容验证 KaTeX / Pagefind / 视觉；
3. Spike 通过后，按 Phase B→C→D 迁移；
4. 题库自测/数据化暂缓（第 4 项）。
