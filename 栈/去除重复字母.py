#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 下午1:20
# @Author  : yangguoli
# @File    : 去除重复字母.py
# @Software: PyCharm
import collections

'''
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"
'''

'''
不同字符的最小子序列

返回 s 字典序最小的
子序列
，该子序列包含 s 的所有不同字符，且只包含一次。

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 1000
s 由小写英文字母组成
'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)