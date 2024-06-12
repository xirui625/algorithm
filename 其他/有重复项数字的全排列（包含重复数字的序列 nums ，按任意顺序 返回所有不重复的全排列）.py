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
        ans = []

        def dfs(nums, path):
            if not nums:  # 如果nums为空，说明找到了一个排列方案，将其加入结果集
                ans.append(path)
                return
            
            # 去重操作，将nums转换成集合，然后再转换成列表，确保同一层级上每个数字只使用一次
            temp = list(set(nums))
            
            for idx, i in enumerate(temp):
                nums.remove(i)  # 移除当前使用的数字i
                dfs(nums, path + [i])  # 递归调用
                nums.append(i)  # 恢复现场，将数字i重新加入nums列表，以便下一轮循环使用

        dfs(nums, [])
        ans.sort(key=lambda x: x[0])  # 按照每个排列的第一个元素排序
        return ans
