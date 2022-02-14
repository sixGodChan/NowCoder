#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
贪心算法

1，最自然智慧的算法
2，用一种局部最功利的标准，总是做出在当前看来是最好的选择
3，难点在于证明局部最功利的标准可以得到全局最优解
4，对于贪心算法的学习主要以增加阅历和经验为主

贪心算法求解的标准过程

1，分析业务
2，根据业务逻辑找到不同的贪心策略
3，对于能举出反例策略直接跳过，不能举出反例的策略要证明有效性
这往往是特别困难的，要求数学能力很高且不具有统一的技巧


贪心算法的解题套路

1，实现一个不依靠贪心策略的解题法X，可以用最暴力的尝试
2，脑补出贪心策略A、贪心策略B、贪心策略C...
3，用解法X和对数器，用实验的方式得知哪个贪心策略正确
4，不要去纠结贪心策略的证明


贪心算法的解题套路实战

一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲。
给你每一个项目开始的时间和结束的时间
你来安排宣讲的日程，要求会议室进行的宣讲的场次最多。
返回最多的宣讲场次。
'''


class Program():
    def __init__(self, start, end):
        self.start = start
        self.end = end


def bestArrange1(programs):
    '''
    暴力！所有情况都尝试！
    :param programs: 
    :return: 
    '''
    if programs == None or len(programs) == 0:
        return 0
    return process(programs, 0, 0)


def process(programs, done, timeLine):
    '''
    目前来到timeLine的时间点，已经安排了done多的会议，剩下的会议programs可以自由安排
    返回能安排的最多会议数量
    :param programs: 还剩下的会议都放在programs里
    :param done: done之前已经安排了多少会议的数量
    :param timeLine: timeLine目前来到的时间点是什么
    :return: 
    '''
    if len(programs) == 0:
        return done

    m = done
    for i in range(len(programs)):
        if programs[i].start >= timeLine:
            lst = copyButExcept(programs, i)
            m = max(m, process(lst, done + 1, programs[i].end))
    return m


def copyButExcept(programs, i):
    '''
    排除i，返回一个新的列表
    :param programs: 
    :param i: 
    :return: 
    '''
    ans = []
    for k in range(len(programs) - 1):
        if i != k:
            ans.append(programs[k])
    return ans


def bestArrange2(programs):
    '''
    会议的开始时间和结束时间，都是数值，不会 < 0
    :param programs: 
    :return: 
    '''
    if programs == None or len(programs) == 0:
        return 0
    programs.sort(key=lambda x: x.end, reverse=False)
    timeLine = 0
    result = 0
    for i in range(len(programs)):
        if timeLine <= programs[i].start:
            result += 1
            timeLine = programs[i].end
    return result


# for test
import random


def generatePrograms(programSize, timeMax):
    ans = []
    for i in range(int(random.random() * (programSize + 1))):
        r1 = int(random.random() * (timeMax + 1))
        r2 = int(random.random() * (timeMax + 1))
        if r1 == r2:
            ans.append(Program(r1, r1 + 1))
        else:
            ans.append(Program(min(r1, r2), max(r1, r2)))


if __name__ == '__main__':
    programSize = 12
    timeMax = 20
    timeTimes = 1000000
    for i in range(timeTimes):
        programs = generatePrograms(programSize, timeMax)
        if bestArrange1(programs) != bestArrange2(programs):
            print('Oops!')
    print('finish!')


# 0:23:20