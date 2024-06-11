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


import collections  # 导入collections模块，以便使用Counter类
import heapq  # 导入heapq模块，以便使用堆操作

class Solution:
    def getKthWord(self, nums, k):
        if not nums:  # 如果输入列表为空，直接返回
            return
        
        counter = collections.Counter(nums)  # 使用Counter统计nums中每个元素的出现次数
        # 使用heapq.nlargest函数，获取出现频率最高的前k个元素
        return heapq.nlargest(k, counter.keys(), key=counter.get)





import collections  # 导入collections模块，以便使用Counter类
import heapq  # 导入heapq模块，以便使用堆操作

class Solution:
    def getKthWordTmp(self, nums, k):
        if not nums:  # 如果输入列表为空，直接返回
            return
        heap = []  # 初始化一个空堆
        counter = collections.Counter(nums)  # 使用Counter统计nums中每个元素的出现次数

        for key, value in counter.items():  # 遍历Counter中的每个元素及其出现次数
            if len(heap) < k:  # 如果堆的大小小于k
                heapq.heappush(heap, (value, key))  # 将元素的出现次数及其对应的元素推入堆中
            else:
                if value > heap[0][0]:  # 如果当前元素的出现次数大于堆顶元素的出现次数
                    heapq.heappop(heap)  # 弹出堆顶元素
                    heapq.heappush(heap, (value, key))  # 将当前元素及其出现次数推入堆中

        return [key for value, key in heap]  # 返回堆中元素对应的元素部分，按出现次数从小到大排序



        