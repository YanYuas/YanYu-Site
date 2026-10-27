# -*- coding: utf-8 -*-
"""
check_site.py · 全站验收工具（零基础自学版）
====================================================================
【这个脚本是干什么的】
  运行 mkdocs build 生成网站后，用这个脚本检查网站有没有问题：
    1. 页面总数统计
    2. 高等代数题库题量检查（每模块应该 32 题）
    3. 讲义完整性检查（每篇应该超过 8000 字符、3 个以上二级标题）
    4. 内链可用性检查（有没有点了 404 的链接）
    5. 公式渲染健康度检查（有没有 $$ 没被正确转换）
    6. 近空页面提示（占位页，只提示不判失败）

【怎么用】
  先构建网站：.venv\\Scripts\\python.exe -m mkdocs build
  再运行验收：.venv\\Scripts\\python.exe tools\\check_site.py

【退出码】
  0 = 通过；1 = 有硬性问题（坏链 / 题量不对 / 讲义过短 / 站点未构建）。
  GitHub Actions 的部署流程会跑这个脚本，不通过就不发布。

【注意】
  路径按脚本所在位置推导，不再写死 D:\\YanYuas\\...，换电脑也能用。
====================================================================
"""
import re
import sys
import urllib.parse
from pathlib import Path

# ============================================================
# 配置区：路径和常量
# ============================================================

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"                     # 构建产物
AA_SITE = SITE / "maththeory" / "advanced-algebra"
AA_DOCS = ROOT / "docs" / "maththeory" / "advanced-algebra"
DOCS = ROOT / "docs"

# 已知「规划中」的链接：作者有意保留、目标页面尚未创建。
# 现在作品页都已建好，若以后又有占位链接，把对应路径片段加到这里即可。
PLANNED_MARKERS = ()

problems = []       # 硬性问题，最后决定退出码


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


# ============================================================
# 开始验收
# ============================================================

print("=" * 70)
print("全站验收")
print("=" * 70)

if not SITE.exists():
    print(f"\n[FAIL] 找不到构建产物：{SITE}")
    print("       请先运行：.venv\\Scripts\\python.exe -m mkdocs build --clean")
    sys.exit(1)

# ----------------------------------------------------------
# 【1】页面总数统计
# ----------------------------------------------------------
pages = sorted(SITE.rglob("index.html"))
aa_pages = sorted(AA_SITE.rglob("index.html"))
lectures = [p for p in aa_pages if p.parent.name == "讲义"]
exercises = [p for p in aa_pages if p.parent.name == "习题集"]

print(f"\n【1】站点页面总数：{len(pages)}")
print(f"    高等代数板块：{len(aa_pages)}")
print(f"      讲义 {len(lectures)} · 习题集 {len(exercises)} · 其他 {len(aa_pages) - len(lectures) - len(exercises)}")

# ----------------------------------------------------------
# 【2】题库题量检查
# ----------------------------------------------------------
print("\n【2】题库题量")
total_q = 0
bad = []
for f in sorted(AA_DOCS.rglob("习题集.md")):
    t = read(f)
    n = t.count("**【")
    total_q += n
    if n != 32:
        bad.append((f.parent.name, n))
        problems.append(f"题量异常：{f.parent.name} = {n} 题（应为 32）")

print(f"  21 个模块合计：{total_q} 题")
if bad:
    for m, n in bad:
        print(f"    !! {m} = {n} 题（非 32）")
else:
    print("  [OK] 每模块 32 题")

# ----------------------------------------------------------
# 【3】讲义完整性检查
# ----------------------------------------------------------
print("\n【3】讲义完整性")
short = []
lect_files = sorted(AA_DOCS.rglob("讲义.md"))
total_chars = 0

for f in lect_files:
    t = read(f)
    total_chars += len(t)
    h2 = len(re.findall(r"^## ", t, re.M))
    h3 = len(re.findall(r"^### ", t, re.M))
    if len(t) < 8000 or h2 < 3:
        short.append((f.parent.name, len(t), h2, h3))
        problems.append(f"讲义过短：{f.parent.name}（{len(t)} 字符, {h2} 个 h2）")

print(f"  {len(lect_files)} 篇讲义，总字符：{total_chars:,}")
if short:
    for m, length, a, b in short:
        print(f"    !! {m}: {length} 字符, {a} 个 h2, {b} 个 h3")
else:
    print("  [OK] 每篇均超过 8000 字符且含 3 个以上二级标题")

# ----------------------------------------------------------
# 【4】内链可用性检查
# ----------------------------------------------------------
print("\n【4】内链可用性")
broken = []
checked = 0

for p in pages:
    html = read(p)
    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith(("http://", "https://", "#", "mailto:", "data:", "javascript:", "tel:")):
            continue

        path = urllib.parse.unquote(href.split("#")[0].split("?")[0])
        if not path:
            continue
        checked += 1

        base = SITE if path.startswith("/") else p.parent
        target = (base / path.lstrip("/")).resolve()
        if not target.suffix:
            target = target / "index.html"

        if not target.exists():
            rel = p.relative_to(SITE)
            if any(m in path for m in PLANNED_MARKERS):
                continue
            broken.append((rel, href))
            problems.append(f"坏链：{rel.parent} -> {href}")

if broken:
    print(f"  [!] {len(broken)} 条失效内链（共检查 {checked} 条）")
    for rel, href in broken[:10]:
        print(f"    {rel.parent} -> {href}")
else:
    print(f"  [OK] 无失效内链（共检查 {checked} 条）")

# ----------------------------------------------------------
# 【5】公式渲染健康度检查
# ----------------------------------------------------------
print("\n【5】公式渲染健康度")
pending = []
ok_total = 0

for p in aa_pages:
    html = read(p)
    m = re.search(r"<article[^>]*>(.*?)</article>", html, re.S)
    if not m:
        continue
    body = m.group(1)
    body = re.sub(r"<(code|pre)[^>]*>.*?</\1>", "", body, flags=re.S)
    dd = len(re.findall(r"\$\$", body))
    ok = len(re.findall(r'class="arithmatex"', body))
    ok_total += ok
    if dd:
        pending.append((p.relative_to(AA_SITE), dd, ok))

print(f"  arithmatex 已转换公式：{ok_total:,} 处")
if pending:
    print(f"  由 MathJax 原生 $$ 兜底的页面：{len(pending)}")
    for rel, dd, ok in sorted(pending, key=lambda x: -x[1])[:6]:
        print(f"    {dd:>3} 处 $$（已转 {ok:>3}）  {rel.parent}")
    print("    → 已配置 MathJax displayMath 含 $$，可正常渲染")
else:
    print("  [OK] 全部由 arithmatex 转换")

# ----------------------------------------------------------
# 【6】近空页面提示（只提示，不判失败）
# ----------------------------------------------------------
print("\n【6】近空页面（占位页提示）")
near_empty = []
for f in sorted(DOCS.rglob("*.md")):
    n = len(read(f))
    if n < 200:
        near_empty.append((n, f.relative_to(DOCS).as_posix()))
if near_empty:
    for n, rel in near_empty:
        print(f"    {n:>6} 字符  {rel}")
    print("    → 如果是故意保留的占位页，可以忽略；否则补内容或先移出 nav")
else:
    print("  [OK] 没有近空页面")

# ----------------------------------------------------------
# 结果
# ----------------------------------------------------------
print("\n" + "=" * 70)
if problems:
    print(f"验收未通过：{len(problems)} 个硬性问题")
    for msg in problems[:20]:
        print(f"  - {msg}")
    print("=" * 70)
    sys.exit(1)
else:
    print("验收通过：没有发现硬性问题")
    print("=" * 70)
    sys.exit(0)
