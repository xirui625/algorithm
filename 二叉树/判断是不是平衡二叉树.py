#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 上午11:40
# @Author  : yangguoli
# @File    : 判断是不是平衡二叉树.py
# @Software: PyCharm

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        return abs(self.helper(pRoot.left) - self.helper(pRoot.right)) < 2 and self.IsBalanced_Solution(
            pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def helper(self, root):
        # 获取二叉树最大深度
        if not root:
            return 0
        return max(self.helper(root.left), self.helper(root.right)) + 1

    #获取树的最大深度
    def getMaxDepth(self, root):
        if not root:
            return 0
        return max(self.getMaxDepth(root.left), self.getMaxDepth(root.right)) + 1

        # 获取树的最大深度
    def getMinDepth(self, root):
        if not root:
            return 0
        return max(self.getMaxDepth(root.left), self.getMaxDepth(root.right)) + 1