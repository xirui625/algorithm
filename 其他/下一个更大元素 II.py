#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   下一个更大元素 II.py
@Time    :   2024/05/01 16:55:06
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。

数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

 

示例 1:

输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
示例 2:

输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        tmp = 2 * nums
        res = [-1 for _ in tmp]
        stack = []
        for i in range(len(tmp)):
            while stack and tmp[stack[-1]] < tmp[i]:
                res[stack.pop()] = tmp[i]
            stack.append(i)
        return res[:len(nums)]
            


