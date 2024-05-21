#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   回文子串-字符串中有多少个回文子字符串.py
@Time    :   2024/05/21 11:43:36
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(s, left, right):
            count = 0
            # 当左右指针在合法范围内且左右字符相同时，扩展回文
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1  # 发现一个回文子串，计数加一
                left -= 1   # 左指针向左移动
                right += 1  # 右指针向右移动
            return count

        total_count = 0
        # 遍历每个字符，考虑奇数长度和偶数长度的回文
        for i in range(len(s)):
            total_count += expandAroundCenter(s, i, i)       # 奇数长度回文子串
            total_count += expandAroundCenter(s, i, i + 1)   # 偶数长度回文子串

        return total_count
    
# 返回所有的回文子串
def findAllPalindromicSubstrings(s: str):
    def expandAroundCenter(s, left, right):
        palindromes = []
        # 当左右指针在合法范围内且左右字符相同时，扩展回文
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right + 1])  # 收集回文子串
            left -= 1   # 左指针向左移动
            right += 1  # 右指针向右移动
        return palindromes

    result = []
    # 遍历每个字符，考虑奇数长度和偶数长度的回文
    for i in range(len(s)):
        result.extend(expandAroundCenter(s, i, i))       # 奇数长度回文子串
        result.extend(expandAroundCenter(s, i, i + 1))   # 偶数长度回文子串

    return result

# 测试用例
print(findAllPalindromicSubstrings("abc"))    
# 输出: ['a', 'b', 'c']
print(findAllPalindromicSubstrings("aaa"))    
# 输出: ['a', 'a', 'a', 'aa', 'aa', 'aaa']
print(findAllPalindromicSubstrings("racecar")) 
# 输出: ['r', 'a', 'c', 'e', 'c', 'a', 'r', 'cec', 'aceca', 'racecar']
print(findAllPalindromicSubstrings("level"))   
# 输出: ['l', 'e', 'v', 'e', 'l', 'eve', 'ele', 'level']
print(findAllPalindromicSubstrings(""))        
# 输出: []
print(findAllPalindromicSubstrings("a"))       
# 输出: ['a']



