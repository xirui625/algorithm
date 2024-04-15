#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   每日温度.py
@Time    :   2024/04/02 22:25:40
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 请根据每日 气温 列表 temperatures ，重新生成一个列表，要求其对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(T)
        for i, j in enumerate(T):
            while stack and j>T[stack[-1]]:
                result[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return result