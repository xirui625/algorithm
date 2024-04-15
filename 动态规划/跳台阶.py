#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午7:59
# @Author  : yangguoli
# @File    : 跳台阶.py
# @Software: PyCharm


# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 达到i阶总共与dp[i]中方法
        dp = [0] * 50
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 达到i阶总共与dp[i]中方法
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b


# 使用最小花费爬楼梯

# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

# 请你计算并返回达到楼梯顶部的最低花费。

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
