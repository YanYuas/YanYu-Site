#!/usr/bin/env python3
"""MkDocs -> Astro/Starlight content migration.

Run from the `astro/` directory:
    ..\\.venv\\Scripts\\python.exe scripts/migrate-docs.py

It is intentionally idempotent: existing generated content is replaced,
while the custom home (`index.mdx`) and custom lab (`.../lab.mdx`) are kept.
"""

from __future__ import annotations

import json
import posixpath
import re
import shutil
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT.parent / "docs"
TARGET = ROOT / "src" / "content" / "docs"
SITE_BASE = "/YanYu-Site"

EXCLUDE = {
    "index.md",  # custom Astro home
    "maththeory/analytic-geometry/lab.md",  # custom Vue lab
}
PRESERVE = {
    "index.mdx",
    "maththeory/analytic-geometry/lab.mdx",
}

ADMONITION_TYPES = {
    "info": "note",
    "note": "note",
    "tip": "tip",
    "hint": "tip",
    "warning": "caution",
    "caution": "caution",
    "danger": "danger",
    "example": "note",
    "abstract": "note",
    "success": "tip",
    "question": "note",
    "quote": "note",
}


def slug(segment: str) -> str:
    # Astro/Starlight strips periods from content slugs (e.g. `01.随机` -> `01随机`).
    return segment.lower().replace(" ", "-").replace(".", "")


def route_for_rel(rel: str) -> str:
    parts = list(PurePosixPath(rel).with_suffix("").parts)
    if parts and parts[-1] == "index":
        parts = parts[:-1]
    slugged = "/".join(slug(p) for p in parts)
    return "/" + (slugged + "/" if slugged else "")


def old_url_for_rel(rel: str) -> str:
    parts = list(PurePosixPath(rel).with_suffix("").parts)
    if parts and parts[-1] == "index":
        parts = parts[:-1]
    path = "/".join(parts)
    return "/" + (path + "/" if path else "")


def split_frontmatter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[4:end], text[end + 4 :]
    return "", text


def make_frontmatter(front: str, title: str) -> str:
    if re.search(r"(?m)^title\s*:", front):
        return front
    quoted = json.dumps(title, ensure_ascii=False)
    return f"title: {quoted}\n" + front


def first_heading(body: str) -> tuple[str | None, str]:
    lines = body.splitlines()
    fence = False
    for i, line in enumerate(lines):
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            title = re.sub(r"[`*_]", "", m.group(1)).strip()
            return title, "\n".join(lines[:i] + lines[i + 1 :])
    return None, body


def convert_admonitions(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    fence = False
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
            out.append(line)
            i += 1
            continue
        if fence:
            out.append(line)
            i += 1
            continue

        m = re.match(r'^(\s*)!!!\s+(\w+)(?:\s+"([^"]*)")?\s*:?\s*$', line)
        if not m:
            out.append(line)
            i += 1
            continue

        base_indent = len(m.group(1))
        kind = ADMONITION_TYPES.get(m.group(2).lower(), "note")
        title = m.group(3) or ""
        i += 1

        # Find first non-blank line to decide indented vs. unindented content.
        j = i
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        indented = j < len(lines) and len(lines[j]) - len(lines[j].lstrip(" ")) >= base_indent + 4

        content: list[str] = []
        if indented:
            while i < len(lines):
                cur = lines[i]
                if cur.strip() == "":
                    content.append("")
                    i += 1
                    continue
                cur_indent = len(cur) - len(cur.lstrip(" "))
                if cur_indent < base_indent + 4:
                    break
                content.append(cur[base_indent + 4 :])
                i += 1
        else:
            # G1/T* "模块信息" style: unindented bullets until a blank line.
            while i < len(lines) and lines[i].strip() != "":
                content.append(lines[i])
                i += 1

        while content and content[-1] == "":
            content.pop()
        while content and content[0] == "":
            content.pop(0)

        header = f":::{kind}"
        if title:
            header += f"[{title}]"
        out.append(header)
        out.extend(content)
        out.append(":::")
        out.append("")
        continue

    return "\n".join(out)


def convert_cards(text: str) -> str:
    pattern = re.compile(r'<div class="grid cards" markdown>\s*(.*?)\s*</div>', re.S)
    item_re = re.compile(
        r"^-?\s*:material-[^:]+:\{[^}]*\}\s+__(.+?)__\s*$|^-?\s*__(.+?)__\s*$",
        re.M,
    )

    def one(block: str) -> str:
        chunks = re.split(r"\n(?=-   :material-|\n-   __)", block)
        cards = []
        for chunk in chunks:
            m = item_re.search(chunk)
            if not m:
                continue
            title = (m.group(1) or m.group(2) or "").strip()
            link_m = re.search(r"\[([^\]]+)\]\(([^)]+)\)", chunk)
            href = link_m.group(2).strip() if link_m else ""
            desc_lines = []
            for raw in chunk.splitlines():
                s = raw.strip()
                if not s or s == "---" or s.startswith("-") or re.match(r"^:material-", s):
                    continue
                if s.startswith("[") and "](" in s:
                    continue
                desc_lines.append(s)
            desc = " ".join(desc_lines).strip()
            if href:
                cards.append(
                    f'<a class="card" href="{href}"><strong>{title}</strong><span>{desc}</span></a>'
                )
            else:
                cards.append(f'<div class="card"><strong>{title}</strong><span>{desc}</span></div>')
        if not cards:
            return block
        return '<div class="card-grid">\n' + "\n".join(cards) + "\n</div>"

    return pattern.sub(lambda m: one(m.group(1)), text)


def load_source_index() -> tuple[list[str], dict[str, str]]:
    files = sorted(
        p.relative_to(DOCS).as_posix()
        for p in DOCS.rglob("*.md")
        if p.relative_to(DOCS).as_posix() not in {"_archive"}
        and "_archive" not in p.parts
    )
    rel_to_route = {rel: route_for_rel(rel) for rel in files}
    # custom lab route (source lab is excluded from copying but links must resolve)
    rel_to_route["maththeory/analytic-geometry/lab.md"] = "/maththeory/analytic-geometry/lab/"
    return files, rel_to_route


def find_target(path: str, rel_to_route: dict[str, str]) -> tuple[str, str] | None:
    path = unquote(path).lstrip("/")
    path = posixpath.normpath(path)
    if path == ".":
        path = "index.md"
    candidates = [path]
    if not path.endswith(".md"):
        candidates += [path + ".md", path + "/index.md"]
    if path.endswith("/"):
        candidates.append(path + "index.md")
    for cand in candidates:
        cand = cand.replace("\\", "/")
        while "/./" in cand:
            cand = cand.replace("/./", "/")
        if cand in rel_to_route:
            return cand, rel_to_route[cand]
    return None


def map_asset(path: str, source_rel: str) -> str | None:
    raw = unquote(path).lstrip("/")
    if raw.startswith("assets/"):
        rel = raw[len("assets/") :]
        if (DOCS / "assets" / rel).exists():
            return f"{SITE_BASE}/assets/{rel}"
    if path.startswith("/"):
        return None
    rel = (PurePosixPath(source_rel).parent / raw)
    norm = PurePosixPath(*[p for p in rel.parts if p not in ("..", ".")])
    # resolve .. properly
    stack: list[str] = []
    for part in rel.parts:
        if part == "..":
            if stack:
                stack.pop()
        elif part != ".":
            stack.append(part)
    norm = PurePosixPath(*stack)
    if norm.parts and norm.parts[0] == "assets":
        candidate = DOCS.joinpath(*norm.parts)
        if candidate.exists():
            return f"{SITE_BASE}/" + "/".join(norm.parts)
    return None


def rewrite_links(text: str, source_rel: str, rel_to_route: dict[str, str]) -> str:
    def internal(url: str) -> str:
        if not url:
            return url
        if re.match(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//|#)", url):
            return url
        if url.startswith(SITE_BASE + "/") or url == SITE_BASE:
            return url
        path, _, anchor = url.partition("#")
        path, _, query = path.partition("?")
        suffix = ("#" + anchor if anchor else "") + ("?" + query if query else "")
        if not path:
            return url

        if path.startswith("/"):
            found = find_target(path, rel_to_route)
        else:
            joined = (PurePosixPath(source_rel).parent / path).as_posix()
            found = find_target(joined, rel_to_route)
        if found:
            return f"{SITE_BASE}{found[1]}{suffix}"
        if path.startswith("/") and not path.startswith(SITE_BASE):
            return f"{SITE_BASE}{path}{suffix}"
        return url

    def asset(url: str) -> str:
        if not url or re.match(r"^(?:https?:|data:|//|#)", url):
            return url
        mapped = map_asset(url, source_rel)
        return mapped or url

    out: list[str] = []
    fence = False
    for line in text.splitlines():
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
            out.append(line)
            continue
        if fence:
            out.append(line)
            continue

        # Markdown links/images
        def md_repl(m: re.Match[str]) -> str:
            prefix, url, close = m.group(1), m.group(2), m.group(3)
            if prefix.startswith("!"):
                return prefix + asset(url) + close
            return prefix + internal(url) + close

        line = re.sub(r"(!?\[[^\]]*\]\()([^)]+)(\))", md_repl, line)

        def attr_repl(m: re.Match[str]) -> str:
            name, quote, url = m.group(1), m.group(2), m.group(3)
            if name == "src":
                return f'{name}={quote}{asset(url)}{quote}'
            return f'{name}={quote}{internal(url)}{quote}'

        line = re.sub(r'(href|src)=("|\')([^"\']+)\2', attr_repl, line)
        out.append(line)
    return "\n".join(out)


def process_file(rel: str, rel_to_route: dict[str, str]) -> str:
    raw = (DOCS / rel).read_text(encoding="utf-8-sig")
    front, body = split_frontmatter(raw)
    heading, body = first_heading(body)
    title = heading or PurePosixPath(rel).stem
    front = make_frontmatter(front, title)
    body = convert_admonitions(body)
    body = convert_cards(body)
    body = rewrite_links(body, rel, rel_to_route)
    body = body.lstrip("\n")
    return f"---\n{front.rstrip()}\n---\n\n{body.rstrip()}\n"


def clean_target() -> None:
    for p in TARGET.rglob("*"):
        if p.is_file() and p.relative_to(TARGET).as_posix() not in PRESERVE:
            p.unlink()
    for p in sorted(TARGET.rglob("*"), key=lambda x: len(x.parts), reverse=True):
        if p.is_dir():
            try:
                p.rmdir()
            except OSError:
                pass


def copy_assets() -> None:
    src = DOCS / "assets"
    dst = ROOT / "public" / "assets"
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)


def yaml_config() -> dict:
    class Loader(yaml.SafeLoader):
        pass

    Loader.add_multi_constructor(
        "tag:yaml.org,2002:python/name:", lambda loader, suffix, node: None
    )
    with (ROOT.parent / "mkdocs.yml").open(encoding="utf-8") as f:
        return yaml.load(f, Loader=Loader)


def generate_sidebar(rel_to_route: dict[str, str]) -> None:
    cfg = yaml_config()
    nav = cfg.get("nav") or []

    def convert(items: list, depth: int = 0) -> list[dict]:
        result = []
        for item in items:
            if isinstance(item, str):
                route = rel_to_route.get(item) or route_for_rel(item)
                result.append({"label": PurePosixPath(item).stem, "link": route})
                continue
            if not isinstance(item, dict):
                continue
            for label, value in item.items():
                if isinstance(value, str):
                    route = rel_to_route.get(value) or route_for_rel(value)
                    result.append({"label": str(label), "link": route})
                elif isinstance(value, list):
                    children = convert(value, depth + 1)
                    group = {"label": str(label), "items": children}
                    if depth >= 1 and len(children) >= 3:
                        group["collapsed"] = True
                    result.append(group)
        return result

    sidebar = []
    for item in nav:
        if isinstance(item, dict):
            for label, value in item.items():
                if isinstance(value, str):
                    route = rel_to_route.get(value) or route_for_rel(value)
                    sidebar.append({"label": str(label), "link": route})
                elif isinstance(value, list):
                    sidebar.append({"label": str(label), "items": convert(value)})
    out = ROOT / "src" / "data" / "sidebar.generated.mjs"
    out.write_text(
        "// Generated by scripts/migrate-docs.py from mkdocs.yml nav.\n"
        "export default " + json.dumps(sidebar, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )


def generate_redirects(files: list[str], rel_to_route: dict[str, str]) -> None:
    def with_base(route: str) -> str:
        return route if route.startswith(SITE_BASE + "/") or route == SITE_BASE else SITE_BASE + route

    redirects: dict[str, str] = {}
    for rel in files:
        old = old_url_for_rel(rel)
        new = rel_to_route[rel]
        if old != new:
            redirects[old] = with_base(new)

    cfg = yaml_config()
    for plugin in cfg.get("plugins", []):
        if isinstance(plugin, dict) and "redirects" in plugin:
            maps = (plugin["redirects"] or {}).get("redirect_maps") or {}
            for old_md, new_md in maps.items():
                old_route = old_url_for_rel(old_md)
                new_route = rel_to_route.get(new_md) or route_for_rel(new_md)
                if old_route != new_route:
                    redirects[old_route] = with_base(new_route)
    out = ROOT / "src" / "data" / "redirects.generated.mjs"
    out.write_text(
        "// Generated by scripts/migrate-docs.py from MkDocs URLs/redirects.\n"
        "export default " + json.dumps(redirects, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )


def main() -> None:
    files, rel_to_route = load_source_index()
    clean_target()
    count = 0
    for rel in files:
        if rel in EXCLUDE:
            continue
        target = TARGET / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(process_file(rel, rel_to_route), encoding="utf-8")
        count += 1

    copy_assets()
    generate_sidebar(rel_to_route)
    generate_redirects(files, rel_to_route)
    print(f"migrated {count} files")
    print(f"sidebar entries: {len(rel_to_route)} routes")


if __name__ == "__main__":
    main()
