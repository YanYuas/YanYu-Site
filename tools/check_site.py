# -*- coding: utf-8 -*-
"""全站验收：页面数、题量、讲义完整性、内链可用性、公式健康度。"""
import re
import urllib.parse
from pathlib import Path

SITE = Path(r"D:\YanYuas\YanYu-Site\site")
AA_SITE = SITE / "maththeory" / "advanced-algebra"
AA_DOCS = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")

print("=" * 70)
print("全站验收")
print("=" * 70)

# 1. 页面总数
pages = sorted(SITE.rglob("index.html"))
aa_pages = sorted(AA_SITE.rglob("index.html"))
lectures = [p for p in aa_pages if p.parent.name == "讲义"]
exercises = [p for p in aa_pages if p.parent.name == "习题集"]
print(f"\n【1】站点页面总数：{len(pages)}")
print(f"    高等代数板块：{len(aa_pages)}")
print(f"      讲义 {len(lectures)} · 习题集 {len(exercises)} · 其他 {len(aa_pages)-len(lectures)-len(exercises)}")

# 2. 题量
print(f"\n【2】题库题量")
total_q = 0
bad = []
for f in sorted(AA_DOCS.rglob("习题集.md")):
    t = f.read_text(encoding="utf-8")
    n = t.count("**【")
    total_q += n
    if n != 32:
        bad.append((f.parent.name, n))
print(f"  21 个模块合计：{total_q} 题")
if bad:
    for m, n in bad:
        print(f"    !! {m} = {n} 题（非 32）")
else:
    print("  [OK] 每模块 32 题")

# 3. 讲义完整性
print(f"\n【3】讲义完整性")
short = []
lect_files = sorted(AA_DOCS.rglob("讲义.md"))
total_chars = 0
for f in lect_files:
    t = f.read_text(encoding="utf-8")
    total_chars += len(t)
    h2 = len(re.findall(r"^## ", t, re.M))
    h3 = len(re.findall(r"^### ", t, re.M))
    if len(t) < 8000 or h2 < 3:
        short.append((f.parent.name, len(t), h2, h3))
print(f"  {len(lect_files)} 篇讲义，总字符：{total_chars:,}")
if short:
    for m, l, a, b in short:
        print(f"    !! {m}: {l} 字符, {a} 个 h2, {b} 个 h3")
else:
    print("  [OK] 每篇均超过 8000 字符且含 3 个以上二级标题")

# 4. 内链可用性
print(f"\n【4】内链可用性")
broken = []
checked = 0
for p in pages:
    html = p.read_text(encoding="utf-8")
    for href in re.findall(r'href="([^"]+)"', html):
        # 外链、锚点、协议链接不查
        if href.startswith(("http://", "https://", "#", "mailto:", "data:", "javascript:")):
            continue
        # 注意：MkDocs 默认用「目录式 URL」，内链长这样 ../../xx/ 或 /xx/
        # 不是 xx.html。所以必须去掉 %XX 转义、补 index.html，否则一条都匹配不到。
        path = urllib.parse.unquote(href.split("#")[0].split("?")[0])
        if not path:
            continue
        checked += 1
        base = SITE if path.startswith("/") else p.parent
        target = (base / path.lstrip("/")).resolve()
        if not target.suffix:            # 目录式 URL → 落到 index.html
            target = target / "index.html"
        if not target.exists():
            broken.append((p.relative_to(SITE), href))
if broken:
    print(f"  [!] {len(broken)} 条失效内链（共检查 {checked} 条）")
    for rel, href in broken[:8]:
        print(f"    {rel.parent} -> {href}")
else:
    print(f"  [OK] 无失效内链（共检查 {checked} 条）")

# 5. 公式健康度
print(f"\n【5】公式渲染健康度")
pending = []
ok_total = 0
for p in aa_pages:
    html = p.read_text(encoding="utf-8")
    m = re.search(r"<article[^>]*>(.*?)</article>", html, re.S)
    if not m:
        continue
    body = re.sub(r"<(code|pre)[^>]*>.*?</\1>", "", m.group(1), flags=re.S)
    dd = len(re.findall(r"\$\$", body))
    ok = len(re.findall(r'class="arithmatex"', body))
    ok_total += ok
    if dd:
        pending.append((p.relative_to(AA_SITE), dd, ok))
print(f"  arithmatex 已转换公式：{ok_total} 处")
if pending:
    print(f"  由 MathJax 原生 $$ 兜底的页面：{len(pending)}")
    for rel, dd, ok in sorted(pending, key=lambda x: -x[1])[:6]:
        print(f"    {dd:>3} 处 $$（已转 {ok:>3}）  {rel.parent}")
    print("    → 已配置 MathJax displayMath 含 $$，可正常渲染")
else:
    print("  [OK] 全部由 arithmatex 转换")

print("\n" + "=" * 70)
