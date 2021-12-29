# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
插入排序
'''
import random


def insertionSort(lst):
    '''
    先让0~0位置有序，再让0~1位置有序，再让0~2位置有序，...最后数组完全有序
    插入排序的工作方式像排序一手扑克牌
        0 ~ 1 两两比较，最小的放最前
        0 ~ 2 两两比较，最小的放最前
        0 ~ 3 两两比较，最小的放最前
        ...
    时间复杂度：最差O(n^2) 最好O(n)
    额外空间复杂度：O(1)
    '''
    if lst == None or len(lst) < 2:
        return lst
    # 0 ~ 0 有序
    # 0 ~ i 想有序
    for i in range(1, len(lst)):  # 0 ~ i 做到有序
        for j in range(i - 1, -1, -1):
            if j >= 0 and lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def comparator(lst):
    return sorted(lst)


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
        arr1 = insertionSort(arr1)
        arr2 = comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
