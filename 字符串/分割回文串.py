#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   分割回文串.py
@Time    :   2024/04/30 16:30:24
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。
'''

# 首先，定义一个空列表 ans 用于存储所有可能的分割方案，以及一个空列表 path 用于存储当前路径中的子串。
# 获取字符串 s 的长度 n。
# 定义深度优先搜索函数 dfs，参数 i 表示当前处理的位置：
# 如果当前位置 i 到达字符串末尾 n，说明已经完成了一种分割方案，将当前路径 path 添加到结果列表 ans 中，并返回。
# 遍历从当前位置 i 开始到字符串末尾的所有可能的子串：
# 判断子串 s[i:j+1] 是否为回文串，如果是回文串，则将其添加到当前路径 path 中。
# 递归调用 dfs(j+1)，将 j+1 作为下一次搜索的起始位置，继续寻找下一个回文子串。
# 当递归返回后，需要将当前路径 path 中添加的子串弹出，恢复现场，以便尝试其他的分割方案。
# 调用深度优先搜索函数 dfs(0)，从字符串的起始位置开始搜索可能的分割方案。
# 返回结果列表 ans，其中存储了所有可能的分割方案。

from typing import List  # 导入List类型用于类型注解

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []  # 存储最终结果
        path = []  # 存储当前的回文子串分割路径
        n = len(s)  # 字符串的长度

        def dfs(i: int) -> None:
            if i == n:  # 如果索引 i 到达字符串末尾
                ans.append(path.copy())  # 复制当前路径并添加到结果中
                return
            for j in range(i, n):  # 枚举子串的结束位置 j
                t = s[i: j + 1]  # 取子串 s[i:j+1]
                if t == t[::-1]:  # 判断子串是否为回文
                    path.append(t)  # 如果是回文，将子串添加到当前路径中
                    dfs(j + 1)  # 递归处理子串的剩余部分
                    path.pop()  # 回溯，恢复现场

        dfs(0)  # 从字符串的起始位置开始进行深度优先搜索
        return ans  # 返回所有可能的回文分割结果


