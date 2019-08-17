# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/17 15:21

# 利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。
# 若“压缩”后的字符串没有变短，则返回原先的字符串


def compress_str(s):
    if not s:
        return None
    prev = s[0]
    res = s[0]
    s_len = 1
    for c in s[1:]:
        if c == prev:
            s_len += 1
        else:
            res += str(s_len) + c
            prev = c
            s_len = 1
    res += str(s_len)
    if len(res) < len(s):
        return res
    else:
        return s


if __name__ == '__main__':
    print(compress_str('aabcccccaaa'))
