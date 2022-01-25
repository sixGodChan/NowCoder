# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

'''
二叉树

题目
请把一段纸条竖着放在桌子上，然后从纸条的下方向上方对折1次，压出折痕
后展开。此时折痕是凹下去的，即折痕突起的方向指向纸条的背面。如果从
纸条的下边向上对折2次，压出折痕后展开，此时有三条折痕，从上到下依次
是下折痕、下折痕和上折痕。
给定一个输入参数N，代表纸条都从下边向上方连续对折N次。请从上到下打印
所有折痕的方向。
例如：N=1时，打印：down；N=2时，打印down down up
N=3，down down up down down up up

规律：每次折叠会在上次折叠上面出现下折痕，下面出现上折痕
             1凹
       2凹         2凸
    3凹   3凸   3凹   3凸
所以最后打印这个二叉树的中序遍历

'''


def printAllFolds(n):
    process(1, n, True)


def process(i, n, down):
    '''
    当前你来了一个节点，脑海中想象的！
    这个节点在第i层，一共有N层，N固定不变的
    这个节点如果是凹的话，down = T
    这个节点如果是凸的话，down = F
    函数的功能：中序打印以你想象的节点为头的整棵树！
    '''
    if i > n:
        return
    process(i + 1, n, True)
    print('down' if down else 'up', ' ', end='')
    process(i + 1, n, False)


if __name__ == '__main__':
    printAllFolds(3)

# 0:57:20