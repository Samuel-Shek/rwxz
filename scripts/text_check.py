#!/usr/bin/env python3
"""rwxz 文本检查（只读，不修改文件）。

用法：
  text_check.py count  <文件|->            计数：中文 Word 口径字数、拼音文字词数、非空白字符数
  text_check.py scan   <文件|-> [--lang zh|en|auto]
                                          套话信号扫描。HARD = 禁区短语，必须清零；
                                          SOFT = 提示，需结合语境判断，不追求零命中
  text_check.py punct  <文件|->            查中文旁边的半角标点（忽略 URL、HTML 标签、代码）
  text_check.py all    <文件|-> [--lang ...]

“-” 表示从标准输入读取。
"""
import re
import sys

# 汉字（含扩展 A、兼容区）、假名不算入中文字数口径
HAN = r'㐀-䶿一-鿿豈-﫿'
# 中文 / 全角标点
CJK_PUNCT = r'　-〿！-／：-＠［-｀｛-･—…“”‘’·'
LATIN_WORD = r"[A-Za-zÀ-ɏ0-9]+(?:['\u2019\-.,][A-Za-zÀ-ɏ0-9]+)*"

HARD = {
    'zh': ['重磅', '颠覆', '全网最强', '闭眼入', '错过后悔', '希望对你有帮助', '希望对您有帮助',
           '以上就是', '让我们一起', '保证有效', '保证涨粉', '保证赚钱', '改变命运', '百分百有效', '包准'],
    'en': ['game-changer', 'game changer', 'revolutionary', "you won't believe", 'i hope this helps',
           'in conclusion', "let's dive in", 'guaranteed results'],
}
SOFT = {
    'zh': ['在当今', '随着', '众所周知', '相信大家都不陌生', '值得注意的是', '值得一提的是', '不可否认',
           '毫无疑问', '换句话说', '本质上', '说白了', '赋能', '闭环', '抓手', '底层逻辑', '无缝',
           '至关重要', '深入探讨', '相互交织', '首先，', '其次，', '综上', '总而言之', '不仅仅是',
           '进行了', '做出了', '加以', '对于', '目的是为了',
           '其实吧', '我跟你说', '你想想看', '说真的', '坦率讲', '说回正题', '话又说回来',
           '余量', '意味', '分寸', '底色', '落点', '张力', '质感'],
    'en': ['delve', 'tapestry', 'leverage', 'utilize', 'robust', 'seamless', 'cutting-edge', 'unlock',
           'elevate', 'empower', 'supercharge', 'landscape', 'realm', 'testament to', "in today's",
           "it's worth noting", "it's important to", 'when it comes to', 'at the end of the day',
           'not just', 'kindly', 'do the needful', 'revert back', 'discuss about', 'could potentially'],
}


def read(path):
    if path == '-':
        return sys.stdin.read()
    with open(path, encoding='utf-8') as f:
        return f.read()


def strip_markup(text):
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)       # 代码块
    text = re.sub(r'`[^`]*`', ' ', text)                    # 行内代码
    text = re.sub(r'<[^>]+>', ' ', text)                    # HTML 标签
    text = re.sub(r'\]\([^)]*\)', ']', text)                # Markdown 链接地址
    text = re.sub(r'https?://\S+', ' ', text)               # 裸 URL
    return text


def count(text):
    body = strip_markup(text)
    body = re.sub(r'^\s{0,3}#{1,6}\s*', '', body, flags=re.M)   # 标题井号
    body = re.sub(r'[*_>|]', ' ', body)                          # 常见 Markdown 符号
    han = len(re.findall(f'[{HAN}]', body))
    punct = len(re.findall(f'[{CJK_PUNCT}]', body))
    latin = len(re.findall(LATIN_WORD, body))
    kana = len(re.findall(r'[぀-ヿ]', body))
    return {
        'zh_word_count': han + punct + latin,     # 中文 Word 口径
        'words': len([w for w in re.findall(r'\S+', re.sub(f'[{HAN}぀-ヿ]', ' ', body))
                      if re.search(r'\w', w)]),  # 拼音文字词数（纯标点不计）
        'chars_no_space': len(re.sub(r'\s', '', body)),
        'han': han, 'kana': kana, 'latin_words': latin,
    }


def detect_lang(text):
    c = count(text)
    return 'zh' if c['han'] > c['latin_words'] else 'en'


def scan(text, lang):
    body = strip_markup(text)
    low = body.lower()
    out = []
    for level, table in (('HARD', HARD), ('SOFT', SOFT)):
        for w in table.get(lang, []):
            n = low.count(w.lower())
            if n:
                out.append((level, w, n))
    # 结构信号：连续一句一段
    paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
    run = best = 0
    for p in paras:
        short = len(p) <= (30 if lang == 'zh' else 90) and '\n' not in p
        run = run + 1 if short else 0
        best = max(best, run)
    if best >= 4:
        out.append(('SOFT', '连续短段落（一句一段）', best))
    dashes = body.count('——') + body.count('—')
    per_k = dashes / max(len(body), 1) * 1000
    if per_k > 3:
        out.append(('SOFT', f'破折号密度 {per_k:.1f}/千字符', dashes))
    return out


def punct(text):
    body = strip_markup(text)
    cjk = f'{HAN}぀-ヿ《》「」『』〈〉【】“”‘’…—☰-☷⚊⚋'
    a = re.findall(f'[{cjk}][,;:?!()]', body)
    b = re.findall(f'[,;:?!()][{cjk}]', body)
    return a + b


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ('count', 'scan', 'punct', 'all'):
        print(__doc__)
        sys.exit(2)
    cmd, path = sys.argv[1], sys.argv[2]
    lang = 'auto'
    if '--lang' in sys.argv:
        lang = sys.argv[sys.argv.index('--lang') + 1]
    text = read(path)
    if lang == 'auto':
        lang = detect_lang(text)
    hard_hits = 0
    if cmd in ('count', 'all'):
        c = count(text)
        print(f"中文字数（Word 口径）: {c['zh_word_count']}  | 词数: {c['words']}  | 非空白字符: {c['chars_no_space']}")
    if cmd in ('scan', 'all'):
        hits = scan(text, lang)
        if not hits:
            print(f'[{lang}] 未发现套话信号')
        for level, w, n in hits:
            print(f'{level}  {w}  ×{n}')
            hard_hits += level == 'HARD'
    if cmd in ('punct', 'all'):
        hits = punct(text)
        if hits:
            print(f'中文旁的半角标点 {len(hits)} 处：' + '  '.join(repr(h) for h in hits[:12]))
        else:
            print('中文旁未发现半角标点')
    sys.exit(1 if hard_hits else 0)


if __name__ == '__main__':
    main()
