#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:54
# @Author  : yangguoli
# @File    : 字符串排列.py
# @Software: PyCharm
class Solution:
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        if length == 1:
            return [s]  # 如果字符串长度为1，直接返回该字符串作为唯一排列

        res = []  # 用于存储所有排列结果的列表

        # 遍历字符串s中的每个字符
        for i in range(length):
            ch = s[i]  # 取出第i个字符作为当前字符
            rest = s[:i] + s[i + 1:]  # 取出除去第i个字符之外的剩余字符串

            # 递归获取剩余字符串的全排列
            for x in self.permutation(rest):
                res.append(ch + x)  # 将当前字符与剩余字符串的每个排列组合起来

        return list(set(res))  # 使用set去重，并将结果转换为列表返回
