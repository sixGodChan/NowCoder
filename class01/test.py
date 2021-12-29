# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi


def selectionSort(lst):
    if lst == None or lst.__len__() < 2:
        return lst
    for i in range(len(lst)):
        minIndex = i
        for j in range(i + 1, len(lst)):
            minIndex = j if lst[minIndex] > lst[j] else minIndex
        lst[minIndex], lst[i] = lst[i], lst[minIndex]
    return lst


def bubbleSort(lst):
    if lst == None or len(lst) < 2:
        return lst
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertionSort(lst):
    if lst == None or len(lst) < 2:
        return lst

    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if j - 1 >= 0 and lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst


def localMin(lst, startIndex, stopIndex):
    '''局部最小值'''
    if lst[startIndex] < lst[startIndex + 1]:
        return startIndex
    if lst[stopIndex] < lst[stopIndex - 1]:
        return stopIndex
    middleIndex = len(lst) // 2
    if lst[middleIndex] < lst[middleIndex - 1] and lst[middleIndex] < lst[middleIndex + 1]:
        return middleIndex
    if lst[middleIndex] > lst[middleIndex - 1]:
        return localMin(lst, startIndex + 1, middleIndex - 1)
    if lst[middleIndex] > lst[middleIndex + 1]:
        return localMin(lst, middleIndex + 1, stopIndex - 1)


if __name__ == '__main__':
    a = [4, 3, 10, 11, 2, 7, 8]
    # print(selectionSort(a))
    # print(bubbleSort(a))
    # print(insertionSort(a))
    print(localMin(a, 0, len(a) - 1))
