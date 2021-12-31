# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
单向链表、双向链表 应用

1）如何反转
1→2→3→None
3→2→1→None

'''
import random


class Node():
    '''节点类'''
    def __init__(self, data):
        self.value = data
        self.next = None


class DoubleNode():
    '''双向节点类'''
    def __init__(self, data):
        self.value = data
        self.last = None
        self.next = None


def reverseLinkedList(head):
    '''反转单链表'''
    pre = None
    next = None
    while head != None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


def reverseDoubleList(head):
    pre = None
    next = None
    while head != None:
        next = head.next
        head.next = pre
        head.last = next
        pre = head
        head = next
    return pre


def generateRandomLinkedList(length, value):
    '''随机生成单链表'''
    size = int(random.random() * (length + 1))
    if size == 0:
        return
    size -= 1
    head = Node(int(random.random() * (value + 1)))
    pre = head
    while size != 0:
        cur = Node(int(random.random() * (value + 1)))
        pre.next = cur
        pre = cur
        size -= 1
    return head

def generateRandomDoubleList(length, value):
    '''随机生成双向链表'''
    size = int(random.random() * (length + 1))
    if size == 0:
        return
    size -= 1
    head = Node(int(random.random() * (value + 1)))
    pre = head
    while size != 0:
        cur = Node(int(random.random() * (value + 1)))
        pre.next = cur
        pre.last = pre
        pre = cur
        size -= 1
    return head


def getLinkedListOriginOrder(head):
    '''将链表值取出加入列表中'''
    lst = []
    while head != None:
        lst.append(head.value)
        head = head.next
    return lst

def getDoubleListOriginOrder(head):
    '''将双向链表值取出加入列表中'''
    lst = []
    while head  != None:
        lst.append(head.value)
        head = head.next
    return lst

def checkLinkedListReverse(lst, head):
    for i in lst[::-1]:
        if i != head.value:
            return False
        head = head.next
    return True

def checkDoubleListReverse(lst, head):
    end = Node(None)
    for i in lst[::-1]:
        if i != head.value:
            return False
        end = head
        head = head.next
    for i in lst:
        if i != end.value:
            return False
        end = end.last
    return True


if __name__ == '__main__':
    length = 50
    value = 100
    testTime = 100000
    print('test begin!')
    for i in range(testTime):
        node1 = generateRandomLinkedList(length, value)
        lst1 = getLinkedListOriginOrder(node1)
        node1 = reverseLinkedList(node1)
        if not checkLinkedListReverse(lst1, node1):
            print('Oops1!')

        node2 = generateRandomDoubleList(length, value)
        lst2 = getDoubleListOriginOrder(node2)
        node2 = reverseDoubleList(node2)
        if not checkLinkedListReverse(lst2, node2):
            print('Oops2!')

    print('test finish!')