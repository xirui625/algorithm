#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   二叉搜索树中第K小的元素.py
@Time    :   2024/04/29 18:46:09
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        ret = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            ret.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return ret[k-1]