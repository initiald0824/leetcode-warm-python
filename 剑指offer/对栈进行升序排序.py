#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/14 21:22

# 对栈进行升序排序

from basic.Stack import Stack


def get_sort_stack(s):
    r = Stack([s.pop()])
    while not s.is_empty():
        tmp = s.pop()
        while not r.is_empty() and tmp < r.top():
            s.push(r.pop())
        r.push(tmp)
    return r


if __name__ == '__main__':
    print(get_sort_stack(Stack([3, 5, 2])).get_data())


