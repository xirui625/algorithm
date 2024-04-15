#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 下午10:09
# @Author  : yangguoli
# @File    : get_min_stack.py 最小值栈
# @Software: PyCharm

# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# 维持一个最小值的辅助栈，入栈的时候进行相应的判断，时刻保持最小值栈的栈顶值最小


class Solution:
    def __init__(self):
        self.stack     = []
        self.mainStack = []

    def push(self, data):
        if not self.mainStack:
            self.mainStack.append(data)
        elif data < self.mainStack[-1]:
            self.mainStack.append(data)
        else:
            self.mainStack.append(self.mainStack[-1])
        self.stack.append(data)

    def pop(self):
        self.mainStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.mainStack[-1]