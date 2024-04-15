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
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and h >= height[st[-1]]:
                bottom_h = height[st.pop()]
                if not st:  # len(st) == 0
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h  # 面积的高
                ans += dh * (i - left - 1)
            st.append(i)
        return ans

作