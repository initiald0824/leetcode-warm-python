#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/17 21:02

# 给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉查找树。
from basic.BinaryTree import TreeNode


def create_min_binary_tree(nums):
    return create_min_binary_tree_func(nums, 0, len(nums)-1)


def create_min_binary_tree_func(nums, start, end):
    if start <= end:
        mid = int((start+end)/2)
        root = TreeNode(nums[mid], None, None)
        root.left = create_min_binary_tree_func(nums, start, mid-1)
        root.right = create_min_binary_tree_func(nums, mid+1, end)
        return root
    else:
        return None
