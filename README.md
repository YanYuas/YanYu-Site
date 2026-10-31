# YanYuas · 个人网站

数学与应用数学本科生的个人学术网站：数学建模、高等代数、解析几何、随笔与交互实验。

- 线上：https://yanyuas.github.io/YanYu-Site/
- 仓库：https://github.com/YanYuas/YanYu-Site

---

## 现在用什么

| 组件 | 技术 |
|---|---|
| 站点生成 | Astro 7.4 |
| 文档主题 | Starlight 0.42 |
| 交互 | Vue 3 islands + Three.js |
| 公式 | KaTeX |
| 搜索 | Pagefind |
| 部署 | GitHub Actions → GitHub Pages |
| Node | 24 |

`docs/` 是 MkDocs 时代的旧内容，只用于回滚；**生产内容在 `astro/src/content/docs/`**。

---

## 本地跑起来

需要 Node.js 24 和 Git。

```powershell
cd D:\YanYuas\YanYu-Site
cd astro
npm install
npm run dev
```

打开：

```text
http://localhost:4321/YanYu-Site/
```

> 必须带 `/YanYu-Site/`，因为站点部署在子路径。

---

## 常用命令

在 `astro/` 目录下执行：

| 命令 | 作用 |
|---|---|
| `npm run dev` | 本地预览 |
| `npm run verify` | 一次跑完 check → formula → build → links |
| `npm run check` | Astro / TypeScript 检查 |
| `npm run check:math` | 扫描 Astro 内容里的公式 |
| `npm run build` | 生成 `astro/dist/` |
| `npm run check:links` | 检查内部链接，严格区分大小写 |
| `npm run measure` | 查看 JS/CSS/资源体积 |
| `npm run check:browser` | Playwright 浏览器检查（可选，需本地静态服务） |

发布前最省事：

```powershell
npm run verify
```

---

## 内容在哪里

```text
astro/
├── src/content/docs/      ★ 文章和页面
│   ├── index.mdx          首页
│   ├── tags.mdx           标签总览
│   ├── 404.md             自定义 404
│   ├── mathmodel/         数学建模
│   ├── maththeory/        数学理论
│   ├── blog/              随笔
│   └── journey/           成长之路
├── src/components/
│   ├── home/              首页 Hero / 3D 轮播
│   ├── labs/              6 个交互实验
│   ├── tags/              标签总览
│   └── content/           文章底部标签条
├── src/data/              labs / sidebar / redirects
├── src/pages/tags/        标签详情动态路由
├── src/styles/custom.css  主题与排版
├── public/assets/         图片、favicon、OG 图
└── scripts/               检查与迁移脚本
```

新增文章：

1. 在对应目录新建 `.md`；
2. frontmatter 写 `title`、`description`、`tags`；
3. 正文不要再写 H1；
4. 站内链接写目录，不写 `.md`；
5. 需要侧边栏时改 `src/data/sidebar.generated.mjs`。

标签会自动出现在 `/tags/`，不需要手写标签页。

---

## 部署

push 到 `main` 会自动触发：

```text
.github/workflows/deploy.yml
```

流程：

```text
npm ci → astro check → check:math → build → check:links → GitHub Pages
```

回滚到 MkDocs 旧版：

```powershell
gh workflow run deploy-mkdocs.yml --ref main
```

或在 GitHub Actions 页面手动运行 `deploy-mkdocs`。

---

## 当前状态

| 项目 | 值 |
|---|---|
| 页面 | 97 页 |
| HTML | 106（含 redirect） |
| sitemap | 96 URLs |
| 标签 | 9 个标签 / 27 篇内容 |
| 检查 | check 0/0/0；链接 0 broken |
| 安全 | `npm audit` 0 vulnerabilities |
| 回滚 | 已实测 |

详细架构与历史报告：

- [ARCHITECTURE.md](ARCHITECTURE.md)
- [Phase A](astro/SPIKE_REPORT.md)
- [Phase B](astro/MIGRATION_REPORT.md)
- [Phase C](astro/PHASE_C_REPORT.md)
- [Phase D](astro/PHASE_D_REPORT.md)

---

## 其他目录

| 目录 | 说明 |
|---|---|
| `docs/` | MkDocs 旧内容，只用于回滚 |
| `visual/` | Three.js 原型/旧实验源码，不参与生产部署 |
| `tools/` | MkDocs 时代的 Python 工具 |
| `手册/` | 本地手册，被 `.gitignore` 忽略，不随仓库同步 |
| `_archive/` | 历史备份 |
| `site/` | 已清理的旧构建产物 |

---

## 本地手册

`手册/` 里有给新手看的：

- `使用手册.md`：日常改内容、加公式、加图片、发布、排错；
- `搭建手册.md`：从新电脑到上线；
- `依赖升级策略.md`：升级依赖但不升坏；
- `遗留与维护清单.md`：还有哪些坑、怎么维护；
- `最终验收报告.md`：当前验收基线。

这些文件**不进 Git**，换电脑需要手动复制。
