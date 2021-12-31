# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
栈和队列的实际实现

1）双向链表实现

'''


class Node():
    '''节点类'''

    def __init__(self, data):
        self.value = data
        self.last = None
        self.next = None


class DoubleEndsQueue():
    '''双向链表可操作类'''

    def __init__(self):
        self.head = None
        self.tail = None

    def addFromHead(self, value):
        '''头部增加节点'''
        cur = Node(value)
        if self.head == None:  # 链表为空
            self.head = cur
            self.tail = cur
        else:
            cur.next = self.head
            self.head.last = cur
            self.head = cur

    def addFromTail(self, value):
        '''尾部增加节点'''
        cur = Node(value)
        if self.head == None:  # 链表为空
            self.head = cur
            self.tail = cur
        else:
            cur.last = self.tail
            self.tail.next = cur
            self.tail = cur

    def popFromHead(self):
        '''头部弹出节点value'''
        if self.head == None:  # 链表为空
            return
        cur = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            cur.next = None
            self.head.last = None
        return cur.value

    def popFromTail(self):
        '''尾部弹出节点value'''
        if self.head == None:  # 链表为空
            return
        cur = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.last
            cur.last = None
            self.tail.next = None
        return cur.value

    def isEmpty(self):
        return self.head == None


class MyStack():
    '''实现堆类'''

    def __init__(self):
        self.stack = DoubleEndsQueue()

    def push(self, value):
        self.stack.addFromHead(value)

    def pop(self):
        return self.stack.popFromHead()

    def isEmpty(self):
        return self.stack.isEmpty()


class MyQueue():
    '''实现队列类'''

    def __init__(self):
        self.queue = DoubleEndsQueue()

    def push(self, value):
        self.queue.addFromHead(value)

    def poll(self):
        return self.queue.popFromTail()

    def isEmpty(self):
        return self.queue.isEmpty()
