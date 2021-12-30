# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
二分法 应用
局部最小值问题
一个无序数组，任意相邻两个必不相同，要求返回任意局部最小值
定义局部最小值：
1）0位置比1位置的数小，0位置是局部最小值
2）N位置比N-1位置的数小，N位置是局部最小值
3）i位置比i-1和i+1位置的数小，i位置是局部最小值
'''

def getlessIndex(lst):
    if lst == None or len(lst) == 0:
        return -1
    # 先判断0位置
    if len(lst) == 1 or lst[0] < lst[1]:
        return 0
    # 再判断N位置
    if lst[len(lst) - 1] < lst[len(lst) - 2]:
        return repr(len(lst) - 1)
    l = 1
    r = len(lst) - 2
    # 再判断中间位置
    while l < r:
        mid = l + ((r - l) >> 1)
        if lst[mid] < lst[mid - 1]:
            r = mid - 1
        elif lst[mid] < lst[mid + 1]:
            l = mid + 1
        else:
            return mid
    return l

