# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

import random


# 归并

def mergeSort(lst):
    '''先二分，再合并

    2*T(N/2) + O(N*1)
    a = 2 b = 2 d = 1
    '''
    if lst == None or len(lst) < 2:
        return
    return process(lst, 0, len(lst)-1)


def process(lst, l, r):
    if l == r:
        return
    m = l + ((r - l) >> 1)
    process(lst, l, m)
    process(lst, m + 1, r)
    merge(lst, l, m, r)


def merge(lst, l, m, r):
    helpLst = []
    leftIndex = l
    rightIndex = m + 1
    while leftIndex <= m and rightIndex <= r:
        if lst[leftIndex] <= lst[rightIndex]:
            helpLst.append(lst[leftIndex])
            leftIndex += 1
        else:
            helpLst.append(lst[rightIndex])
            rightIndex += 1
    while leftIndex <= m:
        helpLst.append(lst[leftIndex])
        leftIndex += 1
    while rightIndex <= m:
        helpLst.append(lst[rightIndex])
        rightIndex += 1

    for i in range(len(helpLst)):
        lst[l+i] = helpLst[i]


def comparator(lst):
    '''对数器'''
    lst.sort()


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst


if __name__ == '__main__':
    testTimes = 50000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        mergeSort(arr1)
        comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
