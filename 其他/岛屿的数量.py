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
            if not 0<=i<m or not 0<=j<n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            helper(grid, i-1, j)
            helper(grid, i+1, j)
            helper(grid, i, j-1)
            helper(grid, i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    helper(grid, i, j)
                    count += 1
        return count