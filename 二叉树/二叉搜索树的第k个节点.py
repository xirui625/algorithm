#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午10:26
# @Author  : yangguoli
# @File    : 二叉搜索树的第k个节点.py
# @Software: PyCharm
# 给定一棵结点数为n 二叉搜索树，请找出其中的第 k 小的TreeNode结点值。

import heapq
class Solution:
    def KthNode(self , head , k ):
        if not head or k==0:
            return -1
        self.ret = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            self.ret.append(root.val)
            helper(root.right)
        helper(head)
        return heapq.nsmallest(k, self.ret)[-1]
