#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   编辑距离.py
@Time    :   2024/04/03 20:08:23
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''


# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符

class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:：定义了一个名为minDistance的方法，该方法接受两个字符串word1和word2作为参数，并返回一个整数。
    # m = len(word1) 和 n = len(word2)：分别获取两个输入字符串的长度。
    # dp = [[0] * (n + 1) for _ in range(m + 1)]：创建一个二维数组dp，
    # 用于存储状态转移方程中的中间结果。dp[i][j]表示将word1的前i个字符变更为word2的前j个字符所需的最少编辑步数。
    # for i in range(1, m+1): 
    # dp[i][0] = i 和 for j in range(1, n+1): dp[0][j] = j：初始化边界情况，即当一个字符串为空时，
    # 需要的编辑步数就是另一个字符串的长度。
    # 接下来是核心部分，双重循环遍历word1和word2的每个字符：
    # a. if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]：如果当前字符相同，
    # 那么当前状态的编辑距离与之前一个状态的编辑距离相同，
    # 因此直接将其赋值为dp[i-1][j-1]。
    # b. else: dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1：如果当前字符不同，
    # 那么需要考虑三种情况，分别是在word1的前i个字符中插入一个字符、删除一个字符或者替换一个字符，
    # 取最小值并加上1，即可得到当前状态的最小编辑步数。
    # return dp[m][n]：返回将word1变更为word2所需的最小编辑步数，即dp数组右下角的值。
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j]表示将word1的前i个字符变更为word2的前j个字符所需的最少编辑步数。
        dp = [[0] * (n + 1) for _ in range(m + 1)] 
        #初始化边界情况，即当一个字符串为空时，需要的编辑步数就是另一个字符串的长度。
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        # 双重循环遍历word1和word2的每个字符：
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 如果当前字符相同,那么当前状态的编辑距离与之前一个状态的编辑距离相同，
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 如果不同，考虑三种情况，分别是在word1的前i个字符中插入一个字符、删除一个字符或者替换一个字符
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[m][n]