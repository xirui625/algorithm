#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   下一个更大元素 IV-非负整数数组 nums, 第二大整数.py
@Time    :   2024/05/21 20:32:49
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)  # 初始化结果数组，全部填充为 -1
        s = []  # 单调递减栈，存储元素下标
        t = []  # 辅助栈，存储元素下标

        # 枚举数组 nums 中的每一个元素及其下标
        for i, x in enumerate(nums):
            # 维护辅助栈 t，使得 t 中的元素始终是右侧第一个大于当前元素 x 的元素
            while t and nums[t[-1]] < x:
                ans[t.pop()] = x  # 将 t 栈顶元素的下一个更大元素设为 x

            # 在 s 中寻找下一个更大元素是 x 的位置 j
            j = len(s) - 1
            while j >= 0 and nums[s[j]] < x:
                j -= 1

            # 将 s 栈顶元素之后的所有元素加入到辅助栈 t 中
            t += s[j + 1:]
            # 弹出 s 栈顶元素之后的所有元素
            del s[j + 1:]
            # 将当前元素下标加入 s 栈中
            s.append(i)

        return ans

# 测试用例
def test_solution():
    solution = Solution()
    assert solution.secondGreaterElement([2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]
    assert solution.secondGreaterElement([3, 3]) == [-1, -1]
    assert solution.secondGreaterElement([1, 2, 4, 3]) == [4, 3, -1, -1]
    assert solution.secondGreaterElement([1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1]
    assert solution.secondGreaterElement([5, 3, 2, 4, 7]) == [7, 7, 4, 7, -1]
    print("所有测试用例通过!")

# 执行测试用例
test_solution()

