#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:58
# @Author  : yangguoli
# @File    : 最长重复子串.py 困难的，忽略掉
# @Software: PyCharm

 
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
# class Solution:
#     def maxValue(self , s , k):
#         l = res = 0
#         while l < len(s) and l+k <= len(s):  #判断不超过索引
#             if int(s[l:l+k]) > int(res):
#                 res = s[l:l+k]
#             l += 1
#         return int(res)
def lengthOfLongestSubstring(s: str) -> int:
    # 初始化哈希集合，用于存储窗口中的字符
    seen = set()
    # 初始化两个指针和最长长度
    left = 0
    max_length = 0
    
    # 遍历字符串
    for right in range(len(s)):
        # 当遇到重复字符时，移动左指针以收缩窗口
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        # 将当前字符添加到哈希集合中
        seen.add(s[right])
        # 更新最长长度
        max_length = max(max_length, right - left + 1)
    
    return max_length

# 测试用例
print(lengthOfLongestSubstring("abcabcbb"))  # 输出: 3 ("abc")
print(lengthOfLongestSubstring("bbbbb"))     # 输出: 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))    # 输出: 3 ("wke")
print(lengthOfLongestSubstring(""))          # 输出: 0
print(lengthOfLongestSubstring("au"))        # 输出: 2 ("au")




# 给你一个字符串 s ，考虑其所有 重复子串 ：即 s 的（连续）子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。

# 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。

# 二分查找：我们在可能的重复子串长度上进行二分查找。初始区间是 [1, n-1]，其中 n 是字符串的长度。
# Rabin-Karp 滚动哈希：在每次二分查找中，使用 Rabin-Karp 算法检查是否存在某个长度的重复子串。

# search(length): 在字符串 s 中搜索长度为 length 的重复子串。
# 计算第一个子串的哈希值。
# 计算剩余子串的哈希值并检查是否有相同哈希值的子串。
# 初始化变量:
# n 是字符串的长度。
# a 是字符集的大小（26 个小写字母）。
# modulus 是哈希值的模数，用来防止哈希值溢出。
# 二分查找:
# 在长度范围 [1, n-1] 上进行二分查找，找到最大的长度。
# 每次二分查找中，调用 search 函数检查是否存在长度为 mid 的重复子串。
# 如果存在，更新 left 和 start。
# 如果不存在，缩小搜索范围。
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(length):
            # 计算第一个子串的哈希值
            h = 0
            for i in range(length):
                h = (h * a + ord(s[i])) % modulus
            seen = {h}
            # 计算 a^length % modulus
            aL = pow(a, length, modulus)
            
            for start in range(1, n - length + 1):
                # 计算下一个子串的哈希值
                h = (h * a - ord(s[start - 1]) * aL + ord(s[start + length - 1])) % modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1

        # 初始化变量
        n = len(s)
        a = 26  # 字符串中的字符种类数
        modulus = 2**63 - 1

        left, right = 1, n
        start = -1
        while left < right:
            mid = (left + right) // 2
            pos = search(mid)
            if pos != -1:
                left = mid + 1
                start = pos
            else:
                right = mid
        
        if start == -1:
            return ""
        else:
            return s[start:start + left - 1]

# 测试用例
print(Solution().longestDupSubstring("banana"))  # 输出: "ana"
print(Solution().longestDupSubstring("abcd"))    # 输出: ""

