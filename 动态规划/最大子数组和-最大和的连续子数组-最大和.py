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

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # 初始化动态规划数组 dp
        dp = [0] * len(nums)
        dp[0] = nums[0]  # 初始条件，第一个元素的最大子数组和就是它本身
        
        # 遍历数组，计算最大子数组和
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])  # 状态转移方程
            
        return max(dp)  # 返回 dp 数组中的最大值作为最终的结果

# 测试用例
def test_maxSubArray():
    solution = Solution()
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "测试用例1失败"
    assert solution.maxSubArray([1]) == 1, "测试用例2失败"
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23, "测试用例3失败"
    assert solution.maxSubArray([-1, -2, -3]) == -1, "测试用例4失败"
    print("所有测试用例通过!")

# 执行测试用例
test_maxSubArray()



