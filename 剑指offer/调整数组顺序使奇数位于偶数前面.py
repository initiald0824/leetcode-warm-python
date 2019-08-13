# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/13 22:16


def divide_odd_even(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] % 2 == 1:
            start += 1
        elif nums[end] % 2 == 0:
            end -= 1
        else:
            nums[start], nums[end] = nums[end], nums[start]


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    divide_odd_even(array)
    print(array)
