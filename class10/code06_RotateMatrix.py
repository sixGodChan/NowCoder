#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
矩阵的处理技巧

3）原地圈旋转正方向矩阵

核心技巧：找到coding上的宏观调度
'''

def rotate(matrix):
    a = 0
    b = 0
    c = len(matrix) - 1
    d = len(matrix[0]) - 1
    while a < c:
        rotateEdge(matrix, a, b, c, d)
        a += 1
        b += 1
        c -= 1
        d -= 1


def rotateEdge(m, a, b, c, d):
    for i in range(d-b):  # 正方形宽度-1=分几组
        tmp = m[a][b+i]
        m[a][b+i] = m[c-i][b]
        m[c-i][b] = m[c][d-i]
        m[c][d-i] = m[a + i][d]
        m[a + i][d] = tmp


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]] # 1 = (a,b) 13 = (c,b) 4 = (a,d) 16 = (c,d)
    rotate(matrix)
    for i in matrix:
        for j in i:
            print(j, ' ', end='')
        print()