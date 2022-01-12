# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
不基于比较的排序
桶排序思想下的排序：计数排序 & 基数排序 & 桶排序
1）桶排序思想下的排序都是不基于比较的排序
2）时间复杂度是O(N),额外空间复杂度是O（M）
3）应用范围有限，需要样本的数据状况满足桶的划分
'''


# 1:20:20

# 计数排序 数组中值的范围0~200
def CountSort(lst):
    if lst == None or len(lst) < 2:
        return
    maxValue = max(lst)
    bucket = [0 for _ in range(maxValue + 1)]
    for i in lst:
        bucket[i] += 1
    index = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            lst[index] = j
            index += 1
            bucket[j] -= 1


def comparator(lst):
    lst.sort()


import random


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)))
    return lst


if __name__ == '__main__':
    testTimes = 50000
    maxSize = 100
    maxValue = 200
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        CountSort(arr1)
        comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
