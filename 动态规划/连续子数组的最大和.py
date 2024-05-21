#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午8:10
# @Author  : yangguoli
# @File    : 连续子数组的最大和.py
# @Software: PyCharm

# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组是数组中的一个连续部分。

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化变量
        max_current = nums[0]  # 当前子数组的最大和，初始值为数组第一个元素
        max_global = nums[0]   # 全局最大和，初始值为数组第一个元素

        # 从第二个元素开始遍历数组
        for i in range(1, len(nums)):
            # 更新当前子数组的最大和
            max_current = max(nums[i], max_current + nums[i])  
            # 更新全局最大和
            max_global = max(max_global, max_current)  

        # 返回最大子数组的和
        return max_global

# 测试用例
def test_maxSubArray():
    solution = Solution()
    # 测试用例1
    assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6, "测试用例1失败"
    # 测试用例2
    assert solution.maxSubArray([1]) == 1, "测试用例2失败"
    # 测试用例3
    assert solution.maxSubArray([5,4,-1,7,8]) == 23, "测试用例3失败"
    # 测试用例4
    assert solution.maxSubArray([-1,-2,-3,-4]) == -1, "测试用例4失败"
    print("所有测试用例通过!")

# 执行测试用例
test_maxSubArray()
