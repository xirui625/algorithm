#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:02
# @Author  : yangguoli
# @File    : 加起来和为目标值的组合(三).py
# @Software: PyCharm

class Solution:
    def combination(self, k, n):
        d = {0: 1}  # 使用字典来记录累积和出现的次数，初始化累积和为0的情况出现了一次
        Sum = 0      # 初始化累积和
        count = 0    # 计数器，用于记录符合条件的连续子数组个数
        
        # 遍历数组 n
        for p in range(len(n)):
            Sum += n[p]  # 计算当前的累积和
            
            # 统计累积和为 Sum - k 的次数，加到 count 中
            count += d.get(Sum - k, 0)
            
            # 更新累积和的次数记录
            d.setdefault(Sum, 0)
            d[Sum] += 1
        
        return count
