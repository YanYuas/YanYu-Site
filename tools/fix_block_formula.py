# -*- coding: utf-8 -*-
"""
修复 arithmatex 块级公式识别失败问题。

问题：md 中 $$...$$ 缩进在列表项续行时，arithmatex 无法识别为块级公式，
      会退化为行内公式并残留 $$ 字面量。

方案：把缩进的「单行 $$...$$」改写成「顶格三行块级」：
        $$...$$        ->      $$
                               内容
                               $$

用法：python _fix_formula.py [--dry-run]
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")
DRY = "--dry-run" in sys.argv

# 匹配：行首缩进 + $$ + 内容 + $$ + 可能的尾随字符
SINGLE_LINE = re.compile(r"^(\s+)\$\$(.+?)\$\$\s*(.*)$")
PURE_DELIM = re.compile(r"^(\s+)\$\$\s*$")


def fix_text(text: str):
    lines = text.split("\n")
    out = []
    fixed = 0

    for idx, line in enumerate(lines):
        stripped = line.strip()

        # A. 纯定界符行（有缩进）→ 顶格，前后补空行
        m = PURE_DELIM.match(line)
        if m and stripped == "$$":
            if out and out[-1].strip() != "":
                out.append("")
            out.append("$$")
            fixed += 1
            continue

        # B. 单行 $$...$$ （有缩进）→ 拆成顶格三行
        m = SINGLE_LINE.match(line)
        if m:
            indent, body, trailing = m.group(1), m.group(2).strip(), m.group(3).strip()
            if out and out[-1].strip() != "":
                out.append("")
            out.append("$$")
            out.append(body)
            out.append("$$")
            if trailing:
                out.append(trailing)
            fixed += 1
            continue

        out.append(line)

    return "\n".join(out), fixed


def main():
    files = sorted(ROOT.rglob("*.md"))
    total_fixed = 0
    changed = []

    for f in files:
        text = f.read_text(encoding="utf-8")
        new_text, n = fix_text(text)
        if n:
            total_fixed += n
            changed.append((f, n))
            if not DRY:
                f.write_text(new_text, encoding="utf-8")

    mode = "[试运行]" if DRY else "[已写入]"
    print(f"{mode} 扫描 {len(files)} 个文件")
    print(f"{mode} 修复 {len(changed)} 个文件，共 {total_fixed} 处\n")
    for f, n in changed:
        print(f"  {n:>3} 处  {f.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
