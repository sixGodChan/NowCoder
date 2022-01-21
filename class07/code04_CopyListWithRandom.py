# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
常见面试题

一种特殊的链表节点类描述如下：
class Node{
int value;
Node next;
Node rand;
Node(int val){value=val;}
}
rand指针是单链表节点结构中新增的指针，rand可能指向链表中的任意一个节点，也可能指向null。
给定一个由Node节点类型组成的无循环单链表的头节点head,请实现一个函数完成这个链表的复制，并返回复制的新链表的头节点。
【要求】
时间复杂度O(N),额外空间复杂度O(1)
'''


class Node():
    def __init__(self, val):
        self.value = val
        self.next = None
        self.rand = None


# 利用哈希表，遍历：key是原节点，value是克隆接节点，再遍历：设置克隆节点的next和rand
def copyListWithRand1(head):
    hashMap = {}
    cur = head
    while cur != None:
        hashMap[cur] = Node(cur.value)
        cur = cur.next

    cur = head
    while cur != None:
        next = cur.next
        rand = cur.rand
        # cur 老
        # hashMop[cur] 新
        hashMap[cur].next = hashMap[next]
        hashMap[cur].rand = hashMap[rand]
        cur = cur.next
    return hashMap[head]


# 不用哈希表,遍历：将克隆节点插入原节点后，再遍历：取原节点和克隆节点设置rand，最后分离
def copyListWithRand2(head):
    if head == None:
        return
    cur = head
    # 1 -> 2 -> 3 -> null
    # 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> null
    while cur != None:
        next = cur.next
        cur.next = Node(cur.vlaue)
        cur.next.next = next
        cur = next

    cur = head
    # 1 1' 2 2' 3 3'
    # 依次设置 1' 2' 3' random指针
    while cur != None:
        clone = cur.next  # 原节点的next是克隆节点
        if cur.rand != None:
            clone.rand = cur.rand.next  # 克隆节点的rand是原节点rand的下一个
        else:
            clone.rand = None
        cur = cur.next.next

    cur = head
    res = head.next
    # 老 新 混在一起，next方向上，random正确
    # next方向上，把新老链表分离
    while cur != None:
        next = cur.next.next
        clone = cur.next
        cur.next = next
        if next != None:
            clone.next = next.next
        else:
            clone.next = None
        cur = next

    return res


# 1:42:00
if __name__ == '__main__':
    a = Node(1)
