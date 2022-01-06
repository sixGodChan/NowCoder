# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi


import random


def reversePair(lst):
    '''逆序对问题
    在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对，请打印所有逆序对。

    需要逆序 （求右侧有多少比左侧小）
    '''
    if lst == None or len(lst) < 2:
        return []
    return process(lst, 0, len(lst) - 1)


def process(lst, l, r):
    if l == r:
        return []
    m = l + ((r - l) >> 1)
    return process(lst, l, m) + process(lst, m + 1, r) + merge(lst, l, m, r)


def merge(lst, l, m, r):
    res = []
    helpLst = []
    p1 = l
    p2 = m + 1
    while p1 <= m and p2 <= r:
        if lst[p2] >= lst[p1]:
            helpLst.append(lst[p2])
            p2 += 1
        else:
            for i in range(p2, r + 1):
                res.append([lst[p1], lst[i]])
            helpLst.append(lst[p1])
            p1 += 1

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
    res = []
    if lst == None or len(lst) < 2:
        return []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                res.append([lst[i], lst[j]])
    return res


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst



if __name__ == '__main__':
    # a = [3, 2, 4, 5, 0]
    # b = a.copy()
    # r1 = reversePair(a)
    # r2 = comparator(b)
    testTimes = 50000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        res1 = reversePair(arr1)
        res2 = comparator(arr2)
        print(res2)
        print(res1)
        if len(res1) != len(res2):
            succeed = False
            break
        for j in res1:
            if j not in res2:
                succeed = False
                break
    print('Nice!' if succeed else 'Fucking fucked!')