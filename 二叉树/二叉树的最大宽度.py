#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午10:43
# @Author  : yangguoli
# @File    : 二叉树的最大宽度.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.res = []

    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        self.levelOrder(root)
        maxWidth = len(self.res[0])
        for index in range(1, len(self.res)):
            maxWidth = max(maxWidth, len(self.res[index]))
        return maxWidth

    def levelOrder(self, head):
        def helper(root, i=0):
            val = root.val if root else "#"
            if len(self.res) == i:
                self.res.append([val])
            else:
                self.res[i].append(val)
            helper(root.left, i + 1)
            helper(root.right, i + 1)

        helper(head)