# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
选择排序
'''
import random


def selectionSort(lst):
    '''
    遍历数组，找到最小值，放到数组最前
    缩小数组范围，再次找到最小值，放到数组最前
        0 ~ N-1 范围内最小的放最前
        1 ~ N-1 范围内最小的放最前
        2 ~ N-1 范围内最小的放最前
        ...
    时间复杂度：O(n^2)
    额外空间复杂度：O(1)
    '''
    if lst == None or len(lst) < 2:
        return lst
    for i in range(len(lst)):  # 遍历i ~ N-1
        minIndex = i
        for j in range(i + 1, len(lst)):  # i ~ N-1上找最小值的下标
            minIndex = minIndex if lst[minIndex] < lst[j] else j  # 比较找到最小值下标
        lst[minIndex], lst[i] = lst[i], lst[minIndex]  # 交换
    return lst


def comparator(lst):
    '''对数器'''
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
        arr1 = selectionSort(arr1)
        arr2 = comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')