# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
递归
求数组中的最大值，递归实现
1）将数组分为最右两部分，
2）递归过程，左部分求做大值，右部分求最大值

'''

import random


'''
    本问题可以使用master公式求解时间复杂度  T(N) = a * T(N/b) + O(N^d)
        a、b、d都是常数
        N 规模
        T(N) 母问题规模 N
        T(N/b) 子问题规模 N/b
        a 子问题被调用次数，子问题是等量的情况下，被调用次数
        d 除去调用子问题之外，剩下问题的时间复杂度

        1) 如果log(b,a)<d,时间复杂度是O(N^d)  # log(b,a)=log以b为低a的对数
        2) 如果log(b,a)=d,时间复杂度是O(N^d*logN)
        3) 如果log(b,a)>d,时间复杂度是O(N^log(b,a))

    本函数时间复杂度符合master公式 T(N) = 2 * T(N/2) + O(1)
        a = 2
        b = 2
        d = 0

        log(2,2)>0  # log(2,2) = 1
        时间复杂度O(N^1)
'''

def getMax(lst):
    '''
    O(N)
    '''
    if lst == None or len(lst) < 2:
        return
    l = 0
    r = len(lst) - 1
    return process(lst, l, r)


def process(lst, l, r):
    if l == r:  # 只有一个值，最大值就只这个值
        return lst[l]

    mid = l + ((r - l) >> 1)  # 中点
    lmax = process(lst, l, mid)
    rmax = process(lst, mid + 1, r)
    return max(lmax, rmax)


def comparator(lst):
    if lst == None or len(lst) < 2:
        return
    return max(lst)


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst


if __name__ == '__main__':
    testTimes = 100000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        res1 = getMax(arr1)
        res2 = comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
