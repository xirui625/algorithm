#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   最大正方形.py
@Time    :   2024/04/30 16:18:15
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
示例 1：

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
'''

# 要解决这个问题，我们可以使用动态规划。我们将创建一个辅助二维数组 dp，其中 dp[i][j] 表示以 matrix[i][j] 为右下角的最大正方形的边长。

# 动态规划步骤
# 如果 matrix[i][j] 为 '0'，则 dp[i][j] 为 0，因为不能形成正方形。
# 如果 matrix[i][j] 为 '1'，则 dp[i][j] 为其上方、左方和左上方的最小值加 1，即 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1。
# 边界条件
# 当 i 或 j 为 0 时，dp[i][j] 直接等于 matrix[i][j]，因为它们无法再延展形成更大的正方形。

from typing import List

class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        # 初始化行数和列数
        rows, cols = len(matrix), len(matrix[0])
        # 创建 dp 数组并初始化为 0
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0  # 最大正方形的边长

        # 遍历矩阵
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    # 如果是第一行或第一列，dp[i][j] = 1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 状态转移方程
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # 更新最大边长
                    max_side = max(max_side, dp[i][j])

        # 返回最大正方形的面积
        return max_side * max_side

