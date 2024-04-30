#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午3:12
# @Author  : yangguoli
# @File    : 最长上升子序列.py
# @Software: PyCharm

# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
# 子序列。

# 状态定义：dp[i]表示以下标i结尾的最长上升子序列的长度。
# 状态初始化：以任意下标结尾的上升子序列长度不小于1，故初始化为1。
# 状态转移：遍历数组中所有的数，再遍历当前数之前的所有数，
# 只要前面某个数小于当前数，则要么长度在之前基础上加1，
# 要么保持不变，取两者中的较大者。即dp[i]=Math.max(dp[i],dp[j]+1)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # dp[i]表示以下标i结尾的最长上升子序列的长度。
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)