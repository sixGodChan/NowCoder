# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
栈和队列常见面试题
1）如何用栈结构实现队列结构
用两个栈push和pop，弹出时，将push导入pop，弹出pop，
a）pop为空才能将push导入pop
b）push导入pop，必须导完

'''
from class03.code03_DoubleEndsQueueToStackAndQueue import MyStack


class TwoStackQueue():
    def __init__(self):
        self.stackPush = MyStack()
        self.stackPop = MyStack()

    # push栈向pop栈倒入数据
    def pushToPop(self):
        if self.stackPop.isEmpty():
            while not self.stackPush.isEmpty():
                self.stackPop.push(self.stackPush.pop())

    def push(self, value):
        self.stackPush.push(value)
        self.pushToPop()

    def poll(self):
        if self.stackPop.isEmpty() and self.stackPush.isEmpty():
            raise Exception('Queue is Empty!')
        self.pushToPop()
        return self.stackPop.pop()

    def peek(self):
        if self.stackPop.isEmpty() and self.stackPush.isEmpty():
            raise Exception('Queue is Empty!')
        self.pushToPop()
        return self.stackPop.peek()


if __name__ == '__main__':
    test = TwoStackQueue()
    test.push(1)
    test.push(2)
    test.push(3)
    print(test.peek())
    print(test.poll())
    print(test.peek())
    print(test.poll())
    print(test.peek())
    print(test.poll())
