#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午10:14
# @Author  : yangguoli
# @File    : 组合总数-无重复元素.py
# @Software: PyCharm

# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        # 用于存储所有符合条件的组合
        res = []
        n = len(candidates)
        # idx 表示当前处理的候选数组的起始索引，path 表示当前正在构建的组合，t 表示当前目标值
        def helper(idx, path, t):

            if t == 0:
                res.append(path[:])
                return
            # 如果当前目标值 t 小于 0，说明当前路径不符合条件，直接返回，结束当前分支的搜索。
            if t < 0:
                return

            for i in range(idx, n):
                path.append(candidates[i])
                # 递归调用 helper 函数，更新目标值为 t - candidates[i]，并将索引更新为 i，表示下一个递归调用时可以继续使用当前候选数字
                helper(i, path, t - candidates[i])
                # 在递归调用返回后，将添加的候选数字从组合 path 中移除，以便尝试其他组合。
                path.pop()
        helper(0, [], target)
        return res