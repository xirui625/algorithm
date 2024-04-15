#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 下午5:24
# @Author  : yangguoli
# @File    : 顺时针旋转矩阵.py
# @Software: PyCharm
#
# 有一个nxn整数矩阵，请编写一个算法，将矩阵顺时针旋转90度。
#
# 给定一个nxn的矩阵，和矩阵的阶数n,请返回旋转后的nxn矩阵。

class Solution:
    def rotateMatrix(self, mat, n):
        new_mat = [[0 * n] * n]
        for i in range(n):
            for j in range(n):
                new_mat[j][n-i-1] = mat[i][j]
        return new_mat
        # write code here