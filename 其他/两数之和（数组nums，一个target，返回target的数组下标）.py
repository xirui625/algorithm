#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 下午4:40
# @Author  : yangguoli
# @File    : 两数之和.py
# @Software: PyCharm

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

# 你可以按任意顺序返回答案。

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         hashmap = {}
#         for i, j in enumerate(nums):
#             if (target-j) in hashmap:
#                 return [i, hashmap[target-j]]
#             hashmap[j] = i

class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            if target - value in hash_map:
                return [index, hash_map[target - value]]
            hash_map[value] = index