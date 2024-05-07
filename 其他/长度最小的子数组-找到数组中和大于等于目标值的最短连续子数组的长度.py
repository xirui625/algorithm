#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   长度最小的子数组.py
@Time    :   2024/05/06 19:12:27
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其总和大于等于 target 的长度最小的 连续
# 子数组
#  [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

class Solution:
    # 首先，代码获取数组nums的长度n，并初始化一个变量ans为n+1，用来记录最短连续子数组的长度。同时，定义两个指针s和left，分别用来表示当前子数组的和以及子数组的左端点。
    # 然后，代码进入一个for循环，使用enumerate函数遍历数组nums。在循环中，每次遍历到一个元素nums[right]，就将其加入当前子数组的和s中。
    # 接着，代码进入一个while循环，条件是s大于等于目标值target。这个循环用来缩小子数组的范围，使得子数组的和尽可能接近目标值。具体操作是，不断地移动左端点left，并且更新ans为当前子数组的长度和原来ans中的较小值。同时，将nums[left]从当前子数组的和s中减去，以继续检查新的子数组。
    # 在循环外部，返回ans作为结果。如果ans仍然为初始值n+1，则说明不存在和大于等于目标值的子数组，返回0。
    # 这段代码的时间复杂度为O(n)，其中n为数组nums的长度。
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1  # 也可以写 inf
        s = left = 0
        for right, x in enumerate(nums):  # 枚举子数组右端点
            s += x
            while s >= target:  # 满足要求
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1  # 左端点右移
        return ans if ans <= n else 0