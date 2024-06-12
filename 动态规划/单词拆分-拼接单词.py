#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   单词拆分.py
@Time    :   2024/04/30 16:22:36
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''
# 首先，获取字符串 s 的长度 n，并初始化一个长度为 n+1 的动态规划数组 dp，用于表示字符串 s 从开始位置到当前位置是否可以被拆分。
# 将动态规划数组 dp 的第一个元素 dp[0] 初始化为 True，表示空字符串可以被拆分。
# 开始遍历字符串 s 中的每个字符，使用双重循环遍历区间 [i, j)，其中 i 表示起始位置，j 表示结束位置（不包含）。这样可以枚举所有可能的子串。
# 对于每个子串 s[i:j]，如果该子串在字典 wordDict 中，则更新动态规划数组 dp[j] = True，表示当前位置可以被拆分。
# 最终返回动态规划数组 dp 中的最后一个元素 dp[-1]，表示整个字符串 s 是否可以被拆分成字典中出现的单词。


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)  # 初始化dp数组，dp[i]表示s的前i个字符是否可以拆分为wordDict中的单词
        dp[0] = True  # 空字符串可以被拆分

        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True  # 更新dp数组，如果s[i:j]在wordDict中，并且dp[i]为True，则dp[j]也为True

        return dp[-1]  # 返回dp数组的最后一个元素，表示整个字符串s是否可以拆分成wordDict中的单词




