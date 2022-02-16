# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
并查集

每个学生三个属性：电话号码、B站id、githubid
任意俩人电话号码或B站id或githubid一样，这就是一个人
给一大堆学生实例，问这里到底有几个独立的人？
'''


class Student():
    def __init__(self, phone, bId, githubId):
        self.phone = phone
        self.bId = bId
        self.githubId = githubId


class Node():
    def __init__(self, value):
        self.vale = value


class unionFind():
    def __init__(self, lst):
        self.nodes = {}
        self.parents = {}
        self.sizeMap = {}

        for i in lst:
            node = Node(i)
            self.nodes[i] = node
            self.parents[node] = node
            self.sizeMap[node] = 1

    def findFather(self, cur):
        tmp = []
        while cur != self.parents[cur]:
            tmp.append(cur)
            cur = self.parents[cur]
        while len(tmp) != 0:
            self.parents[tmp.pop()] = cur
        return cur

    def isSameSet(self, x, y):
        if x not in self.nodes or y not in self.nodes:
            return False
        return self.findFather(self.nodes[x]) == self.findFather(self.nodes[y])

    def union(self, x, y):
        if x not in self.nodes or y not in self.nodes:
            return False
        xHead = self.findFather(self.nodes[x])
        yHead = self.findFather(self.nodes[y])
        if xHead != yHead:
            xSize = self.sizeMap[xHead]
            ySize = self.sizeMap[yHead]
            big = xHead if xSize >= ySize else yHead
            small = yHead if big == xHead else xHead
            self.parents[small] = big
            self.sizeMap[big] = xSize + ySize
            del self.sizeMap[small]


def countPersonNumber(lst):
    u = unionFind(lst)
    map1 = {}
    map2 = {}
    map3 = {}
    for i in lst:
        if i.phone in map1:
            u.union(map1[i.phone], i)
        elif i.bId in map2:
            u.union(map2[i.bId], i)
        elif i.githubId in map3:
            u.union(map3[i.githubId], i)
        else:
            map1[i.phone] = i
            map2[i.bId] = i
            map3[i.githubId] = i
    return len(u.sizeMap)


# 对数器
def comparator(lst):
    if len(lst) == 0 or len(lst) == 1:
        return len(lst)
    tmp = lst
    i = 0
    while i + 1 <= len(tmp):
        j = i + 1
        while j < len(tmp):
            if tmp[i].phone == tmp[j].phone or tmp[i].bId == tmp[j].bId or tmp[i].githubId == tmp[j].githubId:
                del tmp[j]
            else:
                j += 1
        i += 1
    return len(tmp)


# for test
import random


def generateRandomArray(maxSize, maxValue):
    ans = []
    for i in range(int(random.random() * (maxSize + 1))):
        ans.append(Student(str(int(random.random() * (maxValue + 1))), str(int(random.random() * (maxValue + 1))),
                           str(int(random.random() * (maxValue + 1)))))
    return ans


if __name__ == '__main__':
    testTimes = 100000
    maxSize = 100
    maxValue = 10
    for _ in range(testTimes):
        lst = generateRandomArray(maxSize, maxValue)
        # for i in lst:
        #     print('({}, {}, {}) '.format(i.phone, i.bId, i.githubId), end='')
        # print()
        if countPersonNumber(lst) != comparator(lst):
            print('Oops!')
    print('finish!')