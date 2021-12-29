# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random


def quickSort01(lst):
    '''快排1.0
    1）给定一个数组arr,选择数组最后一个数为num，把小于等于num的数放在数组的左边，大于num的数放在数组右边。
    2）将小于num左侧arr和大于num右侧arr分别递归步骤1

    T（N） = a*T(N/b)+O(N^d)

    T（N） = 2*T(N/2)+O(N^1)

    最好O(N*logN)  最差O(N^2)
    '''
    if lst == None or len(lst) < 2:
        return
    process01(lst, 0, len(lst) - 1)


def process01(lst, l, r):
    if l >= r:
        return
    l, i, r = part01(lst, l, r)
    process01(lst, l, i - 1)
    process01(lst, i + 1, r)


def part01(lst, l, r):
    p, i = l - 1, l
    while i < r:
        if lst[i] <= lst[r]:
            p += 1
            lst[i], lst[p] = lst[p], lst[i]
        i += 1
    lst[r], lst[p + 1] = lst[p + 1], lst[r]
    return l, p + 1, r


def quickSort02(lst):
    '''快排2.0
    1）给定一个数组arr，选择数组最后一个数为num，把小于num的数放在数组的左边，等于num的数放在数组的中间，大于num的数放在数组右边。
    2）将小于num左侧arr和大于num右侧arr分别递归步骤1

    T（N） = a*T(N/b)+O(N^d)

    T（N） = 2*T(N/2)+O(N^1)

    最好O(N*logN) 最差O(N^2)
    '''
    if lst == None or len(lst) < 2:
        return
    process02(lst, 0, len(lst) - 1)


def process02(lst, l, r):
    if l >= r:
        return
    p1, p2 = partition02(lst, l, r)
    process02(lst, l, p1 - 1)
    process02(lst, p2 + 1, r)


def partition02(lst, l, r):
    p1 = l - 1  # <区右边界
    p2 = r  # >区左边界
    while l < p2:
        if lst[l] < lst[r]:
            p1 += 1
            lst[l], lst[p1] = lst[p1], lst[l]
            l += 1
        elif lst[l] == lst[r]:
            l += 1
        else:
            p2 -= 1
            lst[l], lst[p2] = lst[p2], lst[l]
    lst[r], lst[l] = lst[l], lst[r]
    return p1 + 1, p2


def quickSort03(lst):
    '''快排3.0
    1）给定一个数组arr，随机选择一个数最为num并放在arr最后，把小于num的数放在数组的左边，等于num的数放在数组的中间，大于num的数放在数组右边。
    2）将小于num左侧arr和大于num右侧arr分别递归步骤1

    T（N） = a*T(N/b)+O(N^d)

    T（N） = 2*T(N/2)+O(N^1)

    O(N*logN)
    空间复杂度:最好 O(logN) 最差 O(N)
    '''
    if lst == None or len(lst) < 2:
        return
    process03(lst, 0, len(lst) - 1)


def process03(lst, l, r):
    if l >= r:
        return
    randomIndex = l + int(random.random() * (r - l + 1))
    lst[randomIndex], lst[r] = lst[r], lst[randomIndex]
    p = partition03(lst, l, r)
    process02(lst, l, p[0])  # <区
    process02(lst, p[1] + 1, r)  # >区


def partition03(lst, l, r):
    '''这是一个处理arr[l...r]的函数
    '''
    p1 = l - 1  # <区右边界
    p2 = r  # >区左边界
    while l < p2:
        if lst[l] < lst[r]:
            p1 += 1
            lst[l], lst[p1] = lst[p1], lst[l]
            l += 1
        elif lst[l] == lst[r]:
            l += 1
        else:
            p2 -= 1
            lst[l], lst[p2] = lst[p2], lst[l]
    lst[r], lst[l] = lst[l], lst[r]
    return p1 + 1, p2


def comparator(lst):
    lst.sort()


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst


if __name__ == '__main__':
    # a = [3, 5, 6, 3, 4, 5, 2, 6, 9, 0]
    # b = a.copy()
    # fastSort01(a)
    # print(a)
    # fastSort02(b)
    # print(b)
    testTimes = 50000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        quickSort03(arr1)
        comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
