#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   从中序与后序遍历序列构造二叉树.py
@Time    :   2024/04/29 18:32:13
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return 
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1: ], postorder[mid:-1])
        return root