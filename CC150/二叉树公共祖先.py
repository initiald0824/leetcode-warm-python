#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/17 21:43

# 设计并实现一个算法，找出二叉树中某两个结点的第一个共同祖先。不得将额外的结点储存在另外的数据结构中。
# 注意：这并不一定是二叉查找树


def cover(p, q):
    if p is None:
        return False
    if p == q:
        return True
    return cover(p.left, q) or cover(p.right, q)


def common_parent_func(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
    p_is_left = cover(root.left, p)
    q_is_left = cover(root.left, q)
    if p_is_left != q_is_left:
        return root
    if p_is_left:
        return common_parent_func(root.left, p, q)
    else:
        return common_parent_func(root.right, p, q)


def common_parent(root, p, q):
    if not cover(root, p) or not cover(root, q):
        return None
    return common_parent_func(root, p, q)
