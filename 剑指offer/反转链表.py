# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/13 23:15

# 定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。
from basic.LinkedList import LinkList


def reverse_link_list(head):
    if head is None or head.next is None:
        return head
    p = head
    prev = None
    while p:
        next_node = p.next
        p.next = prev
        prev = p
        p = next_node
    return prev


if __name__ == '__main__':
    link_list = LinkList()
    link_list.init_list_tail([1, 2, 3, 4, 5])
    head = reverse_link_list(link_list.head)
    p = head
    while p:
        if p:
            print(p.data)
        p = p.next
