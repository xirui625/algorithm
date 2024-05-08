#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   原子的数量.py
@Time    :   2024/05/08 16:29:31
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个字符串化学式 formula ，返回 每种原子的数量 。

原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。

例如，"H2O" 和 "H2O2" 是可行的，但 "H1O2" 这个表达是不可行的。
两个化学式连在一起可以构成新的化学式。

例如 "H2O2He3Mg4" 也是化学式。
由括号括起的化学式并佐以数字（可选择性添加）也是化学式。

例如 "(H2O2)" 和 "(H2O2)3" 是化学式。
返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

 

示例 1：

输入：formula = "H2O"
输出："H2O"
解释：原子的数量是 {'H': 2, 'O': 1}。
示例 2：

输入：formula = "Mg(OH)2"
输出："H2MgO2"
解释：原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
示例 3：

输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
'''
import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # 使用栈来处理带括号的情况
        stack = [collections.Counter()]  # 初始化一个栈，存储原子计数器，初始时压入一个空的计数器
        i = 0  # 初始化字符串索引
        n = len(formula)  # 获取字符串长度
        while i < n:
            if formula[i] == '(':  # 如果遇到左括号
                stack.append(collections.Counter())  # 入栈一个空的计数器
                i += 1  # 移动索引到下一个字符
            elif formula[i] == ')':  # 如果遇到右括号
                top = stack.pop()  # 出栈栈顶的计数器
                i += 1  # 移动索引到右括号的下一个字符
                i_start = i  # 记录右括号后面数字的起始索引
                while i < n and formula[i].isdigit():  # 读取右括号后面的数字
                    i += 1
                count = int(formula[i_start:i] or 1)  # 确定重复次数，如果没有数字默认为1
                for atom, cnt in top.items():  # 更新上一层计数器的原子数量
                    stack[-1][atom] += cnt * count
            else:  # 如果遇到原子符号
                i_start = i  # 记录原子符号的起始索引
                i += 1  # 移动索引到下一个字符
                while i < n and formula[i].islower():  # 读取原子名的小写字母（如果有）
                    i += 1
                atom = formula[i_start:i]  # 获取原子名
                i_start = i  # 记录原子数量的起始索引
                while i < n and formula[i].isdigit():  # 读取原子后面的数字
                    i += 1
                count = int(formula[i_start:i] or 1)  # 确定原子数量，如果没有数字默认为1
                stack[-1][atom] += count  # 更新当前计数器中的原子数量
        # 构造结果字符串，按字典序排序
        result = ''
        for atom, count in sorted(stack[-1].items()):
            result += atom
            if count > 1:
                result += str(count)
        return result

