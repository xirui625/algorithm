#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 上午11:21
# @Author  : yangguoli
# @File    : 判断是不是二叉搜索树.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.res = []

    def isValidBST(self , root ):
        if not root:
            return True
        self.inOrder(root)
        for i in range(1, len(self.res)):
            if self.res[i] <= self.res[i-1]:
                return False
        return True

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root.val)
        self.inOrder(root.right)
