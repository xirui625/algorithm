#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   最大数.py
@Time    :   2024/05/08 23:29:04
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

from functools import cmp_to_key

class Solution:
    def helper(self, num1, num2):
        # 将两个数字转化为字符串，并比较拼接后的大小
        if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
            return -1
        else:
            return 1

    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(self.helper))
        ret = ''.join(map(str, nums))
        return '0' if ret[0] == '0' else ret