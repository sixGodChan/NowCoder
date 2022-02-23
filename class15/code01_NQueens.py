# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
课外：鳄鱼问题、海盗分硬币问题、欧拉信封问题，都是从小样本往大样本推

暴力递归（尝试）

N皇后

N皇后问题是指在N*N的棋盘上要摆N个皇后，
要求任何两个皇后不同行、不同列、也不在同一斜线上

给定一个正数n，返回n皇后的摆法有多少种。
n=1，返回1
n=2或3,2皇后和3皇后问题无论怎么摆都不行，返回0
n=8，返回92

复杂度O(n^2)
'''


def num1(n):
    if n < 1:
        return 0
    record = [None for _ in range(n)]
    return process1(0, record, n)


def process1(i, record, n):
    '''
    当前来到i行，一共是0~N-1行
	在i行上放皇后，所有列都尝试
	必须要保证跟之前所有的皇后不打架
	int[] record record[x] = y 之前的第x行的皇后，放在了y列上
	返回：不关心i以上发生了什么，i.... 后续有多少合法的方法数
    '''
    if i == n:
        return 1
    res = 0
    for j in range(n):  # j是第j列
        if isValid(record, i, j):  # 在record中（i,j）是否验证通过
            record[i] = j
            res += process1(i + 1, record, n)
    return res


def isValid(record, i, j):
    for k in range(i):
        if record[k] == j or abs(k - i) == abs(record[k] - j):
            return False
    return True


# 常数项加速（使用位运算） 不能超过32皇后(java到32就是-1)
def num2(n):
    if n < 1:
        return 0
    # 如果你是13皇后问题，limit 最右13个1，其他都是0
    limit = -1 if n == 32 else (1 << n) - 1
    return process2(limit, 0, 0, 0)


def process2(limit, colLim, leftDiaLim, rightDiaLim):
    '''
    7皇后问题
	limit : 0....0 1 1 1 1 1 1 1
	之前皇后的列影响：colLim
	之前皇后的左下对角线影响：leftDiaLim
	之前皇后的右下对角线影响：rightDiaLim

    colLimt列上不可放皇后的限制
    leftDiaLim左斜线不可放
    rightDiaLim右斜线不可放
    '''
    if limit == colLim:  # 每列都放满
        return 1
    # pos中所有是1的位置，是你可以去尝试皇后的位置
    pos = limit & (~(colLim | leftDiaLim | rightDiaLim))  # 可以的位置
    res = 0
    while pos != 0:
        mostRightOne = pos & (~pos + 1)  # 最右的1
        pos = pos - mostRightOne
        res += process2(limit, colLim | mostRightOne, (mostRightOne | leftDiaLim) << 1,
                        (mostRightOne | rightDiaLim) >> 1)
    return res


if __name__ == '__main__':
    n = 13

    import time

    start = time.time()
    print(num2(n))
    end = time.time()
    print('cost time', end - start, 's')

    start = time.time()
    print(num1(n))
    end = time.time()
    print('cost time', end - start, 's')

# 1:40:00
