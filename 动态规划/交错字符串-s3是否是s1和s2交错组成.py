#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   交错字符串.py
@Time    :   2024/04/30 16:41:03
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 
子字符串
：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。


'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 如果 s1 和 s2 的长度之和不等于 s3 的长度，则直接返回 False
        if len(s1) + len(s2) != len(s3):
            return False
        
        length2 = len(s2)
        # 初始化动态规划数组，dps[i] 表示 s1 和 s2 的前缀能否组成 s3 的前 i 个字符
        dps = [True] + [s2[:i] == s3[:i] for i in range(1, length2 + 1)]
        
        # 遍历 s1 的每个字符
        for index1, char1 in enumerate(s1):
            # 更新 dps[0]，即前缀 "" 能否组成 s3 的前 index1 个字符
            dps[0] = dps[0] and s3[index1] == char1
            # 遍历 s2 的每个字符
            for index2, char2 in enumerate(s2):
                index3 = index1 + index2 + 1
                # 更新 dps[index2 + 1]，即 s2 的前缀能否与 s1 的前 index1 个字符组成 s3 的前 index3 个字符
                dps[index2 + 1] = (char1 == s3[index3] and dps[index2 + 1]) or (char2 == s3[index3] and dps[index2])
        
        # 返回 dps[-1]，即 s1 和 s2 能否组成 s3
        return dps[-1]



