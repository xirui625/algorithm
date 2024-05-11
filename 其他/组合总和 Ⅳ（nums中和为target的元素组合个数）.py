#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   组合总和 Ⅳ.py
@Time    :   2024/04/29 17:05:56
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

# 题目数据保证答案符合 32 位整数范围。

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        计算和为 i 的组合的个数
        dp[i] = sum(dp[i-num] for num in nums if i > nums)
        ''' 
        if not nums:
            return 0
        n = len(nums)
        dp = [0 for i in range(target+1)]
        # 将 dp[0] 初始化为 1，表示和为 0 的组合只有一种，即空组合。
        dp[0] = 1
        
        # 遍历从 1 到 target 的每一个和 i，对于每个和 i，遍历数组 nums 中的每个数字 
        for i in range(1, target+1):
            # 如果当前和 i 大于等于当前数字 nums[j]，则将 dp[i] 增加 dp[i-nums[j]]，
            # 表示将当前数字 nums[j] 加入到和为 i 的组合中，得到的新组合的个数为 dp[i-nums[j]]
            for j in range(n):
                if i>=nums[j]:
                    dp[i] += dp[i-nums[j]]
        return dp[-1]
