# -*- coding: utf-8 -*-
"""
修复Markdown文件中标题后缺少空行的问题
逻辑：遍历每一行，如果是标题行（#开头），且下一行不是空行也不是另一个标题，
就在标题行后插入一个空行。
代码块（```...```）内的内容不处理。
"""
import re
import sys
import os

def fix_heading_spacing(content):
    lines = content.split('\n')
    result = []
    in_code_block = False

    for i, line in enumerate(lines):
        result.append(line)

        # 检测代码块边界
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        # 代码块内不处理
        if in_code_block:
            continue

        # 检测是否是标题行（#开头，后面跟空格）
        is_heading = bool(re.match(r'^#{1,6}\s+\S', line.strip()))

        if is_heading:
            # 看下一行是什么
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # 如果下一行不是空行，也不是另一个标题，也不是代码块开始，就插入空行
                if (next_line.strip() != '' and
                    not re.match(r'^#{1,6}\s+\S', next_line.strip()) and
                    not next_line.strip().startswith('```')):
                    result.append('')  # 插入空行
            # 如果是最后一行，也加空行（一般不会到这里）
            elif i + 1 == len(lines):
                result.append('')

    return '\n'.join(result)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python fix_heading_spacing.py <文件或目录>")
        sys.exit(1)

    path = sys.argv[1]
    fixed_count = 0

    if os.path.isdir(path):
        # 批量处理目录下所有.md文件
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.md'):
                    filepath = os.path.join(root, f)
                    with open(filepath, 'r', encoding='utf-8') as fh:
                        content = fh.read()
                    original_lines = content.count('\n') + 1
                    fixed = fix_heading_spacing(content)
                    fixed_lines = fixed.count('\n') + 1
                    if fixed_lines > original_lines:
                        with open(filepath, 'w', encoding='utf-8') as fh:
                            fh.write(fixed)
                        print(f"✅ {filepath} ({original_lines}行 → {fixed_lines}行)")
                        fixed_count += 1
    else:
        # 处理单个文件
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()
        original_lines = content.count('\n') + 1
        fixed = fix_heading_spacing(content)
        fixed_lines = fixed.count('\n') + 1
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(fixed)
        print(f"✅ {path} ({original_lines}行 → {fixed_lines}行)")
        fixed_count = 1

    print(f"\n共修复 {fixed_count} 个文件")
