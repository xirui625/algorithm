#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   电话号码的字母组合.py
@Time    :   2024/04/29 16:34:20
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

# 定义了一个映射表，将数字映射到对应的字母。例如，数字 2 对应 "abc"，数字 3 对应 "def"，以此类推
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 映射每个数字到相应的字母列表
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        # 回溯函数：combination 表示当前构建的字母组合，next_digits 表示待处理的剩余数字串
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:  # 如果没有更多的数字要处理
                output.append(combination)  # 将当前的组合加入到输出列表中
            else:
                # 遍历当前数字对应的所有字母
                for letter in phone[next_digits[0]]:
                    # 将当前字母加入到组合中，并继续处理剩余的数字
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []  # 初始化输出列表
        if digits:  # 如果输入的数字串不为空
            backtrack("", digits)  # 从空组合和整个数字串开始回溯
        return output  # 返回所有可能的字母组合

        