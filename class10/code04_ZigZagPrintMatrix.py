#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
矩阵的处理技巧

1）zigzag打印矩阵
2）转圈打印矩阵
3）原地圈旋转正方向矩阵

核心技巧：找到coding上的宏观调度
'''


def printMatrixZigZag(matrix):
    Ar = 0  # A点行坐标
    Ac = 0  # A点列坐标
    Br = 0  # B点行坐标
    Bc = 0  # B点列坐标
    endr = len(matrix) - 1  # 最后点行坐标
    endc = len(matrix[0]) - 1  # 最后点列坐标
    fromUp = False  # 是不是从右上往左下打印
    while Ar != endr + 1:
        printLevel(matrix, Ar, Ac, Br, Bc, fromUp)  # 告诉你，斜线的两端，A和B，方向也告诉你，去打印
        Ar = Ar + 1 if Ac == endc else Ar
        Ac = Ac if Ac == endc else Ac + 1
        Bc = Bc + 1 if Br == endr else Bc
        Br = Br if Br == endr else Br + 1
        fromUp = not fromUp
    print()


def printLevel(m, Ar, Ac, Br, Bc, f):
    if f:
        while Ar != Br + 1:
            print(m[Ar][Ac], ' ', end='')
            Ar += 1
            Ac -= 1

    else:
        while Br != Ar - 1:
            print(m[Br][Bc], ' ', end='')
            Br -= 1
            Bc += 1



if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    printMatrixZigZag(matrix)

    # 斜着蛇形打印矩阵，结果：1 2 5 9 6 3 4 7 10 11 8 12

# 1:39:39