# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/14 22:41

# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1、2、3、4、5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，
# 但4、3、5、1、2就不可能是该压栈序列的弹出序列。


def is_pop_order(nums1, nums2):
    if len(nums1) != len(nums2):
        return False
    i = 0
    j = 0
    s = []
    size = len(nums1)
    while i < size:
        if nums1[i] != nums2[j]:
            s.append(nums1[i])
        else:
            j += 1
        i += 1
    if not s:
        return True
    while j < size:
        if nums2[j] != s[-1]:
            return False
        j += 1
        s.pop()
    return True


if __name__ == '__main__':
    print(is_pop_order([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
