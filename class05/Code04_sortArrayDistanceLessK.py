# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
堆有关题目
小根堆

一个几乎有序的数组，如果让数组变为有序，移动任意值的距离不会超过k，请选择排序策略，并排序
'''

import heapq


# 创建一个小根堆，将前k+1个数放入小根堆，将堆顶（最小值）弹出，再将k+2位置的数放入小根堆，再弹出堆顶，。。。
def sortedArrayDistanceLessK(lst, k):  # O(N*logK)
    heap = []  # 小根堆不会超过k
    length = len(lst)
    for i in range(min(k + 1, length)):
        heapq.heappush(heap, lst[i])  # O(logK)
    j = k + 1
    index = 0
    while j < length:
        lst[index] = heapq.heappop(heap)  # O(logK)
        heapq.heappush(heap, lst[j])  # O(logK)
        j += 1
        index += 1
    while len(heap) != 0:
        lst[index] = heapq.heappop(heap)  # O(logK)
        index += 1
    return lst


def comparator(lst, k):
    lst.sort()


import random


def randomArrayNoMoreK(maxSize, maxValue, k):
    length = int(random.random() * (maxSize + 1))
    lst = []
    isSwap = []
    for i in range(length):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * (maxValue)))
        isSwap.append(False)
    lst.sort()
    # // 然后开始随意交换，但是保证每个数距离不超过K
    # // swap[i] == true, 表示i位置已经参与过交换
    # // swap[i] == false, 表示i位置没有参与过交换
    for i in range(length):
        j = min(i + int(random.random() * (k + 1)), length - 1)
        if not isSwap[i] and not isSwap[j]:
            isSwap[i] = True
            isSwap[j] = True
            lst[i], lst[j] = lst[j], lst[i]
    return lst


def copyArray(lst):
    if lst == None:
        return
    res = []
    for i in lst:
        res.append(i)
    return res


def isEqual(lst1, lst2):
    if (lst1 == None and lst2 != None) or (lst1 != None and lst2 == None):
        return False
    if lst1 == None and lst2 == None:
        return True
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


def printArray(lst):
    if lst == None:
        return
    print(' '.join([str(i) for i in lst]))


if __name__ == '__main__':
    print('test begin')
    testTime = 500000
    maxSize = 100
    maxValue = 100
    successd = True
    for i in range(testTime):
        k = int(random.random() * maxSize) + 1
        lst = randomArrayNoMoreK(maxSize, maxValue, k)
        arr1 = copyArray(lst)
        arr2 = copyArray(lst)
        sortedArrayDistanceLessK(arr1, k)
        comparator(arr2, k)
        if not isEqual(arr1, arr2):
            successd = False
            print('K ：%s' % k)
            printArray(lst)
            printArray(arr1)
            printArray(arr2)
            break
    print('Nice!' if successd else 'Oops!')
# 1:51:40