# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: sunqi
'''
前缀树

1）单个字符串中，字符从前到后的加到一颗多叉树上
2）字符放在路上，节点上有专属的数据项（常见的是pass和end值)（pass通过值，end收尾值）
3)所有样本都这样添加，如果没有路就新建，如有路就重复
4）沿途节点的pass值加1，每个字符串结束时来到的节点end值增加1

可以完成前缀树相关查询
'''


# 字符串仅限a~z
class Node1():
    def __init__(self):
        self.passValue = 0
        self.end = 0
        self.nexts = [None for _ in range(26)]  # a ~ z


class Trie1():
    def __init__(self):
        self.root = Node1()

    #  插入word
    def insert(self, word):
        if word == None:
            return
        node = self.root
        node.passValue += 1
        for i in word:
            path = ord(i) - ord('a')
            if node.nexts[path] == None:
                node.nexts[path] = Node1()
            node = node.nexts[path]
            node.passValue += 1
        node.end += 1

    # word 插入过几次
    def search(self, word):
        if word == None:
            return 0
        node = self.root
        for i in word:
            path = ord(i) - ord('a')
            if node.nexts[path] == None:
                return 0
            node = node.nexts[path]
        return node.end

    # 删除word
    def delete(self, word):
        if self.search(word) != 0:
            node = self.root
            node.passValue -= 1
            for i in word:
                path = ord(i) - ord('a')
                if node.nexts[path].passValue - 1 == 0:  # pass为零，其下节点均可放弃
                    node.nexts[path] = None
                    return
                node = node.nexts[path]
                node.passValue -= 1
            node.end -= 1

    # 所有加入的字符串中，有几个是以pre这个字符串为前缀的
    def prefixNumber(self, pre):
        if pre == None:
            return 0
        node = self.root
        for i in pre:
            path = ord(i) - ord('a')
            if node.nexts[path] == None:
                return 0
            node = node.nexts[path]
        return node.passValue


# 字符串不限
class Node2():
    def __init__(self):
        self.passValue = 0
        self.end = 0
        self.hashMap = {}


class Trie2():
    def __init__(self):
        self.root = Node2()

    def insert(self, word):
        if word == None:
            return
        node = self.root
        node.passValue += 1
        for i in word:
            path = ord(i)
            if not node.hashMap.get(path):
                node.hashMap[path] = Node2()
            node = node.hashMap[path]
            node.passValue += 1
        node.end += 1

    def search(self, word):
        if word == None:
            return 0
        node = self.root
        for i in word:
            path = ord(i)
            if not node.hashMap.get(path):
                return 0
            node = node.hashMap[path]
        return node.end

    def delete(self, word):
        if self.search(word) != 0:
            node = self.root
            node.passValue -= 1
            for i in word:
                path = ord(i)
                if node.hashMap[path].passValue - 1 == 0:
                    node.hashMap.pop(path)
                    return
                node = node.hashMap[path]
                node.passValue -= 1
            node.end -= 1

    # 所有加入的字符串中，有几个是以pre这个字符串为前缀的
    def prefixNumber(self, pre):
        if pre == None:
            return 0
        node = self.root
        for i in pre:
            path = ord(i)
            if not node.hashMap.get(path):
                return 0
            node = node.hashMap[path]
        return node.passValue


class Right():
    def __init__(self):
        self.box = {}

    def insert(self, word):
        if word == None:
            return
        if self.box.get(word):
            self.box[word] += 1
        else:
            self.box[word] = 1

    def search(self, word):
        if word == None:
            return 0
        if self.box.get(word):
            return self.box[word]
        else:
            return 0

    def delete(self, word):
        if word in self.box:
            if self.box[word] - 1 == 0:
                self.box.pop(word)
            else:
                self.box[word] -= 1

    # 所有加入的字符串中，有几个是以pre这个字符串为前缀的
    def prefixNumber(self, pre):
        if pre == None:
            return 0
        count = 0
        for i in self.box.keys():
            if i.startswith(pre):
                count += self.box[i]
        return count


import random


def generateRandomString(strLen):
    l = int((random.random() * strLen) + 1)
    ans = []
    for i in range(l):
        value = int(random.random() * 6)
        ans.append(chr(97 + value))
    return ''.join(ans)

def generateRandomStringArray(arrlen, strlen):
    lstLen = int((random.random() * arrlen) + 1)
    ans = []
    for i in range(lstLen):
        ans.append(generateRandomString(strlen))
    return ans


if __name__ == '__main__':
    arrlen = 100
    strlen = 20
    testTimes = 100000
    for i in range(testTimes):
        arr = generateRandomStringArray(arrlen, strlen)
        trie1 = Trie1()
        trie2 = Trie2()
        right = Right()
        for j in range(len(arr)):
            decide = random.random()
            if decide < 0.25:
                trie1.insert(arr[j])
                trie2.insert(arr[j])
                right.insert(arr[j])
            elif decide < 0.5:
                trie1.delete(arr[j])
                trie2.delete(arr[j])
                right.delete(arr[j])
            elif decide < 0.75:
                ans1 = trie1.search(arr[j])
                ans2 = trie2.search(arr[j])
                ans3 = right.search(arr[j])
                if (ans1 != ans2) or (ans2 != ans3):
                    print('Oops!1')
            else:
                ans1 = trie1.prefixNumber(arr[j])
                ans2 = trie2.prefixNumber(arr[j])
                ans3 = right.prefixNumber(arr[j])
                if (ans1 != ans2) or (ans2 != ans3):
                    print('Oops!2')