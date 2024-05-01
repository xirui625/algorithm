#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 下午9:23
# @Author  : yangguoli
# @File    : 全排列.py
# @Software: PyCharm

# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

from itertools import permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        n = len(nums)
        path, res = [], []
        def helper(nums):
            if len(path) == n:
                res.append(path[:])
                return
            for index, value in enumerate(nums):
                if value in path: #排除重复元素
                    continue
                path.append(value)
                helper(nums) #递归，每次都是从第一个元素遍历
                path.pop() #回溯
        helper(nums)
        return res


