# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
链表
常见面试题

给定两个可能有环也可能无环的链表，头节点head1和head2。
请实现一个函数，如果两个链表相交，请返回相交的第一个点。
如果不相交，返回null
【要求】
如果两个链表长度之和是N，时间复杂度请达到O（N），额外空间复杂度请达到O(1)

本题可以是三个面试题的合集
1给一个链表，返回第一入环节点
2两个无环链表，返回第一相交的节点
3两个有环链表，返回第一个相交的节点
'''


# 先实现一个函数，放入头节点，返回第一个入环节点，否侧返回null
# （1.利用set，当某个节点第二次出现，表示其就是第一个入环节点；
#   2.利用快慢指针，慢先走1步，快先走2步，慢每次走1步，快每次走2步，肯定会在环中相遇，快回到head每次走1步，慢继续每次走1步，再次相遇即是第一个入环节点）

def getLoopNode(head):
    '''找到链表第一入环节点，如果无环，返回None'''
    if head == None or head.next == None or head.next.next == None:  # 没有节点或只有一个节点或只有两个节点
        return None
    s = head.next  # 慢指针
    f = head.next.next  # 快指针
    while s != f:
        if s.next == None or f.next == None:
            return None
        s = s.next
        f = f.next.next
    f = head
    while s != f:
        s = s.next
        f = f.next
    return s


# 1:：59：22

# 将head1和head2带入getloopNode(),分别得到入环节点loop1和loop2
# a）如果loop1 == Null and loop2 == Null, 如果相交两个链表肯定后半部分重合
# （1.遍历链表1如set，再遍历链表2是否在set中
#   2.第一个链表（长度len1==100）最后1一个节点end1，第二链表（长度len2==80）最后一个节点end2，判断端end1是否等于end2，等于说明相交，第一个链表先走20，然后第一第二链表一起走，同时判断是否相等，就会找到第一个相交节点。）

def noLoop(head1, head2):
    '''如果两个链表都无环，返回第一相交节点，如果不相交，返回null'''
    if head1 == None or head2 == None:
        return None
    end1 = head1
    end2 = head2
    n = 0  # 差值
    while end1.next != None:
        n += 1
        end1 = end1.next
    while end2.next != None:
        n -= 1
        end2 = end2.next
    if end1 != end2:
        return None
    cur1 = head1 if n > 0 else head2  # 谁长，谁的头变成cur1
    cur2 = head2 if cur1 == head1 else head1  # 谁短，谁的头变成cur2
    n = abs(n)
    while n != 0:
        n -= 1
        cur1 = cur1.next
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1


# 2:08:53

# b）如果loop1 == Null and loop2 != Null, 这种情况两个链表绝对不会相交
# c）如果loop1 ！= Null and loop2 == Null, 这种情况两个链表绝对不会相交
# d）如果loop1 ！= Null and loop2 != Null,两个链表相交，他们肯定是共用环的
# （情况1.两个链表是独立的两个链表，则loop1！=loop2,loop1转一圈不会碰到loop2
# 情况2.两个链表先相交，相交节点是同一个，之后在入环，则loop1==loop2
# 情况3.两个链表分别入环，相交节点在环上，则loop1！=loop2,loop1转一圈会碰到loop2,返回loop1或loop2都行）

def bothLoop(head1, head2, loop1, loop2):
    '''如果两个链表都有环，返回第一相交结点，如果不相交，返回null'''
    if loop1 == loop2:
        end1 = head1
        end2 = head2
        n = 0
        while end1.next != loop1:
            n += 1
            end1 = end1.next
        while end2.next != loop2:
            n -= 1
            end2 = end2.next
        cur1 = head1 if n > 0 else head2
        cur2 = head2 if cur1 == head1 else head1
        n = abs(n)
        while n != 0:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1  # or loop2
            cur1 = cur1.next
        return None


def getIntersectNode(head1, head2):
    if head1 == None or head2 == None:
        return None
    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)
    if loop1 == None and loop2 == None:
        return noLoop(head1, head2)
    elif loop1 != None and loop2 != None:
        return bothLoop(head1, head2, loop1, loop2)
    else:
        return None


class Node():
    def __init__(self, val):
        self.value = val
        self.next = None


if __name__ == '__main__':
    # 1->2->3->4->5->6->7->null
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)

    # 0->9->8->6->7->null
    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next  # 8->6
    print(getIntersectNode(head1, head2).value)

    # 1->2->3->4->5->6->7->4...
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    head1.next.next.next.next.next.next = head1.next.next.next  # 7->4

    # 0->9->8->2...
    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next  # 8->2
    print(getIntersectNode(head1, head2).value)

    # 0->9->8->6->4->5->6..
    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next  # 8->6
    print(getIntersectNode(head1, head2).value)

# 2:25:00