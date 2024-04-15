#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:04
# @Author  : yangguoli
# @File    : 括号生成.py
# @Software: PyCharm

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(left, right, cur):
            if left==0 and right==0:
                res.append(cur)
                return
            if left < 0 or right <0 or left > right:
                return
            dfs(left-1, right, cur + '(')
            dfs(left, right-1, cur + ')')

        dfs(n, n, '')
        return res