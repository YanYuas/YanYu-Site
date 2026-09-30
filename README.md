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
│   │   ├── works/               # 我的竞赛作品（5场比赛）
│   │   ├── paper-analysis/      # 优秀论文精解
│   │   └── research/            # 深入论文研究
│   ├── maththeory/              # 数学理论板块
│   │   └── advanced-algebra/    # 高等代数（三领域七模块）
│   ├── blog/                    # 随笔板块
│   │   ├── posts/               # 日常随笔
│   │   └── ai-practice/         # AI实践
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
4. `git push` 推送到 GitHub，自动部署

## 设计风格

星空学术风（Starry Academic）+ 金色主题：
- 深色模式：深蓝底 + 金色文字 + 玻璃态卡片
- 浅色模式：暖白底 + 深金文字 + 暖白玻璃态
- 首页：史诗插画背景（Ken Burns 缩放）+ 暖白粒子 + 流星 + 打字机名字
