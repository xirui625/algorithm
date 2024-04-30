#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   整数拆分.py
@Time    :   2024/04/30 16:07:44
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。
'''

import math


# 拆分规则：
# 最优： 333 。把数字 nnn 可能拆为多个因子 333 ，余数可能为 0,1,20,1,20,1,2 三种情况。
# 次优： 222 。若余数为 222 ；则保留，不再拆为 1+11+11+1 。
# 最差： 111 。若余数为 111 ；则应把一份 3+13 + 13+1 替换为 2+22 + 22+2，因为 2×2>3×12 \times 2 > 3 \times 12×2>3×1


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)
