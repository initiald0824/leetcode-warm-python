# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/16 0:40

# 输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整数组成一个子数组。
# 求所有子数组的和的最大值。要求时间复杂度为O(n)
# 例如输入的数组为{1, -2, 3, 10, -4, 7, 2 -5}，和最大的子数组为{3, 10, -4, 7, 2}，因此输出为该子数组的和18。


def get_continuous_max_sum(nums):
    if not nums:
        return None
    max_sum = 0
    sum_val = 0
    for num in nums:
        sum_val += num
        if sum_val < 0:
            sum_val = 0
        if sum_val > max_sum:
            max_sum = sum_val
    return max_sum


if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5]
    print(get_continuous_max_sum(array))
