#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午10:19
# @Author  : yangguoli
# @File    : zuhe zongshu.py
# @Software: PyCharm

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
                #如果当前索引 i 大于 idx，且当前候选数字与上一个候选数字相同（即重复数字），则跳过当前候选数字，以避免重复组合
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                helper(i + 1, path, t - candidates[i])
                path.pop()

        helper(0, [], target)
        return res