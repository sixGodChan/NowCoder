#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
打表法

1）问题如果返回值不太多，可以用hardcode的方式列出，作为程序的一部分（查表法，提前维护一个表）

2）一个大问题解决时底层频繁使用规模不大的小问题的解，如果小问题的返
回值满足条件1），可以把小问题的解列成一张表，作为程序的一部分

3）打表找规律（本节课重点），有关1）和2）内容欢迎关注后续课程
'''

'''
打表找规律（的特征）

1）某个面试题，输入参数类型简单，并且只有一个实际参数

2）要求的返回值类型也简单，并且只有一个

3）用暴力方法，把输入参数对应的返回值，打印出来看看，进而优化code
'''

'''
题目一

小虎去买苹果，商店只提供两种类型的塑料袋，每种类型都有人数数量。
1）能装下6哥苹果的袋子
2）能装下8哥苹果的袋子
小虎可以自由使用两种袋子来装苹果，但是小虎有强迫症，他要求自己使用
的袋子数量必须最少，且使用的每个袋子必须装满。
给定一个真正数N，返回至少使用多少个袋子。如果N无法让使用的每个袋子必
须装满，返回-1。
'''


def minBags(apple):
    '''暴力法'''
    if apple < 0:
        return -1
    bag8 = apple >> 3  # apple // 8
    rest = apple - (bag8 << 3)
    while bag8 >= 0:
        if rest % 6 == 0:
            return bag8 + (rest // 6)
        else:
            bag8 -= 1
            rest += 8
    return -1


def minBagsAwesome(apple):
    '''根据暴力法优化'''
    if apple & 1 != 0:  # apple奇数
        return -1
    if apple < 18:
        return 0 if apple == 0 else 1 if apple == 6 or apple == 8 else 2 if apple == 12 or apple == 14 or apple == 16 else -1
    return (apple - 18) // 8 + 3


if __name__ == '__main__':
    for apple in range(1, 200):
        print(apple, ':', minBags(apple))

    for apple in range(0, 200):
        print(apple, ':', minBags(apple) == minBagsAwesome(apple))

# 0:41:33