#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/14 20:20

# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。在该栈中，调用min、push、及pop的时间复杂度都是O(1)。


from basic.Stack import Stack


class MyStack(Stack):
    def __init__(self, data=[]):
        super().__init__(data)
        self.record = []
        for index, val in enumerate(data):
            if index == 0:
                self.record.append(val)
            else:
                if val < self.record[-1]:
                    self.record.append(val)

    def push(self, val):
        super().push(val)
        if not self.record or val < self.record[-1]:
            self.record.append(val)

    def pop(self):
        pop_val = super().pop()
        if pop_val == self.record[-1]:
            self.record.pop()

    def get_min(self):
        if self.record:
            return self.record[-1]
        else:
            return None


if __name__ == '__main__':
    s = MyStack([3, 5, 2])
    print(s.get_min())
    s.pop()
    print(s.get_min())
    s.pop()
    print(s.get_min())
    s.pop()
    print(s.get_min())


