#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 下午10:48
# @Author  : yangguoli
# @File    : 一个栈实现另一个栈的排序
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.help = []  # 初始化一个辅助栈help，用于辅助排序

    def solve(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        while a:  # 当输入栈a不为空时
            cur = a.pop()  # 弹出栈a的栈顶元素，赋值给cur
            # 如果辅助栈help的栈顶元素小于当前元素cur
            while self.help and self.help[-1] < cur:
                a.append(self.help.pop())  # 将辅助栈help的栈顶元素弹出并压入栈a中
            self.help.append(cur)  # 将当前元素cur压入辅助栈help中
        
        while self.help:  # 当辅助栈help不为空时
            a.append(self.help.pop())  # 将辅助栈help的栈顶元素弹出并压入栈a中

        return a  # 返回处理后的栈a
