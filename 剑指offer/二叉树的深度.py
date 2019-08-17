# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/17 13:24

# 输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的结点（含根，叶结点）形成树的一条路径，
# 求最长路径的长度为树的深度。
# 例如，下图中的二叉树深度为4，因为它从根结点到叶结点最长的路径包含4个结点
# （从根结点开始，经过结点2和结点5，最终到达叶结点7）。
#               1
#             /   \
#            2     3
#           / \     \
#          4  5      6
#            /
#           7

from basic.BinaryTree import TreeNode
import copy


def get_tree_max_path(root):
    if not root:
        return None
    res = []
    path = []
    get_tree_max_path_func(root, res, path)
    return max(map(lambda x: len(x), res))


def get_tree_max_path_func(node, res, path):
    if node.left is None and node.right is None:
        path.append(node.data)
        res.append(copy.deepcopy(path))
        path.pop()

    if node.left:
        path.append(node.data)
        get_tree_max_path_func(node.left, res, path)
        path.pop()

    if node.right:
        path.append(node.data)
        get_tree_max_path_func(node.right, res, path)
        path.pop()


def get_depth(root):
    if root is None:
        return 0
    return max(get_depth(root.left), get_depth(root.right)) + 1


if __name__ == '__main__':
    node_7 = TreeNode(7, None, None)
    node_5 = TreeNode(5, node_7, None)
    node_4 = TreeNode(4, None, None)
    node_2 = TreeNode(2, node_4, node_5)
    node_6 = TreeNode(6, None, None)
    node_3 = TreeNode(3, None, node_6)
    node_1 = TreeNode(1, node_2, node_3)
    print(get_depth(node_1))
