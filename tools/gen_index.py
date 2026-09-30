# -*- coding: utf-8 -*-
"""
gen_index.py · 生成高等代数索引页（零基础自学版）
====================================================================
【这个脚本是干什么的】
  自动生成高等代数的4个索引页：
    1. 总览页（advanced-algebra/index.md）
    2. 领域一导览（matrix-basis/index.md）
    3. 领域二导览（linear-space/index.md）
    4. 领域三导览（linear-transform/index.md）

  每个索引页包含一个模块清单表格，列出所有模块的"讲义"和"习题集"链接。

【为什么需要这个脚本】
  高等代数有21个模块，每个模块有讲义和习题集两篇。
  手动维护索引页很容易漏写或写错链接。
  这个脚本自动扫描目录、生成表格，保证索引和实际文件一致。

【怎么用】
  .venv\Scripts\python.exe tools\gen_index.py
  运行后会覆盖写入4个 index.md 文件。

【注意】
  脚本里的路径是硬编码的绝对路径。如果项目挪了位置，需要修改 ROOT 变量。
====================================================================
"""
from pathlib import Path

# 高等代数源代码目录
ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")

# ============================================================
# 三个领域的配置
# 格式：(目录名, 显示名, 模块前缀, 领域介绍)
# ============================================================
DOMAINS = [
    ("matrix-basis", "领域一 · 矩阵与基", "F",
     "从坐标与基底出发，处理「对象的具体计算与结构分类」。"
     "这个领域的答案都是**可算的**——每个概念最终都能落到具体数字上。"),
    ("linear-space", "领域二 · 线性空间", "G",
     "如果说领域一关心「怎么算」，这个领域关心「在什么舞台上算」。"
     "这里把向量空间从具体的 Rⁿ 解放出来，研究它的骨架、度量与各种构造。"),
    ("linear-transform", "领域三 · 线性变换", "T",
     "前两个领域分别处理「怎么算」和「在什么舞台上」，这个领域处理「映射本身」。"
     "视角从矩阵转向**算子**，研究变换作用在空间上留下的不变量。"),
]

# ============================================================
# 每个模块的一句话锚定（从讲义副标题/内容提炼）
# 用于在索引表格里显示"这个模块是讲什么的"
# ============================================================
ANCHOR = {
    "F1": "高等代数几何视域的第一把钥匙",
    "F2": "复合变换的代数语言",
    "F3": "有向体积的代数",
    "F4": "不变方向上的伸缩因子",
    "F5": "换基视角下的变换等价类",
    "F6": "亏损矩阵的终极分类",
    "F7": "几何变换的因式分解",
    "G1": "公理化空间观",
    "G2": "舞台的骨架与标尺",
    "G3": "骨架的度量与垂直",
    "G4": "折叠的舞台与等价类",
    "G5": "欧几里得几何的代数翻译",
    "G6": "无原点的几何与点向量分离",
    "G7": "对称矩阵的合同分类与二次曲面",
    "T1": "空间之间的保持结构映射",
    "T2": "变换的内在几何结构",
    "T3": "同构与线性变换空间",
    "T4": "从不变子空间到谱的几何",
    "T5": "从判据到正规算子的谱分解",
    "T6": "从广义特征空间到 Jordan 链",
    "T7": "从投影幂等到矩阵指数的几何全景",
}


def mod_rows(folder, prefix, relative=False):
    """
    生成一个领域的模块表格行（Markdown 表格格式）。

    参数：
      folder   : 领域目录名（如 "matrix-basis"）
      prefix   : 模块前缀（如 "F"）
      relative : True  = 路径相对领域导览页自身（不含 folder 前缀）
                 False = 路径相对高等代数总览页（含 folder 前缀）

    返回：多行 Markdown 表格行字符串
    """
    rows = []
    # 扫描领域目录下的所有子目录（每个子目录是一个模块）
    # sorted 按名称排序，保证 F1 在 F2 前面
    dirs = sorted([d for d in (ROOT / folder).iterdir() if d.is_dir()],
                  key=lambda p: p.name)

    for d in dirs:
        # 模块代号：目录名第一个 "-" 前面的部分（如 "F1"）
        code = d.name.split("-")[0]
        # 模块标题：第一个 "-" 后面的部分（如 "基底与坐标"）
        title = d.name.split("-", 1)[1]
        # 一句话锚定（从 ANCHOR 字典里取，没有就空字符串）
        anchor = ANCHOR.get(code, "")
        # 基础路径：relative=True 时只用目录名，False 时加上领域目录
        base = d.name if relative else f"{folder}/{d.name}"

        # 收集这个模块有的内容链接
        cells = []
        if (d / "讲义.md").exists():
            cells.append(f"[讲义]({base}/讲义.md)")
        if (d / "习题集.md").exists():
            cells.append(f"[习题集]({base}/习题集.md)")
        # 用 " · " 连接多个链接，没有就显示 "—"
        links = " · ".join(cells) if cells else "—"

        # 拼成一行 Markdown 表格：| 代号 | 标题 | 锚定 | 链接 |
        rows.append(f"| **{code}** | {title} | {anchor} | {links} |")

    return "\n".join(rows)


# 表格头部（Markdown 表格的第一行和分隔行）
TABLE_HEAD = "| 模块 | 标题 | 一句话几何锚定 | 内容 |\n|---|---|---|---|"


def build_domain(folder, label, prefix, intro):
    """
    生成一个领域导览页的完整内容。

    参数：
      folder : 领域目录名
      label  : 显示名（如 "领域一 · 矩阵与基"）
      prefix : 模块前缀（如 "F"）
      intro  : 领域介绍文字

    返回：完整的 Markdown 字符串
    """
    # 生成模块表格行（relative=True，因为导览页自己就在领域目录下）
    rows = mod_rows(folder, prefix, relative=True)
    return f"""# {label}

> {intro}

---

## 模块清单

{TABLE_HEAD}
{rows}

---

[← 返回高等代数总览](index.md)
"""


def main():
    """主函数：生成4个索引页"""
    written = []

    # ---- 生成三个领域导览页 ----
    for folder, label, prefix, intro in DOMAINS:
        content = build_domain(folder, label, prefix, intro)
        p = ROOT / folder / "index.md"
        p.write_text(content, encoding="utf-8")  # 写入文件（UTF-8编码）
        written.append(f"OK {folder}/index.md")

    # ---- 生成高等代数总览页 ----
    parts = []
    # 页面头部：标题 + 引用 + 三领域架构说明
    parts.append("""# 高等代数

> 以几何为锚定的高等代数知识体系：三个相对独立的领域，各含七个模块，
> 共 21 个模块。每个模块配一份**讲义**（理论正文）与一份**习题集**（32 题精编）。

---

## 这套体系怎么组织的

高等代数长期受困于「形式化」与「几何直观」之间的张力。这里的处理办法是
**几何统摄的三领域架构**——把高等代数的几何部分拆成三个各自闭环的领域，
让矩阵、空间、变换三条线索既独立成线，又能被后期缝合。

每个领域都以**几何锚定**为主线、以**七个模块**为骨架。像秩、特征值、内积、
行列式、分解这类交叉主题，会在不同领域以不同视角反复出现——这是有意设计的，
不是重复。

| 领域 | 代号 | 关注的问题 | 模块数 |
|---|---|---|---|
| **矩阵与基** | F1–F7 | 对象的具体计算与结构分类 | 7 |
| **线性空间** | G1–G7 | 舞台本身是什么，如何描述 | 7 |
| **线性变换** | T1–T7 | 结构保持映射的不变性质 | 7 |
""")

    # 每个领域的详细模块清单
    for folder, label, prefix, intro in DOMAINS:
        rng = f"{prefix}1–{prefix}7"  # 模块范围，如 "F1–F7"
        parts.append(f"\n### {label}（{rng}）\n")
        parts.append(intro.replace("**", "") + "\n")  # 去掉粗体标记
        parts.append(TABLE_HEAD)
        parts.append(mod_rows(folder, prefix))  # relative=False，路径含领域目录
        parts.append("")

    # 页面尾部：模块说明 + 方法论链接
    parts.append("""---

## 每个模块有什么

- **讲义**：模块的研究正文。含研究摘要、核心指标、分节论述、实物验证、
  耦合索引与反例边界。讲「这个概念在几何上是什么」。
- **习题集**：32 道精编习题，按 A（计算与直观）→ B（证明与推理）→
  C（综合与联系）→ D（研究级）四层递进，每层内 ★ / ★★ / ★★★ 三级难度。
  每题附完整解答、对应知识点与耦合方向。

建议读法：先通读讲义建立几何直觉，再做习题集的 A 层建立手感，
遇到卡点回查讲义对应章节，最后推进 B/C/D 层。

---

## 方法论与研究

三领域架构背后的设计逻辑、以及对「五阶充要图谱」学习法的批判性诊断，
整理为以下文档：

- [几何统摄与充要图谱：学术论文](theory/几何统摄与充要图谱-学术论文.md)
  —— 三领域架构的设计论证与文献对话
- [充要图谱方法论 v2](theory/充要图谱方法论-v2.md)
  —— 条目模板、命题类型化与理解深度分级规范
- [从初等几何到公理化演进](theory/从初等几何到公理化演进.md)
  —— 四百年演进的深度研究报告
""")

    # 写入总览页
    (ROOT / "index.md").write_text("\n".join(parts), encoding="utf-8")
    written.append("OK index.md")

    # 打印结果
    print(f"已生成 {len(written)} 个索引页：")
    for w in written:
        print("  ", w)


# Python 脚本入口：只有直接运行这个文件时才执行 main()
# 如果被其他文件 import，则不执行
if __name__ == "__main__":
    main()
