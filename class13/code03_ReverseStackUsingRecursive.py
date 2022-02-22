# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
仰望好的尝试？

给你一个栈，请你逆序这个栈，
不能申请额外的数据结构，
只能使用递归函数。如何实现？

揭示了递归栈可以保存一些信息
'''


def reverse(stack):
    '''将栈逆序'''
    if stack.isEmpty():
        return
    res = f(stack)
    reverse(stack)
    stack.push(res)


def f(stack):
    '''只将栈底最后一个数据取出并返回，不改变栈中其他数据结构'''
    result = stack.pop()
    if stack.isEmpty():
        return result
    else:
        last = f(stack)
        stack.push(result)
        return last


class Stack():
    def __init__(self):
        self.lst = []

    def push(self, val):
        self.lst.append(val)

    def pop(self):
        return self.lst.pop()

    def isEmpty(self):
        return len(self.lst) == 0


if __name__ == '__main__':
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.push(5)
    reverse(test)
    while not test.isEmpty():
        print(test.pop())
