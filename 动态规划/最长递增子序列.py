#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午3:12
# @Author  : yangguoli
# @File    : 最长上升子序列.py
# @Software: PyCharm

# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
# 子序列。

# 状态定义：dp[i]表示以下标i结尾的最长上升子序列的长度。
# 状态初始化：以任意下标结尾的上升子序列长度不小于1，故初始化为1。
# 状态转移：遍历数组中所有的数，再遍历当前数之前的所有数，
# 只要前面某个数小于当前数，则要么长度在之前基础上加1，
# 要么保持不变，取两者中的较大者。即dp[i]=Math.max(dp[i],dp[j]+1)

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # dp[i] 表示以下标 i 结尾的最长上升子序列的长度
        dp = [1] * len(nums)
        
        # 遍历数组，计算最长上升子序列的长度
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 如果 nums[i] > nums[j]，更新 dp[i]
        
        return max(dp)  # 返回 dp 数组中的最大值作为最终的结果

# 测试用例
def test_lengthOfLIS():
    solution = Solution()
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "测试用例1失败"
    assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4, "测试用例2失败"
    assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1, "测试用例3失败"
    assert solution.lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3, "测试用例4失败"
    assert solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6, "测试用例5失败"
    print("所有测试用例通过!")

# 执行测试用例
test_lengthOfLIS()
