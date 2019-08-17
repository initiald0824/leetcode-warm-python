# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/17 1:22

# 输入两个链表，找出它们的第一个公共结点。


from basic.LinkedList import LinkNode


def get_common_node(node_1, node_2):
    if node_1 is None or node_2 is None:
        return None
    len_1 = get_list_cnt(node_1)
    len_2 = get_list_cnt(node_2)
    if len_1 < len_2:
        return get_common_node(node_2, node_1)
    p1 = node_1
    p2 = node_2
    dis = len_1 - len_2
    while dis:
        p1 = p1.next
        dis -= 1
    while p1:
        if p1 == p2:
            return p1
        else:
            p1 = p1.next
            p2 = p2.next
    return None


def get_list_cnt(node):
    if node is None:
        return 0
    p = node
    cnt = 0
    while p:
        cnt += 1
        p = p.next
    return cnt


if __name__ == '__main__':
    node_9 = LinkNode(9, None)
    node_7 = LinkNode(7, node_9)
    head_1 = LinkNode(1, node_7)

    node_6 = LinkNode(6, node_7)
    node_5 = LinkNode(5, node_6)
    node_4 = LinkNode(4, node_5)
    node_3 = LinkNode(3, node_4)
    head_2 = LinkNode(0, node_3)

    common_node = get_common_node(head_1, head_2)
    print(common_node.data)

