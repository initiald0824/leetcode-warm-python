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
        if not self.root:
            return res
        queue = [self.root]
        p = self.root.left
        while queue or p:
            if p:
                queue.append(p)
                p = p.left
            else:
                p = queue.pop()
                res.append(p.data)
                p = p.right
        return res

    def in_order_recursion(self):
        res = []
        self.in_order_recursion_func(res, self.root)
        return res

    @staticmethod
    def in_order_recursion_func(res, node):
        if node is None:
            return
        BinaryTree.in_order_recursion_func(res, node.left)
        res.append(node.data)
        BinaryTree.in_order_recursion_func(res, node.right)

    def level_order(self):
        res = []
        queue = [self.root]
        while queue:
            p = queue.pop(0)
            res.append(p.data)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        return res

    @staticmethod
    def build_tree_by_pre_in(pre_order, in_order):
        if not pre_order or not in_order:
            return None
        return BinaryTree.build_tree_by_pre_in_func(pre_order, in_order, 0, len(pre_order), 0, len(in_order))

    @staticmethod
    def build_tree_by_pre_in_func(pre_order, in_order, pre_start, pre_end, in_start, in_end):
        if pre_start == pre_end:
            return None
        if in_start == in_end:
            return None
        root_node = TreeNode(pre_order[pre_start])
        left_size = in_order.index(root_node.data) - in_start
        root_node.left = BinaryTree.build_tree_by_pre_in_func(pre_order, in_order, pre_start+1, pre_start+1+left_size, in_start, in_start+left_size)
        root_node.right = BinaryTree.build_tree_by_pre_in_func(pre_order, in_order, pre_start+1+left_size, pre_end, in_start+left_size+1, in_end)
        return root_node

    @staticmethod
    def build_tree_by_in_post(in_order, post_order):
        res = []
        if not in_order or not post_order:
            return res
        pass


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
    root = BinaryTree.build_tree_by_pre_in(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K'],
                                           ['B', 'D', 'C', 'A', 'E', 'H', 'G', 'K', 'F'])
    tree = BinaryTree(root)
    print(tree.level_order())
