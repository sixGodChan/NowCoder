# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''

题---(找到)--->暴力递归写法（尝试）：O(N)

暴力递归写法（尝试）---(有重复解、可变参数（不讲究组织）)--->记忆化搜索：O(N*表的大小)

记忆化搜索---(精细化组织)--->经典动态规划：没有枚举复杂度与记忆化搜索一样，有枚举


# 1:11:44
题目：
arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim。
每个值都认为是一种面值，且认为张数是无限的。
返回组成aim的方法数
例如：arr = {1,2}，aim = 4
方法如下：1+1+1+1、1+1+2、2+2
一共就3种方法，所以返回3
'''


def ways(arr, aim):
    '''暴力递归'''
    if arr == None or len(arr) == 0 or aim < 0:
        return 0
    return process(arr, 0, aim)


def process(arr, i, rest):
    '''
    可以自由使用arr[i...]的所有面值，每一种面值都可以使用任意张，
    组成rest这么多钱，有多少种方法
    '''
    # 无面值的时候
    if i == len(arr):
        return 1 if rest == 0 else 0
    # 有面值的时候
    ways = 0
    zhang = 0
    while zhang * arr[i] <= rest:  # arr[i]当前面值
        ways += process(arr, i + 1, rest - (zhang * arr[i]))
        zhang += 1
    return ways


def ways2(arr, aim):
    '''记忆化搜索'''
    if arr == None or len(arr) == 0 or aim < 0:
        return 0
    dp = [[-1 for _ in range(aim + 1)] for _ in range(len(arr) + 1)]
    return process2(arr, 0, aim, dp)


def process2(arr, i, rest, dp):
    '''
    可以自由使用arr[i...]的所有面值，每一种面值都可以使用任意张，
    组成rest这么多钱，有多少种方法
    '''
    if dp[i][rest] != -1:
        return dp[i][rest]
    # 无面值的时候
    if i == len(arr):
        dp[i][rest] = 1 if rest == 0 else 0
        return dp[i][rest]
    # 有面值的时候
    dp[i][rest] = 0
    zhang = 0
    while zhang * arr[i] <= rest:  # arr[i]当前面值
        dp[i][rest] += process2(arr, i + 1, rest - (zhang * arr[i]), dp)
        zhang += 1
    return dp[i][rest]


def ways3(arr, aim):
    '''动态规划 有枚举行为'''
    if arr == None or len(arr) == 0 or aim < 0:
        return 0
    n = len(arr)
    dp = [[0 for _ in range(aim + 1)] for _ in range(n + 1)]
    dp[n][0] = 1
    # dp[n][1...aim] = 0
    for i in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            zhang = 0
            while zhang * arr[i] <= rest:  # arr[i]当前面值
                dp[i][rest] += dp[i + 1][rest - (zhang * arr[i])]
                zhang += 1
    return dp[0][aim]

def ways4(arr, aim):
    '''动态规划 枚举行为被替代'''
    if arr == None or len(arr) == 0 or aim < 0:
        return 0
    n = len(arr)
    dp = [[0 for _ in range(aim + 1)] for _ in range(n + 1)]
    dp[n][0] = 1
    # dp[n][1...aim] = 0
    for i in range(n - 1, -1, -1):
        for rest in range(aim + 1):
            dp[i][rest] = dp[i + 1][rest]  #
            if rest - arr[i] >= 0:  #
                dp[i][rest] += dp[i][rest - arr[i]] #
    return dp[0][aim]


if __name__ == '__main__':
    arr = [5, 10, 50, 100]
    aim = 1000
    print(ways(arr, aim))
    print(ways2(arr, aim))
    print(ways3(arr, aim))
    print(ways4(arr, aim))
