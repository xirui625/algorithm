#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午11:23
# @Author  : yangguoli
# @File    : 矩阵的最小路径和.py
# @Software: PyCharm

# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。


from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 获取网格的行数和列数
        m, n = len(grid), len(grid[0])
        
        # 创建一个与 grid 相同大小的二维数组 dp，用于存储路径和
        dp = [[0 for i in range(n)] for i in range(m)]
        
        # 遍历网格的每个元素
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    # 起点位置，路径和就是起点值
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    # 第一行，只能从左边到达
                    dp[0][j] = dp[0][j-1] + grid[0][j]
                elif j == 0:
                    # 第一列，只能从上边到达
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                else:
                    # 其他位置，可以从左边或者上边到达，取路径和较小的那个
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        # 返回右下角的路径和，即最小路径和
        return dp[-1][-1]

# 测试用例
def test_minPathSum():
    solution = Solution()
    assert solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7, "测试用例1失败"
    assert solution.minPathSum([[1,2,3],[4,5,6]]) == 12, "测试用例2失败"
    print("所有测试用例通过!")

# 执行测试用例
test_minPathSum()
