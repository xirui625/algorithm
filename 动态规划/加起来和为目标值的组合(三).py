#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:02
# @Author  : yangguoli
# @File    : 加起来和为目标值的组合(三).py
# @Software: PyCharm

class Solution:
    def combination(self , k , n ):
        # write code here
        d = {0: 1}  # 初始化，累积和为0的情况已经出现了一次
        Sum = 0
        count = 0
        for p in range(len(n)):
            Sum += n[p]
            count += d.get(Sum - k, 0)
            d.setdefault(Sum, 0)
            d[Sum] += 1
        return count