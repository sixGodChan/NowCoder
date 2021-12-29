# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
二分法 应用
在有序数组中找到>=value的最左位置
[1,2,2,2,2,2,3,3,3,3,4,4,4] 2
   ↑
'''

import random


def nearsetIndex(lst, value):
    '''
    O(logN)
    '''
    l = 0
    r = len(lst) - 1
    index = -1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if lst[mid] >= value:
            index = mid
            r = mid - 1
        else:
            l = mid + 1
    return index


def comparator(lst, value):
    for i in range(len(lst)):
        if value <= lst[i]:
            return i
    return -1

def generateRandomArray(maxSize, maxValue):
    '''生成随机数组'''
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
        arr = generateRandomArray(maxSize, maxValue)
        arr.sort()  # 有序
        value = int(random.random() * (maxValue + 1)) - int(random.random() * maxValue)
        if nearsetIndex(arr, value) != comparator(arr, value):
            succeed = False
            break
    print('成功！' if succeed else '失败！')
