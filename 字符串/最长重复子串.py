#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:58
# @Author  : yangguoli
# @File    : 最长重复子串.py 困难的，忽略掉
# @Software: PyCharm

# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

class Solution:
    def maxValue(self , s , k):
        l = res = 0
        while l < len(s) and l+k <= len(s):  #判断不超过索引
            if int(s[l:l+k]) > int(res):
                res = s[l:l+k]
            l += 1
        return int(res)