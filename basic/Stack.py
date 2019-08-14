#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/14 21:03


class Stack(object):
    def __init__(self, data=[]):
        self.data = data

    def is_empty(self):
        return len(self.data) == 0

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]
        else:
            return None

    def get_data(self):
        return self.data


