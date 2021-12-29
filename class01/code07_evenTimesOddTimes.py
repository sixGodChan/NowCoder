# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

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


def oddTimesNum2(lst):
    '''
    一个数组，其中有2类数数量为奇数，其余数数量为偶数，求数量为奇数的2个数分别是多少？
    时间复杂度：O(n)
    空间复杂度：O(1)
    '''
    eor = 0
    for i in lst:
        eor ^= i

    # eor = a ^ b
    # eor != 0
    # eor 必然有一个位置是1
    rightOne = eor & (~eor + 1)  # 提取最右的1

    delta_eor = 0  # eor'
    for i in lst:
        if i & rightOne == 0:  # != 0 或 == rightOne 都行
            delta_eor ^= i
    return delta_eor, eor ^ delta_eor


if __name__ == '__main__':
    a = [2, 1, 3, 1, 3, 1, 3, 2, 1]
    print(oddTimesNum1(a))
    b = [2, 4, 6, 8, 4, 6, 8, 4, 6, 8, 2, 6]
    print(oddTimesNum2(b))
