# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
贪心算法的解题套路实战

输入：正数数组costs、正数数组profits、正数K、正数M

costs[i]表示i号项目的花费
profits[i]表示i号项目在扣除花费之后还能挣到的钱（利润)
K表示你只能串行的最多做k个项目
M表示你初始的资金
说明：每做完一个项目，马上获得的收益，可以支持你去做下一个项目。不能并行的做项目。
输出：你最后获得的最大钱数。
'''


def getMostMoney(costs, profits, k, m):
    '''暴力'''
    if k <= 0:
        return m
    money = m
    for i in range(len(costs)):
        if m >= costs[i]:
            nextcosts, nextprofits = copyButExcept(costs, profits, i)
            money = max(money, getMostMoney(nextcosts, nextprofits, k - 1, m + profits[i]))
    return money


def copyButExcept(costs, profits, i):
    nextcosts, nextprofits = [], []
    for k in range(len(costs)):
        if i != k:
            nextcosts.append(costs[k])
            nextprofits.append(profits[k])
    return nextcosts, nextprofits


import heapq


class Program():
    def __init__(self, costs, profits):
        self.costs = costs
        self.profits = profits

    def __lt__(self, other):  # 小根
        return self.costs < other.costs


class Program2():
    def __init__(self, costs, profits):
        self.costs = costs
        self.profits = profits

    def __lt__(self, other):  # 大根用
        return self.profits > other.profits


def getMostMoney2(costs, profits, k, m):
    '''贪心
    根据花费入小根堆，解锁小于等于初始金额的花费
    根据利润入大根堆，大根堆出堆，
    修改初始金额，从头继续'''
    minCostQ = []
    maxProfitQ = []
    for i in range(len(costs)):
        heapq.heappush(minCostQ, Program(costs[i], profits[i]))
    for _ in range(k):
        while len(minCostQ) != 0 and minCostQ[0].costs <= m:  # 解锁
            p = heapq.heappop(minCostQ)
            heapq.heappush(maxProfitQ, Program2(p.costs, p.profits))
        if len(maxProfitQ) == 0:  # 无项目可做 提前结束
            return m
        m += heapq.heappop(maxProfitQ).profits
    return m


import random


def generateRandomArray(maxSize, maxValue):
    costs = []
    profits = []
    for i in range(int(random.random() * (maxSize + 1))):
        costs.append(int(random.random() * (maxValue + 1)))
        profits.append(int(random.random() * (maxValue + 1)))
    return costs, profits


if __name__ == '__main__':
    testTimes = 100
    maxSize = 10
    maxValue = 10
    for i in range(testTimes):
        costs, profits = generateRandomArray(maxSize, maxValue)
        m = int(random.random() * maxValue)
        k = int(random.random() * len(costs))
        if getMostMoney(costs, profits, k, m) != getMostMoney2(costs, profits, k, m):
            print('Oops!')
    print('finish!')

    # costs = [1, 1, 4, 5]
    # profits = [3, 1, 3, 2]
    # m = 1
    # k = 2
    # print(getMostMoney(costs, profits, k, m))
    # print(getMostMoney2(costs, profits, k, m))
