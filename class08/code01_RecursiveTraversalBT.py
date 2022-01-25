# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二叉树

结构描述：
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

======

二叉树的先序、中序、后序遍历
先序：任何子树的处理顺序都是，先头结点、再左子树、然后右子树
中序：任何子树的处理顺序都是，先左子树、再头结点、然后右子树
后序：任何子树的处理顺序都是，先左子树、再右子树、然后头结点

======
递归方式实现二叉树的先序、中序后序遍历
1）理解递归序
2）先序、中序、后序都可以再递归序的基础上加工出来
3）第一次到达一个节点就打印就是先序、第二次打印即中序、第三次即后序

'''


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def f(head):
    # 递归序 一个节点会在函数中出现三次
    if head == None:
        return
    # 1
    f(head.left)
    # 2
    f(head.right)
    # 3


def pre(head):
    '''先序打印所有节点'''
    if head == None:
        return
    print(head.value, '', end='')
    pre(head.left)
    pre(head.right)


def mid(head):
    '''中序打印所有节点'''
    if head == None:
        return
    mid(head.left)
    print(head.value, '', end='')
    mid(head.right)


def pos(head):
    '''后序打印所有节点'''
    if head == None:
        return
    pos(head.left)
    pos(head.right)
    print(head.value, '', end='')

# 0:22:22

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
    print()
    print('=' * 20)
    mid(head)
    print()
    print('=' * 20)
    pos(head)
    print()
    print('=' * 20)
