#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   乘积最大子数组.py
@Time    :   2024/04/30 16:21:11
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 首先进行基本的判断，如果数组 nums 为空，则直接返回 0。
# 初始化三个变量 mi、ma 和 res，分别表示当前位置结尾的最小乘积、最大乘积和最终结果。初始时，将它们都赋值为数组的第一个元素 nums[0]。
# 遍历数组 nums，从第二个元素开始，对于每个位置 i：
# 如果当前元素 nums[i] 小于 0，表示当前元素为负数，那么最大乘积和最小乘积会互相影响，所以需要交换 mi 和 ma 的值。
# 更新最小乘积和最大乘积。最小乘积 mi 的更新规则是当前元素 nums[i] 与当前元素乘以最小乘积 mi 的较小值；最大乘积 ma 的更新规则是当前元素 nums[i] 与当前元素乘以最大乘积 ma 的较大值。
# 更新最终结果 res，取最大乘积 ma 和当前结果 res 中的较大值。
# 最终返回结果 res，即为数组中连续子数组的最大乘积。

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mi = ma = res = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] <0:
                mi, ma = ma, mi
            mi = min(mi*nums[i], nums[i])
            ma = max(ma*nums[i], nums[i])
            res = max(res, ma)
        return res