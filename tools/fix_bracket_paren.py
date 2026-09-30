# -*- coding: utf-8 -*-
"""
fix_bracket_paren.py · 修复方括号+圆括号被误判为链接（零基础自学版）
====================================================================
【问题】
  Markdown 的链接语法是 [文字](地址)。
  但数学表达式里也经常出现 [xxx](yyy) 的形式，比如：
      [(0.5-0.5+1)/1.5](0.5,-0.5,1)
      [(T-μI)-(T-λI)](T-μI)⁻¹
  Markdown 会把它们误判成链接，导致渲染错误。

【与 fix_matrix_brackets.py 的区别】
  那个处理「矩阵字面量」[[a,b],[c,d]]（用反引号包裹）；
  这个处理「方括号后紧跟圆括号」的算式。

【方案】
  只转义开头的 [ 为 \[ ，改动最小、不影响排版。
  转义后 Markdown 就不会把它当成链接了。

【怎么用】
  试运行：.venv\Scripts\python.exe tools/fix_bracket_paren.py --dry-run
  执行：  .venv\Scripts\python.exe tools/fix_bracket_paren.py
====================================================================
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")
DRY = "--dry-run" in sys.argv

# ============================================================
# 正则表达式
# ============================================================

# 匹配所有 [xxx](yyy) 形式
# 分组：([^\]\n]{1,160}) = 方括号内的文字（1-160字符，不含]和换行）
#       ([^()\n]{0,200})  = 圆括号内的地址（0-200字符，不含()和换行）
BAD_LINK = re.compile(
    r"\[([^\]\n]{1,160})\]"
    r"\(([^()\n]{0,200})\)"
)

# 合法链接目标的特征（用来判断是不是真链接）
LINK_TARGET = re.compile(
    r"^\s*(https?://|#|/|\.{1,2}/)"          # 外链 / 锚点 / 绝对路径 / 相对路径
    r"|.*\.(md|html|png|jpg|jpeg|pdf|svg)\s*$"  # 文档或图片文件
)


def is_real_link(target: str) -> bool:
    """判断圆括号里的内容是不是合法的链接目标"""
    return bool(LINK_TARGET.match(target))


# 行内代码的正则（反引号包裹的内容，里面的 [xxx](yyy) 不需要处理）
INLINE_CODE = re.compile(r"`[^`]*`")


def fix(text: str):
    """
    修复一段文本。
    返回：(修复后的文本, 修复了多少处)
    """
    store = []  # 保存被替换掉的行内代码

    def protect(m):
        """把行内代码替换成占位符，避免误改"""
        store.append(m.group(0))
        return f"\x00C{len(store)-1}\x00"

    # 第一步：保护行内代码（替换成占位符）
    t = INLINE_CODE.sub(protect, text)

    count = 0

    def repl(m):
        """替换函数：判断是不是真链接，不是就转义"""
        nonlocal count
        inner = m.group(1)   # 方括号内的文字
        target = m.group(2)  # 圆括号内的内容
        # 真链接保持原样
        if is_real_link(target):
            return m.group(0)
        # 假链接（数学表达式）：转义开头的 [
        count += 1
        return f"\\[{inner}]({target})"

    # 第二步：替换所有假链接
    t = BAD_LINK.sub(repl, t)

    # 第三步：恢复行内代码
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
