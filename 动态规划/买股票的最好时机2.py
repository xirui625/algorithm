#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午11:06
# @Author  : yangguoli
# @File    : 买股票的最好时机2.py 可多次买入卖出
# @Software: PyCharm
# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

# 返回 你能获得的 最大 利润 。

#所有上涨交易日都买卖

class Solution:
    def maxProfit(self , prices ):
        n = len(prices)
        s = []
        for i in range(n - 1):
            if prices[i + 1] > prices[i]:
                s.append(prices[i + 1] - prices[i])
        return sum(s)