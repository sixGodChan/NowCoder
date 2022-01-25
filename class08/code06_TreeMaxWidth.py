# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二叉树

统计二叉树的最大宽度，宽度多大
哪一层的节点数量最多则宽度最大，宽度表示节点数量

建立发现层结束的标志
'''

import queue


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 二叉树按层遍历解决：使用额外map
def maxWidthUseMap(head):
    if head == None:
        return 0
    q = queue.Queue()
    q.put(head)
    levelMap = {}  # key:节点 value:属于哪层
    levelMap[head] = 1
    curLevel = 1  # 当前正在统计哪一层
    curLevelNodes = 0  # 当前层宽度是多少，从队列中取出时统计
    maxWidth = 0
    while not q.empty():
        cur = q.get()
        curNodeLevel = levelMap[cur]  # 当前节点属于哪层
        if cur.left != None:
            q.put(cur.left)
            levelMap[cur.left] = curNodeLevel + 1
        if cur.right != None:
            q.put(cur.right)
            levelMap[cur.right] = curNodeLevel + 1
        if curNodeLevel == curLevel:
            curLevelNodes += 1
        else:
            maxWidth = max(curLevelNodes, maxWidth)
            curLevel += 1
            curLevelNodes = 1
        maxWidth = max(curLevelNodes, maxWidth)
    return maxWidth


# 二叉树按层遍历解决：不用额外map
def maxWidthNoMap(head):
    if head == None:
        return 0
    q = queue.Queue()
    q.put(head)
    curEnd = head  # 当前层最右节点
    nextEnd = None  # 下一层最右节点
    curLevelNodes = 0  # 当前层节点数量,从队列中取出时统计
    maxWidth = 0
    while not q.empty():
        cur = q.get()
        if cur.left != None:
            q.put(cur.left)
            nextEnd = cur.left
        if cur.right != None:
            q.put(cur.right)
            nextEnd = cur.right
        curLevelNodes += 1
        if cur == curEnd:
          maxWidth = max(maxWidth, curLevelNodes)
          curLevelNodes = 0
          curEnd = nextEnd
    return maxWidth

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

if __name__ == '__main__':
    maxLevel = 10
    maxValue = 100
    testTimes = 100000
    for i in range(testTimes):
        head = generateRandomBST(maxLevel, maxValue)
        if maxWidthUseMap(head) != maxWidthNoMap(head):
            print('Oops!')
    print('finish!')