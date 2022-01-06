# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
归并排序

1）整体是递归，左边排好序+右边排好序+merge让整体有序
2）让其整体有序的过程里用了排外序方法
3）利用master公式来求解时间复杂度
4）当然可用非递归实现

关于小和问题、逆序对，只要关于左边**的个数、右边**的个数问题都可以用逆序对改
'''
'''
    本问题可以使用master公式求解时间复杂度  T(N) = a * T(N/b) + O(N^d)
        N 问题规模
        T(N) 母问题
        T(N/b) 子问题
        a 子问题被调用次数，子问题是等量的情况下，被调用次数
        d 除去调用子问题之外，剩下问题的时间复杂度

        1) 如果log(b,a)<d,时间复杂度是O(N^d)  # log(b,a)=log以b为低a的对数
        2) 如果log(b,a)=d,时间复杂度是O(N^d*logN)
        3) 如果log(b,a)>d,时间复杂度是O(N^log(b,a))
        '''


# O(N*logN)
def mergeSort(lst):
    if lst == None or len(lst) < 2:
        return lst
    l = 0
    r = len(lst) - 1
    return process(lst, l, r)


def merge(lst, l, mid, r):
    '建立新列表，遍历比较左右数组，谁小谁先插入到新列表中'
    i = l
    j = mid + 1
    help = []
    while i <= mid and j <= r:
        if lst[i] <= lst[j]:
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

# T(N) = 2 * T(N/2) + O(N^1)
# log(2,2) = 1
# O(N^1*logN) = O(N*logN)
def process(lst, l, r):
    if l == r:
        return
    mid = l + ((r - l) >> 1)
    process(lst, l, mid)
    process(lst, mid + 1, r)
    merge(lst, l, mid, r)


# 非递归方法实现 O(N*logN)
def mergeSort2(lst):
    '遍历数组，分别两两有序，再四四有序，以此类推'
    if lst == None or len(lst) < 2:
        return
    n = len(lst)
    mergeSize = 1  # 当前有序的，左组长度
    while mergeSize < n:  # logN
        l = 0  # 左侧索引下标
        while l < n:  # N
            mid = l + mergeSize - 1
            if mid >= n:
                break
            r = min(mid + mergeSize, n - 1)
            merge(lst, l, mid, r)
            l = r + 1
        if mergeSize > n / 2:  # 防止内存溢出
            break
        mergeSize <<= 1 # mergeSize * 2

# 1:03:28