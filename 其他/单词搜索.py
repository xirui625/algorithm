#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午10:33
# @Author  : yangguoli
# @File    : 单词搜索.py
# @Software: PyCharm

# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # dfs寻找
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # 当数组越界或不相等时则不匹配
            if not 0 <= i < m or not 0 <= j < n or not board[i][j] == word[k]:
                return False
            # 匹配成功
            if k == len(word) - 1:
                return True
            # 避免走回头路
            board[i][j] = ''
            # 上下左右四个方向进行搜索
            res = dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
            # 恢复当前的网格内字符
            board[i][j] = word[k]
            return res

        # 看是否匹配
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False