# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/17 13:08

# 统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3, 3, 3, 4, 5}和数字3，
# 由于3在这个数组中出现了4次，因此输出4。


def get_num_cnt(nums, target):
    if not nums:
        return 0
    first = get_border_target(nums, target, 'first')
    last = get_border_target(nums, target, 'last')
    return last - first + 1


def get_border_target(nums, target, location):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = int((start + end)/2)
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            if location == 'first':
                if mid == start or nums[mid-1] != target:
                    return mid
                else:
                    end = mid - 1
            elif location == 'last':
                if mid == end or nums[mid+1] != target:
                    return mid
                else:
                    start = mid + 1


if __name__ == '__main__':
    array = [1, 2, 3, 3, 3, 3, 4, 5]
    print(get_num_cnt(array, 3))
