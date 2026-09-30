# -*- coding: utf-8 -*-
"""
海灵传说小说迁移脚本
把 Novelist/海灵传说/ 里的内容复制到网站 docs/blog/literature/ 下
自动重命名为英文文件名，生成各卷索引页
"""

import os
import re
import shutil
from pathlib import Path

# ============ 路径配置 ============
SRC = Path(r"C:\Users\21722\Desktop\YanYuas\Novelist\海灵传说")
DST = Path(r"D:\YanYuas\YanYu-Site\docs\blog\literature")

# 中文目录名 -> 英文目录名映射（保证URL干净）
DIR_MAP = {
    # 世界设定
    "世界与历史": "world-history",
    "体系与规则": "systems",
    "写作参考": "writing-ref",
    "势力与物": "factions",
    "生灵图鉴": "bestiary",
    # 人物
    "主角": "protagonists",
    "反派": "antagonists",
    "配角": "supporting",
    "其他": "misc",
}
# 反向映射：英文目录名 -> 中文显示名
DIR_MAP_REV = {v: k for k, v in DIR_MAP.items()}

# ============ 辅助函数 ============

def read_title(md_path):
    """从 md 文件的 front matter 或第一个 # 标题读取中文标题"""
    try:
        text = md_path.read_text(encoding="utf-8")
    except:
        return md_path.stem
    
    # 先尝试 front matter 里的 title
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    
    # 再尝试第一个 # 标题
    m = re.search(r'^#\s+(.+?)\s*$', text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    
    return md_path.stem


def copy_file(src_path, dst_path):
    """复制文件，确保目标目录存在"""
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_path, dst_path)
    return dst_path


def gen_index(title, intro, items, dst_path):
    """
    生成索引页
    items: [(显示名, 相对链接), ...]
    """
    lines = [f"# {title}\n"]
    if intro:
        lines.append(f"> {intro}\n")
    lines.append("---\n")
    
    for name, link in items:
        lines.append(f"- [{name}]({link})")
    
    lines.append("")
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  生成索引: {dst_path.name} ({len(items)} 项)")


# ============ 1. 迁移正文章节 ============

def migrate_chapters():
    print("\n=== 迁移正文章节 ===")
    chap_dst = DST / "chapters"
    chap_dst.mkdir(parents=True, exist_ok=True)
    
    all_volumes = []  # [(卷名, 索引页相对路径)]
    
    # --- 楔子 ---
    print("\n[楔子]")
    prologue_dir = chap_dst / "prologue"
    prologue_items = []
    src_prologue = SRC / "章节·文学版"
    for f in sorted(src_prologue.glob("楔子*.md")):
        title = read_title(f)
        # 提取楔子编号
        m = re.search(r'楔子(\d+)', f.name)
        num = m.group(1) if m else "1"
        dst_name = f"prologue-{num}.md"
        copy_file(f, prologue_dir / dst_name)
        prologue_items.append((title, f"prologue/{dst_name}"))
        print(f"  {f.name} -> prologue/{dst_name}")
    
    if prologue_items:
        # 索引页在 prologue/ 下，链接只需文件名
        idx_items = [(name, link.split("/")[-1]) for name, link in prologue_items]
        gen_index("楔子", "故事开始前的序章。", idx_items, prologue_dir / "index.md")
        all_volumes.append(("楔子", "prologue/index.md"))
    
    # --- 卷一、卷二、卷四 ---
    volume_map = {
        "卷一-零日·潮信": ("volume-1", "卷一 · 零日·潮信"),
        "卷二-史前威灵": ("volume-2", "卷二 · 史前威灵"),
        "卷四-万流归极": ("volume-4", "卷四 · 万流归极"),
    }
    
    for src_dir_name, (dst_dir_name, vol_title) in volume_map.items():
        src_dir = SRC / "章节·文学版" / src_dir_name
        if not src_dir.exists():
            print(f"\n[{vol_title}] 源目录不存在，跳过")
            continue
        
        print(f"\n[{vol_title}]")
        vol_dir = chap_dst / dst_dir_name
        vol_dir.mkdir(parents=True, exist_ok=True)
        
        items = []
        interlude_count = 0
        
        for f in sorted(src_dir.glob("*.md")):
            # 跳过备份目录
            if "_backup" in str(f):
                continue
            
            title = read_title(f)
            fname = f.name
            
            # 判断文件类型并生成英文文件名
            if "终章" in fname:
                dst_name = "final.md"
            elif "插曲" in fname or "过渡" in fname:
                interlude_count += 1
                dst_name = f"interlude-{interlude_count:02d}.md"
            elif "前言" in fname:
                dst_name = "preface.md"
            else:
                # 普通章节，提取编号
                m = re.match(r'(\d+)-', fname)
                if m:
                    ch_num = int(m.group(1))
                    dst_name = f"ch{ch_num:03d}.md"
                else:
                    dst_name = f.name  #  fallback
            
            copy_file(f, vol_dir / dst_name)
            items.append((title, f"{dst_dir_name}/{dst_name}"))
            print(f"  {fname} -> {dst_dir_name}/{dst_name}")
        
        if items:
            # 索引页在 volume-x/ 下，链接只需文件名
            idx_items = [(name, link.split("/")[-1]) for name, link in items]
            gen_index(vol_title, f"《海灵传说》{vol_title}。", idx_items, vol_dir / "index.md")
            all_volumes.append((vol_title, f"{dst_dir_name}/index.md"))
    
    # --- 生成正文章节总索引 ---
    if all_volumes:
        gen_index(
            "正文章节",
            "《海灵传说》全部已完成章节。",
            all_volumes,
            chap_dst / "index.md"
        )
    
    return all_volumes


# ============ 2. 迁移世界设定 ============

def migrate_world():
    print("\n=== 迁移世界设定 ===")
    world_dst = DST / "world"
    world_dst.mkdir(parents=True, exist_ok=True)
    
    src_world = SRC / "世界设定"
    if not src_world.exists():
        print("  源目录不存在，跳过")
        return []
    
    categories = {}
    cat_counters = {}  # 每个分类的文件序号
    
    for md_file in sorted(src_world.rglob("*.md")):
        # 跳过 README
        if md_file.name.lower() == "readme.md":
            continue
        
        # 确定分类（上层目录名），转成英文
        rel = md_file.relative_to(src_world)
        if len(rel.parts) > 1:
            category = DIR_MAP.get(rel.parts[0], rel.parts[0])
        else:
            category = "misc"
        
        title = read_title(md_file)
        # 用分类内序号命名，保证URL干净
        cat_counters[category] = cat_counters.get(category, 0) + 1
        idx = cat_counters[category]
        dst_name = f"{idx:02d}.md"
        
        cat_dir = world_dst / category
        copy_file(md_file, cat_dir / dst_name)
        
        if category not in categories:
            categories[category] = []
        categories[category].append((title, f"{category}/{dst_name}"))
        print(f"  {rel} -> world/{category}/{dst_name}")
    
    # 生成各分类索引
    all_cats = []
    for cat, items in sorted(categories.items()):
        cat_dir = world_dst / cat
        display_name = DIR_MAP_REV.get(cat, cat)
        # 分类索引页内的链接只需要文件名（index.md 已在该目录下）
        cat_items = [(name, link.split("/")[-1]) for name, link in items]
        gen_index(display_name, "", cat_items, cat_dir / "index.md")
        all_cats.append((display_name, f"{cat}/index.md"))
    
    if all_cats:
        gen_index("世界设定", "《海灵传说》的世界观、历史、地理、种族与体系规则。", all_cats, world_dst / "index.md")
    
    return all_cats


# ============ 3. 迁移人物 ============

def migrate_characters():
    print("\n=== 迁移人物 ===")
    char_dst = DST / "characters"
    char_dst.mkdir(parents=True, exist_ok=True)
    
    src_char = SRC / "人物"
    if not src_char.exists():
        print("  源目录不存在，跳过")
        return []
    
    categories = {}
    cat_counters = {}
    
    for md_file in sorted(src_char.rglob("*.md")):
        if md_file.name.lower() == "readme.md":
            continue
        
        rel = md_file.relative_to(src_char)
        if len(rel.parts) > 1:
            category = DIR_MAP.get(rel.parts[0], rel.parts[0])
        else:
            category = "misc"
        
        title = read_title(md_file)
        cat_counters[category] = cat_counters.get(category, 0) + 1
        idx = cat_counters[category]
        dst_name = f"{idx:02d}.md"
        
        cat_dir = char_dst / category
        copy_file(md_file, cat_dir / dst_name)
        
        if category not in categories:
            categories[category] = []
        categories[category].append((title, f"{category}/{dst_name}"))
        print(f"  {rel} -> characters/{category}/{dst_name}")
    
    all_cats = []
    for cat, items in sorted(categories.items()):
        cat_dir = char_dst / cat
        display_name = DIR_MAP_REV.get(cat, cat)
        cat_items = [(name, link.split("/")[-1]) for name, link in items]
        gen_index(display_name, "", cat_items, cat_dir / "index.md")
        all_cats.append((display_name, f"{cat}/index.md"))
    
    if all_cats:
        gen_index("人物", "《海灵传说》的角色设定与人物弧光。", all_cats, char_dst / "index.md")
    
    return all_cats


# ============ 4. 迁移大纲 ============

def migrate_outline():
    print("\n=== 迁移大纲 ===")
    outline_dst = DST / "outline"
    outline_dst.mkdir(parents=True, exist_ok=True)
    
    src_outline = SRC / "大纲"
    if not src_outline.exists():
        print("  源目录不存在，跳过")
        return []
    
    items = []
    counter = 0
    for md_file in sorted(src_outline.glob("*.md")):
        if md_file.name.lower() == "readme.md":
            continue
        title = read_title(md_file)
        counter += 1
        dst_name = f"{counter:02d}.md"
        copy_file(md_file, outline_dst / dst_name)
        items.append((title, dst_name))
        print(f"  {md_file.name} -> outline/{dst_name}")
    
    if items:
        gen_index("大纲", "《海灵传说》的故事总纲、分卷规划与章节地图。", items, outline_dst / "index.md")
    
    return items


# ============ 5. 更新文学创作总导览页 ============

def update_literature_index(volumes, world_cats, char_cats, outline_items):
    print("\n=== 更新文学创作总导览页 ===")
    
    # 统计章节数
    total_chapters = 0
    chap_dir = DST / "chapters"
    if chap_dir.exists():
        for vol_dir in chap_dir.iterdir():
            if vol_dir.is_dir():
                total_chapters += len(list(vol_dir.glob("ch*.md")))
                total_chapters += len(list(vol_dir.glob("prologue*.md")))
                total_chapters += len(list(vol_dir.glob("interlude*.md")))
                total_chapters += len(list(vol_dir.glob("final.md")))
                total_chapters += len(list(vol_dir.glob("preface.md")))
    
    content = f"""# 文学创作

> 数学系学生的另一面。写长篇小说，也写关于写作的思考。

---

## 作品：《海灵传说》

一部关于海洋、史前巨兽与文明兴衰的长篇史诗小说。

- **已完成章节**：{total_chapters} 章（楔子 + 卷一 + 卷二 + 卷四）
- **世界观**：以海洋为核心，融合地质学、生物学与神话
- **风格**：史诗感 + 硬核设定 + 文学性表达

---

## 内容导航

<div class="grid cards" markdown>

-   :material-book-open-page-variant:{{" .lg .middle "}} __正文章节__

    ---

    楔子 · 卷一·零日潮信 · 卷二·史前威灵 · 卷四·万流归极

    [进入](chapters/index.md)

-   :material-earth:{{" .lg .middle "}} __世界设定__

    ---

    世界历史 · 地理地图 · 体系规则 · 生灵图鉴 · 势力组织

    [进入](world/index.md)

-   :material-account:{{" .lg .middle "}} __人物__

    ---

    主角 · 反派 · 配角 · 人物弧光设计

    [进入](characters/index.md)

-   :material-map:{{" .lg .middle "}} __大纲__

    ---

    故事总纲 · 分卷规划 · 章节地图 · 主线脉络

    [进入](outline/index.md)

</div>

---

!!! note "关于公开"
    本作品为原创小说，正在创作中。公开章节均为已完成版本，转载请注明出处。
"""
    
    idx_path = DST / "index.md"
    idx_path.write_text(content, encoding="utf-8")
    print(f"  已更新 {idx_path}")


# ============ 主函数 ============

def main():
    print("=" * 50)
    print("海灵传说小说迁移脚本")
    print("=" * 50)
    
    DST.mkdir(parents=True, exist_ok=True)
    
    volumes = migrate_chapters()
    world_cats = migrate_world()
    char_cats = migrate_characters()
    outline_items = migrate_outline()
    
    update_literature_index(volumes, world_cats, char_cats, outline_items)
    
    # 统计
    total = len(list(DST.rglob("*.md")))
    total_size = sum(f.stat().st_size for f in DST.rglob("*.md"))
    print(f"\n{'=' * 50}")
    print(f"迁移完成！")
    print(f"  目标目录: {DST}")
    print(f"  文件总数: {total} 个 md")
    print(f"  总大小: {total_size / 1024:.0f} KB")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
