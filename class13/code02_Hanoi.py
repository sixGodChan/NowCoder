# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

# 1:19:20

'''
暴力递归（尝试）

暴力递归就是尝试
1、把问题转化为规模缩小了的同类问题的子问题
2、有明确的不需要继续进行递归的条件（base case）
3、有当得到了子问题的结果之后的决策过程
4、不记录每一个子问题的解


熟悉什么叫尝试？

题目
打印n层汉诺塔从最左边移动到最右边的全部过程（递归+非递归实现）
打印一个字符串的全部子序列
打印一个字符串的全部子序列，要求不要出现重复字面值的子序列
打印一个字符串的全部排列
打印一个字符串的全部排列，要求不要出现重复的排列


结论：n层汉诺塔问题，最优步骤是2^n-1
'''


def hanoi1(n):
    '''汉诺塔1'''
    LeftToRight(n)


def LeftToRight(n):
    '''将n层圆盘从左移到右,移动1~n个'''
    if n == 1:
        print('Move 1 from Left to Right')
        return
    LeftToMid(n - 1)
    print('Move', n, 'from Left to Right')
    MidToRight(n - 1)


def LeftToMid(n):
    '''将n层圆盘从左移到中'''
    if n == 1:
        print('Move 1 from Left to Mid')
        return
    LeftToRight(n - 1)
    print('Move', n, 'from Left to Mid')
    RightToMid(n - 1)


def MidToRight(n):
    if n == 1:
        print('Move 1 from Mid to Right')
        return
    MidToLeft(n - 1)
    print('Move', n, 'from Mid to Right')
    LeftToRight(n - 1)


def RightToMid(n):
    if n == 1:
        print('Move 1 from Right to Mid')
        return
    RightToLeft(n - 1)
    print('Move', n, 'from Right to Mid')
    LeftToMid(n - 1)


def MidToLeft(n):
    if n == 1:
        print('Move 1 from Mid to Left')
        return
    MidToRight(n - 1)
    print('Move', n, 'from Mid to Left')
    RightToLeft(n - 1)


def RightToLeft(n):
    if n == 1:
        print('Move 1 from Right to Left')
        return
    RightToMid(n - 1)
    print('Move', n, 'from Right to Left')
    MidToLeft(n - 1)


def hanoi2(n):
    if n > 0:
        func(n, 'Left', 'Right', 'Mid')


def func(n, fromWhere, to, other):
    '''移动1~n个，从from移动to，另外一个位置other'''
    if n == 1:
        print('Move 1 from', fromWhere, 'to', to)
        return
    func(n - 1, fromWhere, other, to)
    print('Move', n, 'from', fromWhere, 'to', to)
    func(n - 1, other, to, fromWhere)


if __name__ == '__main__':
    n = 3
    hanoi1(n)
    print('=' * 10)
    hanoi2(n)
