#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/17 19:52

# 给定一个有环链表，实现一个算法返回环路的开头结点。
from basic.LinkedList import LinkNode


def get_ring_start(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == '__main__':
    node_3 = LinkNode(3, None)
    node_6 = LinkNode(6, node_3)
    node_5 = LinkNode(5, node_6)
    node_4 = LinkNode(4, node_5)
    node_2 = LinkNode(2, node_3)
    node_1 = LinkNode(1, node_2)
    node_3.next = node_4
    print(get_ring_start(node_1).data)

