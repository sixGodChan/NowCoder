# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
Dijkstra算法 --- 最短路径问题

出发点到所有点的最短距离是多少

前提：在图里要求边的权值不为负
1）Dijkstra算法必须指定一个原点
2）生成一个原点到各个点的最小距离表，一开始只有一条记录，既原点到自
己的最小距离为0，原点到其他所有点的最小距离都为正无穷大
3）从距离表中拿出没拿过记录里的最小记录，通过这个点发出的边，更新原点
到各个点的最小距离表，不断重复这一步
4）原点到所有的点记录如果都被拿过一遍，过程停止，最小记录表得到了
'''
from class12.code01_Graph import Graph


def dijkstra1(head):
    '''
    从第一个点出发到所有点的最小距离
    :param head: 第一个点
    :return: 最小记录表
    '''
    # key：从第一个点出发到达key
    # value:从第一个点出发达到key的最小距离
    # 如果在表中，没有T的记录，含义是从第一个点出发到T这点的距离为正无穷
    distanceMap = {head: 0}  # 降低一个点加入到dict
    selectedNodes = set()  # 已经求过距离的节点，存在selectedNodes中，以后再也不碰
    minNode = getMinDistanceAndUnselectNode(distanceMap, selectedNodes)
    while minNode != None:
        distance = distanceMap[minNode]
        for edge in minNode.edges:
            toNode = edge.toNode
            if toNode not in distanceMap:
                distanceMap[toNode] = distance + edge.weight
            else:
                distanceMap[toNode] = min(distanceMap[toNode], distance + edge.weight)
        selectedNodes.add(minNode)
        minNode = getMinDistanceAndUnselectNode(distanceMap, selectedNodes)
    return distanceMap


def getMinDistanceAndUnselectNode(distanceMap, selectNodes):
    minNode = None
    import sys
    minDistance = sys.maxsize
    for node, distance in distanceMap.items():
        if node not in selectNodes and distance < minDistance:
            minNode = node
            minDistance = distance
    return minNode


# 改进后的dijkstra算法 （将遍历map改为自定义的堆结构）
# 从head出发，所有head能够的节点，生成到达每个节点的最小路径记录并返回

def dijkstra2(head, size):
    nodeHeap = NodeHeap(size)
    nodeHeap.addOrUpdateOrIgnore(head, 0)
    result = {}
    while not nodeHeap.isEmpty():
        record = nodeHeap.pop()
        cur = record.node
        distance = record.distance
        for edge in cur.edges:
            nodeHeap.addOrUpdateOrIgnore(edge.toNode, edge.weight + distance)
        result[cur] = distance
    return result


class NodeRecord():
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class NodeHeap():
    def __init__(self):
        self.nodes = []  # 实际的堆结构
        self.heapIndexMap = {}  # key 某一个node， value 上面堆中的位置 （-1表示节点来过，但是已被锁定）
        self.distanceMap = {}  # key 某一个节点， value 从源节点出发到该节点的目前最小距离
        self.size = 0  # 堆上有多少个点

    def isEmpty(self):
        return self.size == 0

    def addOrUpdateOrIgnore(self, node, distance):
        '''
        有一个点叫node，现在发现了一个从原节点出发到达node的距离为distance
        判断要不要跟新、如果要更新的话，就更新
        '''
        if self.inHeap(node):
            self.distanceMap[node] = min(self.distanceMap[node], distance)
            self.insertHeapify(node, self.heapIndexMap[node])
        if not self.isEntered(node):
            self.nodes.append(node)
            self.heapIndexMap[node] = self.size
            self.distanceMap[node] = distance
            self.insertHeapify(node, self.size)
            self.size += 1

    def pop(self):
        nodeRecord = NodeRecord(self.nodes[0], self.distanceMap[self.nodes[0]])
        self.swap(self.nodes[0], self.nodes[self.size - 1])
        self.heapIndexMap[self.nodes[self.size - 1]] = -1
        del self.distanceMap[self.nodes[self.size - 1]]
        self.heapify(0, self.size - 1)
        return nodeRecord

    def insertHeapify(self, node, index):
        while self.distanceMap[self.nodes[index]] < self.distanceMap[self.nodes[(index - 1) // 2]]:
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def heapify(self, index, size):
        left = index * 2 + 1
        while left < size:
            smallest = left + 1 if left + 1 < size and self.distanceMap[self.nodes[left + 1]] < self.distanceMap[
                self.nodes[left]] else left
            smallest = smallest if self.distanceMap[self.nodes[smallest]] < self.distanceMap[
                self.nodes[index]] else index
            if smallest == index:
                break
            self.swap(smallest, index)
            index = smallest
            left = index * 2 + 1

    def isEntered(self, node):
        '''节点进入过堆'''
        return node in self.heapIndexMap

    def inHeap(self, node):
        '''节点正在堆中'''
        return self.isEntered(node) and self.heapIndexMap[node] != -1

    def swap(self, index1, index2):
        self.heapIndexMap[self.nodes[index1]] = index2
        self.heapIndexMap[self.nodes[index2]] = index1
        self.nodes[index1], self.nodes[index2] = self.nodes[index2], self.nodes[index1]
