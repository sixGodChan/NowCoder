# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二叉树的递归套路深度实践

给定一棵二叉树的头节点head，
返回这棵二叉树中最大的二叉搜索子树的大小（搜索二叉树是树上没有重复值，左树都比我小，右树都比我大）
（大小是二叉数节点数量）

解：
与x节点有关
左右子树都是搜索二叉树，返回左大小+右大小+1
与x节点无关
左子树或右子树是搜索二叉树，返回节点是左子树大小或右子树大小

'''


def maxSubBSTSize(head):
    if head == None:
        return 0
    return process(head).maxSubBSTSize


class info():
    def __init__(self, isAllBST, size, maxValue, minValue):
        self.isAllBST = isAllBST  # 是否为搜索二叉树
        self.maxSubBSTSize = size  # 数的大小
        self.minValue = minValue  # 整棵树最小值 (用于判断是否为搜索二叉树)
        self.maxValue = maxValue  # 整棵数最大值  (用于判断是否为搜索二叉树)


def process(head):
    if head == None:
        return None

    leftInfo = process(head.left)
    rightInfo = process(head.right)

    maxValue = head.value
    minValue = head.value

    if leftInfo != None:
        maxValue = max(maxValue, leftInfo.maxValue)
        minValue = max(minValue, leftInfo.minValue)
    if rightInfo != None:
        maxValue = max(maxValue, rightInfo.maxValue)
        minValue = max(minValue, rightInfo.minValue)

    isAllBST = False
    maxSubBSTSize = 0
    if (True if leftInfo == None else leftInfo.isAllBST) and (True if rightInfo == None else rightInfo.isAllBST) and (True if leftInfo == None else leftInfo.maxValue < head.value) and (True if rightInfo == None else rightInfo.minValue > head.value):

        maxSubBSTSize = (0 if leftInfo == None else leftInfo.maxSubBSTSize) + (
            0 if rightInfo == None else rightInfo.maxSubBSTSize) + 1

        isAllBST = True

    return info(isAllBST, maxSubBSTSize, maxValue, minValue)

# 1:57:49