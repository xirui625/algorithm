#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   字符串相加.py
@Time    :   2024/04/29 18:05:38
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""  # 用于存储相加后的结果
        i, j, carry = len(num1) - 1, len(num2) - 1, 0  # i 和 j 分别表示 num1 和 num2 的索引，carry 表示进位

        while i >= 0 or j >= 0:  # 当 num1 或 num2 还有剩余部分时继续循环
            n1 = int(num1[i]) if i >= 0 else 0  # 获取 num1 当前位的数字，如果超出索引范围，则为 0
            n2 = int(num2[j]) if j >= 0 else 0  # 获取 num2 当前位的数字，如果超出索引范围，则为 0
            tmp = n1 + n2 + carry  # 将当前位的两个数字与进位相加
            carry = tmp // 10  # 计算进位
            res = str(tmp % 10) + res  # 将当前位的结果拼接到 res 的前面
            i, j = i - 1, j - 1  # 移动到下一位

        return "1" + res if carry else res  # 如果最高位有进位，则在最前面加上 "1"，否则直接返回 res
