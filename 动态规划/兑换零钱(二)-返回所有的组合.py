#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午3:03
# @Author  : yangguoli
# @File    : 兑换零钱(二).py
# @Software: PyCharm

# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

# 假设每一种面额的硬币有无限个。 

# 题目数据保证结果符合 32 位带符号整数。
# dp[i][j]=dp[i−1][j]+dp[i][j−v]if:j>=v
# dp[i][j]表示在前i种硬币中挑选，凑出j的方案数
class Solution:
    def change(self, target: int, nums: List[int]) -> int:
        # 创建一个二维数组 dp，dp[i][j] 表示使用前 i 个硬币凑出金额 j 的方法数
        dp = [[0] * (target + 1) for _ in range(len(nums) + 1)]
        
        dp[0][0] = 1  # 用前 0 个元素凑 0 元有且只有一种方法

        for i in range(1, len(nums) + 1):
            value = nums[i - 1]  # 当前硬币的面值
            for j in range(target + 1):
                k = 0  # 挑选 value 的硬币数量
                while k * value <= j:
                    dp[i][j] += dp[i - 1][j - k * value]  # 将挑选的硬币数量为 0, 1, 2,... 统计起来
                    k += 1

        return dp[len(nums)][target]

# 测试用例
def test_change():
    solution = Solution()
    assert solution.change(5, [1, 2, 5]) == 4, "测试用例1失败"
    assert solution.change(3, [2]) == 0, "测试用例2失败"
    assert solution.change(10, [10]) == 1, "测试用例3失败"
    assert solution.change(0, [1, 2, 3]) == 1, "测试用例4失败"
    assert solution.change(500, [1, 2, 5]) == 12701, "测试用例5失败"
    print("所有测试用例通过!")

# 执行测试用例
test_change()
