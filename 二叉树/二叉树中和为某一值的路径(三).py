#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树中和为某一值的路径(三).py
@Time    :   2024/04/15 16:53:07
@Author  :   yangguoli 
@Desc    :   None
'''

# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def findPath(root, sum):
            if root == None:
                return 0
            res = 0
            if root.val == sum:
                res += 1
            res += findPath(root.left, sum-root.val)
            res += findPath(root.right, sum-root.val)
            return res
            
        if root == None:
            return 0
        res = findPath(root, sum) 
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        
        return res