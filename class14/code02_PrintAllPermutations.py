# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
暴力递归（尝试）

打印一个字符串的全部排列
打印一个字符串的全部排列，要求不要出现重复的排列
'''


def permutation(s):
    if s == None or len(s) == 0:
        return s
    res = []
    s = [i for i in s]
    process(s, 0, res)
    return res


def process(s, i, ans):
    '''
    s[0...i-1]已经做好决定
    s[i...]都有机会来到i位置
    i终止位置，str当前的样子，就是一种结果 -> ans
    '''
    if i == len(s):
        ans.append(''.join(s))
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]
        process(s, i + 1, ans)
        s[i], s[j] = s[j], s[i]  # 还原字符串顺序


def permutationNoRepeate(s):
    '''分支限界法'''
    if s == None or len(s) == 0:
        return s
    ans = []
    s = [i for i in s]
    process2(s, 0, ans)
    return ans


def process2(s, i, ans):
    if i == len(s):
        ans.append(''.join(s))
    visit = [False for i in range(26)]  # 26个字母，或者用哈希表
    for j in range(i, len(s)):
        if not visit[ord(s[j]) - ord('a')]:
            visit[ord(s[j]) - ord('a')] = True
            s[i], s[j] = s[j], s[i]
            process2(s, i + 1, ans)
            s[i], s[j] = s[j], s[i]


if __name__ == '__main__':
    print(permutation('abc'))
    print(permutationNoRepeate('abc'))
    print(permutationNoRepeate('acc'))

# 0:55:30