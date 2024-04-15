#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:20
# @Author  : yangguoli
# @File    : 二叉树的直径.py
# @Software: PyCharm

# 给你一棵二叉树的根节点，返回该树的 直径 。

# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

# 两节点之间路径的 长度 由它们之间边数表示。

class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.res = 0
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.res = max(self.res, left+right+1)
            return max(left, right) + 1
        helper(root)
        return self.res-1