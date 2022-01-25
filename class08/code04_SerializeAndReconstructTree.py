# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二叉树

二叉树的序列化和反序列化

1）可以用先序或者中序或者后序或者按层遍历，来实现二叉树的序列化
2）用了什么方式序列化，就用什么方式反序列化

不可忽略空

应用：将内存中二叉树结构按顺序保存到文件，关机重启，再从文件复原到内存中

'''

import queue


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preSerial(head):
    '''先序 序列化'''
    preList = queue.Queue()
    pres(head, preList)
    return preList


def pres(head, preList):
    if head == None:
        preList.put(None)
    else:
        preList.put(head.value)
        pres(head.left, preList)
        pres(head.right, preList)


def buildByPreQueue(preList):
    '''先序 反序列化'''
    if preList == None or preList.qsize() == 0:
        return
    return preb(preList)


def preb(preList):
    value = preList.get()
    if value == None:
        return
    head = Node(value)
    head.left = preb(preList)
    head.right = preb(preList)
    return head


def levelSerial(head):
    '''按层 序列化 序列化时机放在加入队列的时候'''
    ans = queue.Queue()
    if head == None:
        ans.put(None)
    else:
        q = queue.Queue()
        q.put(head)
        ans.put(head.value)
        while not q.empty():
            cur = q.get()
            if cur.left != None:
                q.put(cur.left)
                ans.put(cur.left.value)
            else:
                ans.put(None)

            if cur.right != None:
                q.put(cur.right)
                ans.put(cur.right.value)
            else:
                ans.put(None)
    return ans


def buildByLevelQueue(levelList):
    '''按层 反序列化'''
    if levelList == None or levelList.qsize() == 0:
        return
    head = generateNode(levelList.get())
    q = queue.Queue()
    if head != None:
        q.put(head)
    while not q.empty():
        cur = q.get()
        cur.left = generateNode(levelList.get())
        cur.right = generateNode(levelList.get())
        if cur.left != None:
            q.put(cur.left)
        if cur.right != None:
            q.put(cur.right)
    return head


def generateNode(val):
    if val == None:
        return None
    return Node(val)


def generateRandomBST(maxLevel, maxValue):
    return generate(1, maxLevel, maxValue)


import random


def generate(level, maxLevel, maxValue):
    if level > maxValue or random.random() < 0.5:
        return
    head = Node(int(random.random() * maxValue))
    head.left = generate(level + 1, maxLevel, maxValue)
    head.right = generate(level + 1, maxLevel, maxValue)
    return head


def isSameValueStructure(head1, head2):
    if head1 == None and head2 != None:
        return False
    if head1 != None and head2 == None:
        return False
    if head1 == None and head2 == None:
        return True
    if head1.value != head2.value:
        return False
    return isSameValueStructure(head1.left, head2.left) and isSameValueStructure(head1.right, head2.right)


'''
二叉树

如何设计一个打印整颗数的打印函数(对递归的练习)

先右头左的顺序
'''

def printTree(head):
    print('Binary Tree')
    printInOrder(head, 0, 'H', 17)
    print()

def printInOrder(head, height, to, length):
    '''
    先右头左的顺序
    :param head: 当前节点
    :param height: 当前节点深度
    :param to: 节点类型（头H，左↑，右↓）
    :param length: 预留空格长度
    '''
    if head == None:
        return
    printInOrder(head.right, height + 1, '↓', length)

    val = '%s%s%s' % (to, head.value, to)
    lenM = len(val)
    lenL = (length - lenM) // 2
    lenR = length - lenM - lenL
    val = '%s%s%s' % (' ' * lenL, val, ' ' * lenR)
    print(' ' * height * length, val)

    printInOrder(head.left, height + 1, '↑', length)


if __name__ == '__main__':
    maxLevel = 5
    maxValue = 100
    testTimes = 100000
    print('test begin')
    for i in range(testTimes):
        head = generateRandomBST(maxLevel, maxValue)
        pre = preSerial(head)
        level = levelSerial(head)
        preBuild = buildByPreQueue(pre)
        levelBuild = buildByLevelQueue(level)
        if not isSameValueStructure(preBuild, levelBuild):
            print('Oops!')
    print('finish!')

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

    printTree(head)