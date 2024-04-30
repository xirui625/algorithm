#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   电话号码的字母组合.py
@Time    :   2024/04/29 16:34:20
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n  # 本题 path 长度固定为 n
        def dfs(i: int) -> None:
            if i == n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i] = c  # 直接覆盖
                dfs(i + 1)
        dfs(0)
        return ans
        