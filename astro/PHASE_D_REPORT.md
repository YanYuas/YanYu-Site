# Phase D Report：首页移植与生产切换

- 日期：2026-10-28
- 范围：自定义首页 Hero、3D 轮播、Astro Pages 部署切换、回滚路径
- 结论：**Phase D 完成，生产站点已切换为 Astro 构建**

---

## 1. 首页

自定义 Starlight `Hero` 覆盖：

- 两栏 Hero：左侧问候 / 姓名 / 副标题 / 说明 / 三按钮 / 数据条 / 解析几何入口；
- 右侧 Three.js 四曲面轮播：
  - 椭球面 → 单叶双曲面 → 马鞍面 → 莫比乌斯环；
  - HUD 编号/名称/公式 + 四段进度；
  - 悬停暂停；
  - 桌面 `>1000px` 才懒加载，移动端隐藏；
  - reduced-motion 静态首帧；
  - WebGL 失败保留边框/不发散。
- 首页下方：
  - 三个入口卡片（数学建模 / 数学理论 / 随笔）；
  - 6 张数据驱动实验卡片；
  - 页脚。

文件：

- `src/components/home/HomeHero.astro`
- `src/components/home/Hero3D.vue`
- `src/components/home/hero3d.js`
- `src/content/docs/index.mdx`
- `src/styles/custom.css`

---

## 2. 部署切换

### 新生产 workflow

`.github/workflows/deploy.yml`：

- Node 24 + `npm ci`（`astro/`）；
- `astro check`；
- `astro build`；
- `check-links`；
- `upload-pages-artifact` → `deploy-pages`。

### 回滚

`.github/workflows/deploy-mkdocs.yml`：

- 手动 `workflow_dispatch`；
- 使用原 MkDocs strict build + `check_site.py`；
- 上传 `site/` 并部署。

切换后若需要回退：

```bash
gh workflow run deploy-mkdocs.yml --ref main
```

---

## 3. 线上验证

| 项目 | 结果 |
|---|---|
| 首页 | 200，`首页 | 衍煜 · YanYuas` |
| 首页 Hero | 1 个 `.home-hero`，1 个 `#hero-3d` canvas |
| 首页卡片 | 3 入口 + 6 实验 |
| 3D 轮播 | HUD `01 椭球面` → 8.5s 后 `02 单叶双曲面` |
| 实验台 | 200，6 个标签，canvas 正常 |
| 中文搜索 | “线性空间” 53 条 |
| 旧 sitemap URL | 87/87 200 |
| 新 sitemap URL | 87/87 200 |
| 旧作品 URL | meta redirect 到新 URL，最终标题正确 |
| `/sitemap.xml` | 200 XML（兼容入口） |
| `/sitemap-index.xml` | 200 XML |
| `/robots.txt` | 200 |
| 浏览器 console/page error | 0 / 0 |
| 移动端首页 | 3D 隐藏，单列布局 |
| 部署耗时 | 约 1 分钟 |

> 修复了首版 redirect 目标缺少 `/YanYu-Site` base 的问题：
> 旧大写 URL 的 meta refresh 现在指向带 base 的新地址，canonical 同步正确。

---

## 4. 构建指标

| 项目 | 结果 |
|---|---|
| 页面 | 88 |
| 生成 HTML（含 redirect/alias） | 97 |
| 构建时间 | 约 5–9 s（本地） |
| `astro check` | 0 / 0 / 0 |
| 内部链接 | 0 broken / 97 |
| KaTeX | 2,951 / 0 error |
| Pagefind | 562.7 KB |
| 首页 3D chunk（共享 Three） | 736,692 B raw / 约 185 KB gzip |
| Lab 共享 Three chunk | 756 KB raw / 约 189 KB gzip |
| 单实验 chunk | 约 4 KB raw |

---

## 5. 当前状态与维护约定

- **生产**：`https://yanyuas.github.io/YanYu-Site/` 由 Astro 构建；
- **内容源**：`astro/src/content/docs/`；`docs/` 只作为 MkDocs 回滚/历史源；
- **数据源**：`astro/src/data/`（labs、sidebar、redirects 生成文件）；
- **首页源**：`astro/src/components/home/`；
- **实验源**：`astro/src/components/labs/`；
- **回滚**：`deploy-mkdocs.yml`；
- 后续内容修改请改 Astro 源，不要只改 `docs/`。

---

## 6. 剩余项

1. tags 聚合页（当前只有 `tags.md`）；
2. 自定义 404 文案/页面（当前 Starlight 内置 404）；
3. 首页原 MkDocs 粒子背景/Ken Burns 的逐帧还原（当前保留风格化背景图）；
4. 可选的实验 presets / reset / 参数 URL 编码；
5. 定期清理 `docs/` 与 `visual/` 双源，避免长期漂移。
