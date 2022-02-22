# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi

# 0:10:10

'''
暴力递归（尝试）

打印一个字符串的全部子序列
打印一个字符串的全部子序列，要求不要出现重复字面值的子序列

'''


def subs(s):
    path = ''
    ans = []
    process1(s, 0, ans, path)
    return ans


def process1(s, index, ans, path):
    '''
    :param s: str固定不变
    :param index: index来到的位置，要 or 不要
    :param ans: 如果index来到可str终止的位置，把沿途路径所形成的答案，放入path中
    :param path: 之前作出的选择，就是path
    :return:
    '''
    if index == len(s):
        ans.append(path)
        return ans
    no = path
    process1(s, index + 1, ans, no)
    yes = path + s[index]
    process1(s, index + 1, ans, yes)


def subsNoRepeat(s):
    ans = set()  # set天然去重
    path = ''
    process2(s, 0, ans, path)
    return list(ans)


def process2(s, index, ans, path):
    if index == len(s):
        ans.add(path)
        return ans
    no = path
    process2(s, index + 1, ans, no)
    yes = path + s[index]
    process2(s, index + 1, ans, yes)


if __name__ == '__main__':
    print(subs('abc'))
    print(subsNoRepeat('aaa'))
