#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   最长连续序列-找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度.py
@Time    :   2024/05/01 17:24:06
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# if not nums: return 0：首先检查输入的数组是否为空，如果为空则直接返回0，因为没有连续序列。
# nums = list(set(nums))：利用集合的特性去除数组中的重复元素，然后将其转换为列表，这样可以确保后续遍历时每个数字只会被考虑一次。
# nums.sort()：对去重后的数组进行排序，这样可以使得相邻的元素在数组中的位置相邻，方便后续判断连续性。
# maxlen = 1：初始化最长连续序列的长度为1，因为最短的连续序列至少有一个元素。
# start = 0：初始化连续序列的起始位置为数组的第一个元素的索引。
# for end in range(1, len(nums)):：遍历数组中的每个元素，从第二个元素开始。
# if nums[end] - nums[end - 1] == 1:：判断当前元素与前一个元素之间的差值是否为1，如果是1，说明当前元素与前一个元素是连续的。
# maxlen = max(maxlen, end - start + 1)：更新最长连续序列的长度为当前连续序列的长度与之前最大长度的较大值。
# else:：如果当前元素与前一个元素之间的差值不为1，说明当前元素不与前一个元素连续。
# start = end：更新连续序列的起始位置为当前元素的索引，因为当前元素不连续，需要重新开始计算连续序列的长度。
# return maxlen：最后返回最长连续序列的长度。

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 如果输入列表为空，返回 0
        if not nums:
            return 0
        
        # 使用 set 去重，然后转换回列表
        nums = list(set(nums))
        # 对列表进行排序
        nums.sort()
        
        maxlen = 1  # 初始化最长连续序列的长度
        start = 0  # 初始化连续序列的起始位置
        
        # 遍历排序后的列表
        for end in range(1, len(nums)):
            # 如果当前元素与前一个元素之差为 1，表示连续
            if nums[end] - nums[end - 1] == 1:
                # 更新最长连续序列的长度
                maxlen = max(maxlen, end - start + 1)
            else:
                # 更新连续序列的起始位置
                start = end
        
        # 返回最长连续序列的长度
        return maxlen

