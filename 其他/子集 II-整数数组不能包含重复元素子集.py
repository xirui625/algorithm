#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 下午3:16
# @Author  : yangguoli
# @File    : jis.py
# @Software: PyCharm

# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 
# 子集
# （幂集）。

# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
        def dfs(idx,temp):
            if temp not in ans:
                ans.append(temp[:])
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                dfs(i+1,temp)
                temp.pop()
        dfs(0,[])
        return ans