# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/15 0:38

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true，否则返回false。
# 假设输入的数组的任意两个数字都互不相同。
# 例如输入数组{5, 7, 6, 9, 11, 10, 8}，则返回true，因为这个整数序列是下图的后序遍历的结果。
#            8
#          /   \
#         6    10
#        / \  /  \
#       5  7 9   11
# 如果输入的数组是{7, 4, 6, 5},由于没有哪棵二叉搜索树的后序遍历的结果是这个序列，所以返回false


def is_post_order(nums, start, end):
    if not nums or end < start:
        return False
    if start == end:
        return True
    root = nums[end]
    i = start
    while i < end:
        if nums[i] > root:
            break
        i += 1
    gap = i
    while i < end:
        if nums[i] < root:
            return False
        i += 1
    left = is_post_order(nums, start, gap-1)
    right = is_post_order(nums, gap, end-1)
    return left and right


if __name__ == '__main__':
    array = [5, 7, 6, 9, 11, 10, 8]
    # array = [7, 4, 6, 5]
    print(is_post_order(array, 0, len(array)-1))
