#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:24
# @Author  : yangguoli
# @File    : 另一个子树.py
# @Software: PyCharm

class Solution:
    def isSubtree(self, s, t):
        # 遍历树
        def helper(root):
            if not root:
                return "#"
            return '*' + str(root.val) + helper(root.left) + helper(root.right)
        ss = helper(s)
        tt = helper(t)
        return tt in ss
