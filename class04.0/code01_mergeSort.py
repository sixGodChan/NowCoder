# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random


def mergeSort(lst):
    '''归并排序

    本问题可以使用master公式求解时间复杂度  T(N) = a * T(N/b) + O(N^d)
        N 问题规模
        T(N) 母问题
        T(N/b) 子问题
        a 子问题被调用次数，子问题是等量的情况下，被调用次数
        d 除去调用子问题之外，剩下问题的时间复杂度

        1) 如果log(b,a)<d,时间复杂度是O(N^d)  # log(b,a)=log以b为低a的对数
        2) 如果log(b,a)=d,时间复杂度是O(N^d*logN)
        3) 如果log(b,a)>d,时间复杂度是O(N^log(b,a))

    本函数 a = 2 b = 2 d = 1

        log(b,a)=d
        O(N*logN)
    空间复杂度O(N)
    '''
    if lst == None or len(lst) < 2:
        return
    return process(lst, 0, len(lst) - 1)


def process(lst, l, r):
    if l == r:
        return
    mid = l + ((r - l) >> 1)
    process(lst, l, mid)  # 左侧排序
    process(lst, mid + 1, r)  # 右侧排序
    merge(lst, l, mid, r)  # 合并在一起


def merge(lst, l, m, r):
    helpLst = []
    p1 = l
    p2 = m + 1
    while p1 <= m and p2 <= r:
        if lst[p1] <= lst[p2]:
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


def comparator(lst):
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
