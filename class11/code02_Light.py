#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
贪心算法的解题套路实战

给定一个字符串str，只由'X'和'.'两种字符构成。
'X'表示墙，不能放灯，也不需要点亮
'.'表示居民点，可以放灯，需要点亮
如果灯放在i位置，可以让i-1，i和i+1三个位置被点亮
返回如果点亮str中所有需要点亮的位置，至少需要几盏灯

'''
import sys


def minLight1(road):
    if road == None or len(road) == 0:
        return 0
    return process([i for i in road], 0, [])


def process(string, index, lights):
    '''
	要求选出能照亮所有.的方案，并且在这些有效的方案中，返回最少需要几个灯
    :param string: 字符串列表
    :param index: str[index....]位置，自由选择放灯还是不放灯
                str[0..index-1]位置,已经做完决定了
    :param lights: 那些放了灯的位置，存在lights里
    :return: 
    '''
    if len(string) == index:  # 结束的时候
        for i in range(len(string)):  # 判断该结果是否可行
            if string[i] != 'X':  # 当前位置是'.'
                if (i - 1) not in lights and i not in lights and (i + 1) not in lights:
                    return sys.maxsize
        return len(lights)
    else:  # string还没结束
        no = process(string, index + 1, lights)
        yes = sys.maxsize
        if string[index] == '.':
            lights.append(index)
            yes = process(string, index + 1, lights)
            lights.remove(index)
        return min(no, yes)


def minLight2(road):
    '''
    贪心
    1）i是'X'，继续判断i=i+1
    2）i是'.'，i+1是'X'，i=i+2,res+=1
        i是'.'，i+1是'.'，i=i+3,res+=1
    :param road: 
    :return: 
    '''
    if road == None or len(road) == 0:
        return 0
    road = [i for i in road]
    ans = 0
    i = 0
    while i < len(road):
        if road[i] == 'X':
            i += 1
        else:
            ans += 1
            if i + 1 == len(road):
                break
            else:
                if road[i + 1] == 'X':
                    i += 2
                else:
                    i += 3
    return ans


# for test
import random


def randomString(length):
    res = []
    for i in range(int(random.random() * length) + 1):
        res.append('X' if random.random() < 0.5 else '.')
    return ''.join(res)


if __name__ == '__main__':
    length = 20
    testTime = 100000
    for i in range(testTime):
        test = randomString(length)
        ans1 = minLight1(test)
        ans2 = minLight2(test)
        if ans1 != ans2:
            print('Oops!')
    print('finish!')

# 0:59:55