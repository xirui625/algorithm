#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午11:10
# @Author  : yangguoli
# @File    : 买卖股票的最好时机(三).py 每天最最多两笔交易 买入或者卖出
# @Software: PyCharm

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        #buy1、sell1、buy2、sell2 分别表示第一次买入股票、第一次卖出股票、第二次买入股票、第二次卖出股票的状态。
        # 将 buy1 和 buy2 初始化为第一天的价格的负值，表示第一天买入股票所需花费的金额。

        # 初始化四种状态的初始值
        buy1 = -prices[0]  # 第一次买入股票
        sell1 = 0           # 第一次卖出股票
        buy2 = -prices[0]  # 第二次买入股票
        sell2 = 0           # 第二次卖出股票
        
        for price in prices[1:]:
            # 更新第一次买入股票的状态（注意此时是负值，表示花了多少钱买入）选择保持之前买入的价格或者在这一天买入股票
            buy1 = max(buy1, -price)
            # 更新第一次卖出股票的状态 选择保持之前卖出的价格或者在这一天卖出股票
            sell1 = max(sell1, buy1 + price)
            # 更新第二次买入股票的状态（注意这里用到了第一次卖出股票的状态）选择保持之前买入的价格或者在这一天买入股票
            buy2 = max(buy2, sell1 - price)
            # 更新第二次卖出股票的状态 选择保持之前卖出的价格或者在这一天卖出股票
            sell2 = max(sell2, buy2 + price)
        
        # 最后返回第二次卖出股票的状态，因为最后一定要是手中没有股票
        return sell2
