# -*- coding: utf-8 -*-
"""
html2md.py · 奶油糖果风讲义 HTML 转换为 Markdown（零基础自学版）
====================================================================
【这个脚本是干什么的】
  历史迁移工具。早期的高等代数讲义是用 HTML 写的（奶油糖果风），
  现在要统一改成 Markdown 格式放进 MkDocs 网站。
  这个脚本自动把 HTML 转换成干净的 Markdown。

【源和目标】
  源：C:\Users\21722\Desktop\YanYuas\MathematicalLearning\AdvancedAlgebra\学术研究\
       领域X-YYY\<代号>-<名称>-奶油糖果风.html
  目标：docs\maththeory\advanced-algebra\<领域目录>\<代号>-<名称>\讲义.md

【HTML 组件 → Markdown 的映射】
  <header class="hero"> h1/sub/meta  →  标题 + 引用
  nav.toc                            →  丢弃（站点自带目录）
  section > .sec-head > h2           →  ## 标题
  .abstract-box > p                  →  普通段落
  .kpi-grid                          →  三列表格
  .card > .ct / .cd                  →  ### 小标题 + 段落
  .callout mint|sky|butter           →  !!! tip / !!! note / !!! warning
  table.tbl                          →  Markdown 表格
  <b>                                →  **粗体**
  <br>                               →  换行

【注意】
  这些 HTML 的公式全部用 Unicode 数学字符书写（无 $、无 LaTeX），
  因此直接保留文本即可，不涉及公式定界符转换。

【怎么用】
  试运行：.venv\Scripts\python.exe tools/html2md.py --dry-run
  执行：  .venv\Scripts\python.exe tools/html2md.py
====================================================================
"""
import re           # 正则表达式
import sys          # 系统参数
from html.parser import HTMLParser  # Python 内置 HTML 解析器
from pathlib import Path

# 源 HTML 目录（桌面上的原始讲义）
SRC_ROOT = Path(r"C:\Users\21722\Desktop\YanYuas\MathematicalLearning\AdvancedAlgebra\学术研究")
# 目标 Markdown 目录（网站 docs 下的高等代数）
DST_ROOT = Path(r"D:\YanYuas\YanYu-Site\docs\maththeory\advanced-algebra")

# 领域目录映射：HTML 里的目录名 → 网站里的目录名
DOMAIN_DIR = {
    "领域一-矩阵与基": "matrix-basis",
    "领域二-线性空间": "linear-space",
    "领域三-线性变换": "linear-transform",
}

DRY = "--dry-run" in sys.argv


class DocParser(HTMLParser):
    """
    自定义 HTML 解析器：把 HTML 正文转成 Markdown 行列表。
    继承 Python 内置的 HTMLParser，重写开始标签、结束标签、文本处理方法。
    """

    # 需要整体跳过的标签（脚本、样式、SVG、导航、按钮、头部）
    SKIP_TAGS = {"script", "style", "svg", "nav", "button", "head"}

    def __init__(self):
        super().__init__(convert_charrefs=True)  # 自动转换 &nbsp; 等实体
        self.out = []            # 输出行（最终的 Markdown 行列表）
        self.buf = []            # 当前行内缓冲（收集文字，遇到换行才输出）
        # 跳过机制：记录每个「被跳过子树」的根节点在 stack 中的索引。
        # 只有当结束标签回到该索引时，才结束跳过。
        # （不能用简单计数器——子树内部每个结束标签都会误减计数）
        self.skip_frames = []
        # 各种状态标记
        self.in_h1 = False
        self.in_h2 = False
        self.in_h3 = False
        self.bold = 0
        # 表格相关
        self.table_rows = []     # 表格行收集
        self.in_table = False
        self.in_td = False
        self.td_buf = []
        self.cell_is_head = False
        # 元素栈（tag, class），用于结束标签时找到对应的开始标签
        self.stack = []
        # KPI 卡片相关
        self.kpi_buf = []
        self.in_kpi = False
        self.in_kpi_label = False
        self.in_kpi_num = False
        self.in_kpi_delta = False
        # 提示框（callout）相关
        self.callout_depth = 0
        self.callout_kind = ""
        # 卡片标题
        self.in_card_title = False
        # 代码
        self.in_code = False

    # ---- 工具方法 ----

    def flush_line(self):
        """把当前行内缓冲输出为一行"""
        text = "".join(self.buf).strip()
        self.buf = []
        if text:
            self.out.append(text)

    def emit(self, line):
        """直接输出一行"""
        self.out.append(line)

    def blank(self):
        """输出一个空行（但不连续输出多个空行）"""
        if self.out and self.out[-1] != "":
            self.out.append("")

    # ---- 开始标签处理 ----

    def handle_starttag(self, tag, attrs):
        # 把属性列表转成字典，方便取 class
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
        # 如果当前在跳过的子树里，只维护栈，不处理
        if self.skip_frames:
            self.stack.append((tag, classes))
            return

        # 根据标签类型处理
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
            self.buf.append("**")  # 粗体开始
        elif tag == "br":
            self.buf.append(" ")   # 换行 → 空格
        elif tag == "p":
            self.flush_line()
            if "cd" in classes:
                pass  # 卡片内容段落，正常处理
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
                # 提示框：根据 class 决定类型
                self.flush_line()
                self.blank()
                if "mint" in classes:
                    self.callout_kind = "tip"      # 薄荷绿 → tip
                elif "butter" in classes:
                    self.callout_kind = "warning"  # 奶黄 → warning
                else:
                    self.callout_kind = "note"     # 默认 → note
                self.callout_depth = 1
            elif "ct" in classes:
                # 卡片标题
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

    # ---- 结束标签处理 ----

    def handle_endtag(self, tag):
        if not self.stack:
            return
        # 找到对应的开始标签在 stack 中的位置（从后往前找）
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

        # 根据标签类型处理结束
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
            self.buf.append("**")  # 粗体结束
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
                    t = re.sub(r"^\s*[·•]\s*", "", t)  # 去掉开头的项目符号
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

    # ---- 渲染辅助方法 ----

    def render_kpi(self):
        """把 KPI 卡片渲染成 Markdown 表格"""
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
        """把提示框渲染成 MkDocs admonition"""
        text = "".join(self.buf).strip()
        self.buf = []
        if not text:
            return
        kind = self.callout_kind or "note"
        lines = text.split("\n")
        self.emit(f'!!! {kind} ""')  # 空标题
        for ln in lines:
            if ln.strip():
                self.emit(f"    {ln.strip()}")  # admonition 内容需要缩进4格
        self.emit("")

    def render_table(self):
        """把 HTML 表格渲染成 Markdown 表格"""
        rows = [r for r in self.table_rows if r]
        if not rows:
            return
        # 统一列数（补空单元格）
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        header = rows[0]
        # 表头行
        self.emit("| " + " | ".join(c.replace("|", "\\|") for c in header) + " |")
        # 分隔行
        self.emit("|" + "|".join(["---"] * width) + "|")
        # 数据行
        for r in rows[1:]:
            self.emit("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |")
        self.emit("")
        self.table_rows = []

    # ---- 文本处理 ----

    def handle_data(self, data):
        # 在跳过的子树里，忽略文本
        if self.skip_frames:
            return
        text = data
        # 表格单元格内容
        if self.in_td:
            self.td_buf.append(text)
            return
        # KPI 卡片各部分
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
        # 普通文本：加入行内缓冲
        if text.strip():
            self.buf.append(text)


def extract_header(html_path: Path):
    """从 HTML 的 hero 区提取标题与元信息。"""
    raw = html_path.read_text(encoding="utf-8")

    # 提取 h1 标题
    m = re.search(r"<h1>(.*?)</h1>", raw, re.S)
    title = ""
    if m:
        title = re.sub(r"<br\s*/?>", " · ", m.group(1))  # <br> 换成 " · "
        title = re.sub(r"<[^>]+>", " ", title)           # 去掉所有标签
        title = re.sub(r"\s+", " ", title).strip()       # 合并空白

    # 提取 hero 副标题
    sub = ""
    m = re.search(r'<p class="sub">(.*?)</p>', raw, re.S)
    if m:
        sub = re.sub(r"<[^>]+>", "", m.group(1))
        sub = re.sub(r"\s+", " ", sub).strip()

    # 提取元信息 chips
    meta = []
    for c in re.findall(r'<span class="meta-chip">(.*?)</span>', raw, re.S):
        t = re.sub(r"<[^>]+>", "", c)
        t = re.sub(r"\s+", " ", t).strip()
        if t:
            meta.append(t)

    return title, sub, meta


def convert(html_path: Path) -> str:
    """把一个 HTML 文件转换成 Markdown 字符串"""
    raw = html_path.read_text(encoding="utf-8")
    title, sub, meta = extract_header(html_path)

    # 只取 <main> 部分（去掉导航、页脚等）
    i = raw.find("<main")
    j = raw.find("</main>")
    if i == -1:
        # 没有 main 标签，取 body
        body_start = raw.find("<body")
        i = body_start if body_start != -1 else 0
        j = raw.find("</body>")
    if j == -1:
        j = len(raw)
    html = raw[i:j]

    # 用自定义解析器解析
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
                continue  # 超过1个连续空行就跳过
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
    """主函数：遍历所有 HTML 文件并转换"""
    log = []
    total = 0
    for domain_dir in sorted(SRC_ROOT.iterdir()):
        if not domain_dir.is_dir():
            continue
        if domain_dir.name.startswith("_"):
            continue
        # 映射领域目录
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

            # 内容过短说明转换有问题，跳过
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
