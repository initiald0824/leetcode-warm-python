# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/15 23:36

# 输入一个字符串，打印出该字符串中字符的所有排列。
# 例如输入字符串abc，则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba
import copy


def permute(s):
    res = []
    path = []
    if not s:
        return res
    permute_func(s, path, res)
    return res


def permute_func(s, path, res):
    if len(path) == len(s):
        res.append(copy.deepcopy(path))
        return
    for c in s:
        if c not in path:
            path.append(c)
            permute_func(s, path, res)
            path.pop()


if __name__ == '__main__':
    print(permute('abc'))
