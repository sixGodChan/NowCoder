# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
链表问题
面试时链表结题方法论
1）对于笔试，不用太在意空间复杂度，一切为了时间复杂度
2）对于面试，时间复杂度依然放在第一位，但是一定要找到空间最省的方法

------

链表面试题常用数据结构和技巧
1）使用容器（哈希表，数组等）
2）快慢指针

------

快慢指针

1）输入链表头结点，奇数长度返回中点，偶数长度返回上中点
2）输入链表头结点，奇数长度返回中点，偶数长度返回下中点
3）输入链表头结点，奇数长度返回中点前一个，偶数长度返回上中点前一个
4）输入链表头结点，奇数长度返回中点前一个，偶数长度返回下中点前一个

# 快指针走两步，慢指针走一步，当快指针走完时，慢指针是中点

'''


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


# 1）输入链表头结点，奇数长度返回中点，偶数长度返回上中点
def midOrUpMidNode(head):
    if head == None or head.next == None or head.next.next == None:
        return head
    # 链表有3个点或以上
    slow = head.next
    fast = head.next.next
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


# 2）输入链表头结点，奇数长度返回中点，偶数长度返回下中点
def midOrDownMidNode(head):
    if head == None or head.next == None:
        return head
    # 链表有2个点或以上
    slow = head.next
    fast = head.next
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


# 3）输入链表头结点，奇数长度返回中点前一个，偶数长度返回上中点前一个
def midOrUpMidPreNode(head):
    if head == None or head.next == None or head.next.next == None:
        return None
    # 链表有3个点或以上
    slow = head
    fast = head.next.next
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


# 4）输入链表头结点，奇数长度返回中点前一个，偶数长度返回下中点前一个
def midOrDownMidPreNode(head):
    if head == None or head.next == None:
        return None
    if head.next.next == None:
        return head
    # 链表有3个点或以上
    slow = head
    fast = head.next
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


def right1(head):
    if head == None:
        return None
    cur = head
    lst = []
    while cur != None:
        lst.append(cur)
        cur = cur.next
    return lst[(len(lst) - 1) // 2]


def right2(head):
    if head == None:
        return None
    cur = head
    lst = []
    while cur != None:
        lst.append(cur)
        cur = cur.next
    return lst[len(lst) // 2]


def right3(head):
    if head == None or head.next == None or head.next.next == None:
        return None
    cur = head
    lst = []
    while cur != None:
        lst.append(cur)
        cur = cur.next
    return lst[(len(lst) - 3) // 2]


def right4(head):
    if head == None or head.next == None:
        return None
    cur = head
    lst = []
    while cur != None:
        lst.append(cur)
        cur = cur.next
    return lst[(len(lst) - 2) // 2]


if __name__ == '__main__':
    test = Node(0)
    test.next = Node(1)
    test.next.next = Node(2)
    test.next.next.next = Node(3)
    test.next.next.next.next = Node(4)
    test.next.next.next.next.next = Node(5)
    test.next.next.next.next.next.next = Node(6)
    test.next.next.next.next.next.next.next = Node(7)
    test.next.next.next.next.next.next.next.next = Node(8)

    ans1 = midOrUpMidNode(test)
    ans2 = right1(test)
    print(ans1.value if ans1 != None else '无')
    print(ans2.value if ans2 != None else '无')

    ans1 = midOrDownMidNode(test)
    ans2 = right2(test)
    print(ans1.value if ans1 != None else '无')
    print(ans2.value if ans2 != None else '无')

    ans1 = midOrUpMidPreNode(test)
    ans2 = right3(test)
    print(ans1.value if ans1 != None else '无')
    print(ans2.value if ans2 != None else '无')

    ans1 = midOrDownMidPreNode(test)
    ans2 = right4(test)
    print(ans1.value if ans1 != None else '无')
    print(ans2.value if ans2 != None else '无')

# 0:33:20