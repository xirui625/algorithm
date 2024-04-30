#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   不同的二叉搜索树 II.py
@Time    :   2024/04/29 18:22:29
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate_tree(1, n) if n else []

    def generate_tree(self, start, end):
        '''
        解题思路：递归分别寻找每层中的每个元素可能的左子树与右子树，然后由当前元素分别与左右子树组成的所有结果，再层层往上返回结果
        :param start: 起始数字
        :param end: 终止数字
        :return: 返回所有符合条件的二叉搜索树
        '''
        if start > end:
            return [None]
        allTrees = []
        for i in range(start, end + 1):  # 枚举可行根节点
            # 获得所有可行的左子树集合
            leftTrees = self.generate_tree(start, i - 1)
            # 获得所有可行的右子树集合
            rightTrees = self.generate_tree(i + 1, end)
            # 从每一层的左子树与右子树集合中各选出一棵，拼接到当前遍历元素的根节点上
            # 其中左子树列表元素的个数，取决于当前层的当前元素可以取的左孩子节点的种类数.如：很明显，当前节点为1时，左孩子只有1种，即为None
            # 同理,其中右子树列表元素的个数，取决于当前层的当前元素可以取的右孩子节点的种类数. 如：很明显，当前节点为1时，右孩子只有2种，即为3->2 or 2->3
            for l in leftTrees:
                for r in rightTrees:
                    currTree = TreeNode(i)
                    currTree.left = l
                    currTree.right = r
                    allTrees.append(currTree)  # 将这一层当前元素所有可能组成的搜索树放到列表中，如果已经是最外层，即表示当前元素所生成的所有的二叉搜索树结果放入list中
        return allTrees