#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/16 15:24

# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3, 32, 321}, 则打印出这3个数字能排成的最小数字321323。


def get_min_order(nums):
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            a, b = nums[i], nums[j]
            if compare_num_str(a, b):
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def compare_num_str(a, b):
    return (str(a)+str(b)) > (str(b)+str(a))


if __name__ == '__main__':
    print(get_min_order([3, 32, 321]))