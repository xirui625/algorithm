#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :    左叶子之和.py
@Time    :   2024/04/29 18:45:46
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def is_leaf(node):
            return node and not node.left and not node.right
        if not root:
            return 0
        if is_leaf(root.left):
            sum += root.left.val
        else:
            sum += self.sumOfLeftLeaves(root.left)
        sum += self.sumOfLeftLeaves(root.right)
        return sum