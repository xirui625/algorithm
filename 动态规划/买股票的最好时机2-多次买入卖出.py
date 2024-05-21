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

from typing import List  # 引入 List 类型用于函数类型注解

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)  # 获取价格数组的长度
        s = []  # 用于存储每天的利润
        for i in range(n - 1):  # 遍历数组中的每个元素（到倒数第二个元素）
            if prices[i + 1] > prices[i]:  # 如果第二天的价格高于当天的价格
                s.append(prices[i + 1] - prices[i])  # 计算利润并添加到利润列表中
        return sum(s)  # 返回所有利润的总和

# 测试用例
def test_maxProfit():
    solution = Solution()
    assert solution.maxProfit([7,1,5,3,6,4]) == 7, "测试用例1失败"  # 在第2天买入，第3天卖出，之后在第4天买入，第5天卖出，总利润是7
    assert solution.maxProfit([1,2,3,4,5]) == 4, "测试用例2失败"  # 每天都买卖，总利润是4
    assert solution.maxProfit([7,6,4,3,1]) == 0, "测试用例3失败"  # 没有利润，因为价格持续下降
    print("所有测试用例通过!")

# 执行测试用例
test_maxProfit()
