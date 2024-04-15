#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:12
# @Author  : yangguoli
# @File    : 是否回文字符串.py
# @Software: PyCharm

class Solution:
    def judge(self , str ):
        newStr = str[::-1]
        if newStr == str:
            return True
        else:
            return False
        # write code here