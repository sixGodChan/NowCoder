# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
import random


def dutchFlag01(lst, num):
    '''给定一个数组arr,和一个数num，请把小于等于num的数放在数组的左边，大于num的数放在数组右边。要求额外空间复杂度O(1),时间复杂度O(N)

    (没有要求有序)

    在数组最左侧设定一个'<=区'，i从0开始
    1)i位置<=num，i位置的数和'<=区'的下一个数交换，'<=区'右扩，i++
    2)i位置>num，i++
    '''

    if lst == None or len(lst) < 2:
        return
    p = -1
    i = 0
    while i < len(lst):
        if lst[i] <= num:
            p += 1
            lst[i], lst[p] = lst[p], lst[i]
        i += 1


def dutchFlag02(lst, num):
    '''荷兰国旗问题：
    给定一个数组arr，和一个数num，请把小于num的数放在数组的左边，等于num的数放在数组的中间，大于num的数放在数组右边。要求额外空间复杂度O(1)，时间复杂度O(N)

    在数组最左侧设定一个’<区‘，i从-1开始, 数组最右侧设定一个’>区‘，i从N开始
    1)i位置<num，i位置的数和’<区‘的下一个数交换，‘<区’右扩，i++
    2)i位置=num，i++
    3)i位置>num，i位置的数和’>区‘的下一个数交换，'>区’左扩，i原地不变
    4)i和’>区‘接触时，停止
    '''
    if lst == None or len(lst) < 2:
        return
    p1 = -1
    p2 = len(lst)
    i = 0
    while i < p2:
        if lst[i] < num:
            p1 += 1
            lst[i], lst[p1] = lst[p1], lst[i]
            i += 1
        elif lst[i] == num:
            i += 1
        else:
            p2 -= 1
            lst[i], lst[p2] = lst[p2], lst[i]


if __name__ == '__main__':
    a = [3, 5, 6, 7, 4, 3, 5, 8]
    dutchFlag01(a, 5)
    print(a)
    b = [3, 5, 6, 3, 4, 5, 2, 6, 9, 0]
    dutchFlag02(b, 5)
    print(b)
