#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:43
# @Author  : yangguoli
# @File    : 字符串变形.py
# @Software: PyCharm

class Solution:
    def trans(self, s, n):
        # write code here
        newStr = s.swapcase()
        if newStr.find(' ') == -1:
            return newStr
        tmp = newStr.split(' ')
        return ' '.join(tmp[::-1])
        # l = s.split(' ')  # 将原字符串按照空格分隔成list
        # l = l[::-1]  # 翻转list内的所有单词
        # s = ""
        # for letter in l:
        #     letter = letter.swapcase()  # 调整大小写
        #     s += letter  # 重新串成一个字符串
        #     s += ' '
        # return s[0:len(s) - 1]