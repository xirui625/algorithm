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
        # 调用 helper 函数分别找到左边界和右边界
        left_index = self.helper(nums, target)
        
        # 如果左边界超出数组长度或者左边界对应的值不等于目标值，则说明数组中不存在目标值，返回 [-1, -1]
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        
        # 调用 helper 函数找到右边界，注意右边界需要减去1，因为helper函数返回的是下一个不等于target的索引位置
        right_index = self.helper(nums, target, False)
        
        # 返回结果，左边界和右边界-1
        return [left_index, right_index-1]

    def helper(self, nums, target, left=True):
        """
        :type nums: List[int]
        :type target: int
        :type left: bool
        :rtype: int
        """
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
