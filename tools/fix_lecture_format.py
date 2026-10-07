# -*- coding: utf-8 -*-
"""
修复单行Markdown文件 v2：在块级元素前插入换行符
改进点：
- 标题：前面只要不是#就加换行（中文字符也触发）
- 表格：用 || → |\n| 处理表格行分隔
- 引用块：前面不是单词字符或>就加换行
"""
import re
import sys

def fix_single_line_md(content):
    # 第一步：保护代码块（```...```）
    code_blocks = []
    def save_code_block(m):
        code_blocks.append(m.group(0))
        return f'\x00CODEBLOCK{len(code_blocks)-1}\x00'
    content = re.sub(r'```[\s\S]*?```', save_code_block, content)

    # 第二步：保护行内代码（`...`）
    inline_codes = []
    def save_inline_code(m):
        inline_codes.append(m.group(0))
        return f'\x00INLINE{len(inline_codes)-1}\x00'
    content = re.sub(r'`[^`]+`', save_inline_code, content)

    # 第三步：在块级元素前插入换行符
    def add_newline_before(pattern, text):
        def replacer(m):
            start = m.start()
            if start > 0 and text[start-1] == '\n':
                return m.group(0)
            return '\n' + m.group(0)
        return re.sub(pattern, replacer, text)

    # 1. 标题：# ## ### ####（前面不是#即可，中文字符也触发）
    content = add_newline_before(r'(?<!#)#{1,6}\s+\S', content)

    # 2. 提示框：!!! note / !!! tip 等
    content = add_newline_before(r'!!!\s+\w+', content)

    # 3. 分隔线：---（前后不是字母数字和-）
    content = add_newline_before(r'(?<![\w-])---(?![\w-])', content)

    # 4. 引用块：>（前面不是单词字符、>、或换行）
    content = add_newline_before(r'(?<![\w>\n])>\s+\S', content)

    # 5. 表格行分隔：|| → |\n|（表格行之间用||连接，在中间插入换行）
    content = re.sub(r'\|\|', '|\n|', content)

    # 6. 无序列表：- （前面是空格，后面是空格+非空白）
    content = add_newline_before(r'(?<=\s)-\s+(?=\S)', content)

    # 7. 有序列表：1. 2. 等（前面是空格，后面是空格+非空白）
    content = add_newline_before(r'(?<=\s)\d+\.\s+(?=\S)', content)

    # 第四步：恢复行内代码
    for i, code in enumerate(inline_codes):
        content = content.replace(f'\x00INLINE{i}\x00', code)

    # 第五步：恢复代码块
    for i, code in enumerate(code_blocks):
        content = content.replace(f'\x00CODEBLOCK{i}\x00', code)

    # 第六步：清理多余的连续换行（最多保留2个）
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 去掉开头的多余换行
    content = content.lstrip('\n')

    return content


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python fix_lecture.py <文件路径>")
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    original_lines = content.count('\n') + 1
    fixed = fix_single_line_md(content)
    fixed_lines = fixed.count('\n') + 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed)

    print(f"修复完成: {filepath}")
    print(f"  原始: {original_lines} 行, {len(content)} 字符")
    print(f"  修复后: {fixed_lines} 行, {len(fixed)} 字符")
