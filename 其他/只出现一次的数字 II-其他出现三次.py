#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午11:01
# @Author  : yangguoli
# @File    : 只出现一次的数字 II-其他出现三次.py
# @Software: PyCharm
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。



import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans
