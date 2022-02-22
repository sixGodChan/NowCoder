# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
暴力递归（尝试）

从左往右的尝试模型2 （背包问题）

给定两个长度都为N的数组weights和values。
weights[i]和values[i]分别代表i号物品的重量和价值。
给定一个正数bag，表示一个载重bag的袋子，
给定装的物品不能超过这个重量。
返回你能装下最多的价值是多少？
'''


def maxValue(weights, values, bag):
    return process(weights, values, bag, 0, 0)


def process(w, v, bag, i, alreadyW):
    '''
    0...i-1已确定
    i...待确定
    alreadyW已确定重量
    如果返回-1，认为没有方案
    如果不返回-1，认为返回的值是真实价值
    '''
    if alreadyW > bag:
        return -1
    if i == len(w):
        return 0
    p1 = process(w, v, bag, i + 1, alreadyW)  # 没选当前货
    p2next = process(w, v, bag, i + 1, alreadyW + w[i])  # 选择了当前货
    p2 = -1
    if p2next != -1:
        p2 = v[i] + p2next
    return max(p1, p2)


def maxValue2(weights, values, bag):
    return process2(weights, values, 0, bag)


def process2(w, v, i, rest):
    '''
    0...i-1已确定
    i...待确定
    rest袋子剩余可载重量
    如果返回-1，认为没有方案
    如果不返回-1，认为返回的值是真实价值
    '''
    if rest < 0:
        return -1
    if i == len(w):
        return 0
    p1 = process2(w, v, i + 1, rest)  # 没选当前货
    p2next = process2(w, v, i + 1, rest - w[i])  # 选择了当前货
    p2 = -1
    if p2next != -1:
        p2 = v[i] + p2next
    return max(p1, p2)


if __name__ == '__main__':
    print(maxValue([1, 2, 3], [3, 2, 1], 3))
    print(maxValue2([1, 2, 3], [3, 2, 1], 3))
