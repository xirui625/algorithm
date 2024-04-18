#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午4:03
# @Author  : yangguoli
# @File    : 数组中第K个大元素.py length-(k - 1)
# @Software: PyCharm
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        # 维持一个小顶堆
        heapq.heapify(nums)
        i = 0
        length = len(nums)
        while len(nums) != 0:
            i += 1
            value = heapq.heappop(nums)
            if i == length - (k - 1):
                return value