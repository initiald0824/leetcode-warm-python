# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/13 23:32

# 输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。
# 链表1：  1 -> 3 -> 5 -> 7
# 链表2：  2 -> 4 -> 6 -> 8
# 合并后： 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
from basic.LinkedList import LinkNode, LinkList


def merge_sorted_link_list(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    dummy = LinkNode(None)
    p = dummy
    p1 = head1
    p2 = head2
    while p1 and p2:
        if p1.data < p2.data:
            p.next = LinkNode(p1.data)
            p1 = p1.next
        else:
            p.next = LinkNode(p2.data)
            p2 = p2.next
        p = p.next
    if p1:
        p.next = p1
    if p2:
        p.next = p2
    return dummy.next


if __name__ == '__main__':
    l1 = LinkList()
    l1.init_list_tail([1, 3, 5, 7])
    l2 = LinkList()
    l2.init_list_tail([2, 4, 6, 8])
    head = merge_sorted_link_list(l1.head, l2.head)
    p = head
    while p:
        if p:
            print(p.data)
        p = p.next
