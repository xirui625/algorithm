#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午11:23
# @Author  : yangguoli
# @File    : 矩阵的最小路径和.py
# @Software: PyCharm

# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

class Solution:
    def minPathSum(self , matrix ):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + matrix[i][j]
        return matrix[m-1][n-1]
        # write code here

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[0][j] = dp[0][j-1] + grid[0][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[-1][-1]