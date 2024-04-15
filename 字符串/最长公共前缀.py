#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:27
# @Author  : yangguoli
# @File    : 最长公共前缀.py
# @Software: PyCharm

# 编写一个函数来查找字符串数组中的最长公共前缀。


class Solution:
    def longestCommonPrefix(self , strs ):
        list_len = len(strs)
        if list_len == 0 or strs == '':
            return ""
        new = strs[0]
        for i in range(1, list_len):
            while (strs[i].find(new) != 0):
                new = new[:-1]
        return new
    
# if __name__ == '__main__':
#     s = Solution()
#     print(s.longestCommonPrefix(["abca","abc","abca","abc","abcc"]))
class Solution:
    def longestCommonPrefix(self , strs ):
        length = len(strs)
        if not length:
            return ''
        prefix = strs[0]
        for i in range(1, length):
            while (strs[i].find(prefix) != 0):
                prefix = prefix[:-1]
        return prefix