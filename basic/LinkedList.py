# !/usr/bin/env python3
# coding: utf-8
# Author: initiald0824
# Date: 2019/8/10 19:23


class LinkNode(object):
    def __init__(self, data, node=None):
        self.data = data
        self.next = node


class LinkList(object):
    def __init__(self):
        self.head = None

    def init_list_tail(self, data):
        self.head = LinkNode(data[0])
        p = self.head
        for i in data[1:]:
            p.next = LinkNode(i)
            p = p.next

    def is_empty(self):
        return self.head is None

    def print_list(self):
        p = self.head
        while p:
            print(p.data, end=' ')
            p = p.next
        print('')

    def get_length(self):
        if self.is_empty():
            return 0
        p = self.head
        length = 0
        while p:
            p = p.next
            length += 1
        return length

    def reverse(self):
        if not self.head or not self.head.next:
            return self.head
        p = self.head
        prev = None
        while p:
            next_node = p.next
            p.next = prev
            prev = p
            p = next_node
        self.head = prev


if __name__ == '__main__':
    link_list = LinkList()
    link_list.init_list_tail([1, 2, 3, 4, 5, 6])
    link_list.print_list()
    link_list.reverse()
    link_list.print_list()

