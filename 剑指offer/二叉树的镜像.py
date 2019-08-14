#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/14 13:25

# 题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#          8                         8
#        /  \                      /   \
#       6   10                    10    6
#      /\   /\                   / \   / \
#     5 7  9 11                 11 9  7  5

from basic.BinaryTree import TreeNode


def get_tree_mirror(root_node):
    if root_node is None:
        return None
    if root_node.left is None and root_node.right is None:
        return
    tmp = root_node.left
    root_node.left = root_node.right
    root_node.right = tmp
    if root_node.left:
        get_tree_mirror(root_node.left)
    if root_node.right:
        get_tree_mirror(root_node.right)


