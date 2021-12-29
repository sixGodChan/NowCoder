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
