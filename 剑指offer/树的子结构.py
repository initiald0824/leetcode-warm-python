# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/14 0:09

# 输入两棵二叉树A和B，判断B是不是A的子结构。


def is_child(root_a, root_b):
    res = False
    if root_a is not None and root_b is not None:
        res = is_child_func(root_a, root_b)
    if not res:
        res = is_child(root_a.left, root_b)
    if not res:
        res = is_child(root_a.right, root_b)
    return res


def is_child_func(root_a, root_b):
    if root_b is None:
        return True
    if root_a is None:
        return False
    if root_a.data != root_b.data:
        return False
    return is_child_func(root_a.left, root_b.left) and is_child_func(root_a.right, root_b.right)
