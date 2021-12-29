# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二分法 应用
在有序数组中找num是否存在
'''
import random

def exist(lst, num):
    '''
    O(logN)
    '''
    if lst == None or len(lst) == 0:
        return False
    l = 0
    r = len(lst) - 1
    while l < r:
        mid = l + ((r - l) >> 1)
        if lst[mid] == num:
            return True
        elif lst[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return lst[l] == num


def comparator(lst, num):
    return num in lst


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
        num = int(random.random() * (maxValue + 1)) - int(random.random() * maxValue)
        if exist(arr, num) != comparator(arr, num):
            succeed = False
            break
    print('成功！' if succeed else '失败！')