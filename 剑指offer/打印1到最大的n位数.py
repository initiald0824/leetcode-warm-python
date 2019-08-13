#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/13 19:06

# 题目：输入数字n，按顺序打印出从1到最大的n为十进制数。比如输入3，则打印出1、2、3一直到最大的3位数即999。
import copy


def dfs(n):
    nums = [i for i in range(10)]
    res = []
    path = []
    dfs_func(nums, res, path, n)
    return res


def dfs_func(nums, res, path, n):
    if n == 0:
        res.append(copy.deepcopy(path))
        return
    for i in nums:
        path.append(i)
        dfs_func(nums, res, path, n-1)
        path.pop()


def print_func(nums):
    for num in nums:
        s = ''
        flag = False
        for index, val in enumerate(num):
            if index == len(num) - 1:
                s += str(val)
            elif val == 0 and flag:
                s += str(val)
            elif val != 0:
                flag = True
                s += str(val)
        print(s)


if __name__ == '__main__':
    res = dfs(3)
    print_func(res)