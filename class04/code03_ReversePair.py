# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
归并排序 常见面试题

逆序对

在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对，请打印所有逆序对。

（求右侧有多少比左侧小）
[3,1,7,0,2]
(3,1) (3,0) (3,7)
(1,0)
(7,0) (7,2)
'''


def reversePair(lst):
    if lst == None or len(lst) < 2:
        return []
    l = 0
    r = len(lst) - 1
    return process(lst, l, r)


def process(lst, l, r):
    if l == r:
        return []
    mid = l + ((r - l) >> 1)
    res1 = process(lst, l, mid)
    res2 = process(lst, mid + 1, r)
    res3 = merge(lst, l, mid, r)
    return res1 + res2 + res3


def merge(lst, l, mid, r):
    i = l
    j = mid + 1
    help = []
    pairLst = []
    while i <= mid and j <= r:
        if lst[i] <= lst[j]:
            help.append(lst[i])
            i += 1
        else:
            for x in range(i, mid + 1):
                pairLst.append([lst[x], lst[j]])
            help.append(lst[j])
            j += 1
    while i <= mid:
        help.append(lst[i])
        i += 1
    while j <= r:
        help.append(lst[j])
        j += 1
    for k in range(len(help)):
        lst[k + l] = help[k]
    return pairLst


def comparator(lst):
    res = []
    if lst == None or len(lst) < 2:
        return []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                res.append([lst[i], lst[j]])
    return res


import random


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst


if __name__ == '__main__':
    testTimes = 50000
    maxSize = 5
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        res1 = reversePair(arr1)
        res2 = comparator(arr2)
        if len(res1) != len(res2):
            succeed = False
            break
        for j in res1:
            if j not in res2:
                succeed = False
                break
    print('Nice!' if succeed else 'Fucking fucked!')
