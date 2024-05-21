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

def nextGreaterElement(nums1, nums2):
    # 哈希表，存储每个元素的下一个更大元素
    next_greater = {}
    # 栈，存储尚未找到下一个更大元素的数
    stack = []

    # 遍历 nums2
    for num in nums2:
        # 如果当前元素大于栈顶元素，则栈顶元素的下一个更大元素就是当前元素
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        # 将当前元素压入栈中
        stack.append(num)

    # 对于栈中剩余的元素，设置其下一个更大元素为 -1
    while stack:
        next_greater[stack.pop()] = -1

    # 生成结果数组，遍历 nums1，获取每个元素的下一个更大元素
    return [next_greater[num] for num in nums1]
    

def test_next_greater_element():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert nextGreaterElement(nums1, nums2) == [-1, 3, -1]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    assert nextGreaterElement(nums1, nums2) == [3, -1]

    nums1 = [1, 3, 5, 2, 4]
    nums2 = [6, 5, 4, 3, 2, 1, 7]
    assert nextGreaterElement(nums1, nums2) == [7, 7, 7, 7, 7]

    print("所有测试用例通过!")

# 执行测试用例
test_next_greater_element()

