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

# 创建一个数组 dp，其中 dp[i] 表示将整数 i 拆分成至少两个正整数的和时，这些整数的最大乘积。
# 初始化 dp[1] 为 1，因为将 1 拆分为两个正整数是不可能的。
# 对于每个整数 i，我们尝试将其拆分成两个部分 j 和 i-j，并更新 dp[i]。
# 更新公式为：dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))。


# 初始化特殊情况：

# 当 n 为 2 或 3 时，直接返回结果，因为这些情况可以手动处理。
# 初始化 dp 数组：

# 初始化 dp 数组，其中 dp[i] 表示将整数 i 拆分成至少两个正整数的和时，这些整数的最大乘积。
# 动态规划计算每个整数的最大乘积：

# 外层循环遍历从 4 到 n 的每个整数。
# 内层循环遍历从 1 到 i//2 的每个整数 j，尝试将 i 拆分成 j 和 i-j 两部分，更新 dp[i]。
# 返回结果：

# 最终返回 dp[n] 即为最大乘积。


def integer_break(n: int) -> int:
    # 如果 n 是 2 或 3，直接返回结果
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    # 初始化 dp 数组
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    # 动态规划计算每个整数的最大乘积
    for i in range(4, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], dp[j] * dp[i - j])
    
    return dp[n]

# 测试用例
print(integer_break(2))  # 输出: 1
print(integer_break(10)) # 输出: 36
print(integer_break(4))  # 输出: 4
print(integer_break(6))  # 输出: 9

