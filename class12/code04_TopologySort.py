# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
图的拓扑排序算法


1）在图中找到所有入度为0的点输出
2）把所有入度为0的点在图中删掉（消除边的影响），继续找入度为0的点输出，周而复始
3）图的所有点被删除后，一次输出顺序就是拓扑排序

要求：有向图且其中没有环 （有环和无向图都无法拓扑排序）
应用：时间安排、编译顺序（要做事情，但是事情之间有依赖，将事情先后顺序排列就是拓扑排序）
'''

import queue
from class12.code01_Graph import Graph, Node


def sortedTopology(graph):
    inMap = {}  # {node: 剩余入度}
    zeroInQueue = queue.Queue()  # 入度为0的node入队列
    for _, node in graph.nodes.items():
        inMap[node] = node.goIn
        if node.goIn == 0:
            zeroInQueue.put(node)

    result = []

    while not zeroInQueue.empty():
        cur = zeroInQueue.get()
        result.append(cur)
        for next in cur.nexts:
            inMap[next] -= 1
            if inMap[next] == 0:
                zeroInQueue.put(next)
    return result

# 1:38:57