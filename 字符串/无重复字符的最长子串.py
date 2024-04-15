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
                #如果 i 已经在 ret 中，说明出现了重复字符，需要调整 ret 列表，直到 ret 中不再包含重复字符为止。这里使用了一个 while 循环，不断地从 ret 列表的开头弹出字符，直到 i 不再在 ret 中，然后再将 i 加入 ret
                while i in ret:
                    ret.pop(0)
                ret.append(i)
        print(max_str)
        return max_len


if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring("abcabcbb")
