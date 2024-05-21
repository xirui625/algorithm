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
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        m = len(coins)
        # 创建一个二维数组 dp，dp[i][a] 表示前 i 个硬币凑出金额 a 的最少硬币数量
        dp = [[0] * (amount + 1) for _ in range(m + 1)]

        # 初始化第一行，当没有硬币可用时，凑出金额 a 需要无穷大个硬币
        for a in range(1, amount + 1):
            dp[0][a] = float('inf')

        # 遍历每个硬币和每个金额，计算最少硬币数量
        for i in range(1, m + 1):
            for a in range(1, amount + 1):
                if coins[i - 1] > a:
                    dp[i][a] = dp[i - 1][a]  # 当前硬币大于目标金额，无法使用当前硬币
                else:
                    dp[i][a] = min(dp[i - 1][a], dp[i][a - coins[i - 1]] + 1)
                    # 使用当前硬币和不使用当前硬币的最小值

        # 如果无法凑出金额 amount，则返回 -1
        if dp[m][amount] == float('inf'):
            return -1
        return dp[m][amount]

# 测试用例
def test_coinChange():
    solution = Solution()
    assert solution.coinChange([1, 2, 5], 11) == 3, "测试用例1失败"
    assert solution.coinChange([2], 3) == -1, "测试用例2失败"
    assert solution.coinChange([1], 0) == 0, "测试用例3失败"
    assert solution.coinChange([1], 1) == 1, "测试用例4失败"
    assert solution.coinChange([1], 2) == 2, "测试用例5失败"
    print("所有测试用例通过!")

# 执行测试用例
test_coinChange()

        