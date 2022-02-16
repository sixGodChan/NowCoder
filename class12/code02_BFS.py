# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
图的宽度优先&深度优先遍历

宽度优先遍历

1、利用队列实现
2、从源节点开始依次按照宽度进队列，然后弹出
3、每弹出一个点，把该节点所有没有进过队列的邻接点放入队列
4、直到队列变空

深度优先遍历

1、利用栈实现
2、从源节点开始把节点按照深度放入栈，然后弹出
3、没弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
4、直到栈变空

'''
from class12.code01_Graph import Node
import queue


def bfs(node):
    '''从node出发，进行宽度优先遍历'''
    if node == None:
        return
    q = queue.Queue()
    s = set()  # 一个set防止重复进队列
    q.put(node)
    s.add(node)
    while not q.empty():
        cur = q.get()
        print(cur.value)  # 出队列打印
        for next in cur.nexts:
            if next not in s:
                q.put(next)
                s.add(next)

