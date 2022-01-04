# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
栈和队列常见面试题
实现一个特殊的栈，在基本功能的基础上，再实现返回栈中最小元素的功能

1）pop、push、getMin操作的时间复杂度都是O（1）

2）设计的栈类型可以使用现成的栈结构


方法1：实现两个栈，一个正常记录value，一个记录当min（当前栈顶，value），弹出时都弹出
方法2：实现两个栈，一个正常记录value，一个当value<=前栈顶才记录，第二个栈与value相等时弹出
'''

from class03.code03_DoubleEndsQueueToStackAndQueue import MyStack


class MyStack1():
    ''''''
    def __init__(self):
        self.stackData = MyStack()
        self.stackMin = MyStack()

    def push(self, value):
        top = self.stackData.pop()
        self.stackData.push(top)
        if self.stackData.isEmpty():
            self.stackMin.push(value)
        elif value < self.getMin():
            self.stackMin.push(value)
        else:
            self.stackMin.push(self.getMin())
        self.stackData.push(value)

    def pop(self):
        if self.stackData.isEmpty():
            raise Exception('栈已空')
        self.stackMin.pop()
        return self.stackData.pop()

    def getMin(self):
        if self.stackData.isEmpty():
            raise Exception('栈已空')
        top = self.stackMin.pop()
        self.stackData.push(top)
        return top

class MyStack2():
    ''''''
    def __init__(self):
        self.stackData = MyStack()
        self.stackMin = MyStack()

    def push(self, value):
        if self.stackData.isEmpty():
            self.stackMin.push(value)
        elif value < self.getMin():
            self.stackMin.push(value)
        self.stackData.push(value)

    def pop(self):
        if self.stackData.isEmpty():
            raise Exception('栈已空')
        top = self.stackMin.pop()
        topData = self.stackData.pop()
        if top != topData:
            self.stackMin.push(top)
        return topData

    def getMin(self):
        if self.stackData.isEmpty():
            raise Exception('栈已空')
        top = self.stackMin.pop()
        self.stackData.push(top)
        return top
    # 1:36:20