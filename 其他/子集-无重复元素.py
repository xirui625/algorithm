#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 下午3:17
# @Author  : yangguoli
# @File    : 子集-无重复元素.py
# @Software: PyCharm

# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
# 子集
# （幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

class Solution:
    def __init__(self):
        pass

    def subsets(self, nums):
        ans=[]
        nums.sort()
        def dfs(idx,temp):
            ans.append(temp[:])
            for i in range(idx,len(nums)):
                temp.append(nums[i])
                dfs(i+1,temp)
                temp.pop()
        dfs(0,[])
        return ans