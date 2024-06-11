#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   柱状图中最大的矩形.py
@Time    :   2024/04/02 21:56:54
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
'''

class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        # 左右增加一个高度为 0 的柱子，这样做是为了确保所有的柱子都能够被处理到，而不会因为边界而漏掉
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            #如果当前柱子的高度大于栈顶柱子的高度，则将当前柱子的索引入栈
            stack.append(i)
        return res

class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # 初始化一个空栈，用于存储柱子的索引
        # 在 heights 两端各增加一个高度为 0 的柱子，确保所有柱子都能被处理到
        heights = [0] + heights + [0]
        res = 0  # 初始化结果变量，存储最大的矩形面积
        
        for i in range(len(heights)):  # 遍历 heights 数组的每个元素
            # 当栈不为空且当前柱子的高度小于栈顶柱子的高度时
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()  # 弹出栈顶柱子的索引
                # 计算以弹出柱子为高度的矩形面积，并更新最大面积
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            # 如果当前柱子的高度大于栈顶柱子的高度，则将当前柱子的索引入栈
            stack.append(i)
        
        return res  # 返回最大的矩形面积

    
    
