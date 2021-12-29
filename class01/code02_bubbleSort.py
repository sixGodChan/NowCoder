# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random


def bubbleSort(lst):
    '''
    它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果顺序（如从大到小、首字母从Z到A）错误就把他们交换过来。走访元素的工作是重复
    地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成。
    0 ~ N-1 从头开始两两比较，最大的放最后
    0 ~ N-2 从头开始两两比较，最大的放最后
    0 ~ N~3 从头开始两两比较，最大的放最后
    ...

    时间复杂度：O(n^2)
    空间复杂度：O(1)
    '''
    if lst == None or len(lst) < 2:
        return lst
    for i in range(len(lst)):  # 循环N次
        for j in range(len(lst) - i - 1):  # 0 ~ N-i之间两两交换
            if lst[j] > lst[j + 1]:
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
        arr1 = bubbleSort(arr1)
        arr2 = comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
