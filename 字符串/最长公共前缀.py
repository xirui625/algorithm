#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:27
# @Author  : yangguoli
# @File    : 最长公共前缀.py
# @Software: PyCharm

# 编写一个函数来查找字符串数组中的最长公共前缀。


class Solution:
    def longestCommonPrefix(self, strs):
        list_len = len(strs)
        
        # 如果列表为空或者列表中有空字符串，则直接返回空字符串
        if list_len == 0 or strs == '':
            return ""
        
        new = strs[0]  # 初始化前缀为第一个字符串
        
        # 遍历字符串列表中的每一个字符串
        for i in range(1, list_len):
            # 使用 while 循环，直到当前字符串以 new 开头
            while (strs[i].find(new) != 0):
                new = new[:-1]  # 如果不是以 new 开头，则减少 new 的长度
        
        return new  # 返回最长公共前缀

    
if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["abca","abc","abca","abc","abcc"]))