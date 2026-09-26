# -*- coding: utf-8 -*-
"""
把奶油糖果风的讲义 HTML 转换为干净的 Markdown。

源：学术研究/领域X-YYY/<代号>-<名称>-奶油糖果风.html
目标：docs/maththeory/advanced-algebra/<领域目录>/<代号>-<名称>/讲义.md

HTML 组件 → Markdown 的映射：
  <header class="hero"> h1/sub/meta  →  YAML 无 / 标题 + 引用
  nav.toc                            →  丢弃（站点自带目录）
  section > .sec-head > h2           →  ## 标题
  .abstract-box > p                  →  普通段落
  .kpi-grid                          →  三列表格
  .card > .ct / .cd                  →  ### 小标题 + 段落
  .callout mint|sky|butter           →  !!! tip / !!! note / !!! warning
  table.tbl                          →  Markdown 表格
  <b>                                →  **粗体**
  <br>                               →  换行

注意：这些 HTML 的公式全部用 Unicode 数学字符书写（无 $、无 LaTeX），
      因此直接保留文本即可，不涉及公式定界符转换。

用法：python tools/html2md.py [--dry-run]
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SRC_ROOT = Path(r"C:\Users\21722\Desktop\YanYuas\MathematicalLearning\AdvancedAlgebra\学术研究")
DST_ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")

# 领域目录映射
DOMAIN_DIR = {
    "领域一-矩阵与基": "matrix-basis",
    "领域二-线性空间": "linear-space",
    "领域三-线性变换": "linear-transform",
}

DRY = "--dry-run" in sys.argv


class DocParser(HTMLParser):
    """把 HTML 正文转成 Markdown 行列表。"""

    SKIP_TAGS = {"script", "style", "svg", "nav", "button", "head"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []            # 输出行
        self.buf = []            # 当前行内缓冲
        # 跳过机制：记录每个「被跳过子树」的根节点在 stack 中的索引。
        # 只有当结束标签回到该索引时，才结束跳过。
        # （不能用简单计数器——子树内部每个结束标签都会误减计数）
        self.skip_frames = []
        self.in_h1 = False
        self.in_h2 = False
        self.in_h3 = False
        self.bold = 0
        self.table_rows = []     # 表格收集
        self.in_table = False
        self.in_td = False
        self.td_buf = []
        self.cell_is_head = False
        self.stack = []          # 元素栈（tag, class）
        self.kpi_buf = []        # KPI 卡片
        self.in_kpi = False
        self.in_kpi_label = False
        self.in_kpi_num = False
        self.in_kpi_delta = False
        self.callout_depth = 0
        self.callout_kind = ""
        self.in_card_title = False
        self.in_code = False

    # ---- 工具 ----
    def flush_line(self):
        text = "".join(self.buf).strip()
        self.buf = []
        if text:
            self.out.append(text)

    def emit(self, line):
        self.out.append(line)

    def blank(self):
        if self.out and self.out[-1] != "":
            self.out.append("")

    # ---- 标签处理 ----
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        classes = set(cls.split())

        # 需要整体跳过的子树：script/style/svg/nav/button/head，
        # 以及纯装饰性的 span（章节编号 .num、小圆点 .dot）
        need_skip = (
            tag in self.SKIP_TAGS
            or (tag == "span" and (classes & {"num", "dot"}))
        )
        if need_skip:
            self.skip_frames.append(len(self.stack))
            self.stack.append((tag, classes))
            return
        if self.skip_frames:
            self.stack.append((tag, classes))
            return

        if tag == "h1":
            self.flush_line()
            self.blank()
            self.in_h1 = True
        elif tag == "h2":
            self.flush_line()
            self.blank()
            self.in_h2 = True
        elif tag == "h3":
            self.flush_line()
            self.blank()
            self.in_h3 = True
        elif tag == "b" or tag == "strong":
            self.bold += 1
            self.buf.append("**")
        elif tag == "br":
            self.buf.append(" ")
        elif tag == "p":
            self.flush_line()
            if "cd" in classes:
                pass
        elif tag == "div":
            if "kpi-grid" in classes:
                self.kpi_buf = []
                self.in_kpi = True
            elif "kpi-card" in classes:
                self.kpi_buf.append({})
            elif "kpi-label" in classes:
                self.in_kpi_label = True
            elif "kpi-num" in classes:
                self.in_kpi_num = True
            elif "kpi-delta" in classes:
                self.in_kpi_delta = True
            elif "callout" in classes:
                self.flush_line()
                self.blank()
                if "mint" in classes:
                    self.callout_kind = "tip"
                elif "butter" in classes:
                    self.callout_kind = "warning"
                else:
                    self.callout_kind = "note"
                self.callout_depth = 1
            elif "ct" in classes:
                self.flush_line()
                self.blank()
                self.in_card_title = True
            elif "sec-head" in classes:
                self.flush_line()
        elif tag == "table" or "tbl" in classes:
            if tag == "table":
                self.flush_line()
                self.blank()
                self.in_table = True
                self.table_rows = []
        elif tag == "tr":
            if self.in_table:
                self.table_rows.append([])
        elif tag in ("td", "th"):
            self.in_td = True
            self.td_buf = []
            self.cell_is_head = tag == "th"
        elif tag == "span":
            if "num" in classes:
                pass  # sec-head 里的编号标签，忽略
        elif tag == "code" or tag == "pre":
            self.in_code = True

        self.stack.append((tag, classes))

    def handle_endtag(self, tag):
        if not self.stack:
            return
        # 找到对应的开始标签在 stack 中的位置
        k = None
        for idx in range(len(self.stack) - 1, -1, -1):
            if self.stack[idx][0] == tag:
                k = idx
                classes = self.stack[idx][1]
                break
        if k is None:
            return

        # 若这个结束标签正是「被跳过子树」的根节点，结束跳过并直接返回
        if self.skip_frames:
            if k == self.skip_frames[-1]:
                self.skip_frames.pop()
                del self.stack[k:]
                return
            # 子树内部的结束标签：仅维护栈，不产生输出
            del self.stack[k:]
            return

        del self.stack[k:]

        if tag == "h1":
            title = "".join(self.buf).strip()
            self.buf = []
            self.in_h1 = False
            if title:
                self.emit(f"# {title}")
                self.emit("")
        elif tag == "h2":
            title = "".join(self.buf).strip()
            self.buf = []
            self.in_h2 = False
            if title:
                self.emit(f"## {title}")
                self.emit("")
        elif tag == "h3":
            title = "".join(self.buf).strip()
            self.buf = []
            self.in_h3 = False
            if title:
                self.emit(f"### {title}")
                self.emit("")
        elif tag in ("b", "strong"):
            self.bold = max(0, self.bold - 1)
            self.buf.append("**")
        elif tag == "p":
            self.flush_line()
            if self.callout_depth:
                pass
            self.emit("")
        elif tag == "div":
            if "kpi-grid" in classes:
                self.in_kpi = False
                self.render_kpi()
            elif "kpi-label" in classes:
                self.in_kpi_label = False
            elif "kpi-num" in classes:
                self.in_kpi_num = False
            elif "kpi-delta" in classes:
                self.in_kpi_delta = False
            elif "callout" in classes:
                self.render_callout()
                self.callout_depth = 0
            elif "ct" in classes:
                # 卡片标题 -> ### 小标题
                t = "".join(self.buf).strip()
                self.buf = []
                self.in_card_title = False
                if t:
                    t = re.sub(r"^\s*[·•]\s*", "", t)
                    self.emit(f"### {t}")
                    self.emit("")
            elif "cd" in classes:
                self.flush_line()
                self.emit("")
        elif tag == "table":
            if self.in_table:
                self.render_table()
                self.in_table = False
        elif tag in ("td", "th"):
            self.in_td = False
            if self.in_table and self.table_rows:
                self.table_rows[-1].append("".join(self.td_buf).strip())
            self.td_buf = []
        elif tag in ("code", "pre"):
            self.in_code = False

    def render_kpi(self):
        if not self.kpi_buf:
            return
        self.blank()
        self.emit("| 指标 | 数值 | 说明 |")
        self.emit("|---|---|---|")
        for card in self.kpi_buf:
            label = card.get("label", "").replace("|", "\\|")
            num = card.get("num", "").replace("|", "\\|")
            delta = card.get("delta", "").replace("|", "\\|")
            self.emit(f"| {label} | {num} | {delta} |")
        self.emit("")
        self.kpi_buf = []

    def render_callout(self):
        text = "".join(self.buf).strip()
        self.buf = []
        if not text:
            return
        kind = self.callout_kind or "note"
        lines = text.split("\n")
        self.emit(f'!!! {kind} ""')
        for ln in lines:
            if ln.strip():
                self.emit(f"    {ln.strip()}")
        self.emit("")

    def render_table(self):
        rows = [r for r in self.table_rows if r]
        if not rows:
            return
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        header = rows[0]
        self.emit("| " + " | ".join(c.replace("|", "\\|") for c in header) + " |")
        self.emit("|" + "|".join(["---"] * width) + "|")
        for r in rows[1:]:
            self.emit("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |")
        self.emit("")
        self.table_rows = []

    def handle_data(self, data):
        if self.skip_frames:
            return
        text = data
        if self.in_td:
            self.td_buf.append(text)
            return
        if self.in_kpi_label:
            if self.kpi_buf:
                self.kpi_buf[-1]["label"] = (
                    self.kpi_buf[-1].get("label", "") + text
                ).strip()
            return
        if self.in_kpi_num:
            if self.kpi_buf:
                self.kpi_buf[-1]["num"] = (
                    self.kpi_buf[-1].get("num", "") + text
                ).strip()
            return
        if self.in_kpi_delta:
            if self.kpi_buf:
                self.kpi_buf[-1]["delta"] = (
                    self.kpi_buf[-1].get("delta", "") + text
                ).strip()
            return
        if text.strip():
            self.buf.append(text)


def extract_header(html_path: Path):
    """从 HTML 的 hero 区提取标题与元信息。"""
    raw = html_path.read_text(encoding="utf-8")

    m = re.search(r"<h1>(.*?)</h1>", raw, re.S)
    title = ""
    if m:
        title = re.sub(r"<br\s*/?>", " · ", m.group(1))
        title = re.sub(r"<[^>]+>", " ", title)
        title = re.sub(r"\s+", " ", title).strip()

    # hero 副标题
    sub = ""
    m = re.search(r'<p class="sub">(.*?)</p>', raw, re.S)
    if m:
        sub = re.sub(r"<[^>]+>", "", m.group(1))
        sub = re.sub(r"\s+", " ", sub).strip()

    # 元信息 chips
    meta = []
    for c in re.findall(r'<span class="meta-chip">(.*?)</span>', raw, re.S):
        t = re.sub(r"<[^>]+>", "", c)
        t = re.sub(r"\s+", " ", t).strip()
        if t:
            meta.append(t)

    return title, sub, meta


def convert(html_path: Path) -> str:
    raw = html_path.read_text(encoding="utf-8")
    title, sub, meta = extract_header(html_path)

    # 只取 main 部分
    i = raw.find("<main")
    j = raw.find("</main>")
    if i == -1:
        body_start = raw.find("<body")
        i = body_start if body_start != -1 else 0
        j = raw.find("</body>")
    if j == -1:
        j = len(raw)
    html = raw[i:j]

    p = DocParser()
    p.feed(html)

    # 清理：折叠连续空行，去掉行尾空白
    lines = []
    blank_run = 0
    for ln in p.out:
        ln = ln.rstrip()
        if ln == "":
            blank_run += 1
            if blank_run > 1:
                continue
        else:
            blank_run = 0
        lines.append(ln)

    text = "\n".join(lines).strip()
    # 修正粗体嵌套空格：** xxx ** -> **xxx**
    text = re.sub(r"\*\*\s+([^*]+?)\s+\*\*", r"**\1**", text)
    # 去掉空的 admonition 标题
    text = re.sub(r'!!! (\w+) ""\n(?=!!!|\Z)', "", text)

    # 拼装页面头部
    head = []
    if title:
        head.append(f"# {title}")
        head.append("")
    if sub:
        head.append(f"> {sub}")
        head.append("")
    if meta:
        # 用 admonition 承载元信息。
        # 不用 --- 分隔：mkdocs 的 meta 扩展会把靠文件开头的 --- 当作
        # YAML front matter，而这些条目并非合法 YAML，会触发解析错误。
        head.append('!!! info "模块信息"')
        for m in meta:
            head.append(f"    - {m}")
        head.append("")

    return "\n".join(head) + "\n" + text + "\n"


def main():
    log = []
    total = 0
    for domain_dir in sorted(SRC_ROOT.iterdir()):
        if not domain_dir.is_dir():
            continue
        if domain_dir.name.startswith("_"):
            continue
        target_dir_name = DOMAIN_DIR.get(domain_dir.name)
        if not target_dir_name:
            log.append(f"!! 未知领域目录：{domain_dir.name}")
            continue

        for html_file in sorted(domain_dir.glob("*.html")):
            name = html_file.stem  # 如 F1-基底与坐标-奶油糖果风
            code_part = name.split("-")[0]  # F1
            # 找站点里对应的模块目录
            dst_domain = DST_ROOT / target_dir_name
            cands = [d for d in dst_domain.iterdir()
                     if d.is_dir() and d.name.startswith(code_part + "-")]
            if not cands:
                log.append(f"!! 未找到模块目录：{code_part}（来自 {name}）")
                continue
            mod_dir = cands[0]

            try:
                md = convert(html_file)
            except Exception as e:
                log.append(f"!! 转换失败 {name}: {type(e).__name__} {e}")
                continue

            if len(md) < 500:
                log.append(f"!! 内容过短（{len(md)} 字符），跳过：{name}")
                continue

            out_path = mod_dir / "讲义.md"
            if not DRY:
                out_path.write_text(md, encoding="utf-8")
            total += 1
            log.append(f"OK {len(md):>7} 字符  {target_dir_name}/{mod_dir.name}/讲义.md")

    mode = "[试运行]" if DRY else "[已写入]"
    print(f"{mode} 共转换 {total} 个讲义\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()
