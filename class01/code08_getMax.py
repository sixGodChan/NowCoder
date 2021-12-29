# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random


def getMax(lst):
    '''递归求最大值
    本问题可以使用master公式求解时间复杂度  T(N) = a * T(N/b) + O(N^d)
        N 规模
        T(N) 母问题规模N
        T(N/b) 子问题N规模/b
        a 子问题被调用次数，子问题是等量的情况下，被调用次数
        d 除去调用子问题之外，剩下问题的时间复杂度

        1) 如果log(b,a)<d,时间复杂度是O(N^d)  # log(b,a)=log以b为低a的对数
        2) 如果log(b,a)=d,时间复杂度是O(N^d*logN)
        3) 如果log(b,a)>d,时间复杂度是O(N^log(b,a))

    本函数时间复杂度符合master公式 T(N) = 2 * T(N/2) + O(1)
        a = 2
        b = 2
        d = 0

        log(2,2)>0  # log(2,2) = 1
        时间复杂度O(N^1)
    '''
    if lst == None or len(lst) < 2:
        return
    return process(lst, 0, len(lst) - 1)


def process(lst, l, r):
    if l == r:  # 只有一个数
        return lst[l]
    mid = l + ((r - l) >> 1)  # 求中点 防溢出 等于(l+r)/2
    leftMax = process(lst, l, mid)
    rightMax = process(lst, mid + 1, r)
    return leftMax if leftMax >= rightMax else rightMax


def comparator(lst):
    if lst == None or len(lst) < 2:
        return
    return max(lst)


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst


if __name__ == '__main__':
    testTimes = 500000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        res1 = getMax(arr1)
        res2 = comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
