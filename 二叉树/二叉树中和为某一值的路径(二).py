#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午11:13
# @Author  : yangguoli
# @File    : 二叉树中和为某一值的路径(二).py
# @Software: PyCharm

# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

class Solution:

    def __init__(self):
        self.path = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        def preOrder(node, sum1, path):
            if node == None:
                return

            if node.left == None and node.right == None and sum1 == node.val:
                self.path.append(path)
                return

            if node.left == None and node.right == None:
                return

            if node.left:
                preOrder(node.left, sum1 - node.val, path + [node.left.val])
            if node.right:
                preOrder(node.right, sum1 - node.val, path + [node.right.val])

            return

        preOrder(root, expectNumber, [root.val])
        return self.path