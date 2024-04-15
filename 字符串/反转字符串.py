#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   反转字符串.py
@Time    :   2024/04/08 17:41:02
@Author  :   yangguoli 
@Desc    :   编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """ 
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1

