#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午8:10
# @Author  : yangguoli
# @File    : 连续子数组的最大和.py
# @Software: PyCharm

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        dp = [0] * (len(array) + 1)
        dp[0] = array[0]
        maxTotal = array[0]
        for i in range(1, len(array)):
            dp[i] = max(dp[i-1]+array[i], array[i])
            maxTotal = max(maxTotal, dp[i])
        return maxTotal