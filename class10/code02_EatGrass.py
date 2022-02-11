#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
打表法

题目二

给定一个正整数N，表示有N份青草统一放在仓库里
有一只牛和一只羊，牛先吃，羊后吃，他俩轮流吃草
不管是牛还是羊，每一轮能吃的草量必须是：
1，4，16，64……（4的某次方）
谁最先把草吃完，谁获胜
假设牛和羊都绝顶聪明，谁懂想赢，都会做出理性的决定
根据唯一的参数N，返回谁会赢
'''


def winner1(n):
    # 0  1  2  3  4
    # 后 先 后  先 先
    if n < 5:
        return '后手' if n == 0 or n == 2 else '先手'
    base = 1
    while base <= n:
        if winner1(n - base) == '后手':
            return '先手'
        if base > (n // 4):  # 防止base*4之后溢出
            break
        base *= 4
    return '后手'

def winner2(n):
    if n % 5 == 0 or n % 5 == 2:
        return '后手'
    else:
        return '先手'


if __name__ == '__main__':
    for i in range(50):
        print(i, ':', winner1(i))

    for i in range(50):
        if winner1(i)!=winner2(i):
            print('Oops!')
    print('finish')

# 1:03:28