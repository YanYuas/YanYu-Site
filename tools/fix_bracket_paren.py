# -*- coding: utf-8 -*-
"""
修复 Markdown 把数学表达式 [xxx](yyy) 误判为链接的问题。

与 fix_matrix_brackets.py 的区别：
  那个处理「矩阵字面量」[[a,b],[c,d]]（用反引号包裹）；
  这个处理「方括号后紧跟圆括号」的算式，如
      [(0.5-0.5+1)/1.5](0.5,-0.5,1)
      [(T-μI)-(T-λI)](T-μI)⁻¹
  Markdown 会把它们解析成 [text](url) 链接。
  这里只转义开头的 [ 为 \[ ，改动最小、不影响排版。

用法：python tools/fix_bracket_paren.py [--dry-run]
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")
DRY = "--dry-run" in sys.argv

# 先匹配所有 [xxx](yyy)，再在替换函数里判断 yyy 是否为合法链接目标。
# （不能在正则里用负向预查排除：本地路径含中文，字符类匹配不上会误判）
BAD_LINK = re.compile(
    r"\[([^\]\n]{1,160})\]"
    r"\(([^()\n]{0,200})\)"
)

# 合法链接目标的特征
LINK_TARGET = re.compile(
    r"^\s*(https?://|#|/|\.{1,2}/)"          # 外链 / 锚点 / 绝对路径
    r"|.*\.(md|html|png|jpg|jpeg|pdf|svg)\s*$"  # 文档或图片
)


def is_real_link(target: str) -> bool:
    return bool(LINK_TARGET.match(target))

INLINE_CODE = re.compile(r"`[^`]*`")


def fix(text: str):
    store = []

    def protect(m):
        store.append(m.group(0))
        return f"\x00C{len(store)-1}\x00"

    t = INLINE_CODE.sub(protect, text)

    count = 0

    def repl(m):
        nonlocal count
        inner, target = m.group(1), m.group(2)
        # 真链接保持原样
        if is_real_link(target):
            return m.group(0)
        count += 1
        return f"\\[{inner}]({target})"

    t = BAD_LINK.sub(repl, t)

    for i, s in enumerate(store):
        t = t.replace(f"\x00C{i}\x00", s)
    return t, count


def main():
    files = sorted(ROOT.rglob("*.md"))
    total = 0
    changed = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        new, n = fix(text)
        if n:
            total += n
            changed.append((f, n))
            if not DRY:
                f.write_text(new, encoding="utf-8")
    mode = "[试运行]" if DRY else "[已写入]"
    print(f"{mode} {len(changed)} 个文件，{total} 处")
    for f, n in changed:
        print(f"  {n:>3} 处  {f.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
