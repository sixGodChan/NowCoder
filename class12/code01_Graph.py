# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
图

1）由点的集合和边的集合构成
2）虽然存在有向图和无向图的概念，但实际上都可以用有向图来表示
3）边上可能带有权值

如何表达图：表达方式有很多
    A-C
    | |
    D-B

1）邻接表法:点可以直接到达的点
    A:C,D
    B:C,D
    C:A,B
    D:B,A

2）邻接矩阵法（有连接可以带权重,没有连接正无穷∞）
        A   B   C   D
    A   0   ∞   3   7
    B   ∞   0   6   1
    C   4   5   0   ∞
    D   2   8   ∞   0

3）[[weight，from，to][...]...]
    [[3, A, C]
    [7, A, D]
    ...]

图的面试题如何搞定

图的算法都不算难，只不过coding的代价比较高

1）先用自己最熟练的方式，实现图的结构表达
2）在自己熟悉的结构上，实现所有常用的图的算法作为模板
3）把面试题提供的图结构转化为自己熟悉的图结构，再调整模板或改写即可
'''


# 推荐结构
class Node():
    '''用点结构描述'''

    def __init__(self, value):
        self.value = value
        self.goIn = 0  # 入度
        self.goOut = 0  # 出度
        self.nexts = []  # 出去连接的点
        self.edges = []  # 出去的边


class Edge():
    '''边的描述'''

    def __init__(self, weight, fromNode, toNode):
        self.weight = weight  # 权重
        self.fromNode = fromNode
        self.toNode = toNode


class Graph():
    '''图的描述'''

    def __init__(self):
        self.nodes = {}  # 点集 {value: Node()}
        self.egdes = set()  # 边集


def createGraph(marix):
    '''将[[weight，from，to][...]...]结构 转为 推荐的结构'''
    graph = Graph()
    for i in range(len(marix)):
        weight = marix[i][0]
        goFrom = marix[i][1]
        goTo = marix[i][2]

        if goFrom not in graph.nodes:
            graph.nodes[goFrom] = Node(goFrom)
        if goTo not in graph.nodes:
            graph.nodes[goTo] = Node(goTo)

        fromNode = graph.nodes[goFrom]
        toNode = graph.nodes[goTo]

        newEdge = Edge(weight, fromNode, toNode)
        fromNode.nexts.append(toNode)
        fromNode.goOut += 1
        toNode.goIn += 1
        fromNode.edges.append(newEdge)
        graph.egdes.add(newEdge)

    return graph
# 0:59:20
