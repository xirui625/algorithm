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
from itertools import combinations, permutations

class Solution:
    def Permutation(self, ss):
        if not ss:
            return

        ret = []

        print len(ss)
        for item in combinations(list(ss), len(ss)):
            print item
            ret.append(item)
#         print ret
        return ret
        # 递归法，问题转换为先固定第一个字符，求剩余字符的排列；求剩余字符排列时跟原问题一样。
        # 遍历字符串，固定可能出现在第一个位置的字符，作为第一个字符，后面剩下的字符串的组合用递归使用本函数的方式得到。
        # length = len(ss)
        # if length <= 1:
        #     return ss
        # ret = []
        # for i in range(length):
        #     firstStr = ss[i]
        #     for item in self.Permutation(ss[:i]+ss[i+1:]):
        #         tmp = firstStr + item
        #         if tmp not in ret:
        #             ret.append(tmp)
        # return ret
        # write code here

if __name__ == '__main__':
    # s = Solution()
    # print s.Permutation(['a', 'b', 'c'])
    for item in permutations(['a', 'b', 'c'], 3):
        print item