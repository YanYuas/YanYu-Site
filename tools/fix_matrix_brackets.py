# -*- coding: utf-8 -*-
"""
fix_matrix_brackets.py · 修复矩阵方括号被误判为链接（零基础自学版）
====================================================================
【问题】
  Markdown 里写矩阵字面量 [[A,B],[0,C]] 时，
  会触发 Markdown 链接语法 [text](url)，导致：
    - mkdocs 日志出现 "contains an unrecognized relative link" 警告
    - 矩阵显示异常

【方案】
  把这种「矩阵字面量」用反引号包裹成行内代码，既消除歧义又保持可读。
  只处理明确是矩阵形态的（连续的 [数字/字母/逗号/分号/负号] 组），
  不动正文里真正的链接。

【怎么用】
  试运行：.venv\Scripts\python.exe tools/fix_matrix_brackets.py --dry-run
  执行：  .venv\Scripts\python.exe tools/fix_matrix_brackets.py
====================================================================
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")
DRY = "--dry-run" in sys.argv

# 矩阵字面量：[[...],[...]] 或 [[...],[...],[...]]
# 匹配两组或更多组方括号，里面是数字、字母、逗号、分号、正负号、空格
MATRIX_LITERAL = re.compile(
    r"\[\[[0-9A-Za-z\-\+\.,;\s]*\](?:,\s*\[[0-9A-Za-z\-\+\.,;\s]*\])+\]"
)

# 已在反引号内的不处理
INLINE_CODE = re.compile(r"`[^`]*`")


def protect(text: str):
    """把行内代码段替换为占位符，避免误改。"""
    store = []

    def repl(m):
        store.append(m.group(0))
        return f"\x00CODE{len(store) - 1}\x00"

    return INLINE_CODE.sub(repl, text), store


def restore(text: str, store):
    """把占位符恢复成原来的行内代码"""
    for i, s in enumerate(store):
        text = text.replace(f"\x00CODE{i}\x00", s)
    return text


def fix_file(path: Path):
    """修复单个文件"""
    text = path.read_text(encoding="utf-8")
    # 先保护行内代码
    protected, store = protect(text)

    count = 0

    def repl(m):
        nonlocal count
        count += 1
        # 用反引号包裹矩阵字面量
        return f"`{m.group(0)}`"

    # 替换所有矩阵字面量
    new = MATRIX_LITERAL.sub(repl, protected)
    # 恢复行内代码
    new = restore(new, store)

    # 非试运行模式才写入
    if count and not DRY:
        path.write_text(new, encoding="utf-8")
    return count


def main():
    files = sorted(ROOT.rglob("*.md"))
    total = 0
    changed = []
    for f in files:
        n = fix_file(f)
        if n:
            total += n
            changed.append((f, n))
    mode = "[试运行]" if DRY else "[已写入]"
    print(f"{mode} 处理 {len(changed)} 个文件，共 {total} 处矩阵字面量")
    for f, n in changed:
        print(f"  {n:>3} 处  {f.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
