# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/17 14:37

# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
# 如果有多对数字的和等于s，输出任意一对即可。
# 例如输入数组{1, 2, 4, 7, 11, 15}和数字15，由于4+11=15，因此输出4和11。


def get_sum_target(nums, target):
    i = 0
    j = len(nums) - 1
    res = []
    while i < j:
        if nums[i] + nums[j] == target:
            res.append((nums[i], nums[j]))
            i += 1
            j -= 1
        elif nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
    return res


if __name__ == '__main__':
    array = [1, 2, 4, 7, 8, 11, 15]
    print(get_sum_target(array, 15))
