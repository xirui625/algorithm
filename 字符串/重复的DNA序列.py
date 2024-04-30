#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   重复的DNA序列.py
@Time    :   2024/04/29 17:44:13
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。

# 例如，"ACGAATTCCG" 是一个 DNA序列 。
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。

# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。
from collections import defaultdict


L = 10

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        cnt = defaultdict(int)
        # 遍历给定的 DNA 序列 s，由于要考虑长度为 L 的子序列，
        # 因此循环范围是 range(len(s) - L + 1)，保证最后一个子序列的起始位置不会超出序列的长度。
        for i in range(len(s) - L + 1):
            # 在每次循环中，从当前位置 i 开始，取长度为 L 的子序列 sub = s[i : i + L]。
            sub = s[i : i + L]
            # 将子序列 sub 添加到字典 cnt 中，并增加其出现次数计数。
            cnt[sub] += 1
            # 如果当前子序列 sub 的出现次数等于 2，说明它是一个重复出现的子序列，将其添加到结果列表 ans 中。
            if cnt[sub] == 2:
                ans.append(sub)
        return ans

