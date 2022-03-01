# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''

# 视频2 class16 0:29:20
三维的动态规划

请同学们自行搜索或者想象一个象棋的棋盘，
然后把整个棋盘放入第一象限，棋盘的最左下角是(0,0)位置
那么整个棋盘就是横坐标上9条线、纵坐标上10条线的区域
给你三个 参数 x，y，k
返回“马”从(0,0)位置出发，必须走k步
最后落在(x,y)上的方法数有多少种?
'''


def jump1(x, y, k):
    '''暴力递归'''
    return process1(x, y, k)


def process1(x, y, step):
    '''
    从（a,b）位置出发
    要去（x,y）位置，必须跳step步
	返回方法数
	'''
    # 超出棋盘范围
    if x < 0 or x > 9 or y < 0 or y > 8:
        return 0
    # 剩余0步，在(0,0)位置要去(x=0,y=0)位置,只有1种方法
    if step == 0:
        return 1 if x == 0 and y == 0 else 0

    return process1(x - 1, y + 2, step - 1) \
           + process1(x - 2, y + 1, step - 1) \
           + process1(x - 2, y - 1, step - 1) \
           + process1(x - 1, y - 2, step - 1) \
           + process1(x + 1, y - 2, step - 1) \
           + process1(x + 2, y - 1, step - 1) \
           + process1(x + 2, y + 1, step - 1) \
           + process1(x + 1, y + 2, step - 1)


def jump2(x, y, k):
    '''动态规划'''
    dp = [[[0 for _ in range(k + 1)] for _ in range(9)] for _ in range(10)]
    dp[0][0][0] = 1  # (0,0)到(0,0)0步，1种方法
    for step in range(1, k + 1):  # 上层受限于下一层，按层来
        for i in range(10):
            for j in range(9):
                if i - 1 >= 0 and j + 2 < 9:
                    dp[i][j][step] += dp[i - 1][j + 2][step - 1]
                if i - 2 >= 0 and j + 1 < 9:
                    dp[i][j][step] += dp[i - 2][j + 1][step - 1]
                if i - 2 >= 0 and j - 1 >= 0:
                    dp[i][j][step] += dp[i - 2][j - 1][step - 1]
                if i - 1 >= 0 and j - 2 >= 0:
                    dp[i][j][step] += dp[i - 1][j - 2][step - 1]
                if i + 1 < 10 and j - 2 >= 0:
                    dp[i][j][step] += dp[i + 1][j - 2][step - 1]
                if i + 2 < 10 and j - 1 >= 0:
                    dp[i][j][step] += dp[i + 2][j - 1][step - 1]
                if i + 2 < 10 and j + 1 < 9:
                    dp[i][j][step] += dp[i + 2][j + 1][step - 1]
                if i + 1 < 10 and j + 2 < 9:
                    dp[i][j][step] += dp[i + 1][j + 2][step - 1]
    return dp[x][y][k]  # (0,0)到(x,y)k步，几种方法


if __name__ == '__main__':
    x = 7
    y = 7
    step = 10
    print(jump1(x, y, step))  # 515813
    print(jump2(x, y, step))
