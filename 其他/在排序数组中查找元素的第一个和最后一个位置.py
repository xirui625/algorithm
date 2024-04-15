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

    # def insort_right(a, x, lo=0, hi=None):
    #     """Insert item x in list a, and keep it sorted assuming a is sorted.
    #
    #     If x is already in a, insert it to the right of the rightmost x.
    #
    #     Optional args lo (default 0) and hi (default len(a)) bound the
    #     slice of a to be searched.
    #     """

        # if lo < 0:
        #     raise ValueError('lo must be non-negative')
        # if hi is None:
        #     hi = len(a)
        # while lo < hi:
        #     mid = (lo + hi) // 2
        #     if x < a[mid]:
        #         hi = mid
        #     else:
        #         lo = mid + 1
        # a.insert(lo, x)
        #
        # if lo < 0:
        #     raise ValueError('lo must be non-negative')
        # if hi is None:
        #     hi = len(a)
        # while lo < hi:
        #     mid = (lo + hi) // 2
        #     if a[mid] < x:
        #         lo = mid + 1
        #     else:
        #         hi = mid
        # a.insert(lo, x)