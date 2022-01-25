# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
二叉树

非递归方式实现二叉树的先序、中序后序遍历
1）任何递归都可以改为非递归
2）自己设计的压栈来实现

'''

from class03.code03_DoubleEndsQueueToStackAndQueue import MyStack


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre(head):
    '''
    栈：先序
    1弹出就打印
    2如有右，压入右
    3如有左，压入左
    '''
    print('pre order:')
    if head != None:
        stack = MyStack()
        stack.push(head)
        while not stack.isEmpty():
            head = stack.pop()
            print(head.value, ' ', end='')  # 1弹出就打印
            if head.right != None:  # 2如有右，压入右
                stack.push(head.right)
            if head.left != None:  # 3如有左，压入左
                stack.push(head.left)
    print()


def pos(head):
    '''
    栈：后序
    1弹出再压入新栈
    2如有左，压入左
    3如有右，压入右
    '''
    print('pos order:')
    if head != None:
        stack = MyStack()
        pstack = MyStack()
        stack.push(head)
        while not stack.isEmpty():
            head = stack.pop()
            pstack.push(head.value)  # 1弹出再压入新栈
            if head.left != None:  # 2如有左，压入左
                stack.push(head.left)
            if head.right != None:  # 3如有右，压入右
                stack.push(head.right)
    while not pstack.isEmpty():
        print(pstack.pop(), ' ', end='')
    print()


def mid(head):
    '''
    栈：中序
    1整条左边界，依次入栈
    2当1无法继续，弹出并打印，来到弹出节点的右子树数继续执行1
    '''
    print('mid order:')
    if head != None:
        stack = MyStack()
        while not stack.isEmpty() or head != None:
            if head != None:
                stack.push(head)
                head = head.left
            else:
                head = stack.pop()
                print(head.value, ' ', end='')
                head = head.right
        print()


def pos2(head):
    '''只用一个栈'''
    print('pos2 order:')
    if head != None:
        stack = MyStack()
        stack.push(head)
        while not stack.isEmpty():
            c = stack.peek()
            if c.left != None and c.left != head and c.right != head:
                stack.push(c.left)
            elif c.right != None and c.right != head:
                stack.push(c.right)
            else:
                print(stack.pop().value, ' ', end='')
                head = c
    print()


# 1:13:36

if __name__ == '__main__':
    '''
          1
      2       3
    4   5   6   7
    '''
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)

    pre(head)
    print('=' * 20)
    mid(head)
    print('=' * 20)
    pos(head)
    print('=' * 20)
    pos2(head)
