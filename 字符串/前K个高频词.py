#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:46
# @Author  : yangguoli
# @File    : 前K个高频词.py
# @Software: PyCharm
import collections
import heapq



# 「堆 heap」是一种满足特定条件的完全二叉树
# 「小顶堆 min heap」：任意节点的值小于其子节点的值。
# 「大顶堆 max heap」：任意节点的值大于其子节点的值。
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

class Solution:
    def getKthWord(self, nums, k):
        if not nums:
            return
        counter = collections.Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)
        # 先建一个小顶堆
        # heap = []
        # for key, val in counter.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (val, key))
        #     else:
        #         if val > heap[0][0]:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap, (val, key))
        # return [key for val, key in heap]
        