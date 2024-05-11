#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午11:07
# @Author  : yangguoli
# @File    : 有重复项数字的全排列.py
# @Software: PyCharm
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        DFS
剪枝:保证当前层的节点值的唯一性，每一步对可用节点set一下。
        """
        ans =[]
        def dfs(nums, path):
            if not nums:
                ans.append(path)
                return
            temp = list(set(nums))
            for idx,i in enumerate(temp):
                nums.remove(i)
                dfs(nums, path + [i])
                nums.append(i)
        dfs(nums,[])
        ans.sort(key=lambda x:x[0])
        return ans