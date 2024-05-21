#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 下午1:26
# @Author  : yangguoli
# @File    : 移掉 K 位数字.py 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
# @Software: PyCharm
# 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []    # 用于模拟栈的数据结构
        remain = len(num) - k   # 计算剩余数字的个数
        for digit in num:   # 遍历 num 中的每个数字
            while k and stack and stack[-1] > digit:  # 当仍需移除数字，栈不为空，且栈顶元素大于当前数字时
                stack.pop()   # 弹出栈顶元素
                k -= 1   # 更新还需移除的数字的个数
            stack.append(digit)   # 将当前数字加入栈中
        return ''.join(stack[:remain]).lstrip('0') or '0'   # 构建结果字符串并返回
