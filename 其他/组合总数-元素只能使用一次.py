#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午10:19
# @Author  : yangguoli
# @File    : zuhe zongshu.py
# @Software: PyCharm



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        n = len(candidates)

        def helper(idx, path, t):
            if t == 0:
                res.append(path[:])
                return

            if t < 0:
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                helper(i + 1, path, t - candidates[i])
                path.pop()

        helper(0, [], target)
        return res