#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 下午11:17
# @Author  : yangguoli
# @File    : 二叉树展开为链表.py
# @Software: PyCharm

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        p = root
        p.left = None
        i = 1
        for i in range(1, len(res)):
            p.right = TreeNode(res[i])
            p = p.right
        return p

