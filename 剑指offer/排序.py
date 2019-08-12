#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/12 10:15


# 快速排序
def quick_sort(nums, start, end):
    if start < end:
        i = start
        j = end
        val = nums[start]
        while i < j:
            while i < j and nums[j] >= val:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] <= val:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = val
        quick_sort(nums, start, i - 1)
        quick_sort(nums, i + 1, end)


if __name__ == '__main__':
    array = [11, 12, 4, 16, 8, 2]
    quick_sort(array, 0, len(array) - 1)
    print(array)
