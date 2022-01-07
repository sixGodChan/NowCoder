# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
堆排序
额外空间复杂度O（1）
时间复杂度O（N*log(N)）

'''
from class05.code01_heap01 import MyMaxHeap


# 先将数组改为大根堆，再执行循环执行heapify（将当前节点向下优化到最佳位置），直到数组大小减为零
def heapSort(lst):
    if lst == None or len(lst) < 2:
        return
    length = len(lst)
    heap = MyMaxHeap(length)
    for i in range(length):
        heap.push(lst[i])
    while heap.heapSize > 0:
        heap.pop()
    return heap.lst


# ===
def heapSort01(lst):
    if lst == None or len(lst) < 2:
        return

    # 创建大根堆  O（N*logN)
    # for i in range(len(lst)):
    #     heapInsert(lst, i)  # O（logN)

    # 优化创建大根堆  O(N)
    # 默认数组是个二叉树，从末尾向前开始heapify（将当前节点向下优化到最佳位置）
    for i in range(len(lst) - 1, -1):
        heapify(lst, i, len(lst))

    heapSize = len(lst)
    heapSize -= 1
    lst[0], lst[heapSize] = lst[heapSize], lst[0]
    while heapSize > 0:  # O（N*logN)
        heapify(lst, 0, heapSize)  # O（logN)
        heapSize -= 1  # O（1)
        lst[0], lst[heapSize] = lst[heapSize], lst[0]  # O（1)


def heapInsert(lst, index):
    while lst[index] > lst[(index - 1) // 2 if (index - 1) // 2 else 0]:
        lst[index], lst[(index - 1) // 2] = lst[(index - 1) // 2], lst[index]
        index = (index - 1) // 2 if (index - 1) // 2 else 0


def heapify(lst, index, heapSize):
    l = index * 2 + 1  # 左孩子索引
    while l < heapSize:
        if l + 1 < heapSize and lst[l + 1] > lst[l]:
            maxIndex = l + 1
        else:
            maxIndex = l
        if lst[maxIndex] < lst[index]:
            maxIndex = index
        if maxIndex == index:
            break
        heapSize -= 1
        lst[maxIndex], lst[index] = lst[index], lst[maxIndex]
        index = maxIndex
        l = index * 2 + 1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 11, 34, 3, 23, 24, 23, 5, 5, 6]
    print(heapSort(a))
