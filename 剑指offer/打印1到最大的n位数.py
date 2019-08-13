#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/13 19:06

# 题目：输入数字n，按顺序打印出从1到最大的n为十进制数。比如输入3，则打印出1、2、3一直到最大的3位数即999。


def dfs(n):
    nums = [i for i in range(10)]
    path = []
    res = []
    dfs_func(nums, n, path)
    return res


def dfs_func(nums, n, path):

    pass


if __name__ == '__main__':
    dfs(3)
