# -*- coding: utf-8 -*-
"""
gen_nav.py · 生成 mkdocs.yml 中高等代数的 nav 片段（零基础自学版）
====================================================================
【这个脚本是干什么的】
  自动扫描高等代数目录，生成 mkdocs.yml 里 nav 部分的高等代数片段。
  包括：三个领域、21个模块、每个模块的"讲义"和"习题集"链接。

【为什么需要这个脚本】
  高等代数导航有100多行，手动写容易出错（路径写错、缩进不对）。
  这个脚本自动扫描目录生成，保证导航和实际文件一致。

【怎么用】
  .venv\Scripts\python.exe tools\gen_nav.py
  运行后会把生成的 nav 片段打印到屏幕上。
  你需要手动复制输出，替换 mkdocs.yml 里 nav 部分的高等代数内容。

  （注意：这个脚本不会自动修改 mkdocs.yml，只输出文本供你复制。）
====================================================================
"""
from pathlib import Path

# 高等代数源代码目录
ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")

# 三个领域的配置：(目录名, 显示名)
GROUPS = [
    ("matrix-basis", "领域一 · 矩阵与基"),
    ("linear-space", "领域二 · 线性空间"),
    ("linear-transform", "领域三 · 线性变换"),
]

lines = []

# ============================================================
# 顶层固定项（不随高等代数内容变化）
# ============================================================
lines.append("  - 首页: index.md")
lines.append("  - 数学建模:")
lines.append("      - 板块导览: mathmodel/index.md")
lines.append("      - 知识库: mathmodel/kb/index.md")
lines.append("      - 竞赛作品: mathmodel/works/index.md")
lines.append("  - 数学理论:")
lines.append("      - 板块导览: maththeory/index.md")
lines.append("      - 高等代数:")
lines.append("          - 总览: maththeory/advanced-algebra/index.md")

# ============================================================
# 方法论与研究（扫描 theory 目录下的所有 .md 文件）
# ============================================================
lines.append("          - 方法论与研究:")
for f in sorted((ROOT / "theory").glob("*.md")):
    # f.stem = 文件名不含后缀（如 "从初等几何到公理化演进"）
    # f.name = 完整文件名（如 "从初等几何到公理化演进.md"）
    lines.append(f"              - {f.stem}: maththeory/advanced-algebra/theory/{f.name}")

# ============================================================
# 三个领域 + 21个模块
# ============================================================
for folder, label in GROUPS:
    # 领域标题
    lines.append(f"          - {label}:")
    # 领域导览页
    lines.append(f"              - 领域导览: maththeory/advanced-algebra/{folder}/index.md")

    # 扫描领域目录下的所有模块子目录
    dirs = sorted([d for d in (ROOT / folder).iterdir() if d.is_dir()],
                  key=lambda p: p.name)

    for d in dirs:
        # 模块标题：把目录名的第一个 "-" 换成 " · "
        # 如 "F1-基底与坐标" → "F1 · 基底与坐标"
        title = d.name.replace("-", " · ", 1)
        # 模块在 nav 里的路径前缀
        base = f"maththeory/advanced-algebra/{folder}/{d.name}"

        # 模块作为一个二级分组：下面有讲义和习题集
        lines.append(f"              - {title}:")
        if (d / "讲义.md").exists():
            lines.append(f"                  - 讲义: {base}/讲义.md")
        if (d / "习题集.md").exists():
            lines.append(f"                  - 习题集: {base}/习题集.md")

# ============================================================
# 尾部固定项
# ============================================================
lines.append("  - 随笔: blog/index.md")
lines.append("  - 关于: about.md")

# 输出到屏幕（用换行连接所有行）
print("\n".join(lines))
