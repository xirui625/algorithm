#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:32
# @Author  : yangguoli
# @File    : 翻转二叉树.py
# @Software: PyCharm

class Solution:
    def invertTree(self, root):
        if not root:
            return
        node = root
        node.left, node.right = self.invertTree(root.right), self.invertTree(root.left)
        return node
