#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午4:03
# @Author  : yangguoli
# @File    : 数组中第K个大元素.py length-(k - 1)
# @Software: PyCharm

# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # 将数组转换为最小堆
        heap = []
        for num in nums:
            # 将元素压入堆中
            heapq.heappush(heap, num)
            # 如果堆的大小超过了 k，则弹出堆顶元素，保持堆的大小为 k
            if len(heap) > k:
                heapq.heappop(heap)
        # 最终堆顶元素即为第 k 个最大的元素
        return heap[0]