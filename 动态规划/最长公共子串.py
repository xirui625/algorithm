#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午8:40
# @Author  : yangguoli
# @File    : 最长公共子串.py
# @Software: PyCharm

class Solution:
    def LCS(self , str1 , str2 ):
        if not str1 or not str2:
            return ''
        #获取DP
        dp = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)] # 代表str1在i位置，str2在j位置最长公共子串
        maxLength = 0
        end = 0
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > maxLength:
                        maxLength = dp[i][j]
                        end = i
        return str1[end-maxLength+1:end+1]

    def LCS2(self , str1 , str2 ):
        res = ''
        left = 0
        for i in range(len(str1) + 1):
            if str1[left:i+1] in str2:
                res = str1[left:i+1]
            else:
                left += 1
        return res
        # res = ""
        # left = 0
        # for i in range(len(str1) + 1):
        #     if str1[left:i + 1] in str2:
        #         res = str1[left:i + 1]
        #     else:
        #         left = left + 1
        # return res




