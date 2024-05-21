#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午10:19
# @Author  : yangguoli
# @File    : zuhe zongshu.py
# @Software: PyCharm

class Solution:
    def combinationSum2(self, candidates, target):
        # 对候选数组进行排序，以便后续去重
        candidates.sort()
        res = []  # 存储最终的组合结果
        n = len(candidates)  # 候选数组的长度

        def helper(idx, path, t):
            # 如果目标值 t 为 0，说明找到一个满足条件的组合
            if t == 0:
                res.append(path[:])  # 将当前组合添加到结果集中
                return

            # 如果目标值 t 小于 0，说明当前组合不符合条件
            if t < 0:
                return

            # 遍历候选数组，从当前索引开始
            for i in range(idx, n):
                # 如果当前索引 i 大于 idx，且当前候选数字与上一个候选数字相同（即重复数字），则跳过当前候选数字，以避免重复组合
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                # 将当前候选数字添加到组合中
                path.append(candidates[i])
                # 递归调用 helper 函数，更新索引和目标值
                helper(i + 1, path, t - candidates[i])
                # 回溯，移除最后一个添加的数字
                path.pop()

        # 从索引 0 开始调用 helper 函数，初始组合为空，目标值为 target
        helper(0, [], target)
        # 返回所有满足条件的组合
        return res
