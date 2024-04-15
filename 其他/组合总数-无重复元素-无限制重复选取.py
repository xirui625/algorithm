#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午10:14
# @Author  : yangguoli
# @File    : 组合总数-无重复元素.py
# @Software: PyCharm

class Solution:
    def combinationSum(self, candidates, target):
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