# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二叉树

实现二叉树的按层遍历
1）其实就是宽度优先遍历，用队列
2）可以通过设置flag变量的方式，来发现某一层的结束（看题目code07）
'''
import queue

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level(head):
    '''从头节点开始一层一层打印'''
    if head == None:
        return
    q = queue.Queue()
    q.put(head)
    while not q.empty():
        tmp = q.get()
        print(tmp.value, ' ', end='')
        if tmp.left != None:
            q.put(tmp.left)
        if tmp.right != None:
            q.put(tmp.right)

# 1:20:39

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

    level(head)
