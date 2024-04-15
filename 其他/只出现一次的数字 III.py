#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午11:03
# @Author  : yangguoli
# @File    : 只出现一次的数字 III.py
# @Software: PyCharm

# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1]
        return ans