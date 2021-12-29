# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random


def selectionSort(lst):
    '''
    第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，然后放
    到已排序的序列的末尾。以此类推，直到全部待排序的数据元素的个数为零
    0 ~ N-1 范围内最小的放最前
    1 ~ N-1 范围内最小的放最前
    2 ~ N-1 范围内最小的放最前
    ...

    时间复杂度：O(n^2)
    空间复杂度：O(1)
    '''
    if lst == None or len(lst) < 2:
        return lst
    for i in range(len(lst)):  # i ~ N-1
        minIndex = i
        for j in range(i + 1, len(lst)):  # i ~ N-1上找最小值的下标
            minIndex = minIndex if lst[minIndex] < lst[j] else j
        lst[minIndex], lst[i] = lst[i], lst[minIndex]
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