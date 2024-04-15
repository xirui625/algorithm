#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午9:50
# @Author  : yangguoli
# @File    : 在二叉树中找到两个节点的最近公共祖先.py
# @Software: PyCharm

# 给定一棵二叉树(保证非空)以及这棵树上的两个节点对应的val值 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点

class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        if not root or root == o1 or root == o2:
            return root
        left = self.lowestCommonAncestor(root.left, o1, o2)
        right = self.lowestCommonAncestor(root.right, o1, o2)
        if left and right:
            return root
        return left or right
        # write code here