#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   01背包.py
@Time    :   2024/04/03 19:10:42
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 给定N个物品，第i个物品的重量是wgt[i-1]，价格val[i-1]，和一个容量为cap的背包，每个物品只能选择一次，问在限定的背包容量下能放入物品的最大价值

from functools import cache


class Solution:
    def knapsackDp(self , wgt, val, cap):
        # 这里需要注意的是物品是按照1开始的，但是wgt和val从0开始
        m = len(wgt)
        @cache
        def dfs(i, c):
            if i< 0:
                return 0
            if wgt[i] > c:
                return dfs(i-1, c)
            return max(dfs(i-1, c), dfs(i-1, c-wgt[i]) + val[i])
        return dfs(m-1, cap)

# 完全背包

class Solution:
    def knapsackDp(self , wgt, val, cap):
    # 这里需要注意的是物品是按照1开始的，但是wgt和val从0开始
        m = len(wgt)
        @cache
        def dfs(i, c):
            if i< 0:
                return 0
            if wgt[i] > c:
                return dfs(i-1, c)
            return max(dfs(i-1, c), dfs(i, c-wgt[i]) + val[i])
        return dfs(m-1, cap)
          