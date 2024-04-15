#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 下午6:23
# @Author  : yangguoli
# @File    : 螺旋矩阵.py
# @Software: PyCharm
class Solution:
    def spiralOrder(self , matrix ):
        res = []
        while matrix:
            res += matrix[0]
            matrix = list(map(list, zip(*matrix[1:])))[::-1]
            # matrix = list(map(list, zip(*matrix[1:])))[::-1]

            # matrix = list(zip(*matrix[1:]))[::-1]

        return res