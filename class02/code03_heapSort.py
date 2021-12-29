# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random

'''
    完全二叉树：
    i的父索引(i-1)//2
    i的左孩子i*2+1
    i的右孩子i*2+2
    完全二叉树高度=logN
    
    堆：
    1堆结构就是用数组实现的完全二叉树结构
    2完全二叉树中如果每棵子树的最大值都在顶部就是大根堆
    3完全二叉树中如果每棵子树的最小值都在顶部就是小根堆
    4堆结构的heapInsert和heapify操作
    5堆结构的增增大和减小
    6优先级队列结构，就是堆结构
'''


def heapSort(lst):
    '''堆排序
    1先让整个数组都变成大根堆结构，建立堆的过程：
        1）从上到下的方法，时间复杂度为O(N*logN)
        2)从下到上的方法，时间复杂度为O(N)
    2把堆的最大值和堆尾的值交换，然后减少堆的大小之后，再去调整堆，一直周而复始，时间复杂度为O（N*logN）
    3堆的大小减小成0之后，排序完成

    O(N*logN)
    空间复杂度O(1)
    '''
    if lst == None or len(lst) < 2:
        return
    heapSize = len(lst)
    # 整个数组变成大根堆方式1  O(N*logN)
    # for i in range(len(lst)):  # O(N)  整个数组变成大根堆方式1
    #     heapInsert(lst, i)  # O(logN)

    # 整个数组变成大根堆方式2  O(N)
    for i in range(len(lst) - 1, -1, -1):
        heapify(lst, i, heapSize)

    while heapSize > 0:  # O(N)
        lst[0], lst[heapSize - 1] = lst[heapSize - 1], lst[0]  # O(1)
        heapSize -= 1  # O(1)
        heapify(lst, 0, heapSize)  # O(logN)


def createHeap(lst):
    '''整个数组变成大根堆方式1'''
    # for i in range(len(lst)):
    #     heapInsert(lst, i)

    # 整个数组变成大根堆方式2
    for i in range(len(lst) - 1, -1, -1):
        heapify(lst, i, len(lst))


def heapInsert(lst, index):
    '''某个数出现在index位置，往上继续移动
    调整代价O(logN)
    '''
    while lst[index] > lst[int((index - 1) / 2)]:
        lst[index], lst[int((index - 1) / 2)] = lst[int((index - 1) / 2)], lst[index]
        index = int((index - 1) / 2)


def heapify(lst, index, heapSize):
    '''某个数出现在index位置，能否往下移(堆化)
    调整代价O(logN)
    '''
    left = index * 2 + 1  # 左孩子下标
    while left < heapSize:  # 下方有孩子
        # 两个孩子中谁的值较大，把下标给largest
        largest = left + 1 if left + 1 < heapSize and lst[left + 1] > lst[left] else left
        # 父和较大孩子中谁的值较大，把下标给largest
        largest = largest if lst[largest] > lst[index] else index
        if largest == index:
            break
        lst[index], lst[largest] = lst[largest], lst[index]
        index = largest
        left = index * 2 + 1


def comparator(lst):
    lst.sort()


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst


if __name__ == '__main__':
    # a = [3, 6, 5, 7, 7]
    # createHeap(a)
    # print(a)  # [7, 7, 5, 3, 6] / [7, 7, 5, 6, 3]
    #
    # b = [1, 7, 5, 3, 6]
    # heapify(b, 0, len(b))
    # print(b)  # [7, 3, 5, 1, 6]
    #
    # c = [5, 4, 6, 3, 6, 7, 9]
    # heapSort(c)
    # print(c)

    testTimes = 50000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        heapSort(arr1)
        comparator(arr2)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')
