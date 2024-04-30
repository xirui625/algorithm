#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   不同的二叉搜索树.py
@Time    :   2024/04/29 18:22:33
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
'''
class Solution:
    def numTrees(self, n: int) -> int:
        f = [0] * (n + 10)
        f[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                f[i] += f[j - 1] * f[i - j]
        return f[n]

