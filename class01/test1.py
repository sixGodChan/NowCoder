# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

def selectionSort(lst):
    if lst == None or len(lst) < 2:
        return lst

    for i in range(len(lst)):
        minIndex = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        lst[minIndex], lst[i] = lst[i], lst[minIndex]
    return lst


def bubbleSort(lst):
    if lst == None or len(lst)<2:
        return lst

    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def insertionSort(lst):
    if lst == None or len(lst)<2:
        return lst

    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if j >= 0 and lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst



if __name__ == '__main__':
    a = [4, 3, 10, 11, 2, 7, 8]
    # print(selectionSort(a))

    # print(bubbleSort(a))
    print(insertionSort(a))

