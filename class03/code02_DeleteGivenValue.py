# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
单向链表、双向链表 应用

2）如何删除给定值
删除链表中节点value等于X全部节点，并返回头结点
'''

class Node():
    '''节点类'''
    def __init__(self, data):
        self.value = data
        self.next = None

def removeValue(head, num):
    '''删除链表中value==num全部节点'''
    while head != None:
        if head.value != num:
            break
        head = head.next
    pre = head
    cur = head
    while cur != None:
        if cur.value == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return head