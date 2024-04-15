#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午12:56
# @Author  : yangguoli
# @File    : 合并区间.py
# @Software: PyCharm

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return
        result = []
        #根据多结点排序
        intervals = sorted(intervals, key=lambda x:x[0])
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            tmp_s = intervals[i][0]
            if tmp_s >= start and tmp_s <= end:
                end = max(intervals[i][1], end)
            else:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start, end])
        return result