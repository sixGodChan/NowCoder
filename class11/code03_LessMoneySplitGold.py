#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
贪心算法的解题套路实战



一块金条切成两半，是需要话费长度数值一样的铜板的。
比如长度为20的金条，不管怎么切，都需要话费20个铜板。一群人想整分整条金条，怎么分最剩铜板？

例如，给定数组{10，20，30}，代表一共3个人，整块金条长度为60，金条要分成10，20，30三个部分。

如果先把长度60的金条分成10和50，花费60；再把长度为50的金条分成20和30，花费50；一共花费110铜板。
但如果先把长度60的金条分成30和30，花费60；再把长度为30的金条分成10和20，花费30；一共花费90铜板。

输入一个数组，返回分割的最小代价。

贪心解决（哈夫曼树问题）
'''

import sys


def lessMoney(arr):
    '''
    纯暴力
    :param arr: 
    :return: 
    '''
    if arr == None or len(arr):
        return 0
    return process(arr, 0)


def process(arr, pre):
    '''
	arr中只剩一个数字的时候，停止合并，返回最小的总代价
    :param arr:等待合并的数都在arr里 
    :param pre: pre之前的合并行为产生了多少总代价
    :return: 
    '''
    if len(arr) == 1:
        return pre
    ans = sys.maxsize
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ans = min(ans, process(copyAndMergeTwo(arr, i, j), pre + arr[i] + j[j]))
    return ans


def copyAndMergeTwo(arr, i, j):
    ans = []
    for k in range(len(arr)):
        if k != i and k != j:
            ans.append(arr[k])
    return ans.append(arr[i] + arr[j])


import heapq


def lessMoney2(arr):
    '''贪心  哈夫曼树'''
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])

    sum = 0
    while len(heap) > 1:
        cur = heapq.heappop(heapq) + heapq.heappop(heapq)
        sum += cur
        heapq.heappush(heap, cur)
    return sum


import random


def generateRandomArray(maxSize, maxValue):
    arr = []
    for i in range(int(random.random() * (maxSize + 1))):
        arr.append(int(random.random() * (maxValue + 1)))
    return arr


if __name__ == '__main__':
    testTime = 100000
    maxSize = 6
    maxValue = 1000
    for i in range(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        if lessMoney(arr) != lessMoney2(arr):
            print('Oops!')
    print('finish!')
# 1:15:28