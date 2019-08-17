#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/17 20:52

# 实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个结点，其两棵子树的高度差不超过1。


def get_height(node):
    if not node:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1


def is_balance(node):
    if not node:
        return True
    dis = abs(get_height(node.left) - get_height(node.right))
    if dis > 1:
        return False
    else:
        return is_balance(node.left) and is_balance(node.right)

