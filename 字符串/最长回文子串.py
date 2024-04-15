#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午10:05
# @Author  : yangguoli
# @File    : 最长回文子串.py 中心法，不采用动态规划
# @Software: PyCharm

# 给你一个字符串 s，找到 s 中最长的回文子串。

# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。




class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.res = ''
        n = len(s)
        self.max_len = 0
        # 采用双指针中心扩散法
        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            self.max_len = max(self.max_len, j - i - 1)
            if len(self.res) < j-i-1:
                self.res = s[i+1:j] #结束循环时l比回文串的内容多左移了一个 r多右移了一个

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.max_len, self.res


if __name__ == '__main__':
    str1 = 'assbssb'
    so = Solution()
    so.longestPalindrome(str1)
    





class Solution(object):
    def longestPalindrome(self, s):
        n = len(n)
        self.res = ''
        def helper(i, j):
            while i>=0 and j < n and s[i] == s[j]:
                i += 1
                j -= 1
            if len(self.res) < j-i-1:
                self.res = s[i+1: j]
        for i in range(n):
            helper(i, i)
            helper(i, i+1)
        return self.res