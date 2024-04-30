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
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        else:
            return max(self.longestSubstring(t, k) for t in s.split(c))