# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random


# 选择

def selectionSort(lst):
    if lst == None or len(lst) < 2:
        return

    for i in range(len(lst)):
        minIndex = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        lst[minIndex], lst[i] = lst[i], lst[minIndex]


# 冒泡

def bubbleSort(lst):
    if lst == None or len(lst) < 2:
        return

    for i in range(len(lst)):
        for j in range(1, len(lst) - i):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]


# 插入

def insertionSort(lst):
    if lst == None or len(lst) < 2:
        return
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if j - 1 >= 0 and lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]


def comparator(lst):
    '''对数器'''
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
        insertionSort(arr1)
        comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
