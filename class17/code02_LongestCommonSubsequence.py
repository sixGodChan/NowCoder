# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
多样本位置全应对的尝试模型

题目

给定两个字符串str1和str2，
返回这两个字符串的最长公共子序列长度
比如 ： str1 = “a12b3c456d”,str2 = “1ef23ghi4j56k”
最长公共子序列是“123456”，所以返回长度6

链接：https://leetcode.com/problems/longest-common-subsequence/
'''


def longestCommonSubsequence1(str1, str2):
    '''
    str1[0...i]和str2[0...j]，这个范围上最长公共子序列长度是多少？
	可能性分类:
	a) 最长公共子序列，一定不以str1[i]字符结尾、也一定不以str2[j]字符结尾
	b) 最长公共子序列，可能以str1[i]字符结尾、但是一定不以str2[j]字符结尾
	c) 最长公共子序列，一定不以str1[i]字符结尾、但是可能以str2[j]字符结尾
	d) 最长公共子序列，必须以str1[i]字符结尾、也必须以str2[j]字符结尾
	注意：a)、b)、c)、d)并不是完全互斥的，他们可能会有重叠的情况
	但是可以肯定，答案不会超过这四种可能性的范围
	那么我们分别来看一下，这几种可能性怎么调用后续的递归。
	a) 最长公共子序列，一定不以str1[i]字符结尾、也一定不以str2[j]字符结尾
	   如果是这种情况，那么有没有str1[i]和str2[j]就根本不重要了，因为这两个字符一定没用啊
	   所以砍掉这两个字符，最长公共子序列 = str1[0...i-1]与str2[0...j-1]的最长公共子序列长度(后续递归)
	b) 最长公共子序列，可能以str1[i]字符结尾、但是一定不以str2[j]字符结尾
	   如果是这种情况，那么我们可以确定str2[j]一定没有用，要砍掉；但是str1[i]可能有用，所以要保留
	   所以，最长公共子序列 = str1[0...i]与str2[0...j-1]的最长公共子序列长度(后续递归)
	c) 最长公共子序列，一定不以str1[i]字符结尾、但是可能以str2[j]字符结尾
	   跟上面分析过程类似，最长公共子序列 = str1[0...i-1]与str2[0...j]的最长公共子序列长度(后续递归)
	d) 最长公共子序列，必须以str1[i]字符结尾、也必须以str2[j]字符结尾
	   同时可以看到，可能性d)存在的条件，一定是在str1[i] == str2[j]的情况下，才成立的
       所以，最长公共子序列总长度 = str1[0...i-1]与str2[0...j-1]的最长公共子序列长度(后续递归) + 1(共同的结尾)
	综上，四种情况已经穷尽了所有可能性。四种情况中取最大即可
	其中b)、c)一定参与最大值的比较，
	当str1[i] == str2[j]时，a)一定比d)小，所以d)参与
	当str1[i] != str2[j]时，d)压根不存在，所以a)参与
	但是再次注意了！
	a)是：str1[0...i-1]与str2[0...j-1]的最长公共子序列长度
	b)是：str1[0...i]与str2[0...j-1]的最长公共子序列长度
	c)是：str1[0...i-1]与str2[0...j]的最长公共子序列长度
	a)中str1的范围 < b)中str1的范围，a)中str2的范围 == b)中str2的范围
	所以a)不用求也知道，它比不过b)啊，因为有一个样本的范围比b)小啊！
	a)中str1的范围 == c)中str1的范围，a)中str2的范围 < c)中str2的范围
	所以a)不用求也知道，它比不过c)啊，因为有一个样本的范围比c)小啊！
	至此，可以知道，a)就是个垃圾，有它没它，都不影响最大值的决策
	所以，当str1[i] == str2[j]时，b)、c)、d)中选出最大值
	当str1[i] != str2[j]时，b)、c)中选出最大值
    :param str1:
    :param str2:
    :return:
    '''
    dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    dp[0][0] = 1 if str1[0] == str2[0] else 0
    for i in range(1, len(str1)):
        dp[i][0] = max(dp[i - 1][0], 1 if str1[i] == str2[0] else 0)  # 设置第0列
    for j in range(1, len(str2)):
        dp[0][j] = max(dp[0][j - 1], 1 if str2[j] == str1[0] else 0)  # 设置第0行
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    return dp[len(str1) - 1][len(str2) - 1]

if __name__ == '__main__':
    str1 = 'a12b3c456d'
    str2 = '1ef23ghi4j56k'
    print(longestCommonSubsequence1(str1, str2))

# 2:00:20