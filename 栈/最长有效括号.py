#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午9:59
# @Author  : yangguoli
# @File    : 最长括号.py
# @Software: PyCharm

# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

class Solution:
    def longestValidParentheses(self, s):
        stack = []
        res = 0
        for i in range(len(s)):
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
                res = max(res, i - (stack[-1] if stack else - 1))
        return res
    

class Solution:
    def longestValidParentheses(self, s):
        # 构建一个栈，如果遇到栈为空、栈顶元素为右括号、当前元素为左括号这三种情况，则将当前元素的索引进栈，当括号匹配时栈顶元素出栈，返回当前元素与栈顶元素的索引差值，取最大就是答案
        stack=[] # 构建一个栈记录字符index
        ans=0
        for i in range(len(s)):
            # 如果栈非空，且当前为右括号，且有记录的左括号，则出栈
            if stack and s[i]==")" and s[stack[-1]]=="(":
                stack.pop()
                # 如果出栈后变成空栈，则说明整个[0:i]的区间都是合格的，长度为i+1
                # 如果出栈后非空，则说明区间[stack[-1]:i]是合格的
                ans=max(ans,i-(stack[-1] if stack else -1))
            else:
                # 以下3个条件会触发else
                # 如果是空栈
                # 或者当前字符为左括号（需要寻找匹配的右括号）
                # 或者当前字符为右括号，而且栈顶记录的也是右括号（不合格的情况，永远不会被pop）
                stack.append(i)
        return ans