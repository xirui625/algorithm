#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   至少有 K 个重复字符的最长子串.py
@Time    :   2024/04/29 17:51:29
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

# 如果不存在这样的子字符串，则返回 0。
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        # 找到字符串 s 中出现次数最少的字符 c
        c = min(set(s), key=s.count)
        # 如果最少出现次数的字符 c 在字符串 s 中出现的次数大于等于 k 次，
        # 则说明整个字符串 s 就是满足条件的最长子串，直接返回字符串 s 的长度 len(s)
        if s.count(c) >= k:
            return len(s)
        else:
            # 递归地处理字符串 s 中去除掉字符 c 的每个子串，并找到这些子串中满足条件的最长子串的长度。
            # 具体做法是通过 s.split(c) 来将字符串 s 按照字符 c 进行拆分，得到多个子串，然后对每个子串递归调用 self.longestSubstring(t, k) 来找到满足条件的最长子串的长度。
            return max(self.longestSubstring(t, k) for t in s.split(c))