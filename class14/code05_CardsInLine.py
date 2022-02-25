# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
暴力递归（尝试）

范围上尝试的模型

给定整形数组arr，代表数值不同的纸牌排成一条线，
玩家A和玩家B依次拿走每张纸牌，
规定玩家A先拿，玩家B后拿，
但是每个玩家每次只能拿走最左或最右的纸牌，
玩家A和玩家B都决定聪明。请返回最后获胜者的分数。

'''


def win1(arr):
    if arr == None or len(arr) == 0:
        return 0
    return max(f(arr, 0, len(arr) - 1), s(arr, 0, len(arr) - 1))


def f(arr, l, r):
    '''在arr[l:r]先手拿'''
    if l == r:  # 只剩1张，拿走
        return arr[l]
    return max(arr[l] + s(arr, l + 1, r), arr[r] + s(arr, l, r - 1))  # 变后手


def s(arr, l, r):
    '''在arr[l:r]后手拿'''
    if l == r:  # 只剩1张，没得拿
        return 0
    return min(f(arr, l + 1, r), f(arr, l, r - 1))  # 对手只会留下小的 变先手


def win3(arr):
    '''动态规划'''
    if arr == None or len(arr) == 0:
        return 0
    n = len(arr)
    dpf = [[0 for _ in range(n)] for _ in range(n)]
    dps = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dpf[i][i] = arr[i]

    # dps[i][i] = 0

    for i in range(1, n):
        l = 0
        r = i
        while l < n and r < n:
            dpf[l][r] = max(arr[l] + dps[l + 1][r], arr[r] + dps[l][r - 1])
            dps[l][r] = min(dpf[l + 1][r], dpf[l][r - 1])
            l += 1
            r += 1

    # # 打印二维表
    # for i in range(len(dpf)):
    #     for j in range(len(dpf[i])):
    #         print(('%s' % dpf[i][j]).rjust(4, ' '), end='')
    #     print()
    # print('=====')
    # for i in range(len(dps)):
    #     for j in range(len(dps[i])):
    #         print(('%s' % dps[i][j]).rjust(4, ' '), end='')
    #     print()

    return max(dpf[0][n - 1], dps[0][n - 1])


if __name__ == '__main__':
    print(win1([70, 100, 1, 4]))
    print(win3([70, 100, 1, 4]))
    # print(win1([5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 6, 1, 7]))
    # print(win3([5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 6, 1, 7]))
