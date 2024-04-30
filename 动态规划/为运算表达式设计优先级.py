#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   为运算表达式设计优先级.py
@Time    :   2024/04/30 16:34:34
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。

生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 104 。

 

示例 1：

输入：expression = "2-1-1"
输出：[0,2]
解释：
((2-1)-1) = 0 
(2-(1-1)) = 2
示例 2：

输入：expression = "2*3-4*5"
输出：[-34,-14,-10,-10,10]
解释：
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''

# from functools import lru_cache: 这一行代码导入了functools模块中的lru_cache装饰器，该装饰器用于缓存函数的结果，以提高函数的性能。
# class Solution:: 这里定义了一个名为Solution的类，该类包含了一个方法diffWaysToCompute，用于计算表达式中不同运算顺序可能得到的结果。
# @lru_cache(): 这是lru_cache装饰器的应用，用于对diffWaysToCompute方法进行结果缓存。
# def diffWaysToCompute(self, input):: 这是diffWaysToCompute方法的定义，它接受一个字符串input作为参数，表示要计算的表达式。
# ans = list(): 这一行创建了一个空列表ans，用于存储计算结果。
# for i in range(len(input)):: 这是一个循环，遍历输入字符串input中的每个字符。
# c = input[i]: 在循环中，将当前字符存储在变量c中。
# if c in "+-*":: 这个条件判断语句检查当前字符是否是运算符（加号、减号或乘号）。
# le = self.diffWaysToCompute(input[:i]): 这一行调用了diffWaysToCompute方法递归地计算当前运算符左边部分的可能值，并将结果存储在变量le中。
# ri = self.diffWaysToCompute(input[i+1:]): 这一行调用了diffWaysToCompute方法递归地计算当前运算符右边部分的可能值，并将结果存储在变量ri中。
# if c == "+":, elif c == "-":, else:: 这些条件语句根据当前运算符执行相应的运算操作，并将结果添加到ans列表中。
# if not ans:: 这个条件语句检查ans列表是否为空，如果为空，则表示当前输入字符串中没有运算符，直接将输入字符串转换为整数并将其添加到ans列表中。
# return ans: 最后，返回存储了所有可能计算结果的ans列表。

from functools import lru_cache #使用这个可以尽量提高递归算法的效率
class Solution:
	@lru_cache()
	def diffWaysToCompute(self,input):
		ans=list()
		for i in range(len(input)):
			c=input[i]
			if c in "+-*":
				le=self.diffWaysToCompute(input[:i]) #左边部分可能的值
				ri=self.diffWaysToCompute(input[i+1:]) #右边部分可能的值
				if c=="+": #对应着三种运算符的笛卡尔积
					ans.extend(x+y for x in le for y in ri)
				elif c=="-":
					ans.extend(x-y for x in le for y in ri)
				else:
					ans.extend(x*y for x in le for y in ri)
		if not ans: #说明当前的input中是没有运算符的
			ans.append(int(input))
		return ans




