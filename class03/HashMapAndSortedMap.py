# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
哈希表、有序表

哈希表
key value 查询时间复杂度O(1)

有序表
key value 插入后自动有序, 查询时间复杂度O(logN)

'''
import collections


def hashMapAndSoredMap():
    dic = dict()
    print(dic.setdefault(10, '我是10'))
    print(dic.setdefault(9, '我是9'))
    print(dic.get(10))

    odic = {}
    odic[3] = 3
    odic[2] = 2
    odic[5] = 5
    odic[4] = 4
    print(odic)
    print(sorted(odic, key=lambda s: s))
    # odic = collections.OrderedDict(sorted(odic, key=lambda s: s[1]))
    # print(odic)
    # print(odic.pop(2))
    # odic[2] = 2
    # print(odic)


if __name__ == '__main__':
    hashMapAndSoredMap()
