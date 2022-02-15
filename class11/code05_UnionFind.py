# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
并查集

联通性的问题都可以用并查集

1）有若干个样本a、b、c、d...类型假设是V
2）在并查集中一开始认为每个样本都在单独的集合里
3）用户可以再任何时候调用如下两个方法：
    boolean isSameSet(x,y):查询样本x和样本y是否属于一个集合
    void union(x,y):把x和y各自所在集合的所有样本合并成一个集合
4）isSameSet和union方法的代价越低越好
'''


class Node():
    def __init__(self, value):
        self.value = value


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
        path = []
        while cur != self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]
        while len(path) != 0:
            self.parents[path.pop()] = cur
        return cur

    def isSameSet(self, x, y):
        if x not in self.nodes or y not in self.nodes:
            return False
        return self.findFather(self.nodes[x]) == self.findFather(self.nodes[y])

    def union(self, x, y):
        if x not in self.nodes or y not in self.nodes:
            return False
        xhead = self.findFather(self.nodes[x])
        yhead = self.findFather(self.nodes[y])
        if xhead != yhead:
            xSize = self.sizeMap[x]
            ySize = self.sizeMap[y]
            if xSize >= ySize:
                self.parents[yhead] = xhead
                self.sizeMap[xhead] = xSize + ySize
                del self.sizeMap[yhead]
            else:
                self.parents[xhead] = yhead
                self.sizeMap[yhead] = xSize + ySize
                del self.sizeMap[xhead]

# 2:17:30