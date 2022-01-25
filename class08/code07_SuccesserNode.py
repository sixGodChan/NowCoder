# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二叉树

题目
二叉树结构如下定义：
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # 多了一个指向父节点的属性

给你二叉树中的某个节点，返回该节点的后继节点
后继节点指的是一颗二叉树在中序遍历的序列中，一个节点的下一个节点（对应前驱节点）
解1）暴力解，通过parent找到头，在中序遍历，在找到x的下个节点， 时间复杂度O（N）
2）如果x节点有右树，则其后继必是右树最左节点；
    如果x没有右树，如果x是其父节点的右孩子，继续向上找，x=x.parent,直到x是其父节点的左孩子，其父是后继节点（等同，h节点左树中最右的节点是x，则x的后继是h）；
    时间复杂度O（k）
'''


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # 多了一个指向父节点的属性


def getSuccessorNode(cur):
    if cur == None:
        return
    if cur.right != None:  # 有右子树
        return getLeftMost(cur.right)
    else:  # 没有右子树
        while cur.parent != None:
            if cur.parent.left == cur:  # cur是其父节点的左孩子
                return cur.parent
            cur = cur.parent
        return None

def getLeftMost(cur):
    '''找到最左'''
    if cur == None:
        return None
    while cur.left != None:
        cur = cur.left
    return cur

if __name__ == '__main__':
    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    from class08.code04_SerializeAndReconstructTree import printTree
    from class08.code01_RecursiveTraversalBT import mid

    printTree(head)
    print(mid(head))

    test = head.left.left
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.left.left.right
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.left
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.left.right
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.left.right.right
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.right.left.left
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.right.left
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.right
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.right.right  # 10's next is None
    print(test.value, " next: ", getSuccessorNode(test))
