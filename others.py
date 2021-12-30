# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

# 1 带符号右移动, 除2
a = -33

print(a >> 1)  # a / 2
print('=====')

# 2 倒排序
for i in range(10, 0, -1):
    print('-', i, '-')
    for j in range(i):
        print(j)
print('=====')
for i in range(1, 10):  # 0 ~ i 做到有序
    print('-', i, '-')
    for j in range(i - 1, -1, -1):  # 或 range(i - 1, -1 , -1)
        print(j)
print('=====')

# 3 异或运算
'''
异或运算就记成无进位相加！
6 ^ 7 = 1
  110
+ 111
-----
  001

1)0 ^ N = N, N ^ N = 0
2)异或运算满足交换律和结合律(同样一批数，不用考虑异或顺序，异或起来结果是一样的)
'''
# a b交换，不使用额外变量(前提两个变量指向的内存不同)
a = 6
b = -1000
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
print('=====')
#