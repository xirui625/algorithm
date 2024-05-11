#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   没有重复项的全排列.py
@Time    :   2024/05/11 10:19:59
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return
        n = len(nums)
        # ret = []
        # for item in permutations(nums, len(nums)):
        #     print item
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