#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   二叉树的右视图.py
@Time    :   2024/04/29 18:41:34
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

'''


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None: return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans