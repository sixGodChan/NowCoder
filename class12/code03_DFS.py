# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
图的宽度优先&深度优先遍历

宽度优先遍历

1、利用队列实现
2、从源节点开始依次按照宽度进队列，然后弹出
3、每弹出一个点，把该节点所有没有进过队列的邻接点放入队列
4、直到队列变空

深度优先遍历

1、利用栈实现
2、从源节点开始把节点按照深度放入栈，然后弹出
3、没弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
4、直到栈变空

'''
from class12.code01_Graph import Node


def dfs(node):
    '''从node出发，进行宽度优先遍历'''
    if node == None:
        return
    stack = Stack()
    s = set()
    stack.push(node)
    s.add(node)
    print(node.value)  # 入栈打印
    while not stack.empty():
        cur = stack.pop()
        for next in cur.nexts:
            if cur not in s:
                stack.push(cur)  # 再次入栈
                stack.push(next)
                s.add(next)
                print(next.value)  # 入栈打印
                break


class Stack():
    def __init__(self):
        self.lst = []

    def push(self, value):
        self.lst.append(value)

    def pop(self):
        return self.lst.pop()

    def empty(self):
        return len(self.lst) == 0

    def gettop(self):
        return self.lst[-1]
