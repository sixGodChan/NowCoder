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
    def __init__(self):
        self.heapSize = 0
        self.lst = []
        self.hashMap = {}

    def isEmpty(self):
        return self.heapSize == 0

    def size(self):
        return self.heapSize

    def contains(self, key):
        return key in self.hashMap

    def push(self, value):
        self.lst.insert(self.heapSize, value)
        self.hashMap[value] = self.heapSize
        self.heapInsert(self.heapSize)
        self.heapSize += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('heap is empty')
        ans = self.lst[0]
        self.heapSize -= 1
        self.lst[0], self.lst[self.heapSize] = self.lst[self.heapSize], self.lst[0]
        self.hashMap[self.lst[0]] = 0
        self.hashMap[self.lst[self.heapSize]] = self.heapSize
        self.hashMap.pop(self.lst[self.heapSize])
        self.lst.pop(self.heapSize)
        self.heapify(0)
        return ans

    def heapInsert(self, index):
        while self.lst[index] > self.lst[(index - 1) // 2 if (index - 1) // 2 >= 0 else 0]:
            self.lst[index], self.lst[(index - 1) // 2 if (index - 1) // 2 >= 0 else 0] = self.lst[(index - 1) // 2 if (
                                                                                                                               index - 1) // 2 >= 0 else 0], \
                                                                                          self.lst[index]
            self.hashMap[self.lst[index]] = index
            self.hashMap[self.lst[(index - 1) // 2 if (index - 1) // 2 >= 0 else 0]] = (index - 1) // 2 if (
                                                                                                                   index - 1) // 2 >= 0 else 0
            index = (index - 1) // 2 if (index - 1) // 2 >= 0 else 0

    def heapify(self, index):
        left = index * 2 + 1
        while left < self.heapSize:
            if left + 1 < self.heapSize and self.lst[left] < self.lst[left + 1]:
                maxIndex = left + 1
            else:
                maxIndex = left
            maxIndex = index if self.lst[maxIndex] < self.lst[index] else maxIndex
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


class Student():
    def __init__(self, c, a, i):
        self.classNo = c
        self.age = a
        self.id = i

    def __lt__(self, other):
        return -1 * self.age < -1 * other.age


if __name__ == '__main__':
    s1 = Student(2, 50, 11111)
    s2 = Student(1, 60, 22222)
    s3 = Student(6, 10, 33333)
    s4 = Student(3, 20, 44444)
    s5 = Student(7, 72, 55555)
    s6 = Student(1, 14, 66666)

    import heapq

    heap = []

    heapq.heappush(heap, s1)
    heapq.heappush(heap, s2)
    heapq.heappush(heap, s3)
    heapq.heappush(heap, s4)
    heapq.heappush(heap, s5)
    heapq.heappush(heap, s6)

    while len(heap) != 0:
        cur = heapq.heappop(heap)
        print(cur.classNo, ',', cur.age, ',', cur.id)

    print('=' * 20)

    myHeap = MyMaxHeap()
    myHeap.push(s1)
    myHeap.push(s2)
    myHeap.push(s3)
    myHeap.push(s4)
    myHeap.push(s5)
    myHeap.push(s6)

    while not myHeap.isEmpty():
        cur = myHeap.pop()
        print(cur.classNo, ',', cur.age, ',', cur.id)

    print('=' * 20)

    heapq.heappush(heap, s1)
    heapq.heappush(heap, s2)
    heapq.heappush(heap, s3)
    heapq.heappush(heap, s4)
    heapq.heappush(heap, s5)
    heapq.heappush(heap, s6)

    s2.age = 6
    s4.age = 12
    s5.age = 10
    s6.age = 84

    while len(heap) != 0:
        cur = heapq.heappop(heap)
        print(cur.classNo, ',', cur.age, ',', cur.id)

    print('=' * 20)

    myHeap = MyMaxHeap()
    myHeap.push(s1)
    myHeap.push(s2)
    myHeap.push(s3)
    myHeap.push(s4)
    myHeap.push(s5)
    myHeap.push(s6)

    s2.age = 6
    myHeap.resign(s2)
    s4.age = 12
    myHeap.resign(s4)
    s5.age = 10
    myHeap.resign(s5)
    s6.age = 84
    myHeap.resign(s6)

    while not myHeap.isEmpty():
        cur = myHeap.pop()
        print(cur.classNo, ',', cur.age, ',', cur.id)
