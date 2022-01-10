# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
堆结构可以存储对象，并按照对象中某个属性值排序
这时修改某个对象中的属性值，会导致堆结构不符合大根或小根结构
所以修改某个对象中的属性值，需要将其调整到正确位置，
增加hashmap实时记录对象所在堆结构中的位置，
若修改某对象的属性值，可将该位置heapInsert()和heapify(),heapInsert和heapify只会中一个
'''

class MyMaxHeap():
    def __init__(self, limit):
        self.heapSize = 0
        self.lst = []
        self.hashMap = {}
        self.limit = limit

    def isEmpty(self):
        return self.heapSize == 0

    def isFull(self):
        return self.heapSize == self.limit

    def size(self):
        return self.heapSize

    def contains(self, key):
        return key in self.hashMap

    def push(self, value):
        if self.isFull():
            raise Exception('heap is full')
        self.lst.insert(self.heapSize, value)
        self.hashMap[value] = self.heapSize
        self.heapInsert(self.heapSize)
        self.heapSize += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('heap is empty')
        ans = self.lst[0]
        self.lst[0], self.lst[self.heapSize - 1] = self.lst[self.heapSize - 1], self.lst[0]
        self.hashMap[self.lst[0]] = 0
        self.hashMap[self.lst[self.heapSize - 1]] = 0
        self.lst.pop(self.heapSize - 1)
        self.hashMap.pop(self.heapSize - 1)
        self.heapify(0)
        self.heapSize -= 1
        return ans

    def heapInsert(self, index):
        while self.lst[index].value > self.lst[(index - 1) // 2 if (index - 1) // 2 >= 0 else 0].value:
            self.lst[index], self.lst[(index - 1) // 2 if (index - 1) // 2 >= 0 else 0] = self.lst[(index - 1) // 2 if (index - 1) // 2 >= 0 else 0], self.lst[index]
            self.hashMap[self.lst[index]] = index
            self.hashMap[self.lst[(index - 1) // 2 if (index - 1) // 2 >= 0 else 0]] = (index - 1) // 2 if (index - 1) // 2 >= 0 else 0
            index = (index - 1) // 2 if (index - 1) // 2 >= 0 else 0

    def heapify(self, index):
        left = index * 2 + 1
        while left < self.heapSize:
            if left + 1 < self.heapSize and self.lst[left].value < self.lst[left + 1].value:
                maxIndex = left + 1
            else:
                maxIndex = left
            maxIndex = index if self.lst[maxIndex].value < self.lst[index].value else maxIndex
            if maxIndex == index:
                break
            self.lst[index], self.lst[maxIndex] = self.lst[maxIndex], self.lst[index]
            self.hashMap[self.lst[index]] = index
            self.hashMap[self.lst[maxIndex]] = maxIndex
            index = maxIndex
            left = index * 2 + 1

    def resign(self, value):  # 某对象属性值变了，重新调整为大根堆 O（logN）
        index = self.hashMap[value]
        self.heapInsert(index)
        self.heapify(index)