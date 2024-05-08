#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   N 叉树的前序遍历.py
@Time    :   2024/04/29 18:17:51
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''


class Solution:
    def preorder(self, root):
        ans = []
        def dfs(node) -> None:
            if node is None:
                return
            ans.append(node.val)
            for c in node.children:
                dfs(c)
        dfs(root)
        return ans
