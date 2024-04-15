#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 下午9:27
# @Author  : yangguoli
# @File    : 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。


# @Software: PyCharm

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        ret = []
        max_str = ''
        for i in s:
            if i not in ret:
                ret.append(i)
                if len(ret) > max_len:
                    max_len = len(ret)
                    max_str = ''.join(ret)
            else:
                while i in ret:
                    ret.pop(0)
                ret.append(i)
        print(max_str)
        return max_len


if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring("abcabcbb")
