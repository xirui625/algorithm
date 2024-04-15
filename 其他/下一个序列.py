#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午10:29
# @Author  : yangguoli
# @File    : 下一个序列.py
# @Software: PyCharm
class Solution(object):
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(self, nums, l, r):
        while l < r:
            self.swap(nums, l, r)
            l += 1
            r -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            i -= 1
        if i == 0:
            self.reverse(nums, 0, n-1)
            return
        j = n-1
        i -= 1
        # nums[j]<=nums[i]<=nums[j-1]
        while j > i and nums[j] <= nums[i]:
            j -= 1
        self.swap(nums, i, j)
        self.reverse(nums, i+1, n-1)
        return nums