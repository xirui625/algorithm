#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   从中序与后序遍历序列构造二叉树.py
@Time    :   2024/04/29 18:32:13
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 首先进行基本的判断，如果后序遍历序列为空 postorder，则直接返回 None，表示当前子树为空树。
# 在后序遍历序列中，最后一个元素 postorder[-1] 表示根节点的值，因此创建根节点 root，值为 postorder[-1]。
# 在中序遍历序列中，找到根节点的值 postorder[-1] 所在的位置 mid，将中序遍历序列分为左子树部分和右子树部分。
# 递归构建左子树和右子树：
# 左子树的中序遍历序列为 inorder[:mid]，左子树的后序遍历序列为 postorder[:mid]，递归调用 self.buildTree(inorder[:mid], postorder[:mid]) 构建左子树。
# 右子树的中序遍历序列为 inorder[mid+1:]，右子树的后序遍历序列为 postorder[mid:-1]，递归调用 self.buildTree(inorder[mid+1:], postorder[mid:-1]) 构建右子树。
# 将左子树和右子树连接到根节点上，即 root.left = self.buildTree(inorder[:mid], postorder[:mid]) 和 root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])。
# 最后返回根节点 root。

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