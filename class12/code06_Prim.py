# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
最小生成树算法之Prim

1）从某点，记录这个点，解锁其相连的全部边根据权重入小根堆，
2）找堆顶边另外一头的点，判断这个点是否被记录，
3）记录过，跳到2）
4）没记录过，记录这个边，从这个点开始，跳转到1）

不涉及并查集
'''

from class12.code01_Graph import Graph
import heapq


def primMST(graph):
    result = set()  # 依次挑选的的边在result里
    nodeSet = set()  # 哪些点被解锁出来了
    edgeSet = set()
    edgeHeap = []  # 解锁的边进入小根堆
    for node in graph.nodes.values:  # 随便挑了一个点 （for循环防森林用）
        # node 是开始点
        if node not in nodeSet:
            nodeSet.add(nodeSet)
            for edge in node.edges:  # 由一个点，解锁所有相连的边
                if edge not in edgeSet:
                    heapq.heappush(edgeHeap, edge)
                    edgeSet.add(edge)
            while len(edgeHeap) == 0:
                edge = heapq.heappop(edgeHeap)  # 弹出解锁的边中，最小的边
                toNode = edge.toNode  # 可能的一个新的点
                if toNode not in nodeSet:  # 不含有的时候，就是新的点
                    result.add(edge)
                    nodeSet.add(toNode)
                    for nextEdge in toNode.deges:
                        if nextEdge not in nodeSet:
                            heapq.heappush(edgeHeap, nextEdge)
                            edgeSet.add(nextEdge)
        # break
    return result


class Edge():
    '''边的描述'''

    def __init__(self, weight, fromNode, toNode):
        self.weight = weight  # 权重
        self.fromNode = fromNode
        self.toNode = toNode

    def __lt__(self, other):  # 比较器
        return self.weight < other.weight
