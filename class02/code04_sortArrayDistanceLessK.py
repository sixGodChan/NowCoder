# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
from heapq import *


def sortArrayDistanceLessK(lst, k):
    if lst == None or len(lst) < 2:
        return
    heap = []
    for i in range(min(k, len(lst))):
        heappush(heap, lst[i])
    index, i = k, 0
    while index < len(lst):
        # lst[i] = heappop(heap)
        # heappush(heap, lst[index])
        lst[i] = heapreplace(heap, lst[index])
        i += 1
        index += 1
    while len(heap) > 0:
        lst[i] = heappop(heap)
        i += 1


def smallHeapInsert(lst, index):
    while lst[index] < lst[int((index - 1) / 2)]:  # 节点index小于父节点
        lst[index], lst[int((index - 1) / 2)] = lst[int((index - 1) / 2)], lst[index]
        index = int((index - 1) / 2)


def smallHeapify(lst, index, heapSize):
    left = index * 2 + 1
    while left < heapSize:
        smallest = left + 1 if left + 1 < heapSize and lst[left + 1] < left[left] else left
        smallest = smallest if left[smallest] < left[index] else index
        if smallest == index:
            break
        lst[smallest], lst[index] = lst[index], lst[smallest]
        index = smallest
        left = index * 2 + 1


if __name__ == '__main__':
    c = [5, 4, 6, 3, 6, 7, 9]
    sortArrayDistanceLessK(c, 5)
    print(c)
