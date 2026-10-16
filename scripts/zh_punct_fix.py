#!/usr/bin/env python3
"""把中文旁边的半角标点改成全角。只动紧挨汉字的 , ; : ? ! ( )，
不动 URL、Markdown 链接地址、HTML 标签、代码、数字千分位和纯英文句子。

用法：
  zh_punct_fix.py <文件>             修复，原文件先备份为 <文件>.bak
  zh_punct_fix.py <文件> --dry-run   只显示会改多少处，不写文件

v2 版脚本的两个错误在这里已修正：括号被“修”回半角（等于没修）；
字符集里混入了半角引号，导致英文引号旁的逗号也被改。
"""
import re
import shutil
import sys

HAN = '㐀-䶿一-鿿豈-﫿'
# 中文语境字符：汉字、中文书名号/引号/括号、省略号、破折号、八卦符号与阴阳爻
CJK = HAN + '《》「」『』〈〉【】“”‘’…—☰-☷⚊⚋'
FULL = {',': '，', ';': '；', ':': '：', '?': '？', '!': '！', '(': '（', ')': '）'}


def fix(text):
    keep = []

    def protect(m):
        keep.append(m.group(0))
        return f'\x00{len(keep) - 1}\x00'

    # 先保护不能动的片段
    text = re.sub(r'```.*?```', protect, text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', protect, text)
    text = re.sub(r'\]\([^)]*\)', protect, text)
    text = re.sub(r'https?://[^\s)）]+', protect, text)
    tags = []

    def protect_tag(m):
        tags.append(m.group(0))
        return f'\x01{len(tags) - 1}\x01'

    text = re.sub(r'<[^>]+>', protect_tag, text)

    n = 0

    def sub(pattern, repl_char):
        nonlocal text, n
        text, k = re.subn(pattern, repl_char, text)
        n += k

    for half, full in FULL.items():
        h = re.escape(half)
        if half == ':':
            sub(rf'(?<=[{CJK}]):(?!//)', full)
        else:
            sub(rf'(?<=[{CJK}]){h}', full)
        if half in ',;(':
            sub(rf'{h}(?=[{CJK}])', full)
        if half == ')':
            sub(rf'\)(?=[{CJK}])', full)
        # 中文 + HTML 闭合标签 + 半角标点，例如 ☰</span>: 三根
        sub(rf'([{CJK}])(\x01\d+\x01){h}', rf'\1\2{full}')

    for i, t in enumerate(tags):
        text = text.replace(f'\x01{i}\x01', t)
    for i, t in enumerate(keep):
        text = text.replace(f'\x00{i}\x00', t)
    return text, n


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = sys.argv[1]
    with open(path, encoding='utf-8') as f:
        src = f.read()
    out, n = fix(src)
    if '--dry-run' in sys.argv:
        print(f'将修改 {n} 处')
        return
    if n == 0:
        print('没有需要修改的地方')
        return
    shutil.copy2(path, path + '.bak')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'已修改 {n} 处；原文件备份为 {path}.bak')


if __name__ == '__main__':
    main()
