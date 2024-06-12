#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 下午4:30
# @Author  : yangguoli
# @File    : 打家劫舍2.py
# @Software: PyCharm


# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # 定义一个辅助函数，用来计算偷窃房屋的最大金额
        def helper(nums):
            pre = cur = 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        
        # 不偷第一个房子，不偷最后一个房子
        return max(helper(nums[1:]), helper(nums[:-1]))
