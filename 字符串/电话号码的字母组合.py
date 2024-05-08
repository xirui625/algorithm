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
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        # combination，表示当前正在构建的字母组合，和next_digits，表示待处理的剩余数字串
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output
        