#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:40
# @Author  : yangguoli
# @File    : 二叉树的所有路径.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.paths = []

    def binaryTreePaths(self, root):
        if not root:
            return
        def helper(node, path=''):
            if not root:
                return
            path += str(node.val)
            if not node.left and not node.right:
                self.paths.append(path)
            else:
                path += '=>'
                helper(node.left, path)
                helper(root.right, path)
        helper(root)
        return self.paths

            