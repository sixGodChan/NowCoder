# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
不基于比较的排序
桶排序思想下的排序：计数排序 & 基数排序 & 桶排序
1）桶排序思想下的排序都是不基于比较的排序
2）时间复杂度是O(N),额外空间复杂度是O（M）
3）应用范围有限，需要样本的数据状况满足桶的划分
'''


# 基数排序 数组中值均为非负整数
def radixSort(lst):
    if lst == None or len(lst) < 2:
        return
    radixSort2(lst, 0, len(lst) - 1, maxbits(lst))


def maxbits(lst):
    maxValue = max(lst)
    res = 0
    while maxValue != 0:
        res += 1
        maxValue //= 10
    return res


# arr[L..R]排序  ,  最大值的十进制位数digit
def radixSort2(lst, l, r, digit):
    radix = 10
    # 有多少个数准备多少个辅助空间
    help = [0 for _ in range(r - l + 1)]
    for d in range(1, digit + 1):  # 有多少位就进出几次
        # 10个空间
        # count[0] 当前位(d位)是0的数字有多少个
        # count[1] 当前位(d位)是(0和1)的数字有多少个
        # count[2] 当前位(d位)是(0、1和2)的数字有多少个
        # count[i] 当前位(d位)是(0~i)的数字有多少个
        count = [0 for _ in range(radix)]  # count[0..9]
        for i in range(l, r + 1):
            j = getDigit(lst[i], d)
            count[j] += 1
        for k in range(1, radix):
            count[k] = count[k] + count[k - 1]
        for n in range(r, l - 1, -1):
            j = getDigit(lst[n], d)
            help[count[j] - 1] = lst[n]
            count[j] -= 1
        j = 0
        for m in range(l, r + 1):
            lst[m] = help[j]
            j += 1

# 2:14:36

def getDigit(x, d):  # 取x的d位（个位、十位、百位。。。）值
    return int((x / pow(10, d - 1)) % 10)

def comparator(lst):
    lst.sort()


import random


def generateRandomArray(maxSize, maxValue):
    lst = []
    for i in range(int(random.random() * (maxSize + 1))):
        lst.append(int(random.random() * (maxValue + 1)))
    return lst


if __name__ == '__main__':
    testTimes = 50000
    maxSize = 100
    maxValue = 200
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()
        radixSort(arr1)
        comparator(arr2)
        print(arr2, arr1)
        if arr1 != arr2:
            succeed = False
            break
    print('Nice!' if succeed else 'Fucking fucked!')

