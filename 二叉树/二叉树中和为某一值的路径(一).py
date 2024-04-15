#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午11:05
# @Author  : yangguoli
# @File    : 二叉树中和为某一值的路径(一).py
# @Software: PyCharm

class Solution:
    def hasPathSum(self , root , sum ):
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)