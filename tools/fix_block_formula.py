# -*- coding: utf-8 -*-
"""
fix_block_formula.py · 修复块级公式识别问题（零基础自学版）
====================================================================
【问题】
  Markdown 里写 $$...$$ 公式时，如果公式行有缩进（比如在列表项里），
  pymdownx.arithmatex 扩展无法识别为块级公式，
  会退化为行内公式并残留 $$ 字面量（页面上显示 $$ 符号）。

【方案】
  把缩进的「单行 $$...$$」改写成「顶格三行块级」：
      原来：  $$x + y = 1$$
      改成：  $$
             x + y = 1
             $$

【怎么用】
  试运行（只看会改什么，不实际写入）：
    .venv\Scripts\python.exe tools/fix_block_formula.py --dry-run
  实际执行：
    .venv\Scripts\python.exe tools/fix_block_formula.py

【注意】
  只处理高等代数目录下的 .md 文件。
====================================================================
"""
import re           # 正则表达式
import sys          # 系统参数（用来读 --dry-run）
from pathlib import Path

# 高等代数源代码目录
ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")
# 是否试运行模式（--dry-run 参数）
DRY = "--dry-run" in sys.argv

# ============================================================
# 正则表达式模式
# ============================================================

# 匹配：行首缩进 + $$ + 内容 + $$ + 可能的尾随字符
# 例如："  $$x + y = 1$$"
# 分组：(\s+) = 缩进，(.+?) = 公式内容，(.*) = 尾随字符
SINGLE_LINE = re.compile(r"^(\s+)\$\$(.+?)\$\$\s*(.*)$")

# 匹配：行首缩进 + 纯 $$（只有定界符，没有内容）
# 例如："  $$"
PURE_DELIM = re.compile(r"^(\s+)\$\$\s*$")


def fix_text(text: str):
    """
    修复一段文本中的块级公式。

    参数：text = 原始文本
    返回：(修复后的文本, 修复了多少处)
    """
    lines = text.split("\n")  # 按行拆分
    out = []                  # 输出行列表
    fixed = 0                 # 修复计数

    for idx, line in enumerate(lines):
        stripped = line.strip()  # 去掉首尾空白后的内容

        # ---- 情况 A：纯定界符行（有缩进的 $$）→ 顶格，前后补空行 ----
        m = PURE_DELIM.match(line)
        if m and stripped == "$$":
            # 如果上一行不是空行，先补一个空行（公式前后需要空行）
            if out and out[-1].strip() != "":
                out.append("")
            out.append("$$")  # 顶格写 $$
            fixed += 1
            continue

        # ---- 情况 B：单行 $$...$$（有缩进）→ 拆成顶格三行 ----
        m = SINGLE_LINE.match(line)
        if m:
            indent = m.group(1)    # 缩进（不用，因为要顶格）
            body = m.group(2).strip()   # 公式内容
            trailing = m.group(3).strip()  # 尾随字符

            # 前面补空行
            if out and out[-1].strip() != "":
                out.append("")
            # 三行格式：$$ / 内容 / $$
            out.append("$$")
            out.append(body)
            out.append("$$")
            # 如果有尾随字符，另起一行
            if trailing:
                out.append(trailing)
            fixed += 1
            continue

        # ---- 其他行：原样保留 ----
        out.append(line)

    return "\n".join(out), fixed


def main():
    """主函数：扫描所有文件并修复"""
    # 递归查找所有 .md 文件
    files = sorted(ROOT.rglob("*.md"))
    total_fixed = 0
    changed = []

    for f in files:
        text = f.read_text(encoding="utf-8")
        new_text, n = fix_text(text)
        if n:
            total_fixed += n
            changed.append((f, n))
            # 非试运行模式才写入
            if not DRY:
                f.write_text(new_text, encoding="utf-8")

    # 输出结果
    mode = "[试运行]" if DRY else "[已写入]"
    print(f"{mode} 扫描 {len(files)} 个文件")
    print(f"{mode} 修复 {len(changed)} 个文件，共 {total_fixed} 处\n")
    for f, n in changed:
        print(f"  {n:>3} 处  {f.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
