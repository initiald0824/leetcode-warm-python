#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/16 16:03

# 在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。
# 例如在数组{7, 5, 6, 4}中，一共存在5个逆序对，分别是(7, 6), (7, 5), (7, 4), (6, 4), (5, 4)
import copy


def inverse_pair(data, copy_data, start, end):
    if start == end:
        copy_data[start] = data[start]
        return 0
    mid = int((start+end)/2)
    left = inverse_pair(copy_data, data, start, mid)
    right = inverse_pair(copy_data, data, mid+1, end)
    i = mid
    j = end
    index = end
    cnt = 0
    while i >= start and j >= (mid+1):
        if data[i] > data[j]:
            cnt += (j-mid)
            copy_data[index] = data[j]
            j -= 1
            index -= 1
        else:
            copy_data[index] = data[i]
            index -= 1
            i -= 1
    while i >= start:
        copy_data[index] = data[i]
        index -= 1
        i -= 1
    while j >= (mid+1):
        copy_data[index] = data[j]
        index -= 1
        j -= 1
    return left+right+cnt


def reverse_cnt(data, length):
    if not data or length <= 0:
        return 0
    copy_data = copy.deepcopy(data)
    return inverse_pair(data, copy_data, 0, length-1)


if __name__ == '__main__':
    array = [7, 5, 6, 4]
    print(reverse_cnt(array, len(array)))
