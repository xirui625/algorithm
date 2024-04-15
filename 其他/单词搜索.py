#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午10:33
# @Author  : yangguoli
# @File    : 单词搜索.py
# @Software: PyCharm

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