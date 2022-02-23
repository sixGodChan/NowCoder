# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
怎么尝试一件事？

1）有经验但是没有方法论？
2）怎么判断一个尝试就是最优尝试？
3）难道尝试这件事真的只能拼天赋？那我咋搞定我的面试？
4）动态规划是什么？好高端的样子哦...和尝试有什么关系？
接下来->暴力递归到动态规划的套路！解决任何面试中的动态规划问题！

暴力递归到动态规划

什么暴力递归可以继续优化？

有重复调用同一个子问题的解，这种递归可以优化
如果每一个子问题都是不同的解，无法优化也不用优化

'''


def f(n):
    '''斐波那契数列'''
    if n == 1:
        return 1
    if n == 2:
        return 1
    return f(n - 1) + f(n - 2)


'''
题目一

假设有排成一行的N个位置记为1~N，N一定大于或等于2
开始时机器人在其中的M位置上(M一定是1~N中的一个)
如果机器人来到1位置，那么下一步只能往右来到2位置；
如果机器人来到N位置，那么下一步只能往左来到N-1位置；
如果机器人来到中间位置，那么下一步可以往左走或者往右走；
规定机器人必须走K步，最终能来到P位置(P也是1~N中的一个)的方法有多少种
给定四个参数 N、M、K、P，返回方法数

'''


def ways1(N, M, K, P):
    '''暴力递归'''
    if N < 2 or M < 1 or M > N or K < 1 or K < N:
        return -1
    return work1(N, M, K, P)


def work1(N, cur, rest, P):
    '''
    :param N: 有哪些位置？1~N
    :param cur: 机器人当前来到的位置是cur
    :param rest: 机器人还有rest步需要去走
    :param P: 最终的目标是P
    :return: 机器人从cur出发，走过rest步之后，最终停在aim的方法数，是多少？
    '''
    if rest == 0:  # 来到最后
        return 1 if cur == P else 0  # 这种方法是否成立
    if cur == 1:  # 只能往左走
        return work1(N, cur + 1, rest - 1, P)
    if cur == N:  # 只能往右走
        return work1(N, cur - 1, rest - 1, P)
    # 可以王左也可以往右走
    return work1(N, cur + 1, rest - 1, P) + work1(N, cur - 1, rest - 1, P)


def ways2(N, M, K, P):
    '''最糙的动态规划 -> 计划搜索'''
    if N < 2 or M < 1 or M > N or K < 1 or K < N:
        return -1
    dp = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]  # 二维表 [[-1, -1], [-1, -1], [-1, -1]]
    return work2(N, M, K, P, dp)


def work2(N, cur, rest, P, dp):
    '''
    :param N: 有哪些位置？1~N
    :param cur: 机器人当前来到的位置是cur
    :param rest: 机器人还有rest步需要去走
    :param P: 最终的目标是P
    :param dp: 历史结果缓存
    :return: 机器人从cur出发，走过rest步之后，最终停在aim的方法数，是多少？
    '''
    if dp[cur][rest] != -1:
        return dp[cur][rest]
    if rest == 0:  # 来到最后
        dp[cur][rest] = 1 if cur == P else 0  # 这种方法是否成立
        return dp[cur][rest]
    if cur == 1:  # 只能往左走
        dp[cur][rest] = work1(N, cur + 1, rest - 1, P)
        return dp[cur][rest]
    if cur == N:  # 只能往右走
        dp[cur][rest] = work1(N, cur - 1, rest - 1, P)
        return dp[cur][rest]
    # 可以王左也可以往右走
    dp[cur][rest] = work1(N, cur + 1, rest - 1, P) + work1(N, cur - 1, rest - 1, P)
    return dp[cur][rest]

# 2:17:17