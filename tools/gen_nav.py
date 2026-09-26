# -*- coding: utf-8 -*-
"""生成 mkdocs.yml 中高等代数的 nav 片段（含讲义 + 习题集）。"""
from pathlib import Path

ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")

GROUPS = [
    ("matrix-basis", "领域一 · 矩阵与基"),
    ("linear-space", "领域二 · 线性空间"),
    ("linear-transform", "领域三 · 线性变换"),
]

lines = []
# 顶层固定项（不随高等代数内容变化）
lines.append("  - 首页: index.md")
lines.append("  - 数学建模:")
lines.append("      - 板块导览: mathmodel/index.md")
lines.append("      - 知识库: mathmodel/kb/index.md")
lines.append("      - 竞赛作品: mathmodel/works/index.md")
lines.append("  - 数学理论:")
lines.append("      - 板块导览: maththeory/index.md")
lines.append("      - 高等代数:")
lines.append("          - 总览: maththeory/advanced-algebra/index.md")
lines.append("          - 方法论与研究:")
for f in sorted((ROOT / "theory").glob("*.md")):
    lines.append(f"              - {f.stem}: maththeory/advanced-algebra/theory/{f.name}")

for folder, label in GROUPS:
    lines.append(f"          - {label}:")
    lines.append(f"              - 领域导览: maththeory/advanced-algebra/{folder}/index.md")
    dirs = sorted([d for d in (ROOT / folder).iterdir() if d.is_dir()],
                  key=lambda p: p.name)
    for d in dirs:
        title = d.name.replace("-", " · ", 1)
        base = f"maththeory/advanced-algebra/{folder}/{d.name}"
        # 模块作为一个二级分组：讲义 + 习题集
        lines.append(f"              - {title}:")
        if (d / "讲义.md").exists():
            lines.append(f"                  - 讲义: {base}/讲义.md")
        if (d / "习题集.md").exists():
            lines.append(f"                  - 习题集: {base}/习题集.md")

# 尾部固定项
lines.append("  - 随笔: blog/index.md")
lines.append("  - 关于: about.md")

print("\n".join(lines))
