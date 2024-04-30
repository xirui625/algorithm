#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 上午11:40
# @Author  : yangguoli
# @File    : 判断是不是平衡二叉树.py
# @Software: PyCharm

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.helper(root.left) - self.helper(root.right)) < 2 and self.isBalanced(
            root.left) and self.isBalanced(root.right)
            
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