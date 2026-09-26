# -*- coding: utf-8 -*-
"""
修复 Markdown 误把矩阵方括号 [[A,B],[0,C]] 当作链接的问题。

现象：mkdocs 日志出现
  contains an unrecognized relative link '坐标交换', it was left as is.

原因：形如 [[A,B],[0,C]] 的文本触发 Markdown 链接语法 [text](url)。

处理：把这种「矩阵字面量」用反引号包裹成行内代码，既消除歧义又保持可读。
      只处理明确是矩阵形态的（连续的 [数字/字母/逗号/分号/负号] 组），
      不动正文里真正的链接。
用法：python _fix_brackets.py [--dry-run]
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")
DRY = "--dry-run" in sys.argv

# 矩阵字面量：[[...],[...]] 或 [[...],[...],[...]]
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
    for i, s in enumerate(store):
        text = text.replace(f"\x00CODE{i}\x00", s)
    return text


def fix_file(path: Path):
    text = path.read_text(encoding="utf-8")
    protected, store = protect(text)

    count = 0

    def repl(m):
        nonlocal count
        count += 1
        return f"`{m.group(0)}`"

    new = MATRIX_LITERAL.sub(repl, protected)
    new = restore(new, store)

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
