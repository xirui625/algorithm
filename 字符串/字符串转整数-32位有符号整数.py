#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   字符串转整数.py
@Time    :   2024/05/21 13:30:34
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。

# 函数 myAtoi(string s) 的算法如下：

# 空格：读入字符串并丢弃无用的前导空格（" "）
# 符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
# 转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
# 舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
# 返回整数作为最终结果。


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # 1. 去掉前导空格
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. 处理符号
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # 3. 转换数字部分
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # 检查是否会超出范围
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        
        return sign * result

# 测试用例
print(myAtoi("42"))             # 输出: 42
print(myAtoi("   -42"))         # 输出: -42
print(myAtoi("4193 with words")) # 输出: 4193
print(myAtoi("words and 987"))   # 输出: 0
print(myAtoi("-91283472332"))   # 输出: -2147483648 (超出下限)
print(myAtoi("91283472332"))    # 输出: 2147483647 (超出上限)
print(myAtoi("   +0 123"))      # 输出: 0


