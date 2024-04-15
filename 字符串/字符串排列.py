#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:54
# @Author  : yangguoli
# @File    : 字符串排列.py
# @Software: PyCharm
from itertools import combinations, permutations

class Solution:
    def Permutation1(self, ss):
        if not ss:
            return
        ret = set()
        for item in permutations(ss, len(ss)):
            ret.add("".join(item))
        return list(ret)


    def permutation2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        if length == 1:
            return [s]  # 边界
        else:
            res = []
            for i in range(length):
                ch = s[i]  # 取出s中每一个字符
                rest = s[:i] + s[i + 1:]
                for x in self.permutation2(rest):  # 递归
                    res.append(ch + x)  # 将ch 和子问题的解依次组合
        return list(set(res))