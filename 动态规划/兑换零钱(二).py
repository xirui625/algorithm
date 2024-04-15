#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午3:03
# @Author  : yangguoli
# @File    : 兑换零钱(二).py
# @Software: PyCharm

# 给定一个整数数组 nums 表示不同数额的硬币和一个正整数 target 表示总金额，请你计算并返回可以凑出总金额的的组合数。如果凑不出 target 则返回 0。
# dp[i][j]=dp[i−1][j]+dp[i][j−v]if:j>=v
# dp[i][j]表示在前i种硬币中挑选，凑出j的方案数
class Solution:
    def change(self , target , nums ):
        dp = [[0] * (target + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1  # 用前0个元素凑0元有且只有一种方法
        for i in range(1, len(nums) + 1):
            value = nums[i - 1]
            for j in range(target + 1):
                k = 0  # 挑选value的硬币数量
                while k * value <= j:
                    dp[i][j] += dp[i - 1][j - k * value]  # 迭代将挑新的硬币数量为0，1，2...都统计起来
                    k += 1
        return dp[len(nums)][target]