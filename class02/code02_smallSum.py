# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random


def smallSum(lst):
    '''小和问题
    在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。
    求一个数组的小和。

    （求右侧有多少比左侧大）
    '''
    if lst == None or len(lst) < 2:
        return 0
    return process(lst, 0, len(lst) - 1)


def process(lst, l, r):
    '''lst[l...r]既要排好序 又要求小和'''
    if l == r:
        return 0
    m = l + ((r - l) >> 1)
    return process(lst, l, m) + process(lst, m + 1, r) + merge(lst, l, m, r)


def merge(lst, l, m, r):
    res = 0
    helpLst = []
    p1 = l
    p2 = m + 1
    while p1 <= m and p2 <= r:
        if lst[p1] < lst[p2]:
            res += lst[p1] * (r - p2 + 1)
            helpLst.append(lst[p1])
            p1 += 1
        else:
            helpLst.append(lst[p2])
            p2 += 1
    while p1 <= m:
        helpLst.append(lst[p1])
        p1 += 1
    while p2 <= r:
        helpLst.append(lst[p2])
        p2 += 1

    for i in range(len(helpLst)):
        lst[l + i] = helpLst[i]
    return res


def comparator(lst):
    res = 0
    if lst == None or len(lst) < 2:
        return res
    for i in range(len(lst)):
        for j in range(i):
            if lst[j] < lst[i]:
                res += lst[j]
    return res


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst


if __name__ == '__main__':
    # a = [1, 3, 4, 2, 5]
    # b = a.copy()
    # print(littleSum(a))
    # print(comparator(b))
    testTimes = 500000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        res1 = smallSum(arr1)
        res2 = comparator(arr2)
        print(arr1)
        if res1 != res2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
