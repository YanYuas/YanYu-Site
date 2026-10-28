# YanYuas · 个人网站

数学与应用数学本科生的个人网站，用 MkDocs + Material 主题搭建。

## 网站内容

- **数学建模**：建模手的自我修养、数学与算法基础、竞赛作品、优秀论文精解、深入论文研究
- **数学理论**：高等代数（三领域 × 七模块 = 21模块、672道习题）
- **随笔**：日常随笔、AI实践

## 技术栈

| 组件 | 技术 |
|------|------|
| 静态站点生成器 | MkDocs 1.6.1 |
| 主题 | Material for MkDocs 9.7.7 |
| 中文搜索 | jieba 分词 |
| 数学公式 | MathJax（本地部署） |
| 流程图 | Mermaid |
| 首页特效 | Canvas 粒子背景 + Ken Burns 背景图 |
| 旧链接重定向 | mkdocs-redirects |
| 自动部署 | GitHub Actions → GitHub Pages |

## 本地运行

```bash
# 1. 创建虚拟环境（第一次）
python -m venv .venv

# 2. 激活虚拟环境
.venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动本地预览（http://127.0.0.1:8000）
mkdocs serve

# 5. 构建网站（输出到 site/ 目录）
mkdocs build --clean

# 6. 发布前严格检查 + 站点验收（CI 也是这两步）
mkdocs build --clean --strict
.venv\Scripts\python.exe tools\check_site.py
```

## 项目结构

```
YanYu-Site/
├── docs/                        # 网站内容（Markdown）
│   ├── index.md                 # 首页（粒子背景 + 史诗插画）
│   ├── about.md                 # 关于页
│   ├── mathmodel/               # 数学建模板块（5个子模块）
│   │   ├── self-cultivation/    # 建模手的自我修养
│   │   ├── fundamentals/        # 数学与算法基础
│   │   ├── works/               # 我的竞赛作品（6个目录，05 暂为占位）
│   │   ├── paper-analysis/      # 优秀论文精解
│   │   └── research/            # 深入论文研究
│   ├── maththeory/              # 数学理论板块
│   │   ├── advanced-algebra/    # 高等代数（三领域七模块）
│   │   ├── analytic-geometry/   # 解析几何专题（含 Three.js 交互实验）
│   │   └── probability-theory/  # 概率论（骨架，建设中）
│   ├── blog/                    # 随笔板块
│   │   ├── posts/               # 日常随笔
│   │   └── ai-practice/         # AI实践
│   ├── journey/                 # 成长之路（灰度，暂未进导航）
│   ├── assets/images/           # 图片资源（首页背景图等）
│   ├── stylesheets/             # 自定义样式
│   │   ├── home.css             # 首页样式（已逐行注释）
│   │   └── starry-academic.css  # 全站视觉系统
│   └── javascripts/             # 自定义脚本
│       ├── particle-bg.js       # 粒子背景引擎
│       ├── home-greet.js        # 首页问候语（按时段变化）
│       └── mathjax.js           # LaTeX 渲染配置
├── _archive/                    # 存档（不参与构建）
│   └── literature/              # 海灵传说小说（180章）
├── tools/                       # 维护脚本（验收 / 改名 / 内容修复）
├── visual/                      # P2 视觉原型（Three.js，暂不参与构建）
├── overrides/                   # 自定义模板（404 页面）
├── .github/workflows/           # GitHub Actions 自动部署
├── mkdocs.yml                   # 网站总配置（已详细注释）
├── requirements.txt             # Python 依赖清单
├── .gitignore                   # Git 忽略规则
└── .gitattributes               # Git 属性配置
```

## 怎么加新内容

1. 在 `docs/` 对应目录下新建 `.md` 文件
2. 在 `mkdocs.yml` 的 `nav` 里添加链接
3. `mkdocs serve` 预览效果
4. 推送前跑一遍 `mkdocs build --clean --strict`，确认没有警告
5. `git push` 推送到 GitHub，自动部署

**如果移动/改名已有页面**：不要手动改链接，用下面这个脚本，它会同时改
Markdown 链接、`mkdocs.yml` 的 nav，并自动补上旧 URL 的 redirect：

```bash
.venv\Scripts\python.exe tools/rename_page.py 旧路径 新路径
```

先加 `--dry-run` 可以只看计划、不写文件。

## 维护工具

| 工具 | 作用 |
|---|---|
| `tools/check_site.py` | 全站验收：页面数、题量、讲义、内链、公式；不通过退出码非 0 |
| `tools/rename_page.py` | 页面/目录改名：自动改 Markdown 链接、nav、redirect |
| `tools/gen_nav.py` / `gen_index.py` | 生成 nav 与索引页 |
| `tools/fix_*.py` | 修复公式/矩阵/标题格式（新导入内容时用） |

- CI 部署前会跑 `mkdocs build --clean --strict` 和 `python tools/check_site.py`，
  有坏链或警告就不会发布。
- 旧 URL 由 `mkdocs-redirects` 负责跳转；`rename_page.py` 会自动维护映射。
- 手动改文件名后，记得补 `mkdocs.yml` 的 `redirect_maps`，否则旧链接会 404。

## P2 视觉升级

- **首页 Hero**：桌面端右侧按「椭球面 → 单叶双曲面 → 马鞍面 → 莫比乌斯环」交替展示，
  悬停暂停、切换时交叉淡入；只在 >1000px 且支持 WebGL 时懒加载。
- **解析几何专题**：`maththeory/analytic-geometry/` 采用三领域八模块结构，
  并配交互实验台：3D 二次曲面/平面/环面/莫比乌斯环，2D 圆锥曲线、2D 线性变换。
- `visual/` 是视觉实验与 Three.js 源码目录；正式产物在
  `docs/javascripts/vendor/`，由 `docs/javascripts/*.js` 按页面懒加载。
- 改完源码后重新打包：

```bash
cd visual
npm install
npm run build:hero   # 首页 hero
npm run build:geo    # 解析几何实验台
```

细节见 [visual/README.md](visual/README.md)。

## Astro 生产站（Phase D 完成）

**生产站点已切换为 Astro 构建**，部署 workflow 为 `.github/workflows/deploy.yml`；
MkDocs 保留为手动回滚：`.github/workflows/deploy-mkdocs.yml`。

- 架构决策：[ARCHITECTURE.md](ARCHITECTURE.md)
- Phase A：[astro/SPIKE_REPORT.md](astro/SPIKE_REPORT.md)
- Phase B：[astro/MIGRATION_REPORT.md](astro/MIGRATION_REPORT.md)
- Phase C：[astro/PHASE_C_REPORT.md](astro/PHASE_C_REPORT.md)
- Phase D：[astro/PHASE_D_REPORT.md](astro/PHASE_D_REPORT.md)
- 内容源：`astro/src/content/docs/`（`docs/` 只用于 MkDocs 回滚/历史）
- 数据源：`astro/src/data/`
- 本地运行：

```bash
cd astro
npm install
npm run dev      # http://localhost:4321/YanYu-Site/
npm run check
npm run check:math
npm run check:links
```

回滚：

```bash
gh workflow run deploy-mkdocs.yml --ref main
```

## 设计风格

星空学术风（Starry Academic）+ 金色主题：
- 深色模式：深蓝底 + 金色文字 + 玻璃态卡片
- 浅色模式：暖白底 + 深金文字 + 暖白玻璃态
- 首页：两栏 Hero（左文字 / 右 Three.js 四种曲面交替）+ 风格化史诗插画背景 + 数据条 + 6 个实验入口
