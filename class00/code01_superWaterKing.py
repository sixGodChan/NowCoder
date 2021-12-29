# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
水王问题
比喻论坛灌水，超过一半的帖子都是一个人发的，称呼这个人是水王
有水王返回水王，没有返回-1
'''
import random


def waterKing(lst):
    '''巧妙水王
    每次寻找两个不同的数据，一起消掉
    两个变量：候选=None，血量=0
    遍历数据，1）当血量==0，候选=当前数据，血量+=1
    2）当血量！=0，a)候选==当前数据，血量+=1
                b)候选！=当前数据，血量-=1
    遍历结束，血量==0，返回-1
    候选数量>(数组长度/2),返回候选，否则，返回-1
    '''
    if lst == None or len(lst) == 0:
        return -1

    number = None
    hp = 0
    for i in lst:
        if hp == 0:
            hp += 1
            number = i
        else:
            if number == i:
                hp += 1
            else:
                hp -= 1

    if hp == 0:
        return -1

    count = 0
    for i in lst:
        if i == number:
            count += 1
    n = len(lst)
    return number if count > (n >> 1) else -1


def comparator(lst):
    '''对数器
    哈希表，遍历计数，最后判断有没有水王
    '''
    if lst == None or len(lst) == 0:
        return -1

    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    n = len(lst)
    for key, val in dic.items():
        if val > (n >> 1):
            return key
    return -1


def generateRandomArray(maxSize, maxValue):
    '''生成随机数组'''
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)) - int(random.random() * maxValue))
    return lst


if __name__ == '__main__':
    testTimes = 50000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        res1 = waterKing(arr1)
        res2 = comparator(arr2)
        if res1 != res2:
            succeed = False
            break
    print('成功！' if succeed else '失败！')
