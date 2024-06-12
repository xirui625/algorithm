#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午10:22
# @Author  : yangguoli
# @File    : 最长公共子序列.py
# @Software: PyCharm

# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

from functools import cache


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        dp[i][j] 表示text1[0:i] 和 text2[0:j] 的最长公共子序列
        """
        if not text1 or not text2:
            return 0  # 如果有一个字符串为空，则直接返回0，因为没有公共子序列

        m, n = len(text1), len(text2)
        # 初始化DP方程
        dp = [['' for i in range(n+1)] for j in range(m+1)]

        # 动态规划填表
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    # 如果text1的第i个字符和text2的第j个字符相等
                    dp[i][j] = dp[i-1][j-1] + text1[i-1]
                else:
                    # 如果text1的第i个字符和text2的第j个字符不相等，选择dp[i-1][j]或dp[i][j-1]中的较长子序列
                    tmp1 = dp[i-1][j]
                    tmp2 = dp[i][j-1]
                    dp[i][j] = tmp1 if len(tmp1) > len(tmp2) else tmp2

        # 结果处理
        if dp[m][n] == '':
            return 0, -1  # 如果最长公共子序列为空字符串，返回0和-1
        else:
            return len(dp[m][n]), dp[m][n]  # 返回最长公共子序列的长度和该子序列本身



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(n - 1, m - 1)

