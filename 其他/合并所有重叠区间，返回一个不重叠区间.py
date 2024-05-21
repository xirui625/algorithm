#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午12:56
# @Author  : yangguoli
# @File    : 合并区间.py
# @Software: PyCharm

# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

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
        # 初始化两个变量 start 和 end 分别表示当前合并区间的起始位置和结束位置，初始值为排序后的第一个区间的起始位置和结束位置
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            tmp_s = intervals[i][0]
            # 如果当前区间的起始位置 tmp_s 在当前合并区间的范围内，
            # 则更新当前合并区间的结束位置 end，取当前区间的结束位置和原合并区间的结束位置的较大值。
            if tmp_s >= start and tmp_s <= end:
                end = max(intervals[i][1], end)
            else:
                # 如果当前区间的起始位置 tmp_s 不在当前合并区间的范围内，
                # 则将当前合并区间 [start, end] 添加到结果列表 result 中，
                # 并更新当前合并区间的起始位置 start 和结束位置 end 为当前区间的起始位置和结束位置。
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start, end])
        return result