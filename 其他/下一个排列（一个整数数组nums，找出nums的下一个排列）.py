#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午10:29
# @Author  : yangguoli
# @File    : 下一个序列.py

# @Software: PyCharm

# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。

# 必须 原地 修改，只允许使用额外常数空间。
class Solution:
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