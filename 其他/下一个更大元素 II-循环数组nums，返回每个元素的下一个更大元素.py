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
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n  # 初始化结果数组为 -1
        stack = []  # 单调栈，存储元素下标

        # 遍历两次数组
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                # 当当前元素大于栈顶元素时，更新栈顶元素的下一个更大元素
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i % n)  # 只将下标存储一次
        return res
    

# def test_next_greater_elements():
assert Solution().nextGreaterElements([1, 2, 1]) == [2, -1, 2]
assert Solution().nextGreaterElements([5, 4, 3, 2, 1]) == [-1, 5, 5, 5, 5]
assert Solution().nextGreaterElements([2, 1, 2, 4, 3]) == [4, 2, 4, -1, 4]
assert Solution().nextGreaterElements([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1]
print("所有测试用例通过!")
            


