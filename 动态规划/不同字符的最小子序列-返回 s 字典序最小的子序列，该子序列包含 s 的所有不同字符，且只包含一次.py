#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   不同字符的最小子序列.py
@Time    :   2024/05/01 17:16:47
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
'''

import collections

class Solution:
    # stack = []：创建一个空列表 stack，用于存储构建的子序列。
    # remain_counter = collections.Counter(s)：利用 collections.Counter 创建一个字典，记录字符串 s 中每个字符的出现次数。
    # for c in s:：遍历字符串 s 中的每个字符。
    # if c not in stack:：如果当前字符 c 不在栈 stack 中，表示当前字符是第一次出现，需要考虑是否将其加入到结果中。
    # while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:：进入一个 while 循环，条件是栈 stack 不为空、当前字符 c 小于栈顶元素并且栈顶元素在剩余字符中的数量大于 0。这个循环的目的是将栈顶元素弹出，直到满足条件停止。
    # stack.pop()：弹出栈顶元素，因为它不满足构建字典序最小子序列的条件。
    # stack.append(c)：将当前字符 c 加入到栈 stack 中，因为它是字典序最小的字符之一。
    # remain_counter[c] -= 1：将当前字符 c 在剩余字符计数器 remain_counter 中的数量减 1，表示已经使用了一个 c。
    # return ''.join(stack)：返回栈 stack 中的字符拼接成的字符串，这就是构建的字典序最小的子序列。
    def smallestSubsequence(self, s: str) -> str:
        stack = []  # 用于存放结果的栈
        remain_counter = collections.Counter(s)  # 统计每个字符剩余的数量

        for c in s:
            if c not in stack:
                # 如果当前字符 c 没有在栈中，并且栈顶元素大于当前元素 c，且栈顶元素在后续还会出现，则弹出栈顶元素
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)  # 将当前字符 c 入栈
            remain_counter[c] -= 1  # 字符 c 的剩余数量减 1
        
        return ''.join(stack)  # 返回栈中的元素组成的字符串
