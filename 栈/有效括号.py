#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 下午11:15
# @Author  : yangguoli
# @File    : valid_parentheses.py 有效括号
# @Software: PyCharm

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。

class Solution:
    def __init__(self):
        self.stack = []

    def isValid(self , s):
        d = {'}': '{', ']': '[', ')': '('}
        for item in s:
            if item in '{[(':
                self.stack.append(item)
            if item in '}])':
                if not self.stack:
                    return False
                if d[item] == self.stack[-1]:
                    self.stack.pop()
                else:
                    return False
        return not self.stack


class Solution:

    def isValid(self , s):
        d = {'}': '{', ']': '[', ')': '('}
        stack = []
        for item in s:
            if item in '[{(':
                stack.append(item)
            if item in ']})':
                if not stack:
                    return False
                if d[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True



