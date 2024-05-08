#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   组合总和-相加之和为 n 的 k 个数的组合.py
@Time    :   2024/04/29 17:01:18
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

# 只使用数字1到9
# 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # i 表示当前处理的数字，s 表示当前剩余的和
        def dfs(i: int, s: int):
            if s == 0:
                if len(t) == k:
                    ans.append(t[:])
                return
            # 如果当前数字 i 超过 9（因为数字范围是从 1 到 9），或者当前数字 i 大于剩余和 s，或者当前组合长度已经达到了 k，则直接返回，结束当前分支的搜索
            if i > 9 or i > s or len(t) >= k:
                return
            # 对于当前数字 i，从 i 开始遍历到 9
            for j in range(i, 10):
                t.append(j)
                dfs(j + 1, s - j)
                t.pop()
        # 结果列表 ans 和临时组合 t
        ans = []
        t = []
        dfs(1, n)
        return ans
