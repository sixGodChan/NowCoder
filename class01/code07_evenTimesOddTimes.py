# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
异或 应用
'''


def oddTimesNum1(lst):
    '''
    一个数组，其中有一类数数量为奇数，其余数数量为偶数，求数量为奇数的数是多少？
    时间复杂度：O(n)
    空间复杂度：O(1)
    '''
    eor = 0
    for i in lst:
        eor ^= i
    return eor


def findRightOne(n):
    '''
    如何把一个int类型的数，提取出最右侧的1来
    N & (N取反加1)
    00111010 N
    11000101 取反
    11000110 +1
    00000010 &
    '''
    return n & (~n + 1)


def oddTimesNum2(lst):
    '''
    一个数组，其中有两种数出现了奇数次，其它数都出现了偶数次，怎么找到并打印这两种数
    时间复杂度：O(n)
    空间复杂度：O(1)
    '''
    eor = 0
    for i in lst:
        eor ^= i

    # eor = a ^ b
    # eor 一定不等于 0
    # eor 必然有一个位置是1
    rightOne = eor & (~eor + 1)  # 提取最右的1(位置x)
    # 整个数组就可分为两类位置x为1和位置x为0

    delta_eor = 0  # eor'
    for i in lst:
        if (i & rightOne) != 0:  # 或 (i & rightOne) == rightOne
            delta_eor ^= i

    return delta_eor, eor ^ delta_eor


def bit1counts(n):
    '''
    数出二进制1的个数
    '''
    count = 0
    while n != 0:
        rightOne = n & ((~n) + 1)
        count += 1
        n ^= rightOne

    return count


if __name__ == '__main__':
    a = [2, 1, 3, 1, 3, 1, 3, 2, 1]
    print(oddTimesNum1(a))

    print(findRightOne(6))

    b = [2, 4, 6, 8, 4, 6, 8, 4, 6, 8, 2, 6]
    print(oddTimesNum2(b))

    print(bit1counts(6))
