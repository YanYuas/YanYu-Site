# -*- coding: utf-8 -*-
"""
check_site.py · 全站验收工具（零基础自学版）
====================================================================
【这个脚本是干什么的】
  运行 mkdocs build 生成网站后，用这个脚本检查网站有没有问题：
    1. 页面总数统计
    2. 高等代数题库题量检查（每模块应该32题）
    3. 讲义完整性检查（每篇应该超过8000字符、3个以上二级标题）
    4. 内链可用性检查（有没有点了404的链接）
    5. 公式渲染健康度检查（有没有 $$ 没被正确转换）

【怎么用】
  先构建网站：.venv\Scripts\python.exe -m mkdocs build
  再运行验收：.venv\Scripts\python.exe tools\check_site.py

【注意】
  脚本里的路径是硬编码的绝对路径（D:\YanYuas\YanYu-Site\...）。
  如果项目挪了位置，需要修改下面的 SITE 和 AA_DOCS 变量。
====================================================================
"""

# re：正则表达式库，用来在文本里搜索特定模式
import re
# urllib.parse：URL 处理库，用来解码 %XX 这样的转义字符
import urllib.parse
# pathlib.Path：Python 3.4+ 的面向对象路径处理，比 os.path 好用
from pathlib import Path

# ============================================================
# 配置区：路径和常量
# ============================================================

# 构建后的网站目录（mkdocs build 的输出目录）
SITE = Path(r"D:\YanYuas\YanYu-Site\site")
# 高等代数在构建后网站里的路径
AA_SITE = SITE / "maththeory" / "advanced-algebra"
# 高等代数在源代码 docs/ 里的路径（用来检查讲义字数和题量）
AA_DOCS = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")

# 已知「规划中」的链接：作者有意保留、目标页面尚未创建。
# 不算故障，验收时单独归到「规划中」而不是「失效」。
# 建好对应页面后，把它的代号从这行删掉即可。
PLANNED_MARKERS = (
    "02_EEMCM",   # 电工杯（目录存在但内容还没写）
    "03_HSMCM",   # 华数杯
    "04_CUMCM",   # 高教社杯
    "05_APMCM",   # 亚太杯
)

# ============================================================
# 开始验收
# ============================================================

# 打印分隔线和标题
print("=" * 70)
print("全站验收")
print("=" * 70)

# ----------------------------------------------------------
# 【1】页面总数统计
# ----------------------------------------------------------
# rglob("index.html") = 递归查找所有子目录里的 index.html
# sorted() = 按路径排序，输出更整齐
pages = sorted(SITE.rglob("index.html"))
# 高等代数板块的页面
aa_pages = sorted(AA_SITE.rglob("index.html"))
# 讲义页面：父目录名叫"讲义"的那些
lectures = [p for p in aa_pages if p.parent.name == "讲义"]
# 习题集页面：父目录名叫"习题集"的那些
exercises = [p for p in aa_pages if p.parent.name == "习题集"]

print(f"\n【1】站点页面总数：{len(pages)}")
print(f"    高等代数板块：{len(aa_pages)}")
print(f"      讲义 {len(lectures)} · 习题集 {len(exercises)} · 其他 {len(aa_pages)-len(lectures)-len(exercises)}")

# ----------------------------------------------------------
# 【2】题库题量检查
# ----------------------------------------------------------
# 每本习题集应该有32道题（A层8 + B层8 + C层8 + D层8）
# 题目用 "**【" 开头标记（比如 **【A1】**）
print(f"\n【2】题库题量")
total_q = 0       # 总题数
bad = []          # 题数不对的模块列表

# 遍历所有习题集.md文件
for f in sorted(AA_DOCS.rglob("习题集.md")):
    t = f.read_text(encoding="utf-8")   # 读取文件内容（UTF-8编码）
    n = t.count("**【")                  # 数有多少个题目标记
    total_q += n                         # 累加到总数
    if n != 32:                          # 如果不是32题，记录下来
        bad.append((f.parent.name, n))

print(f"  21 个模块合计：{total_q} 题")
if bad:
    # 有模块题数不对，列出来
    for m, n in bad:
        print(f"    !! {m} = {n} 题（非 32）")
else:
    print("  [OK] 每模块 32 题")

# ----------------------------------------------------------
# 【3】讲义完整性检查
# ----------------------------------------------------------
# 每篇讲义应该超过8000字符，且有3个以上二级标题（## 开头）
print(f"\n【3】讲义完整性")
short = []            # 不达标讲义列表
lect_files = sorted(AA_DOCS.rglob("讲义.md"))
total_chars = 0       # 总字符数

for f in lect_files:
    t = f.read_text(encoding="utf-8")
    total_chars += len(t)
    # re.findall(r"^## ", t, re.M) = 找所有以 "## " 开头的行（二级标题）
    # re.M = MULTILINE 模式，让 ^ 匹配每一行的开头
    h2 = len(re.findall(r"^## ", t, re.M))
    h3 = len(re.findall(r"^### ", t, re.M))
    # 少于8000字符 或 少于3个二级标题 = 不达标
    if len(t) < 8000 or h2 < 3:
        short.append((f.parent.name, len(t), h2, h3))

print(f"  {len(lect_files)} 篇讲义，总字符：{total_chars:,}")
if short:
    for m, l, a, b in short:
        print(f"    !! {m}: {l} 字符, {a} 个 h2, {b} 个 h3")
else:
    print("  [OK] 每篇均超过 8000 字符且含 3 个以上二级标题")

# ----------------------------------------------------------
# 【4】内链可用性检查
# ----------------------------------------------------------
# 遍历所有HTML页面，找出所有 href 链接，检查目标文件是否存在
print(f"\n【4】内链可用性")
broken = []     # 失效链接列表
planned = []    # 规划中链接列表
checked = 0     # 已检查链接数

for p in pages:
    html = p.read_text(encoding="utf-8")
    # 正则找出所有 href="..." 里的链接地址
    for href in re.findall(r'href="([^"]+)"', html):
        # 外链、锚点、协议链接不查（这些不是本站内链）
        if href.startswith(("http://", "https://", "#", "mailto:", "data:", "javascript:")):
            continue

        # 注意：MkDocs 默认用「目录式 URL」，内链长这样 ../../xx/ 或 /xx/
        # 不是 xx.html。所以必须去掉 %XX 转义、补 index.html，否则一条都匹配不到。
        # unquote = 把 %E7%BA%BF%E6%80%A7 解码成"线性"
        # split("#")[0] = 去掉锚点部分（#后面的）
        # split("?")[0] = 去掉查询参数（?后面的）
        path = urllib.parse.unquote(href.split("#")[0].split("?")[0])
        if not path:
            continue
        checked += 1

        # 判断链接是绝对路径（/开头）还是相对路径
        base = SITE if path.startswith("/") else p.parent
        # resolve() = 解析成绝对路径（处理 ../ 等）
        target = (base / path.lstrip("/")).resolve()

        # 目录式 URL → 落到 index.html
        # 如果路径没有后缀名（比如 /mathmodel/），就当成目录，找里面的 index.html
        if not target.suffix:
            target = target / "index.html"

        # 检查目标文件是否存在
        if not target.exists():
            rel = p.relative_to(SITE)  # 当前页面的相对路径（用于报错显示）
            # 如果链接里包含规划中的标记，归到"规划中"而不是"失效"
            if any(m in path for m in PLANNED_MARKERS):
                planned.append((rel, href))
            else:
                broken.append((rel, href))

if broken:
    print(f"  [!] {len(broken)} 条失效内链（共检查 {checked} 条）")
    # 最多显示前8条，避免输出太长
    for rel, href in broken[:8]:
        print(f"    {rel.parent} -> {href}")
else:
    print(f"  [OK] 无失效内链（共检查 {checked} 条）")

if planned:
    print(f"  [规划中] {len(planned)} 条指向尚未创建的页面（作者有意保留）")
    for rel, href in planned:
        print(f"    {rel.parent} -> {href}")
    print("    → 建好页面后，把代号从脚本顶部的 PLANNED_MARKERS 删掉")

# ----------------------------------------------------------
# 【5】公式渲染健康度检查
# ----------------------------------------------------------
# 检查高等代数页面里的公式是否都被 arithmatex 正确转换了
# 正常情况：$$ 应该被转成 class="arithmatex" 的元素
# 如果页面里还有裸露的 $$，说明 arithmatex 没识别到，需要 MathJax 兜底
print(f"\n【5】公式渲染健康度")
pending = []     # 需要 MathJax 兜底的页面
ok_total = 0     # 已正确转换的公式数

for p in aa_pages:
    html = p.read_text(encoding="utf-8")
    # 提取 <article> 标签内的内容（正文区域）
    m = re.search(r"<article[^>]*>(.*?)</article>", html, re.S)
    if not m:
        continue
    body = m.group(1)
    # 去掉代码块里的内容（代码里的 $$ 不是公式）
    # re.sub(r"<(code|pre)[^>]*>.*?</\1>", "", body, flags=re.S)
    body = re.sub(r"<(code|pre)[^>]*>.*?</\1>", "", body, flags=re.S)
    # 数还有多少个裸露的 $$
    dd = len(re.findall(r"\$\$", body))
    # 数有多少个已转换的公式（class="arithmatex"）
    ok = len(re.findall(r'class="arithmatex"', body))
    ok_total += ok
    if dd:
        pending.append((p.relative_to(AA_SITE), dd, ok))

print(f"  arithmatex 已转换公式：{ok_total} 处")
if pending:
    print(f"  由 MathJax 原生 $$ 兜底的页面：{len(pending)}")
    # 按 $$ 数量排序，最多显示前6个
    for rel, dd, ok in sorted(pending, key=lambda x: -x[1])[:6]:
        print(f"    {dd:>3} 处 $$（已转 {ok:>3}）  {rel.parent}")
    print("    → 已配置 MathJax displayMath 含 $$，可正常渲染")
else:
    print("  [OK] 全部由 arithmatex 转换")

# 打印结束分隔线
print("\n" + "=" * 70)
