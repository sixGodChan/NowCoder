# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
最小生成树算法之Kruskal

（连通全部点，且边的集合权值最小）

1）总是从权值最小的边开始考虑，依次考察权值依次变大的边
2）当前的边要么进入最小生成树的集合，要么丢弃
3）如果当前的边进入最小生成树的集合中不会形成环，就要当前边
4）如果当前的边进入最小生成树的集合中会形成环，就不要当前边
5）考察完所有边之后，最小生成树的集合也得到了

使用并查集，会很简单
'''
from class12.code01_Graph import Graph
import heapq


class Edge():
    '''边的描述'''

    def __init__(self, weight, fromNode, toNode):
        self.weight = weight  # 权重
        self.fromNode = fromNode
        self.toNode = toNode

    def __lt__(self, other):  # 比较器
        return self.weight < other.weight


def kruskalMST(graph):
    '''从小的边到大的边，依次弹出，小根堆！'''
    u = UnionFind([i for i in graph.nodes.values])
    heap = []  # 小根堆
    for edge in graph.egdes:  # M 条边
        heapq.heappush(heap, edge)  # O(logM)
    result = set()
    while len(heap) != 0:  # M 条边
        edge = heapq.heappop(heap)  # O(logM)
        if not u.isSameSet(edge.fromNode, edge.toNode):  # # O(1)
            result.add(edge)
            u.union(edge.fromNode, edge.toNode)
    return result


class Node():
    def __init__(self, value):
        self.value = value


class UnionFind():
    def __init__(self, lst):
        self.nodes = {}
        self.parents = {}
        self.sizeMap = {}

        for i in range(len(lst)):
            node = Node(i)
            self.nodes[lst[i]] = node
            self.parents[node] = node
            self.sizeMap[node] = 1

    def findFather(self, node):
        tmp = []
        while node != self.parents[node]:
            node = self.parents[node]
            tmp.append(node)
        while len(tmp) != 0:
            self.parents[tmp.pop()] = node
        return node

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
            big = xSize if xSize >= ySize else ySize
            small = ySize if big == xSize else xSize
            self.parents[small] = big
            self.sizeMap[big] = xSize + ySize
            del self.sizeMap[small]
