#! usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

""" 
    auth: wormer@wormer.cn
    proj: site_salary
    date: 2017-11-15
    desc: 
        用于拆分中英文字符串，返回中文列表，英文列表
"""


def is_chinese(padding_str):
    """
        判断字符是否为中文
    """
    int_char = ord(padding_str)

    # Punct & Radicals
    if 0x2e80 <= int_char <= 0x33ff:
        return True
    # Fullwidth Latin Characters
    elif 0xff00 <= int_char <= 0xffef:
        return True
    # CJK Unified Ideographs & CJK Unified Ideographs Extension A
    elif 0x4e00 <= int_char <= 0x9fbb:
        return True
    # CJK Compatibility Ideographs
    elif 0xf900 <= int_char <= 0xfad9:
        return True
    # CJK Unified Ideographs Extension B
    elif 0x20000 <= int_char <= 0x2a6d6:
        return True
    # CJK Compatibility Supplement
    elif 0x2f800 <= int_char <= 0x2fa1d:
        return True
    else:
        return False


def split_chinese_english(pending_char):
    """
        用于拆分中文，英文
    """
    english_group = []
    chinese_group = []

    zh_gather = ""
    en_gather = ""
    zh_status = False

    for char in pending_char:
        if not zh_status and is_chinese(char):
            zh_status = True
            if en_gather != "":
                english_group.append(en_gather)
                en_gather = ""
        elif not is_chinese(char) and zh_status:
            zh_status = False
            if zh_gather != "":
                chinese_group.append(zh_gather)
        if zh_status:
            zh_gather += char
        else:
            en_gather += char
            zh_gather = ""

    if en_gather != "":
        english_group.append(en_gather)
    elif zh_gather != "":
        chinese_group.append(zh_gather)

    return chinese_group, english_group


if __name__ == "__main__":
    test_chars = u"圣诞节法律书籍的jsdf撒娇了快点放假啦jksljkdj就啊水力发电就啊看世界"
    chi_list, eng_list = split_chinese_english(test_chars)

    for chi in chi_list:
        print chi

    print "------------------------------------"

    for eng in eng_list:
        print eng
