#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   N 叉树的后序遍历.py
@Time    :   2024/04/29 18:20:15
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

class Solution:
    def postorder(self, root) -> List[int]:
        ans = []
        def dfs(node) -> None:
            if node is None:
                return
            for c in node.children:
                dfs(c)
            ans.append(node.val)
        dfs(root)
        return ans
