# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/13 23:02
# 输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第1个结点。
# 例如一个链表有6个结点，从头结点开始它们的值一次是1、2、3、4、5、6。这个链表的倒数第3个结点是值为4的结点。

from basic.LinkedList import LinkList


def get_count_back_k(head, k):
    if head is None or k <= 0:
        return None
    fast = head
    for i in range(k):
        fast = fast.next
        if fast is None:
            return None
    slow = head
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow.data


if __name__ == '__main__':
    link_list = LinkList()
    link_list.init_list_tail([1, 2, 3, 4, 5, 6])
    print(get_count_back_k(link_list.head, 3))


