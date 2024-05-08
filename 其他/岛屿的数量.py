#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午2:44
# @Author  : yangguoli
# @File    : 岛屿的数量.py
# @Software: PyCharm
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        count = 0
        def helper(grid, i, j):
            # 首先进行边界条件的判断，如果当前坐标 (i, j) 超出了网格范围，或者当前位置为水域 '0'，则直接返回
            if not 0<=i<m or not 0<=j<n or grid[i][j] == '0':
                return
            # 将当前位置标记为水域，即将 '1' 修改为 '0'，表示已经访问过,确保每个岛屿只被统计一次，并且避免重复访问格子
            grid[i][j] = '0'
            # 分别向上、向下、向左、向右四个方向递归调用 helper 函数，以继续探索当前位置的上下左右相邻位置。
            helper(grid, i-1, j)
            helper(grid, i+1, j)
            helper(grid, i, j-1)
            helper(grid, i, j+1)

        for i in range(m):
            for j in range(n):
                # 如果当前位置为陆地 '1'，则调用 helper 函数开始探索该岛屿的连通区域，并将岛屿数
                if grid[i][j] == '1':
                    helper(grid, i, j)
                    count += 1
        return count