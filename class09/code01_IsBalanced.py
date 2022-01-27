# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二叉树的递归套路（在树上做动态规划）
（动态规划就是用时间换空间）

可以解决面试中绝大多数的二叉树问题尤其是树形dp问题
本质是利用递归遍历二叉树的便利性

======
二叉树的递归套路

1）假设以x节点为头，假设可以向x左树和x右树要任何信息
2）在上一步的假设下，讨论以x为头节点的树，得到答案的可能性（最重要）
3）列出所有可能性后，确定到底需要向左树和右树要什么样的信息
4）把左树信息和右树信息求全集，就是任何一颗子树都需要返回的信息s
5）递归函数都返回s，每一颗子树都这么要求
6）写代码，在代码中考虑如何把左树的信息和右树的信息整合出整棵树的信息

======
二叉树的递归套路深度实践

给定一颗二叉树的头节点head，返回这颗二叉树是不是平衡二叉树

解：
2）head平衡，就要求head左子树平衡，并且head右子树平衡，并且head左子树与head右子树高度差超过1
3）假设可以向head左树和head右树要其是否平衡和高度
'''


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isBalanced(head):
    return process(head).isBalanced


class info():
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def process(head):
    if head == None:
        return info(True, 0)
    leftInfo = process(head.left)
    rightInfo = process(head.right)
    height = max(leftInfo.height, rightInfo.height) + 1
    isBalanced = True
    if not leftInfo.isBalanced or not rightInfo.isBalanced or abs(leftInfo.height - rightInfo.height) > 1:
        isBalanced = False
    return info(isBalanced, height)


def isBalanced2(head):
    ans = [True]
    process2(head, ans)
    return ans[0]


def process2(head, ans):
    if not ans[0] or head == None:
        return -1
    leftHeight = process2(head.left, ans)
    rightHeight = process2(head.right, ans)
    if abs(leftHeight - rightHeight) > 1:
        ans[0] = False
    return max(leftHeight, rightHeight) + 1


# test
import random


def generateRandomBST(maxLevel, maxValue):
    return generate(1, maxLevel, maxValue)


def generate(level, maxLevel, maxValue):
    if level > maxLevel or random.random() < 0.5:
        return None
    head = Node(int(random.random() * maxValue))
    head.left = generate(level + 1, maxLevel, maxValue)
    head.right = generate(level + 1, maxLevel, maxValue)
    return head


if __name__ == '__main__':
    maxLevel = 5
    maxValue = 100
    testTimes = 1000000
    for i in range(testTimes):
        head = generateRandomBST(maxLevel, maxValue)
        if isBalanced(head) != isBalanced2(head):
            print('Oops!')
    print('finish!')

# 1:13:18
