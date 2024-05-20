#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午8:40
# @Author  : yangguoli
# @File    : 最长公共子串.py
# @Software: PyCharm

class Solution:
    def LCS(self , str1 , str2 ):
        # 获取两个字符串的长度
        m, n = len(str1), len(str2)
        # 初始化二维DP数组 dp，大小为 (m+1) x (n+1)，每个元素初始化为空字符串
        dp = [['' for _ in range(n + 1)] for _ in range(m + 1)]
        
        # 遍历字符串 str1 的每一个字符
        for i in range(1, m + 1):
            # 遍历字符串 str2 的每一个字符
            for j in range(1, n + 1):
                # 如果 str1 和 str2 当前字符匹配
                if str1[i - 1] == str2[j - 1]:
                    # 更新 dp[i][j] 为 dp[i-1][j-1] 加上当前字符
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    # 如果字符不匹配，取 dp[i-1][j] 和 dp[i][j-1] 中较长的那个
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
        
        # 返回 dp[m][n]，即为最长公共子串
        return dp[m][n]
        # if not str1 or not str2:
        #     return ''
        # #获取DP
        # dp = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)] # 代表str1在i位置，str2在j位置最长公共子串
        # maxLength = 0
        # end = 0
        # for i in range(len(str1)):
        #     for j in range(len(str2)):
        #         if str1[i] == str2[j]:
        #             if i == 0 or j == 0:
        #                 dp[i][j] = 1
        #             else:
        #                 dp[i][j] = dp[i - 1][j - 1] + 1
        #             if dp[i][j] > maxLength:
        #                 maxLength = dp[i][j]
        #                 end = i
        # return str1[end-maxLength+1:end+1]

    # def LCS2(self , str1 , str2 ):
    #     res = ''
    #     left = 0
    #     for i in range(len(str1) + 1):
    #         if str1[left:i+1] in str2:
    #             res = str1[left:i+1]
    #         else:
    #             left += 1
    #     return res
    def LCS2(self, str1, str2):
        # 初始化结果字符串 res 为空
        res = ''
        # 初始化左指针 left 为 0
        left = 0
        # 遍历 str1 的长度加 1 的范围
        for i in range(len(str1) + 1):
            # 如果 str1 从 left 到 i+1 的子串存在于 str2 中
            if str1[left:i+1] in str2:
                # 更新结果字符串 res 为当前子串
                res = str1[left:i+1]
            else:
                # 如果当前子串不在 str2 中，左指针 left 右移一位
                left += 1
        # 返回最终找到的最长公共子串
        return res




