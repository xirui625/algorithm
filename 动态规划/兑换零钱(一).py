#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午2:30
# @Author  : yangguoli
# @File    : 兑换零钱(一).py
# @Software: PyCharm

# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

# 你可以认为每种硬币的数量是无限的。

# fx = f[x-arr_i] +1
import sys

class Solution:
    def coinChange(self, coins, amount) -> int:
        m = len(coins)
        dp = [[0] * (amount + 1)] * (m + 1) #前i个硬币能够凑出金额a的最少硬币数量
        for a in range(1, amount + 1):
            dp[0][a] = float('inf')
        for i in range(1, m+1):
            for a in range(1, amount+1):
                if coins[i-1] > a:
                    dp[i][a] = dp[i-1][a]
                else:
                    dp[i][a] = min(dp[i-1][a], dp[i][a - coins[i-1]] + 1)
        if dp[m][amount] == float('inf'):
            return -1
        return dp[m][amount]
        