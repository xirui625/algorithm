#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 下午3:16
# @Author  : yangguoli
# @File    : jis.py
# @Software: PyCharm

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