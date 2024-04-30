#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   交错字符串.py
@Time    :   2024/04/30 16:41:03
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 
子字符串
：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。


'''
# def isInterleave(self, s1: str, s2: str, s3: str) -> bool:: 这是一个方法的定义，它接受三个参数s1、s2和s3，它们都是字符串类型，并返回一个布尔值表示s3是否由s1和s2交错组成。
# if len(s1) + len(s2) != len(s3): return False: 这行代码首先检查s1和s2的长度之和是否等于s3的长度，如果不等，则返回False，因为无法通过交错s1和s2的字符得到s3。
# length2 = len(s2): 这一行计算s2的长度，以后会频繁用到。
# dps = [True] + [s2[:i] == s3[:i] for i in range(1, length2 + 1)]: 这一行初始化了一个动态规划数组dps，
# 用于存储当前交错位置是否满足条件。它的长度为s2的长度加1，初始值为True，
# 表示空字符串与s3的前缀是否相同。接着通过列表解析式判断s2的前缀是否与s3的对应前缀相同。
# for index1, char1 in enumerate(s1):: 这是一个循环，遍历s1中的每个字符及其索引。
# dps[0] = dps[0] and s3[index1] == char1: 这行代码更新了dps[0]，判断当前位置s1的字符是否与s3的对应位置字符相同。
# for index2, char2 in enumerate(s2):: 这是一个嵌套的循环，遍历s2中的每个字符及其索引。
# index3 = index1 + index2 + 1: 这行代码计算了s3中当前交错位置的索引。
# dps[index2 + 1] = (char1 == s3[index3] and dps[index2 + 1]) or (char2 == s3[index3] and dps[index2]): 这行代码更新了dps[index2 + 1]，判断当前位置s1和s2的字符是否与s3的对应位置字符相同，以及前一个位置的结果是否满足条件。
# return dps[-1]: 最后，返回dps数组的最后一个元素，表示整个字符串s3是否由s1和s2交错组成。
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        length2 = len(s2)
        dps = [True] + [s2[:i] == s3[:i] for i in range(1, length2 + 1)]
        for index1, char1 in enumerate(s1):
            dps[0] = dps[0] and s3[index1] == char1
            for index2, char2 in enumerate(s2):
                index3 = index1 + index2 + 1
                dps[index2 + 1] = (char1 == s3[index3] and dps[index2 + 1]) or (char2 == s3[index3] and dps[index2])
        return dps[-1]


