#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/15 17:08

# 输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# 例如下图中二叉树的和为22，则打印出两条路径，第一条路径包含结点10、12，
# 第二条路径包含结点10、5、和 7。
#        10
#       /  \
#      5   12
#     /\
#    4  7

from basic.BinaryTree import TreeNode
import copy


def get_tree_target_path(root, target):
    path = []
    res = []
    if root is None:
        return res
    get_tree_target_path_func(root, path, res, target)
    return res


def get_tree_target_path_func(node, path, res, target):
    if node.left is None and node.right is None:
        path.append(node.data)
        if sum(path) == target:
            res.append(copy.deepcopy(path))
        path.pop()
    if node.left:
        path.append(node.data)
        get_tree_target_path_func(node.left, path, res, target)
        path.pop()
    if node.right:
        path.append(node.data)
        get_tree_target_path_func(node.right, path, res, target)
        path.pop()


if __name__ == '__main__':
    node_4 = TreeNode(4, None, None)
    node_7 = TreeNode(7, None, None)
    node_5 = TreeNode(5, node_4, node_7)
    node_12 = TreeNode(12, None, None)
    node_root = TreeNode(10, node_5, node_12)
    print(get_tree_target_path(node_root, 22))
