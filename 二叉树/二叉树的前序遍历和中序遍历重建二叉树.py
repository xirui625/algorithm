#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午10:10
# @Author  : yangguoli
# @File    : 二叉树的前序遍历和中序遍历.py
# @Software: PyCharm


from 二叉树 import TreeNode


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, preorder, inorder):
        if not preorder or not inorder:
            return
        # 确定头节点
        root_val = preorder[0]
        # 获取头节点的在中序遍历的位置
        mid = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.reConstructBinaryTree(preorder[1: mid + 1], inorder[:mid + 1])
        root.right = self.reConstructBinaryTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
        # write code here