#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
打表法

题目三

连续M个正数和

定义一种数：可以表示成若干（数量>1）连续正数和的数
比如：
5=2+3，5就是这样的数
12=3+4+5，12就是这样的数
1不是这样的数，因为要求数量大于1个、连续正数和
2=1+1，2也不是，因为等号右边不是连续正数
给定一个参数N，返回是不是可以表示成若干连续正数和的数
'''


def isMSum1(n):
    for i in range(1, n + 1):
        sum = i
        for j in range(i + 1, n + 1):
            if sum + j > n:
                break
            if sum + j == n:
                return True
            sum += j

    return False


def isMSum2(n):
    if n < 3:
        return False
    return n & (n - 1) != 0  # n是否为2的某次方


if __name__ == '__main__':
    for i in range(1, 200):
        print(i, 'True' if isMSum1(i) else 'False')

    print('test begin')
    for i in range(1, 500):
        if isMSum1(i) != isMSum2(i):
            print('Oops!')
    print('test end')
