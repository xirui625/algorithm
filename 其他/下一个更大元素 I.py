#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   下一个更大元素 I.py
@Time    :   2024/05/01 16:52:51
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

 

示例 1：

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
示例 2：

输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
'''

class Solution:
    # res = {}：创建一个空字典 res，用于存储 nums2 中每个元素的下一个更大的元素。
    # st = []：创建一个空列表 st，用于存储数组 nums2 中的索引。
    # for i in range(len(nums2)):：遍历数组 nums2 中的每个元素。
    # while st and nums2[st[-1]] < nums2[i]:：这是一个 while 循环，用于找到 nums2[i] 右边第一个比它大的元素。如果栈 st 不为空且 nums2[i] 大于栈顶元素对应的值 nums2[st[-1]]，则说明找到了下一个更大的元素。
    # j = st.pop()：弹出栈顶元素的索引，并将其赋值给 j。
    # res[nums2[j]] = nums2[i]：将栈顶元素对应的值作为键，将 nums2[i] 作为值存入字典 res，表示栈顶元素的下一个更大的元素是 nums2[i]。
    # st.append(i)：将当前元素的索引 i 添加到栈 st 中。
    # return [res[i] if i in res else -1 for i in nums1]：最后，构建结果列表，遍历 nums1 中的每个元素 i，如果 i 在字典 res 中，则取出对应的值，否则返回 -1，表示在 nums2 中不存在右边更大的元素。
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        st = []
        for i in range(len(nums2)):
            while st and nums2[st[-1]] < nums2[i]:
                j = st.pop()
                res[nums2[j]] = nums2[i]
            st.append(i)
        return [res[i] if i in res else -1 for i in nums1]

