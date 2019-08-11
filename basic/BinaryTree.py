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

    # 增加新节点
    def add(self, item=None):
        node = TreeNode(item)
        if self.root is None:
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.left is None:
                    cur.left = node
                    return
                elif cur.right is None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)

    def pre_order(self):
        res = []
        if self.root is None:
            return res
        queue = []
        p = self.root
        queue.append(p)
        while queue:
            p = queue.pop()
            res.append(p.data)
            if p.right:
                queue.append(p.right)
            if p.left:
                queue.append(p.left)
        return res

    def in_order(self):
        res = []
        if self.root is None:
            return res
        queue = []
        p = self.root
        queue.append(p)


if __name__ == '__main__':
    D = TreeNode('D')
    H = TreeNode('H')
    K = TreeNode('K')
    G = TreeNode('G', H, K)
    F = TreeNode('F', G, None)
    E = TreeNode('E', None, F)
    C = TreeNode('C', D, None)
    B = TreeNode('B', None, C)
    A = TreeNode('A', B, E)
    Tree = BinaryTree(A)
    print(Tree.pre_order())
