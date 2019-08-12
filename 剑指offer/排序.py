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


# 堆排序 建堆 下沉 堆排序
def build_heap(nums):
    l_range = range(int(len(nums)/2))[::-1]
    for i in l_range:
        percolate_down(nums, i, len(nums))


def percolate_down(nums, index, size):
    while index*2+1 < size:
        min_index = index*2 + 1
        if index*2+2 < size and nums[index*2+2] < nums[min_index]:
            min_index = index * 2 + 2
        if nums[index] > nums[min_index]:
            nums[index], nums[min_index] = nums[min_index], nums[index]
            index = min_index
        else:
            break


def heap_sort(nums):
    build_heap(nums)
    nums_size = len(nums)
    index = nums_size - 1
    while index > 0:
        nums[0], nums[index] = nums[index], nums[0]
        nums_size -= 1
        index -= 1
        percolate_down(nums, 0, nums_size)


# 选择排序
def select_sort(nums):
    i = 0
    while i < len(nums):
        min_index = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[min_index]:
                min_index = j
            j += 1
        nums[i], nums[min_index] = nums[min_index], nums[i]
        i += 1


# 归并排序
def merge_sort(nums):
    res = [None] * len(nums)
    merge_sort_func(nums, 0, len(nums)-1, res)


def merge_sort_func(nums, start, end, res):
    if start < end:
        mid = int((start + end)/2)
        merge_sort_func(nums, start, mid, res)
        merge_sort_func(nums, mid+1, end, res)
        merge_sort_array(nums, start, mid, end, res)


def merge_sort_array(nums, start, mid, end, res):
    i = start
    j = mid + 1
    m = mid
    k = 0
    while i <= m and j <= end:
        if nums[i] < nums[j]:
            res[k] = nums[i]
            i += 1
        else:
            res[k] = nums[j]
            j += 1
        k += 1

    while i <= m:
        res[k] = nums[i]
        i += 1
        k += 1
    while j <= end:
        res[k] = nums[j]
        j += 1
        k += 1

    for i in range(k):
        nums[start+i] = res[i]


if __name__ == '__main__':
    array = [11, 12, 4, 16, 8, 2, 13, 12, 15]
    merge_sort(array)
    print(array)
