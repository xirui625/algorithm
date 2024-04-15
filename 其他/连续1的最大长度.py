#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午1:56
# @Author  : yangguoli
# @File    : 连续1的最大长度.py
# @Software: PyCharm

class Soultion:
    def __init__(self):
        pass

    def solution(self, nums, n):
        if not nums:
            return
        zero_times = 0
        max_length = 0
        pre = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_times += 1
            while zero_times>n:
                if nums[pre] == 0:
                    zero_times -= 1
                pre += 1
            max_length = max(max_length, i-pre+1)
        return max_length

if __name__ == '__main__':
    nums = [0,1,0,1,1,0]
    s = Soultion()
    print s.solution(nums, 1)