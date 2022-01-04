# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
栈和队列常见面试题

2）如何用队列结构实现栈结构
用两个队列,data和help，弹出时，将data中的数据导入到help，但是留1个，最后交换help和data
'''
import random
from queue import Queue

from class03.code03_DoubleEndsQueueToStackAndQueue import MyStack


class TwoQueueStack():
    def __init__(self):
        self.data = Queue()
        self.help = Queue()

    def push(self, value):
        self.data.put(value)

    def poll(self):
        while self.data.qsize() > 1:
            self.help.put(self.data.get())

        res = self.data.get()
        self.data, self.help = self.help, self.data
        return res

    def peek(self):
        while self.data.qsize() > 1:
            self.help.put(self.data.get())

        res = self.data.get()
        self.help.put(res)
        self.data, self.help = self.help, self.data
        return res

    def isEmpty(self):
        return self.data.empty()


if __name__ == '__main__':
    print('test start')
    myStack = TwoQueueStack()
    test = MyStack()
    testTime = 1000000
    max = 1000000
    for i in range(testTime):
        if myStack.isEmpty():
            if not test.isEmpty():
                print('Oops!')
            num = int(random.random() * max)
            myStack.push(num)
            test.push(num)
        else:
            if random.random() < 0.25:
                num = int(random.random() * max)
                myStack.push(num)
                test.push(num)
            elif random.random() < 0.5:
                if myStack.peek() != test.peek():
                    print('Oops!')
            elif random.random() < 0.75:
                if myStack.poll() != test.pop():
                    print('Oops!')
            else:
                if myStack.isEmpty() != test.isEmpty():
                    print('Oops!')
    print('test finish！')
