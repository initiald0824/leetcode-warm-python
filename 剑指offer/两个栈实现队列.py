#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author initiald0824
# @Time 2019/8/12 19:17


class MyQueue(object):
    def __init__(self, stack1=[], stack2=[]):
        self.stack1 = stack1
        self.stack2 = stack2

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if self.stack2:
            print(self.stack2.pop())
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                print(self.stack2.pop())
            else:
                raise Exception("Queue is empty")


if __name__ == '__main__':
    my_queue = MyQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.dequeue()
    my_queue.enqueue(4)
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
