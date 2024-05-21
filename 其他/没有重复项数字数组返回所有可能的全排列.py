#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 下午9:23
# @Author  : yangguoli
# @File    : 全排列.py
# @Software: PyCharm

# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        n = len(nums)  # 获取输入列表的长度
        path, res = [], []  # 初始化路径和结果列表

        def helper(nums):
            # 如果路径的长度等于输入列表的长度，说明找到一个全排列
            if len(path) == n:
                res.append(path[:])  # 将当前路径的副本添加到结果中
                return
            
            # 遍历输入列表中的每一个元素
            for index, value in enumerate(nums):
                # 排除已在路径中的元素以避免重复
                if value in path:
                    continue
                path.append(value)  # 将当前元素添加到路径中
                helper(nums)  # 递归调用，继续生成排列
                path.pop()  # 回溯，移除最后一个添加的元素

        helper(nums)  # 从输入列表的第一个元素开始调用递归函数
        return res  # 返回所有生成的全排列



