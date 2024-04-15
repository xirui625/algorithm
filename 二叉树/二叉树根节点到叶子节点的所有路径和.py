#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午10:18
# @Author  : yangguoli
# @File    : 二叉树根节点到叶子节点的所有路径和.py
# @Software: PyCharm    

class Solution:
    def sumNumbers(self , root ):
        if not root:
            return 0
        def helper(head, preSum):
            if not head:
                return 0
            curSum = preSum * 10 + head.val
            if not head.left and not head.right:
                return curSum
            return helper(head.left, curSum) + helper(head.right, curSum)
        return helper(root, 0)
        # write code here
