# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
二叉树的递归套路深度实践

派对的最大快乐值问题

员工信息定义如下：
class Employee():
    def __init__(self, happy):
        self.happy = happy  # 这个员工可以带来的快乐值
        self.subordinates = []  # 这名员工有哪些直接下级

公司的每个员工都符合Employee类的描述。整个公司的人员结构可以看作
是一颗标准的、没有环的多叉树。树的头节点是公司唯一的老板。除老板之
外的每一个员工都有唯一的直接上级。叶节点是没有任何下属的基层员工
（subordinates列表为空），除基层额员工外，每个员工都有一个或多个直接下级。

这个公司现在要办party，你可以决定哪些员工来，哪些员工不来，规则：
1.如果某个员工来了，那么这个员工的所有直接下级都不能来
2.派对的整体快乐值是所有到场员工快乐值的累加
3.你的目标是让派对的的整体快乐值尽量大
给定一棵多叉树的头节点boss，请返回派对的最大快乐值。
'''

'''
二叉树的递归套路
1）假设以x节点为头，假设可以向x左树和x右树要任何信息
2）在上一步的假设下，讨论以x为头节点的树，得到答案的可能性（最重要）
3）列出所有可能性后，确定到底需要向左树和右树要什么样的信息
4）把左树信息和右树信息求全集，就是任何一颗子树都需要返回的信息s
5）递归函数都返回s，每一颗子树都这么要求
6）写代码，在代码中考虑如何把左树的信息和右树的信息整合出整棵树的信息
'''

'''
解：
1）x不来
获取其下级们来或不来的最大快乐值中的max

2）x来
获取x的快乐值，然后其下级都不来的最大快乐值的和


'''


class Employee():
    def __init__(self, happy):
        self.happy = happy  # 这个员工可以带来的快乐值
        self.nexts = []  # 这名员工有哪些直接下级


def maxHappy(head):
    allInfo = process(head)
    return max(allInfo.yes, allInfo.no)


class info():
    def __init__(self, yes, no):
        self.yes = yes  # 当前节点来的最大happy值
        self.no = no  # 当前节点不来的最大happy值


def process(head):
    if len(head.nexts) == 0:
        return info(head.happy, 0)
    yes = head.happy
    no = 0
    for next in head.nexts:
        nextInfo = process(next)
        yes += nextInfo.no
        no += max(nextInfo.yes, nextInfo.no)
    return info(yes, no)
