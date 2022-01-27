# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二叉树的递归套路深度实践

给定一棵二叉树的头节点head，任何两个节点之间都存在距离，
返回整棵二叉树的最大距离

解：
最大距离与x无关
1）以head开始，可以向左右子树要任何信息
2）max（左子树最大距离，右子树最大距离） = 最大距离
3）可以向左右子树要其最大距离和高度
最大距离与x有关
1）左树高度+1+右树高度
'''


def maxDistance(head):
    return process(head).maxDistance


class info():
    def __init__(self, maxDistance, height):
        self.maxDistance = maxDistance
        self.height = height


def process(head):
    if head == None:
        return info(0, 0)
    leftInfo = process(head.left)
    rightInfo = process(head.right)
    maxDistance = max(max(leftInfo.maxDistance, rightInfo.maxDistance), leftInfo.height + rightInfo.height + 1)
    height = max(leftInfo.height, rightInfo.height) + 1
    return info(maxDistance, height)
