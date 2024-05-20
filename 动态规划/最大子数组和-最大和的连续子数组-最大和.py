#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   最大子数组和.py
@Time    :   2024/04/30 16:19:43
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组
是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
'''

# 首先进行基本的判断，如果数组 nums 为空，则直接返回 0。
# 初始化一个长度为 len(nums) 的动态规划数组 dp，用于存储以每个位置结尾的连续子数组的最大和。初始时，将数组第一个元素 nums[0] 赋值给 dp[0]。
# 遍历数组 nums，从第二个元素开始，对于每个位置 i：
# 计算以当前位置 i 结尾的连续子数组的最大和，有两种情况：
# 子数组只包含当前元素 nums[i]，即 nums[i] 本身就是最大子数组。
# 子数组包含当前元素 nums[i]，并且包含前面连续的子数组，即 dp[i-1] 加上当前元素 nums[i]。
# 取这两种情况中的较大值作为 dp[i] 的值，即 dp[i] = max(nums[i], dp[i-1]+nums[i])。
# 最终返回动态规划数组 dp 中的最大值，即 max(dp)，表示整个数组中连续子数组的最大和。
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)


