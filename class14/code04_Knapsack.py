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


def maxValue3(weights, values, bag):
    '''动态规划'''
    dp = [[0 for _ in range(bag + 1)] for _ in range(len(weights) + 1)]
    for i in range(len(weights) - 1, -1, -1):
        for rest in range(bag + 1):
            p1 = dp[i + 1][rest]
            p2 = -1
            if rest - weights[i] >= 0:
                p2 = values[i] + dp[i + 1][rest - weights[i]]
            dp[i][rest] = max(p1, p2)
    # 打印二维表
    # for i in range(len(dp)):
    #     for j in range(len(dp[i])):
    #         print(('%s' % dp[i][j]).rjust(3, ' '), end='')
    #     print()

    return dp[0][bag]


if __name__ == '__main__':
    weights = [3, 2, 4, 7, 3, 1, 7]
    values = [5, 6, 3, 19, 12, 4, 2]
    bag = 15
    print(maxValue(weights, values, bag))
    print(maxValue2(weights, values, bag))
    print(maxValue3(weights, values, bag))
