#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 上午11:58
# @Author  : yangguoli
# @File    : 二叉树序列化反序列化.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:return "null,"
        left=self.serialize(root.left)
        right=self.serialize(root.right)
        return str(root.val)+','+left+right
    

    def deserialize(self, data):
        data=data.split(',')
        root=self.helper(data)
        return root

    def helper(self,data):

        val=data.pop(0)
        if val=='null':return None
        node=TreeNode(val)
        node.left=self.helper(data)
        node.right=self.helper(data)
        return node