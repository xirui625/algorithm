#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   分割回文串-最少分割次数.py
@Time    :   2024/05/21 11:58:14
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定一个字符串 s，请将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的 最少分割次数 。
'''

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # dp[i] 表示子串 s[:i+1] 的最小分割次数
        dp = [0] * n
        # is_palindrome[i][j] 表示子串 s[i:j+1] 是否为回文
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            min_cut = i  # 最多的分割次数是每个字符都分割一次
            for j in range(i + 1):
                if s[j] == s[i] and (i - j <= 1 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    # 如果 j 为 0，说明 s[:i+1] 本身是回文，不需要分割
                    min_cut = 0 if j == 0 else min(min_cut, dp[j - 1] + 1)
            dp[i] = min_cut

        return dp[-1]
    

# 测试用例
print(Solution().minCut("aab"))        # 输出: 1 ("aa", "b")
print(Solution().minCut("a"))          # 输出: 0
print(Solution().minCut("ab"))         # 输出: 1 ("a", "b")
print(Solution().minCut("racecar"))    # 输出: 0
print(Solution().minCut("noonabbad"))  # 输出: 2 ("noon", "abba", "d")

