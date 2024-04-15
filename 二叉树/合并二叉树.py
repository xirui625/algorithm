#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:37
# @Author  : yangguoli
# @File    : 合并二叉树.py
# @Software: PyCharm
class Solution:
    def mergeTree(self, l1, l2):
        if not l1 and l2:
            return
        if l1 and l2:
            l1.val += l2.val
            l1.left = self.mergeTree(l1.left, l2.left)
            l1.right = self.mergeTree(l1.right, l2.right)
        if l1 and not l2:
            l1 = l1
        else:
            l1 = l2
        return l1