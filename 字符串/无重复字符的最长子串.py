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
        max_len = 0  # 初始化最长不重复子串的长度
        ret = []  # 用于存储当前的不重复子串
        max_str = ''  # 最长不重复子串的字符串表示

        for i in s:
            if i not in ret:  # 如果字符 i 不在 ret 中，说明当前字符可以加入到不重复子串中
                ret.append(i)  # 将字符 i 加入到 ret 中
                if len(ret) > max_len:  # 更新最长不重复子串的长度和字符串表示
                    max_len = len(ret)
                    max_str = ''.join(ret)
            else:
                # 如果字符 i 已经在 ret 中，说明出现了重复字符，需要调整 ret 列表，
                # 直到 ret 中不再包含重复字符为止
                while i in ret:
                    ret.pop(0)  # 从 ret 的开头开始弹出字符，直到不重复
                ret.append(i)  # 将字符 i 加入到 ret 中

        # 打印最长的不重复子串
        print(max_str)
        return max_len  # 返回最长不重复子串的长度



if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring("abcabcbb")
