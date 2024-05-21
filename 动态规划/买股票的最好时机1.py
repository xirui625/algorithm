#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午10:44
# @Author  : yangguoli
# @File    : 买股票的最好时机.py
# @Software: PyCharm

# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

class Solution:
    def maxProfit(self, prices):
        # 1、使用变量记录历史最低价格
        # minprice
        # 2、则在第
        # i
        # 天卖出股票能得到的利润就是
        # prices[i] - minprice
        # 3、因此，我们只需要遍历价格数组一遍，记录历史最低点
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            # 找到最低股票价格
            minprice = min(price, minprice)
        return maxprofit