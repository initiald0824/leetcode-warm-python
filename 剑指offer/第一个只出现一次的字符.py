#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/16 15:45

# 在字符串中找出第一个只出现一次的字符，如输入"abaccdeff",则输出'b'


def get_first_only(s):
    if not s:
        return None
    record = {}
    for c in s:
        if c not in record:
            record[c] = True
        else:
            record[c] = False
    for k, v in record.items():
        if v:
            return k
    return None


if __name__ == '__main__':
    print(get_first_only('abaccdeff'))
