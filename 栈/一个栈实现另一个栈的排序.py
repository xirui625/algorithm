#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 下午10:48
# @Author  : yangguoli
# @File    : 一个栈实现另一个栈的排序
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.help = []

    def solve(self , a ):
        while a:
            cur = a.pop()
            # 如果help的栈顶元素小于cur
            while not self.help and self.help[-1] < cur:
                a.append(self.help.pop())
            self.help.append(cur)
        while self.help:
            a.append(self.help.pop())

        return a