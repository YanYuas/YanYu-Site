# Phase B Migration Report

- 日期：2026-10-27
- 范围：把 MkDocs/Material 内容迁入 Astro/Starlight，保持 URL 可用
- 结论：**Phase B 完成**；进入 Phase C（实验迁移）前还有 3 个收尾项

---

## 1. 迁移结果

| 项目 | 结果 |
|---|---|
| 源 Markdown | 87 |
| 迁入 Astro 的 Markdown | 85（保留自定义首页 + 自定义实验台） |
| 内容条目 | 87（85 + home + lab） |
| 构建页面 | 88 |
| 生成 HTML（含 redirect/alias） | 97 |
| sitemap URL | 87 |
| 构建时间 | 14.30 s |
| `astro check` | 0 errors / 0 warnings / 0 hints |
| 内部链接检查 | 0 broken / 97 HTML |
| KaTeX 渲染 | 2,951 个 / 0 个 `katex-error` |
| Pagefind 索引 | 562.7 KB / 97 HTML |
| 中文搜索 | “线性空间” 53 条结果 |
| 旧 URL（87） | 87/87 返回 200 |
| 新 URL（87） | 87/87 返回 200 |
| 浏览器 console/page error | 0 / 0 |

---

## 2. 转换流水线

脚本：[`scripts/migrate-docs.py`](./scripts/migrate-docs.py)

按顺序处理：

1. **frontmatter / title**：没有 title 的页面从第一个 H1 提取；有 title 的页面删除正文 H1，避免重复。
2. **MkDocs admonitions → Starlight asides**：
   - 35 处 `!!! note/info/tip` → `:::note/tip`；
   - 支持 G1/T* 的「无缩进模块信息」特殊格式；
   - 全部转换后 HTML 中 raw `!!!` 为 0。
3. **Material grid cards → HTML cards**：
   - 4 个可渲染的 `grid cards` 块 → `.card-grid` / `.card`；
   - 对应 CSS 已加入 `src/styles/custom.css`；
   - 全部转换后 raw `grid cards` 为 0。
4. **链接重写**：
   - 105 个 `.md` 链接 → 新 Astro 路由；
   - 相对/绝对路径按源文件位置解析；
   - 内链统一加 `/YanYu-Site` base；
   - HTML 内 `href`/`src` 同样处理。
5. **图片/资源**：`docs/assets` → `astro/public/assets`；当前只有 hero 背景与 favicon。
6. **sidebar 生成**：解析 `mkdocs.yml` nav，生成 `src/data/sidebar.generated.mjs`；
   - 路由为 Astro 的 lowercase slug；
   - 深层分组默认折叠，当前页自动展开。
7. **redirects 生成**：旧 MkDocs URL → 新 Astro 路由；包含大小写差异与旧作品 redirect maps；
   - `redirects.generated.mjs`。

---

## 3. 验证

### 构建与内容

- `astro build`：88 pages，14.30 s；
- `astro check`：0/0/0；
- `check-links.mjs`：97 HTML，0 broken；
- KaTeX：2,951 个渲染，0 error；
- 页面 H1：除 5 个旧作品 redirect 页外，均为 1 个 H1。

### URL parity

- 旧 sitemap 87 条：**87/87 200**；
- 新 sitemap 87 条：**87/87 200**；
- 63 条旧 URL 与新 URL 仅大小写不同（如 `G1-...` vs `g1-...`）；
  旧 URL 可访问，canonical 指向新 URL。

### 浏览器（Playwright + 系统 Chrome）

已验证：

- 首页：4 个入口、2 张数据卡片、卡片跳转；
- G1 讲义：侧边栏、KaTeX、aside、TOC；
- 竞赛作品：表格；
- 随笔：卡片（修复了初版的纯文本堆叠）；
- 解析几何实验台：2 个 canvas、Vue islands 独立 chunk；
- 旧 `/mathmodel/works/01_51MCM-2026/` → 200；
- 移动端 390×844：实验台正常；
- console/page error：0。

### 体积

- dist：23.18 MB raw / 2.74 MB gzip；
- Three.js island：760,658 B raw / 190,933 B gzip；
- Canvas 2D island：3,805 B / 1,947 B；
- Pagefind：562.7 KB（对比 MkDocs 8.86 MB）。

> dist raw 偏大主要来自 Windows 大小写不敏感文件系统把 uppercase/lowercase alias
> 合并到同一物理路径；Ubuntu Astro Check artifact 约 3.35 MB，Linux 下 alias 是轻量 redirect。

---

## 4. 剩余问题（Phase C/D）

1. **大小写 alias 体积**：旧 uppercase URL 当前返回完整内容（不是轻量 redirect），
   dist raw 因此偏大；需要在 Phase D 做 post-build 或 Astro integration 统一成 redirect。
2. **旧作品 redirect 页无 H1**：5 个 meta redirect 页面，正常；不参与搜索。
3. **Starlight 404 fallback warning**：使用内置 404；无阻断。
4. **Three.js chunk >500 KB raw warning**：gzip 191 KB，符合预算；可调整 warning limit 或动态 import。
5. **首页视觉**：当前是 Starlight splash（4 个入口 + 背景图 + 数据卡片），
   尚未移植原 MkDocs 的两栏 Hero + 3D 轮播；Phase D 完成。
6. **tags**：`tags.md` 已迁移，但未生成 MkDocs 风格的 tag 聚合页；Phase D 处理。
7. **两处 `.md` 链接**：仅存在于 HTML 注释/占位文字中，不影响渲染。

---

## 5. 结论

内容层已经达到可切换状态：

- 所有 87 个 sitemap URL 新旧均可访问；
- 公式、搜索、侧边栏、链接、卡片、移动端均通过；
- 生产仍是 MkDocs，Astro 未部署。

下一步 **Phase C**：

1. 把实验台拆成可复用 lab registry / LabShell；
2. 迁移其余实验（向量、直线与平面、圆锥曲线、线性变换）；
3. 实验 chunk 预算与降级；
4. 之后 Phase D：完整首页移植、redirect 优化、CI 切换。
