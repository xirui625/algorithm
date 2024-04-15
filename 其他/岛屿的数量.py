#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午2:44
# @Author  : yangguoli
# @File    : 岛屿的数量.py
# @Software: PyCharm

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