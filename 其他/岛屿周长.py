#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午2:47
# @Author  : yangguoli
# @File    : 岛屿州长.py
# @Software: PyCharm

class Solution(object):
    def islandPerimeter(self, grid):
        m, n = len(grid), len(grid[0])
        C = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    C += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        C -= 1
                    if i + 1 < m and grid[i + 1][j] == 1:
                        C -= 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        C -= 1
                    if j + 1 < n and grid[i][j + 1] == 1:
                        C -= 1
        return C
