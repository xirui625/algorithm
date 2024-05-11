#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 下午6:23
# @Author  : yangguoli
# @File    : 螺旋矩阵.py
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# @Software: PyCharm

class Solution:
    def spiralOrder(self , matrix ):
        res = []
        while matrix:
            res += matrix[0]
            matrix = list(map(list, zip(*matrix[1:])))[::-1]
        return res