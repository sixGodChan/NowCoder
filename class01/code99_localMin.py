# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random




def localMin(lst):
    '''局部最小值
    一个数组，相邻两个必不相同，求局部最小
    使用二分法
    '''
    if lst == None or len(lst) < 2:
        return
    return porcess(lst, 0, len(lst) - 1)

def porcess(lst, startIndex, stopIndex):
    if lst[startIndex] < lst[startIndex + 1]:
        return startIndex
    if lst[stopIndex] < lst[stopIndex - 1]:
        return stopIndex
    middleIndex = len(lst) // 2
    if lst[middleIndex] < lst[middleIndex - 1] and lst[middleIndex] < lst[middleIndex + 1]:
        return middleIndex
    if lst[middleIndex] > lst[middleIndex - 1]:
        return porcess(lst, startIndex + 1, middleIndex - 1)
    if lst[middleIndex] > lst[middleIndex + 1]:
        return porcess(lst, middleIndex + 1, stopIndex - 1)


def comparator(lst):
    if lst == None or len(lst) < 2:
        return [None]
    res = []
    startIndex, stopIndex = 0, len(lst) - 1
    if lst[startIndex] < lst[startIndex + 1]:
        res.append(startIndex)
    if lst[stopIndex] < lst[stopIndex - 1]:
        res.append(stopIndex)
    for i in range(startIndex + 1, stopIndex):
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            res.append(i)
    return res


def generateRandomArray(maxSize, maxValue):
    lst = []
    i = 0
    size = int(random.random() * (maxSize + 1))
    while i < size:
        res = int(random.random() * (maxValue + 1)) - int(random.random() * maxValue)
        if i == 0:
            lst.append(res)
            i += 1
        else:
            if res != lst[i - 1]:
                lst.append(res)
                i += 1
    return lst


if __name__ == '__main__':
    testTimes = 500000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr = generateRandomArray(maxSize, maxValue)
        res1 = localMin(arr)
        res2 = comparator(arr)
        if res1 not in res2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
