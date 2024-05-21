#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 上午11:06
# @Author  : yangguoli
# @File    : 二叉树右视图.py 请根据二叉树的前序遍历，中序遍历恢复二叉树，并打印出二叉树的右视图
# @Software: PyCharm

from binary_tree import TreeNode

class Solution:

    def __init__(self):
        self.res = []

    def solve(self , xianxu , zhongxu):
        if not xianxu or not zhongxu:
            return
        #构建二叉树
        root = self.buildTree(xianxu, zhongxu)
        # 层次遍历
        self.helper(root)
        # 返回每层最后最右结点
        return [item[-1] for item in self.res]

    def buildTree(self, xianxu, zhongxu):
        root_val = xianxu[0]
        mid_index = zhongxu.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(xianxu[1:mid_index+1], zhongxu[:mid_index+1])
        root.right = self.buildTree(xianxu[mid_index+1:], zhongxu[mid_index+1:])
        return root

    def helper(self, root, level=0):
        if not root:
            return
        if len(self.res) == level:
            self.res.append([root.val])
        else:
            self.res[level].append(root.val)
        self.helper(root.left, level+1)
        self.helper(root.right, level+1)