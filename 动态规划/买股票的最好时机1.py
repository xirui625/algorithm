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
    # 假设你有一个数组prices，长度为n，其中prices[i]
    # 是股票在第i天的价格，请根据这个价格数组，返回买卖股票能获得的最大收益
    # 1.
    # 你可以买入一次股票和卖出一次股票，并非每天都可以买入或卖出一次，总共只能买入和卖出一次，且买入必须在卖出的前面的某一天
    # 2.
    # 如果不能获取到任何利润，请返回0
    # 3.
    # 假设买入卖出均无手续费
    def maxProfit(self , prices ):
        # db[i][j] 代表第i天的持股状态j：j 为0 不持股 为1 持股
        dp = [[0]*2] * (len(prices)+1)
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(len(prices)):
            # dp[i][0]：规定了今天不持股，有以下两种情况：
            # 昨天不持股，今天什么都不做；
            # 昨天持股，今天卖出股票（现金数增加）
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # dp[i][1]：规定了今天持股，有以下两种情况：
            # 昨天持股，今天什么都不做（现金数与昨天一样）；
            # 昨天不持股，今天买入股票（注意：只允许交易一次，因此手上的现金数就是当天的股价的相反数）
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[len(prices)-1][0]

    def maxProfit1(self, prices):
        # write code here
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])
        return res

    def maxProfit2(self, prices):
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