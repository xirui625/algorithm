#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   目标和.py
@Time    :   2024/04/12 17:44:03
@Author  :   yangguoli 
@Desc    :   None
'''

# 给你一个非负整数数组 nums 和一个整数 target 。

# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2
        @cache  # 记忆化搜索
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        return dfs(len(nums) - 1, target)
    

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(index: int, current_sum: int) -> None:
            # 如果已经处理到数组的末尾
            if index == len(nums):
                # 检查当前和是否等于目标值
                if current_sum == target:
                    nonlocal count
                    count += 1
                return
        
            # 在当前数字前加上 '+'
            backtrack(index + 1, current_sum + nums[index])
            # 在当前数字前加上 '-'
            backtrack(index + 1, current_sum - nums[index])
    
        count = 0
        backtrack(0, 0)
        return count
    

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
    
        # 如果总和小于目标值，或者总和加目标值为奇数，则无法分成两部分
        if abs(target) > total_sum or (total_sum + target) % 2 == 1:
            return 0
        
        # 子集和的问题，求和为 (total_sum + target) // 2 的方法数
        subset_sum = (total_sum + target) // 2
        
        # dp[i] 表示和为 i 的子集数
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # 和为 0 的方法数为 1（什么都不选）

        # 遍历每个数字
        for num in nums:
            # 从后往前更新 dp 数组，避免重复计算
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]