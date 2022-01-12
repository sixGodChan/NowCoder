# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import heapq

def top_k(numbers, k):
  heap = [(n, i) for i, n in enumerate(numbers)]
  heapq.heapify(heap)
  print(heap)

  return list(map(lambda x: heapq.heappop(heap)[1], range(k)))

if __name__ == '__main__':
  print(top_k([5, 4, 3, 2, 1], 3)) # [4, 3, 2]

  import heapq


class Node:
  def __init__(self, value):
      self.value = value

  def __lt__(self, other):
      return self.value < other.value


def top_k(nodes, k):
  heap = [node for node in nodes]
  heapq.heapify(heap)
  print([i.value for i in heap])

  return list(map(lambda x: heapq.heappop(heap).value, range(k)))


if __name__ == '__main__':
  print(top_k([Node(5), Node(4), Node(3), Node(2), Node(1)], 3))  # [1, 2, 3]