#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 下午11:13
# @Author  : yangguoli
# @File    : 字符串排列.py
# @Software: PyCharm
# 输入一个长度为 n 字符串，打印出该字符串中字符的所有排列，你可以以任意顺序返回这个字符串数组。
# 例如输入字符串ABC,则输出由字符A,B,C所能排列出来的所有字符串ABC,ACB,BAC,BCA,CBA和CAB

# from itertools import combinations

# -*- coding:utf-8 -*-

class Solution:
    def Permutation(self, ss):
        # 计算字符串的长度
        length = len(ss)
        # 如果字符串长度小于等于1，直接返回该字符串
        if length <= 1:
            return ss
        
        # 初始化一个空列表，用来存放全排列结果
        ret = []
        
        # 遍历字符串
        for i in range(length):
            # 取出第一个字符
            firstStr = ss[i]
            # 递归求剩余字符的全排列
            for item in self.Permutation(ss[:i] + ss[i+1:]):
                # 拼接字符串
                tmp = firstStr + item
                # 判断拼接结果是否已经存在于结果列表中，如果不存在，则加入结果列表
                if tmp not in ret:
                    ret.append(tmp)
        
        # 返回全排列结果列表
        return ret

        # write code here

if __name__ == '__main__':
    s = Solution()
    print(s.Permutation(['a', 'b', 'c']))
