#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午10:14
# @Author  : yangguoli
# @File    : 树的最大深度.py
# @Software: PyCharm

class Solution:
    def maxDepth(self , root ):
        if not root:
            return 0
        # if not root.left:
        #     return self.maxDepth(root.right) + 1
        # if not root.right:
        #     return self.maxDepth(root.left) + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1