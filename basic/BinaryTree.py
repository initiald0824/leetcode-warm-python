# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/11 0:11


class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, node=None):
        self.root = node
    