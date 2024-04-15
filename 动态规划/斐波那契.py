#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午9:46
# @Author  : yangguoli
# @File    : 斐波那契.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

        # write code here