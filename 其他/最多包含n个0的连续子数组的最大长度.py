#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午1:56
# @Author  : yangguoli
# @File    : 最多包含n个0的连续子数组的最大长度.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        pass

    def solution(self, nums, n):
        # 如果输入数组为空，则直接返回
        if not nums:
            return
        
        zero_times = 0  # 记录当前窗口内0的个数
        max_length = 0  # 记录最大长度
        pre = 0  # 记录窗口的起始位置
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_times += 1  # 如果遇到0，zero_times加1
            
            # 当0的个数超过n时，缩小窗口，直到zero_times <= n
            while zero_times > n:
                if nums[pre] == 0:
                    zero_times -= 1  # 窗口左边界右移，若遇到0，则zero_times减1
                pre += 1  # 窗口左边界右移
            
            max_length = max(max_length, i - pre + 1)  # 更新最大长度
        
        return max_length


