#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   滑动窗口最大值.py
@Time    :   2024/04/02 22:55:49
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''


# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回 滑动窗口中的最大值 

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        if k >= len(nums):
            return [max(nums)] 
        ans = []
        q = deque()  # 双端队列
        for i, x in enumerate(nums):
            # 1. 入
            # 保证单调递减
            while q and nums[q[-1]] <= x:
                q.pop()  # 维护 q 的单调性
            # 队首元素始终是当前窗口的最大值的索引
            q.append(i)  # 入队
            # 2. 出
            # 检查队首元素的索引是否已经离开了当前窗口
            if i - q[0] >= k:  # 队首已经离开窗口了
                q.popleft()
            # 3. 记录答案
            if i >= k - 1:
                # 由于队首到队尾单调递减，所以窗口最大值就是队首
                ans.append(nums[q[0]])
        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
n = 12
so = Solution()
print(so.maxSlidingWindow(nums, n))