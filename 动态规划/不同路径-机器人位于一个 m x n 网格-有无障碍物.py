#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午1:54
# @Author  : yangguoli
# @File    : 不同路径的数目一.py
# @Software: PyCharm
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

# 问总共有多少条不同的路径？
# dp[i][j] 代表从起点到达位置 (i, j) 的不同路径数量

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化一个 m 行 n 列的二维数组 dp，初始值全部为 0
        dp = [[0 for i in range(n)] for i in range(m)]
        
        # 遍历二维数组的每一个位置
        for i in range(m):
            for j in range(n):
                # 如果在起点位置 (0, 0)，路径数量设为 1
                if i == 0 and j == 0:
                    dp[i][j] = 1
                # 如果在第一行（但不是起点），路径数量等于左边格子的路径数量
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                # 如果在第一列（但不是起点），路径数量等于上边格子的路径数量
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                # 其他位置的路径数量等于上边格子和左边格子的路径数量之和
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # 返回右下角的路径数量，即所有可能的路径数量
        return dp[-1][-1]

    
    
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

# 网格中的障碍物和空位置分别用 1 和 0 来表示
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 获取网格的行数 m 和列数 n
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 初始化一个 m 行 n 列的二维数组 dp，初始值全部为 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 遍历二维数组的每一个位置
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:  # 如果当前位置是障碍物
                    dp[i][j] = 0  # 路径数量为 0
                else:
                    # 如果在起点位置 (0, 0)，且无障碍物，路径数量设为 1
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    # 如果在第一行（但不是起点），且无障碍物，路径数量等于左边格子的路径数量
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                    # 如果在第一列（但不是起点），且无障碍物，路径数量等于上边格子的路径数量
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j]
                    # 其他位置的路径数量等于上边格子和左边格子的路径数量之和
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # 返回右下角的路径数量，即所有可能的路径数量
        return dp[-1][-1]
