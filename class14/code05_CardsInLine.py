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


if __name__ == '__main__':
    print(win1([70, 100, 1, 4]))
