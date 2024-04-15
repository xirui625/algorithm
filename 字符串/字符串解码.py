#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午5:13
# @Author  : yangguoli
# @File    : 字符串解码.py
# @Software: PyCharm

class Solution:

    def decodeString(self, s):
        # write code here
        stack, digits, digit, cur = [], [], 0, ""
        for c in s:
            if "0" <= c <= "9":
                digit += 10 * digit + int(c)
            elif c == "[":
                digits.append(digit)
                digit = 0
                stack.append(cur)
                cur = ""
            elif c == "]":
                stack[-1] += cur * digits.pop()
                cur = stack.pop()
            else:
                cur += c
        return stack[-1] + cur if stack else cur