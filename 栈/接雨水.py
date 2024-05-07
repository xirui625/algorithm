#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   接雨水.py
@Time    :   2024/04/02 22:57:03
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0  # 初始化接水总量
        st = []  # 用于存储高度的栈
        for i, h in enumerate(height):  # 遍历每个高度
            while st and h >= height[st[-1]]:  # 如果当前高度大于栈顶的高度
                bottom_h = height[st.pop()]  # 弹出栈顶的高度，作为底部的高度
                if not st:  # 如果栈为空，则无法形成凹槽，结束循环
                    break
                left = st[-1]  # 获取左边界的索引
                dh = min(height[left], h) - bottom_h  # 计算凹槽的高度，即两侧较低的高度减去底部高度
                ans += dh * (i - left - 1)  # 计算凹槽的面积，即高度乘以宽度
            st.append(i)  # 将当前高度的索引加入栈中
        return ans  # 返回接水总量
