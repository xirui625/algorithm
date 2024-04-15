#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   二分查找.py
@Time    :   2024/04/01 11:24:48
@Author  :   yangguoli 
@Desc    :   数组为有序数组，同时题目还强调数组中无重复元素 这是先决条件
'''


class Solution:
    '''
    左闭右闭
    '''
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            return mid if nums[mid] == target else -1
        


class Solution:
    '''
    左闭右开
    '''
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while (left < right):
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            return mid if nums[mid] == target else -1