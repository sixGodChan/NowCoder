# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
暴力递归转动态归化

# 0:3:00
给定一个字符串str，给定一个字符串类型的数组arr。
出现的字符都是小写英文arr每一个字符串，代表一张贴纸，你可以把单个字符剪开使用，目的是拼出str来。
返回需要至少多少张贴纸可以完成这个任务。每张贴纸都有无限个。
例子：str= "babac"，arr = {"ba","c","abcd"}
至少需要两张贴纸‘ba’和‘abcd’，因为使用这两张贴纸，把每一个字符单独剪开，
含有2个a、2个b、1个c。是可以拼出str的。所以返回2。
ba + ba + c  3  abcd + abcd 2  abcd+ba 2
所以返回2

// 本题测试链接：https://leetcode.com/problems/stickers-to-spell-word

'''
import sys


def minStickers1(arr, s):
    ans = process1(arr, s)
    return -1 if ans == sys.maxsize else ans


def process1(arr, rest):
    '''
    字符串rest剩余字母
    返回使用贴纸数量
    '''
    # 不剩字母
    if rest == '':
        return 0
    # 搞定rest的，第一张贴纸是什么
    next = sys.maxsize
    for first in arr:
        nextRest = delFirstFromRest(rest, first)
        if len(nextRest) != len(rest):  # 防止无限递归
            cur = process1(arr, nextRest)
            next = min(cur, next)
    return next + (0 if next == sys.maxsize else 1)


def delFirstFromRest(rest, first):
    str1 = rest
    str2 = first
    count = [0 for _ in range(26)]
    for i in str1:
        count[ord(i) - ord('a')] += 1
    for i in str2:
        count[ord(i) - ord('a')] -= 1
    res = ''
    for i in range(26):
        if count[i] > 0:
            for _ in range(count[i]):
                res += chr(i + ord('a'))
    return res


def minStickers2(arr, s):
    '''关键优化（用词频代替贴纸数组）'''
    counts = [[0 for _ in range(26)] for _ in range(len(arr))]
    for i in range(len(arr)):
        for cha in arr[i]:
            counts[i][ord(cha) - ord('a')] += 1
    dp = {'': 0}
    ans = process2(counts, s, dp)
    return -1 if ans == sys.maxsize else ans


def process2(counts, rest, dp):
    if rest in dp:
        return dp[rest]

    # rest做词频统计
    rCount = [0 for _ in range(26)]
    for i in rest:
        rCount[ord(i) - ord('a')] += 1

    next = sys.maxsize
    for i in range(len(counts)):
        # 尝试第一张贴纸是谁
        stricker = counts[i]
        # 最关键的优化(重要的剪枝!这一步也是贪心!)
        if stricker[ord(rest[0]) - ord('a')] > 0:
            builder = ''
            for j in range(26):
                if rCount[j] > 0:
                    nums = rCount[j] - stricker[j]
                    for k in range(nums):
                        builder += chr(j + ord('a'))
            next = min(next, process2(counts, builder, dp))
    ans = next + (0 if next == sys.maxsize else 1)
    dp[rest] = ans
    return ans


if __name__ == '__main__':
    s = "babac"
    arr = ["ba", "c", "abcd"]
    print(minStickers1(arr, s))
    print(minStickers2(arr, s))