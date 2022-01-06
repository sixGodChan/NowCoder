# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
Partition过程 （分层过程）(Partition 1.0)
给定一个数组arr。和一个整数num。请把小于等于num的数放在数组左边，大于num的数放在数组右边。
要求额外空间复杂度O（1），时间复杂度O（N）
'''
import random


def partition1(lst, num):
    if lst == None:
        return
    if len(lst) < 1:
        return []
    minArea = -1  # 小于区域
    i = 0  # 当前值位置
    while i < len(lst):
        if lst[i] > num:  # 当前值>num,当前值+=1
            i += 1
        else:  # 当前值<=num,当前值与minArea的后一个值交换位置，maxArea-=1,当前值+=1
            minArea += 1
            lst[minArea], lst[i] = lst[i], lst[minArea]
            i += 1


# (Partition 2.0)
# 给定一个数组arr。和一个整数num。请把小于num的数放在数组左边，等于num的数放在数组中间，大于num的数放在数组右边。（荷兰国旗问题）
# 要求额外空间复杂度O（1），时间复杂度O（N）

def partition2(lst, num):  # 荷兰国旗
    if lst == None:
        return
    if len(lst) < 1:
        return []
    minArea = -1  # 小于区域
    maxArea = len(num)  # 大于区域
    i = 0  # 当前值位置
    while i < maxArea:
        if lst[i] > num:  # 当前值>num,当前值与maxArea的前一个值交换位置，maxArea-=1
            maxArea -= 1
            lst[maxArea], lst[i] = lst[i], lst[maxArea]
        elif lst[i] == num:  # 当前值=num, 当前值+=1
            i += 1
        else:  # 当前值<num,当前值与minArea的后一个值交换位置,minArea+=1,当前值+=1
            minArea += 1
            lst[minArea], lst[i] = lst[i], lst[minArea]
            i += 1


# 快速排序 1.0
# 最坏O(N^2)
def quickSort1(lst):
    if lst == None or len(lst) < 2:
        return

    return process1(lst, 0, len(lst) - 1)


def process1(lst, l, r):
    if l >= r:
        return
    mid = partition1plus(lst, l, r)
    process1(lst, l, mid - 1)
    process1(lst, mid + 1, r)


# 2:30:24

def partition1plus(lst, l, r):
    if l > r:
        return -1
    if l == r:
        return l
    minArea = l - 1
    num = lst[r]
    i = l
    while i < r:
        if lst[i] > num:
            i += 1
        else:
            minArea += 1
            lst[minArea], lst[i] = lst[i], lst[minArea]
            i += 1

    lst[minArea + 1], lst[r] = lst[r], lst[minArea + 1]
    return minArea + 1


# 快速排序 2.0
# 最坏O(N^2)
def quickSort2(lst):
    if lst == None or len(lst) < 2:
        return
    return process2(lst, 0, len(lst) - 1)


def process2(lst, l, r):
    if l >= r:
        return
    equalArea = partition2plus(lst, l, r)
    process2(lst, l, equalArea[0] - 1)
    process2(lst, equalArea[1] + 1, r)


def partition2plus(lst, l, r):
    if l > r:
        return [-1, -1]
    if l == r:
        return [l, r]
    minArea = l - 1
    maxArea = r
    num = lst[r]
    i = l
    while i < maxArea:
        if lst[i] > num:
            maxArea -= 1
            lst[maxArea], lst[i] = lst[i], lst[maxArea]
        elif lst == num:
            i += 1
        else:
            minArea += 1
            lst[minArea], lst[i] = lst[i], lst[minArea]
            i += 1

    lst[maxArea], lst[r] = lst[r], lst[maxArea]
    return [minArea + 1, maxArea]


# 快速排序 3.0
# O(NlogN) 空间复杂度O（logN）
def quickSort3(lst):
    if lst == None or len(lst) < 2:
        return
    return process3(lst, 0, len(lst) - 1)


def process3(lst, l, r):
    if l >= r:
        return
    index = int(random.random() * (r - l + 1))
    lst[index], lst[r] = lst[r], lst[index]
    equalArea = partition2plus(lst, l, r)
    process3(lst, l, equalArea[0] - 1)
    process3(lst, equalArea[1] + 1, r)
