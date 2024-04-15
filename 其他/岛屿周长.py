#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午2:47
# @Author  : yangguoli
# @File    : 岛屿周长.py
# @Software: PyCharm

# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

# 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

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
