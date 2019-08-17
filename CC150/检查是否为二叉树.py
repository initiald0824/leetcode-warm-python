#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/17 21:16

# 实现一个函数，检查一棵树是否为二叉查找树是否为二叉查找树。
import sys


def check_select_binary_tree(root):
    return check_select_binary_tree_func(root, -sys.maxsize-1, sys.maxsize)


def check_select_binary_tree_func(node, min_val, max_val):
    if not node:
        return True
    if node.data < min_val or node.data > max_val:
        return False
    if not check_select_binary_tree_func(node.left, min_val, node.data) \
            or not check_select_binary_tree_func(node.right, node.data, max_val):
        return False
    return True
