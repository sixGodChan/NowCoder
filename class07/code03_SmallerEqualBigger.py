# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
常见面试题

将单向链表按某值划分成左边小，中间相等，右边大的形式

1）把链表放入数组里，在数组中做partition（笔试用）

2）分成小、中、大三部分，再把各个部分串起来(面试用)
'''


def listPartition1(head, value):
    if head == None or head.next == None:
        return head

    lst = []
    while head != None:
        lst.append(head)
        head = head.next

    l = -1
    r = len(lst)
    index = 0
    while index != r:
        if lst[index].value < value:
            l += 1
            lst[l], lst[index] = lst[index], lst[l]
            index += 1
        elif lst[index].value == value:
            index += 1
        else:
            r -= 1
            lst[r], lst[index] = lst[index], lst[r]

    for i in range(len(lst) - 1):
        lst[i].next = lst[i + 1]
    lst[len(lst) - 1].next = None
    return lst[0]


def listPartition2(head, value):  # O（N）稳定
    if head == None or head.next == None:
        return head
    smaller = None
    equal = None
    bigger = None
    start = None
    mid = None
    end = None
    while head != None:
        next = head.next
        head.next = None
        if head.value < value:
            if start == None:
                start = head
                smaller = head
            else:
                smaller.next = head
                smaller = head
        elif head.value == value:
            if mid == None:
                mid = head
                equal = head
            else:
                equal.next = head
                equal = head
        else:
            if end == None:
                end = head
                bigger = head
            else:
                bigger.next = head
                bigger = head
        head = next

    if smaller != None:
        smaller.next = mid
        if equal == None:
            equal = smaller
    if equal != None:
        equal.next = end
    if start != None:
        return start
    elif mid != None:
        return mid
    else:
        return end


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def printLinkedList(head):
    print('Linked List:', end='')
    while head != None:
        print(head.value, '', end='')
        head = head.next
    print()


if __name__ == '__main__':
    head1 = Node(7)
    head1.next = Node(9)
    head1.next.next = Node(1)
    head1.next.next.next = Node(8)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(2)
    head1.next.next.next.next.next.next = Node(5)
    head1.next.next.next.next.next.next.next = Node(4)
    # head1 = listPartition1(head1, 6)
    head1 = listPartition2(head1, 5)
    printLinkedList(head1)
