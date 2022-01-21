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

常见面试题
给定一个单链表的头节点head，请判断该链表是否为回文结构
1）栈的方法特别简单（笔试用）
2）改原链表的方法就要注意边界了（面试用）
'''


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


from class03.code03_DoubleEndsQueueToStackAndQueue import MyStack


# 栈的方法1，遍历链表，压入栈，再遍历链表，同时弹出栈比对，完全一致是回文(额外空空间复杂度N)
def isPalindrome1(head):
    tmp = head
    mystack = MyStack()
    while tmp != None:
        mystack.push(tmp)
        tmp = tmp.next
    while not mystack.isEmpty():
        if mystack.pop().value != head.value:
            return False
        head = head.next
    return True


# 栈的方法2，快慢指针找到中点，从中点右侧依次压入栈，弹出栈，同时从头遍历链表比对，完全一致是回文(额外空空间复杂度N/2)
def isPalindrome2(head):
    if head == None or head.next == None:
        return True
    slow = head.next
    fast = head  # fast = head.next 也行
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    mid = slow
    mystack = MyStack()
    while mid != None:
        mystack.push(mid)
        mid = mid.next
    while not mystack.isEmpty():
        if mystack.pop().value != head.value:
            return False
        head = head.next
    return True


# 改原链表的方法，找到中间节点，将后半部分链表逆序，左右指针同时向中间走并比较value,得出结论后将链表还原(额外空空间复杂度O(1))
def isPalindrome3(head):
    if head == None or head.next == None:
        return True
    if head.next.next == None:
        return True if head.value == head.next.value else False
    slow = head.next
    fast = head.next.next
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    cur = slow.next  # slow中点
    slow.next = None
    # 逆序后半段
    front = None
    while cur != None:
        last = cur.next
        cur.next = front
        front = cur
        cur = last

    cur1 = front  # 逆序头结点记录
    res = True
    while front != None and head != None:
        if front.value != head.value:
            res = False
            break
        front = front.next
        head = head.next

    # 再逆序后半段
    front1 = None
    while cur1 != None:
        last = cur1.next
        cur1.next = front1
        front1 = cur1
        cur1 = last
    slow.next = front1
    return res

# 0:49:00

def printLinkedList(node):
    print('Linked list:', end='')
    while node != None:
        print(node.value, " ", end='')
        node = node.next
    print()


if __name__ == '__main__':
    head = None
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)

    head = Node(1)
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)

    head = Node(1)
    head.next = Node(2)
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)

    head = Node(1)
    head.next = Node(1)
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(1)
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(1)
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    printLinkedList(head)
    print(isPalindrome1(head), '|', end='')
    print(isPalindrome2(head), '|', end='')
    print(isPalindrome3(head), '|')
    printLinkedList(head)
    print('=' * 20)
