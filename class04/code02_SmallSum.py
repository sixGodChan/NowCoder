# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
归并排序 常见面试题

小和问题

在一个数组中，一个数左边比它小的数的总和，叫小和，所有数的小和累加起来，叫数组小和。求数组小和。
例子：[1,3,4,2,5]
1左边比1小的数：没有1
3左边比3小的数：1
4左边比4小的数：1、3
2左边比2小的数：1
5左边比5小的数:1、3、4、2
所以数组的小和为1+1+3+1+1+3+4+2=16
'''


def smallSum(lst):
    '''
    暴力 O（N^2）
    归并排序merge中计算小和
    '''
    if lst == None or len(lst) < 2:
        return lst
    l = 0
    r = len(lst) - 1
    return process(lst, l, r)

def merge(lst, l, mid, r):
    i = l
    j = mid + 1
    help = []
    count = 0
    while i <= mid and j <= r:
        if lst[i] < lst[j]:  # <
            count += lst[i] * (r - j + 1)  # 左组比右组小几个
            help.append(lst[i])
            i += 1
        else:
            help.append(lst[j])
            j += 1
    while i <= mid:
        help.append(lst[i])
        i += 1
    while j <= r:
        help.append(lst[j])
        j += 1
    for k in range(len(help)):
        lst[k + l] = help[k]
    return count


def process(lst, l, r):
    if l == r:
        return 0  # 没有数，不会产生小和
    mid = l + ((r - l) >> 1)
    res1 = process(lst, l, mid)  # 左侧merge行为，返回小和
    res2 = process(lst, mid + 1, r)  # 右侧merge行为，返回小和
    res3 = merge(lst, l, mid, r)  # 左右整体merge行为，返回小和
    return res1 + res2 + res3  # 三者相加是全部小和
