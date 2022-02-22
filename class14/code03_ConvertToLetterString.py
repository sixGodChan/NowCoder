# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
暴力递归（尝试）

从左往右的尝试模型1

规定1和A对应、2和B对应、3和C对应...
那么一个数字字符串比如'111'就可以转化为：
'AAA'、'KA'和'AK'
给定一个只有数字字符组成的字符串str，返回有多少种转化结果
'''


def convert(s):
    if s == None and len(s) == 0:
        return 0

    return process(s, 0)


def process(s, i):
    '''
    s[0...i-1]已经转化完了，固定了
    i之前的位置，如何转化已经做过决定了，不用再关心
    i...有多少种转化的结果
    '''
    if i == len(s):  # base case
        return 1
    # i有到终止位置
    if s[i] == '0':
        return 0
    # i没有到终止位置
    # str[i]字符不是'0'
    if s[i] == '1':
        res = process(s, i + 1)  # i自己作为单独的部分，后续有多少种方法
        if i + 1 < len(s):
            res += process(s, i + 2)  # (i和i+1)作为单独的部分，后续有多少种方法
        return res
    if s[i] == '2':
        res = process(s, i + 1)  # i自己作为单独的部分，后续有多少种方法
        # (i和i+1)作为单独的部分并且没有超过26，后续有多少种方法
        if i + 1 < len(s) and s[i + 1] >= '0' and s[i + 1] <= '6':
            res += process(s, i + 2)  # (i和i+1)作为单独的部分，后续有多少种方法
        return res
    # str[i] == '3' ~ '9'
    return process(s, i + 1)


if __name__ == '__main__':
    print(convert('111'))
