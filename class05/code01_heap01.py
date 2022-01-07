# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
堆
堆在结构上是完全二叉树
    完全二叉树
        父节点从0开始
        i位置左孩子位置=i*2+1
        i位置右孩子位置=i*2+2
        i父节点位置=(i-1)/2
        数高度 = logN

        父节点从1开始
        i位置左孩子位置=i*2（i<<1）
        i位置右孩子位置=i*2+1(i<<1|1)
        i父节点位置=i/2(i>>1)

堆分为大根堆、小根堆
    大根堆
        每个子树的最大值是头结点的数
    小根堆
        每个子树的最小值是头结点的数

'''


# 依次给数字，组成大根堆
# 每个数字和自己的父节点比, 比父大和父位置交换，交换后再和父比;比父小停住

def heap(lst):
    if lst == None:
        return
    if len(lst) == 1:
        return lst
    heapSize = 1
    while heapSize < len(lst):
        i = heapSize
        while lst[i] > lst[(i - 1) // 2 if (i - 1) // 2 >= 0 else 0]:
            lst[i], lst[(i - 1) // 2] = lst[(i - 1) // 2], lst[i]
            i = (i - 1) // 2 if (i - 1) // 2 >= 0 else 0
        heapSize += 1

class MyMaxHeap():
    def __init__(self, limit):
        self.limit = limit
        self.heapSize = 0
        self.lst = []

    def heapInsert(self, i):
        while self.lst[i] > self.lst[(i - 1) // 2 if (i - 1) // 2 >= 0 else 0]:
            self.lst[i], self.lst[(i - 1) // 2] = self.lst[(i - 1) // 2], self.lst[i]
            i = (i - 1) // 2 if (i - 1) // 2 >= 0 else 0

    def push(self, value):
        if self.heapSize == self.limit:
            raise Exception('heap is full')
        self.lst.insert(self.heapSize, value)
        self.heapInsert(self.heapSize)
        self.heapSize += 1

    # 0:36:13

    # 将大根堆中最大值删除，调整为新的大根堆
    # 将堆顶值换为堆最后一个值，再将取左右孩子中最大的与顶交换，以此类推

    # 从index位置，往下看，不断的下沉，（将当前节点向下优化到最佳位置）
    # 停：我的孩子都不比我大；没有孩子了
    def heapify(self, i):
        l = i * 2 + 1
        while l < self.heapSize:  # 有左孩子
            if l + 1 < self.heapSize and self.lst[l + 1] > self.lst[l]:  # 有右孩子，右孩子比左孩子大
                maxIndex = l + 1
            else:  # 没有右孩子 或 有右孩子，右孩子没有左孩子大
                maxIndex = l
            if self.lst[maxIndex] > self.lst[i]:  # 两个孩子中最大的大于自己
                maxIndex = maxIndex
            else:  # 两个孩子中最大的小于等于自己
                maxIndex = i
            if maxIndex == i:
                break
            self.lst[i], self.lst[maxIndex] = self.lst[maxIndex], self.lst[i]
            i = maxIndex
            l = i * 2 + 1

    def pop(self):
        res = self.lst[0]
        self.heapSize -= 1
        self.lst[0], self.lst[self.heapSize] = self.lst[self.heapSize], self.lst[0]
        self.heapify(0)
        return res

    # 1:04:46

    def isEmpty(self):
        return self.heapSize == 0

    def isFull(self):
        return self.heapSize == self.limit


class RightMaxHeap():
    def __init__(self, limt):
        self.lst = []
        self.limit = limt
        self.heapSize = 0

    def isEmpty(self):
        return self.heapSize == 0

    def isFull(self):
        return self.heapSize == self.limit

    def push(self, value):
        if self.heapSize == self.limit:
            raise Exception('heap is full')
        self.lst.insert(self.heapSize, value)
        self.heapSize += 1

    def pop(self):
        maxIndex = 0
        for i in range(self.heapSize):
            if self.lst[i] > self.lst[maxIndex]:
                maxIndex = i
        ans = self.lst[maxIndex]
        self.heapSize -= 1
        self.lst[maxIndex] = self.lst[self.heapSize]
        return ans


if __name__ == '__main__':
    import random

    value = 1000
    limit = 100
    testTime = 1000000
    for i in range(testTime):
        curLimit = int(random.random() * limit) + 1
        my = MyMaxHeap(curLimit)
        test = RightMaxHeap(curLimit)
        curOpTimes = int(random.random() * limit)
        for j in range(curOpTimes):
            if my.isEmpty() != test.isEmpty():
                print('Oops1!')
            if my.isFull() != my.isFull():
                print('Oops2!')
            if my.isEmpty():
                curValue = int(random.random() * value)
                my.push(curValue)
                test.push(curValue)
            elif my.isFull():
                if my.pop() != test.pop():
                    print('Oops3!')
            else:
                if random.random() < 0.5:
                    curValue = int(random.random() * value)
                    my.push(curValue)
                    test.push(curValue)
                else:
                    if my.pop() != test.pop():
                        print('Oops4!')
    print('finish!')

