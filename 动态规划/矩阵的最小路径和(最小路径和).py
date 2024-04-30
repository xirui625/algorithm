#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午11:23
# @Author  : yangguoli
# @File    : 矩阵的最小路径和.py
# @Software: PyCharm

# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。


# 首先获取网格的行数 m 和列数 n，并初始化一个大小为 m x n 的动态规划数组 dp，其中 dp[i][j] 表示从左上角到达网格 (i, j) 位置的最小路径和。
# 开始遍历网格中的每个位置 (i, j)，使用双重循环遍历整个网格。
# 对于每个位置 (i, j)，根据动态规划的思想，考虑四种情况：
# 如果当前位置是网格的左上角 (0, 0)，则最小路径和就是当前位置的值 grid[0][0]。
# 如果当前位置位于第一行（i == 0），则只能从左边一格移动到当前位置 (i, j)，此时最小路径和为 dp[0][j-1] + grid[0][j]。
# 如果当前位置位于第一列（j == 0），则只能从上面一格移动到当前位置 (i, j)，此时最小路径和为 dp[i-1][0] + grid[i][0]。
# 如果当前位置不位于第一行也不位于第一列，则可以从左边一格或上面一格移动到当前位置 (i, j)，此时最小路径和为 min(dp[i][j-1], dp[i-1][j]) + grid[i][j]，即取左边一格和上面一格的最小路径和，再加上当前位置的值 grid[i][j]。
# 最终返回动态规划数组 dp 中的最后一个元素 dp[-1][-1]，即为从左上角移动到右下角的最小路径和。

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