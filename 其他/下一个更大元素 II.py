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
    # tmp = 2 * nums：创建一个新列表 tmp，它将原始数组 nums 重复拼接一次。这样做的目的是为了处理循环数组的情况，因为右边第一个比当前元素大的元素可能在数组的头部。
    # res = [-1 for _ in tmp]：创建一个与 tmp 相同长度的结果列表 res，并将其初始化为 -1。这个列表用于存储每个元素的下一个更大的元素，初始化为 -1 表示暂时没有找到更大的元素。
    # stack = []：创建一个空栈 stack，用于存储 tmp 中元素的索引。
    # for i in range(len(tmp)):：遍历 tmp 中的每个元素的索引 i。
    # while stack and tmp[stack[-1]] < tmp[i]:：这是一个 while 循环，用于找到 tmp[i] 右边第一个比它大的元素。如果栈 stack 不为空且栈顶元素对应的值 tmp[stack[-1]] 小于 tmp[i]，则说明找到了下一个更大的元素。
    # res[stack.pop()] = tmp[i]：弹出栈顶元素的索引，并将 tmp[i] 存入结果列表 res 中对应位置，表示栈顶元素的下一个更大的元素是 tmp[i]。
    # stack.append(i)：将当前元素的索引 i 添加到栈 stack 中。
    # return res[:len(nums)]：最后，返回结果列表 res 的前半部分，即原始数组 nums 长度的部分，因为只需考虑原始数组的部分即可。
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        tmp = 2 * nums
        res = [-1 for _ in tmp]
        stack = []
        for i in range(len(tmp)):
            while stack and tmp[stack[-1]] < tmp[i]:
                res[stack.pop()] = tmp[i]
            stack.append(i)
        return res[:len(nums)]
            


