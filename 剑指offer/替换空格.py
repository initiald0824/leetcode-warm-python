# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/10 19:16

# 请输入一个函数，把字符串中的每个空格替换成"%20"。例如输入"We are happy.",则输出"We%20are%20happy."


def replace_space(s):
    return s.replace(' ', '%20')


if __name__ == '__main__':
    print(replace_space('We are happy'))
