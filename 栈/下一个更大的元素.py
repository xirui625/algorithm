#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   下一个更大的元素.py
@Time    :   2024/04/02 22:14:10
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

'''
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 
'''


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # nums2 构建一个单调递减栈
        res = {}
        st = []
        for i in range(len(nums2)):
            while st and nums2[st[-1]] < nums2[i]:
                j = st.pop()
                res[nums2[j]] = nums2[i]
            st.append(i)
        return [res[i] if i in res else -1 for i in nums1]


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # nums2 构建一个单调递减栈
        res = {}  # 用于存储结果，键为元素值，值为下一个更大元素值
        st = []   # 单调递减栈，存储 nums2 中元素的索引

        # 遍历 nums2 中的每个元素
        for i in range(len(nums2)):
            # 如果栈不为空且当前元素大于栈顶元素，则栈顶元素的下一个更大元素为当前元素
            while st and nums2[st[-1]] < nums2[i]:
                j = st.pop()  # 弹出栈顶元素索引
                res[nums2[j]] = nums2[i]  # 记录下一个更大元素
            st.append(i)  # 当前元素入栈

        # 遍历 nums1，构建结果数组
        return [res[i] if i in res else -1 for i in nums1]

    
    
#给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。

#数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

            
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
                