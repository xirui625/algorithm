#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   无重叠区间.py
@Time    :   2024/04/30 16:10:21
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。

 

示例 1:

输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: intervals = [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
'''

# 首先，获取区间列表的长度 n，如果区间列表为空，则直接返回 0，因为此时不存在重叠的区间。
# 初始化动态规划数组 dp，长度为 n，每个元素初始值为 1，表示以当前区间结尾的最大非重叠区间数量。
# 初始化变量 ans 为 1，表示最终的结果，即至少保留一个区间不重叠。
# 对区间列表进行排序，按照区间的起始位置进行升序排序。
# 遍历区间列表，对于每个区间 intervals[i]：
# 从当前区间的前一个区间开始向前遍历，直到第一个区间，检查是否与当前区间重叠。如果当前区间的起始位置大于或等于前一个区间的结束位置，则表示两个区间不重叠。
# 更新动态规划数组 dp[i]，dp[i] 的值为当前区间与前一个非重叠区间的最大数量加上 1。这里之所以加上 1，是因为当前区间本身也算一个非重叠区间。
# 由于区间已经按照起始位置排序，一旦找到第一个不重叠的区间，后面的区间就不需要再考虑了，因此可以通过 break 语句跳出内层循环，进行剪枝操作。
# 最终返回 n - max(dp)，即删除的最少区间数量，即保留的最大非重叠区间数量。

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0: return 0
        dp = [1] * n
        ans = 1
        intervals.sort(key=lambda a: a[0])

        for i in range(len(intervals)):
            for j in range(i - 1, -1, -1):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break # 由于是按照开始时间排序的, 因此可以剪枝
                
        return n - max(dp)




