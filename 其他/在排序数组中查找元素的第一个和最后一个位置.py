#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 下午9:32
# @Author  : yangguoli
# @File    : 在排序数组中查找元素的第一个和最后一个位置.py
# @Software: PyCharm
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = self.helper(nums, target)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        right_index = self.helper(nums, target, False)
        return [left_index, right_index-1]


    def helper(self, nums, target, left=True):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo