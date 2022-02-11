#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
矩阵的处理技巧

2）转圈打印矩阵

核心技巧：找到coding上的宏观调度
'''

def spiralOrderPrint(matrix):
    Ar = 0
    Ac = 0
    endr = len(matrix) - 1
    endc = len(matrix[0]) - 1
    while Ar <= endr and Ac <= endc:
        printEdge(matrix, Ar, Ac, endr, endc)
        Ar += 1
        Ac += 1
        endr -= 1
        endc -= 1

def printEdge(m, Ar, Ac, endr, endc):
    if Ar == endr:  # 只剩一条横线
        for i in range(Ac, endc + 1):
            print(m[Ar][i], ' ', end='')
    elif Ac == endc:  # 只剩一条竖线
        for i in range(Ar, endr + 1):
            print(m[i][Ac], ' ', end='')
    else:  # 围绕边缘打印
        curC = Ac
        curR = Ar
        while curC != endc:
            print(m[Ar][curC], ' ', end='')
            curC += 1
        while curR != endr:
            print(m[curR][endc], ' ', end='')
            curR += 1
        while curC != Ac:
            print(m[endr][curC], ' ', end='')
            curC -= 1
        while curR != Ar:
            print(m[curR][Ac], ' ', end='')
            curR -= 1

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    spiralOrderPrint(matrix)

    # 转圈打印矩阵，结果：1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

# 1:50:55