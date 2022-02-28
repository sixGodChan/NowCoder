# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
寻找业务限制的尝试模型

题目
给定一个数组arr，代表每个人喝完咖啡准备刷杯子的时间(arr有序)
只有一台清洗机，一次只能洗一个杯子，时间耗费a，洗完才能洗下一杯
每个咖啡杯也可以自己挥发干净，时间耗费b，咖啡杯可以并行挥发
返回让所有咖啡杯变干净的最早完成时间
三个参数：arr, a, b
'''

import sys

def minTime1(arr, a, b):
    return process(arr, a, b, 0, 0)


def process(drinks, a, b, index, washLine):
    '''
    drinks, a, b 固定参数
    drinks[0...index-1]已洗完不用管
    washLine表示清洗机何时可用
    从时间点washLine开始洗完drinks[index...]这些杯子的最早时间
    '''
    if index == len(drinks) - 1:  # 最后一个杯
        return min(max(drinks[index], washLine) + a, drinks[index] + b)
    # 不是最后一杯
    # drinks[index]洗
    wash = max(drinks[index], washLine) + a
    next1 = process(drinks, a, b, index + 1, wash)
    p1 = max(wash, next1)
    # drinks[index]挥发
    dry = drinks[index] + b
    next2 = process(drinks, a, b, index + 1, washLine)
    p2 = max(dry, next2)
    return min(p1, p2)


def minTime2(arr, a, b):
    '''
    动态归化
    '''
    drinks = arr
    n = len(drinks)

    if a >= b:  # 清洗时间大于等于挥发时间
        return drinks[n - 1] + b

    limit = 0  # washLine的最大值，就是都洗最终时间
    for i in range(n):
        limit = max(limit, drinks[i]) + a

    dp = [[0 for _ in range(limit + 1)] for _ in range(n)]

    for washLine in range(limit + 1):
        dp[n - 1][washLine] = min(max(drinks[n - 1], washLine) + a, drinks[n - 1] + b)

    for index in range(n - 2, -1, -1):
        for washLine in range(limit + 1):
            p1 = sys.maxsize
            wash = max(drinks[index], washLine) + a
            if wash <= limit:
                next1 = dp[index + 1][wash]
                p1 = max(wash, next1)
            # drinks[index]挥发
            dry = drinks[index] + b
            next2 = dp[index + 1][washLine]
            p2 = max(dry, next2)
            dp[index][washLine] = min(p1, p2)
    return dp[0][0]


if __name__ == '__main__':
    arr = [2, 2, 3, 4, 5, 6, 12, 15, 15, 16, 18]
    a = 3
    b = 10
    print(minTime1(arr, a, b))
    print(minTime2(arr, a, b))
