# -*- coding: utf-8 -*-
"""
rename_page.py · 页面/目录改名时自动同步所有引用（零基础自学版）
====================================================================
【它解决什么问题】
  以前改一个目录名，要手动同步好几处：
    - mkdocs.yml 的 nav
    - 各页面里指向它的 Markdown 链接
    - 旧 URL 的 redirect 映射
    - README 里的路径说明
  漏掉任何一处，站内就会出现 404，或者导航指向不存在的文件。
  这个脚本把「移动 + 改链接 + 改 nav + 加 redirect」一次做完。

【用法】
  试运行（只打印计划，不改文件）：
    .venv\\Scripts\\python.exe tools/rename_page.py OLD NEW --dry-run

  真正执行：
    .venv\\Scripts\\python.exe tools/rename_page.py OLD NEW

  OLD / NEW 可以写：
    docs/mathmodel/works/xxx/index.md
    mathmodel/works/xxx/index.md        （省略 docs/ 也行）
  也支持整个目录：
    tools/rename_page.py mathmodel/works/old-dir mathmodel/works/new-dir

  可选参数：
    --no-redirect   不自动写 mkdocs.yml 的 redirect_maps
    --build         改完后立刻跑 mkdocs build --strict 验证
    --dry-run       只显示会发生什么，不动文件

【注意】
  - 脚本假设仓库在 Git 管理下；已跟踪文件用 git mv，未跟踪文件直接移动。
  - 只处理 docs/ 下的 Markdown 链接和 mkdocs.yml nav；外部链接、锚点不动。
  - 改名后旧 URL 会由 mkdocs-redirects 生成跳转页（如果启用了该插件）。
====================================================================
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"

# Markdown 行内链接/图片：[文字](路径) 或 ![描述](路径)
MD_LINK = re.compile(r"(!?\[[^\]]*\]\()(\s*)([^)\s]+)(\s*\))")
# HTML 里的 href/src="路径"
HTML_LINK = re.compile(r'(\b(?:href|src)=["\'])([^"\']+)(["\'])')
# 代码块和行内代码：里面的“链接”不处理
FENCED = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")

SKIP_PREFIX = ("http://", "https://", "#", "mailto:", "data:", "javascript:", "tel:")


def resolve_docs(arg: str) -> Path:
    """把命令行参数解析成 docs/ 下的绝对路径。"""
    p = Path(arg)
    if p.is_absolute():
        return p.resolve()
    if p.parts and p.parts[0] == "docs":
        return (ROOT / p).resolve()
    return (DOCS / p).resolve()


def docs_rel(p: Path) -> str:
    return p.relative_to(DOCS).as_posix()


def should_skip(target: str) -> bool:
    return target.startswith(SKIP_PREFIX) or target.startswith("/") or target.startswith("<")


def split_suffix(target: str) -> tuple[str, str]:
    m = re.match(r"^([^#?]*)(.*)$", target)
    return m.group(1), m.group(2)


def rewrite_target(target: str, src_parent: Path, old_abs: Path, new_abs: Path) -> str | None:
    """如果 target 指向 old_abs，返回指向 new_abs 的相对路径（保留 #锚点 / ?查询）。"""
    if should_skip(target):
        return None
    path, suffix = split_suffix(target)
    if not path:
        return None
    resolved = (src_parent / path).resolve()
    if resolved != old_abs:
        return None
    new_rel = os.path.relpath(new_abs, src_parent).replace(os.sep, "/")
    return new_rel + suffix


def mask_code(text: str) -> tuple[str, list[str]]:
    """把代码块/行内代码替换成占位符，避免改到示例代码。"""
    store: list[str] = []

    def repl(m: re.Match) -> str:
        store.append(m.group(0))
        return f"\x00CODE{len(store) - 1}\x00"

    text = FENCED.sub(repl, text)
    text = INLINE.sub(repl, text)
    return text, store


def unmask_code(text: str, store: list[str]) -> str:
    for i, s in enumerate(store):
        text = text.replace(f"\x00CODE{i}\x00", s)
    return text


def update_text(text: str, src_parent: Path, mapping: list[tuple[Path, Path]]) -> tuple[str, int]:
    """更新一段文本里的链接，返回 (新文本, 改动数)。"""
    text, store = mask_code(text)
    count = 0

    for old_abs, new_abs in mapping:
        def repl_md(m: re.Match) -> str:
            nonlocal count
            new_target = rewrite_target(m.group(3), src_parent, old_abs, new_abs)
            if new_target is None:
                return m.group(0)
            count += 1
            return m.group(1) + m.group(2) + new_target + m.group(4)

        def repl_html(m: re.Match) -> str:
            nonlocal count
            new_target = rewrite_target(m.group(2), src_parent, old_abs, new_abs)
            if new_target is None:
                return m.group(0)
            count += 1
            return m.group(1) + new_target + m.group(3)

        text = MD_LINK.sub(repl_md, text)
        text = HTML_LINK.sub(repl_html, text)

    text = unmask_code(text, store)
    return text, count


def move_path(old: Path, new: Path, dry: bool) -> None:
    """优先 git mv（保留 Git 历史），失败则普通移动。"""
    if dry:
        print(f"  [dry-run] 移动：{old.relative_to(ROOT)} -> {new.relative_to(ROOT)}")
        return

    old_rel = str(old.relative_to(ROOT))
    new_rel = str(new.relative_to(ROOT))
    result = subprocess.run(["git", "mv", old_rel, new_rel], cwd=ROOT,
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [git mv 失败，改用普通移动] {result.stderr.strip()}")
        new.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old), str(new))
    else:
        print(f"  已移动：{old_rel} -> {new_rel}")


def update_nav(old_rel: str, new_rel: str, dry: bool) -> bool:
    """更新 mkdocs.yml 里的 nav 路径。"""
    text = MKDOCS.read_text(encoding="utf-8")
    if old_rel not in text:
        return False
    new_text = text.replace(old_rel, new_rel)
    if not dry:
        MKDOCS.write_text(new_text, encoding="utf-8")
    print(f"  nav 已更新：{old_rel} -> {new_rel}")
    return True


def add_redirect(old_rel: str, new_rel: str, dry: bool) -> None:
    """往 mkdocs.yml 的 redirect_maps 里加一行（如果插件存在）。"""
    text = MKDOCS.read_text(encoding="utf-8")
    if "redirect_maps:" not in text:
        print("  [提示] mkdocs.yml 里没有 redirect_maps，跳过自动重定向")
        return

    entry = f"        '{old_rel}': '{new_rel}'"
    if entry in text:
        print(f"  redirect 已存在：{old_rel}")
        return
    if dry:
        print(f"  [dry-run] 新增 redirect：{entry.strip()}")
        return

    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "redirect_maps:":
            lines.insert(i + 1, entry)
            break
    MKDOCS.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  redirect 已新增：{old_rel} -> {new_rel}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="改名/移动页面，并自动同步 Markdown 链接、mkdocs nav、redirects"
    )
    parser.add_argument("old", help="旧路径（相对 docs/ 或写 docs/...）")
    parser.add_argument("new", help="新路径（相对 docs/ 或写 docs/...）")
    parser.add_argument("--dry-run", action="store_true", help="只打印计划，不改文件")
    parser.add_argument("--no-redirect", action="store_true", help="不自动添加 redirect_maps")
    parser.add_argument("--build", action="store_true", help="改完立即运行 mkdocs build --strict")
    args = parser.parse_args()

    old = resolve_docs(args.old)
    new = resolve_docs(args.new)

    if not old.exists():
        print(f"[FAIL] 找不到旧路径：{old}")
        return 1
    if new.exists():
        print(f"[FAIL] 新路径已存在：{new}")
        return 1
    if not old.is_relative_to(DOCS) or not new.is_relative_to(DOCS):
        print("[FAIL] 只处理 docs/ 目录内的文件")
        return 1

    # ---------- 1. 计算要移动的文件清单 ----------
    if old.is_dir():
        old_files = sorted(old.rglob("*.md"))
        if not old_files:
            print(f"[FAIL] 目录里没有 .md 文件：{old}")
            return 1
        mapping = [
            (f, new / f.relative_to(old))
            for f in old_files
        ]
    else:
        mapping = [(old, new)]

    print(f"计划移动 {len(mapping)} 个文件：")
    for o, n in mapping:
        print(f"  {docs_rel(o)} -> {docs_rel(n)}")

    # ---------- 2. 移动 ----------
    move_path(old, new, args.dry_run)

    # ---------- 3. 更新链接 ----------
    changed_files = 0
    total_links = 0
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        new_text, count = update_text(text, md.parent, mapping)
        if count:
            changed_files += 1
            total_links += count
            if not args.dry_run:
                md.write_text(new_text, encoding="utf-8")
            print(f"  {'[dry-run] ' if args.dry_run else ''}改链接 {count} 处：{docs_rel(md)}")

    # ---------- 4. 更新 nav + redirect ----------
    for o, n in mapping:
        old_rel, new_rel = docs_rel(o), docs_rel(n)
        update_nav(old_rel, new_rel, args.dry_run)
        if not args.no_redirect:
            add_redirect(old_rel, new_rel, args.dry_run)

    # ---------- 5. 提示 ----------
    print(f"\n完成：{len(mapping)} 个文件移动，{changed_files} 个文件共 {total_links} 条链接更新")
    if args.dry_run:
        print("这是 dry-run，没有写入任何文件。去掉 --dry-run 才会真正执行。")
    else:
        print("下一步建议：")
        print("  1. 检查 git diff，确认改动符合预期")
        print("  2. 跑 mkdocs build --strict（或加 --build 参数）")

    # ---------- 6. 可选构建 ----------
    if args.build and not args.dry_run:
        print("\n开始 mkdocs build --strict ...")
        result = subprocess.run([sys.executable, "-m", "mkdocs", "build", "--clean", "--strict"], cwd=ROOT)
        if result.returncode != 0:
            print("[FAIL] 构建未通过，请检查上面的警告")
            return result.returncode

    return 0


if __name__ == "__main__":
    sys.exit(main())
