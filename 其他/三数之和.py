#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 下午4:41
# @Author  : yangguoli
# @File    : 三数之和.py
# @Software: PyCharm

# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

# 你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。
import collections

# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # 哈希表的方式解决
#         nums_dict = collections.Counter(nums)
#         ret = []
#         #先排序
#         nums.sort()
#         #特殊情况考虑
#         if 0 in nums_dict and nums_dict[0] >= 3:
#             ret.append([0, 0, 0])
#         n = list(filter(lambda a: a < 0, nums_dict))
#         p = list(filter(lambda a: a >= 0, nums_dict))
#         for i in n:
#             for j in p:
#                 dif = 0 - i - j
#                 if dif in nums_dict:
#                     if dif in (i, j) and nums_dict[dif] >=2:
#                         ret.append([i, j, dif])
#                     if dif < i or dif >j:
#                         ret.append([i, j, dif])
#         return ret
class Solution(object):
    def threeSum(self, nums):
        nums_dict = collections.Counter(nums)
        ret = []
        # 先排序
        nums.sort()
        if 0 in nums_dict and nums_dict[0] >= 3:
            ret.append([0, 0, 0])
        n = list(filter(lambda a: a < 0, nums_dict))
        p = list(filter(lambda a: a >= 0, nums_dict))
        for i in n:
            for j in p:
                dif = 0 - i - j
                if dif in nums_dict:
                    if dif in (i, j) and nums_dict[dif] >=2:
                        ret.append([i, j, dif])
                    if dif < i or dif > j:
                        ret.append([i, j, dif])
        return ret