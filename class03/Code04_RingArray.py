# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
栈和队列的实际实现

2）数组实现
怎么用数组实现不超过固定大小的队列和栈

栈：正常使用
队列：环形数组
'''


class MyStack():
    ''''''

    def __init__(self, limit):
        self.lst = []
        self.index = -1
        self.limit = limit

    def push(self, value):
        if self.index == self.limit - 1:
            raise Exception('栈已满，不能再加了')
        self.index += 1
        self.lst[self.index] = value

    def pop(self):
        if self.index == -1:
            raise Exception('栈已空，不能再拿了')
        res = self.lst[self.index]
        self.index -= 1
        return res

    def isEmpty(self):
        return self.index == -1


class MyQueue():
    '''循环数组实现队列'''

    def __init__(self, limit):
        self.lst = []  # 假设数组长度有限制
        self.pushi = 0  # 插入位置索引
        self.polli = 0  # 弹出位置索引
        self.size = 0  # 计数器
        self.limit = limit

    def push(self, value):
        if self.size == self.limit:
            raise Exception('队列已满，不能再加了')
        self.size += 1
        self.lst[self.pushi] = value
        self.pushi = self.nextIndex(self.pushi)

    def poll(self):
        if self.size == 0:
            raise Exception('队列已空，不能再拿了')
        self.size -= 1
        res = self.lst[self.polli]
        self.polli = self.nextIndex(self.polli)
        return res

    def isEmpty(self):
        return self.size == 0

    def nextIndex(self, index):
        '''如果现在的下标是i，返回下一个位置'''
        return (index + 1) if index < self.limit - 1 else 0

    # 1:27:19
