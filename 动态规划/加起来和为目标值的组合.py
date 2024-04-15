#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午3:42
# @Author  : yangguoli
# @File    : 加起来和为目标值的组合.py
# @Software: PyCharm
# 给定一个无重复元素的正整数数组 nums 和一个正整数 target ，
# 找出 nums 中所有可以使数字之和为目标数 target 的组合，nums 中的数可以重复选取，
# 只要选出的组合中有一个数不同则视为是不同组合。

# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        size = len(candidates)
        # 剪枝的前提是数组元素排序
        # 深度深的边不能比深度浅的边还小
        # 要排序的理由：1、前面用过的数后面不能再用；2、下一层边上的数不能小于上一层边上的数。
        candidates.sort()
        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.helper(candidates, 0, size, path, res, target)
        return res

    def helper(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.helper(candidates, index, size, path, res, residue)
            path.pop()