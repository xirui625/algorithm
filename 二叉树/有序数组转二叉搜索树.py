#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:33
# @Author  : yangguoli
# @File    : 有序数组转二叉树.py
# @Software: PyCharm
from binary_tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node