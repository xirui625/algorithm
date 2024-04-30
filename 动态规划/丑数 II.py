#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   丑数 II.py
@Time    :   2024/04/30 16:17:23
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是质因子只包含 2、3 和 5 的正整数。

 

示例 1：

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
示例 2：

输入：n = 1
输出：1
解释：1 通常被视为丑数。
'''

# 解题思路：
# 根据题意，每个丑数都可以由其他较小的丑数通过乘以 222 或 333 或 555 得到。

# 所以，可以考虑使用一个优先队列保存所有的丑数，每次取出最小的那个，然后乘以 222 , 333 , 555 后放回队列。然而，这样做会出现重复的丑数。例如：

# 初始化丑数列表 [1]
# 第一轮： 1 -> 2, 3, 5 ，丑数列表变为 [1, 2, 3, 5]
# 第二轮： 2 -> 4, 6, 10 ，丑数列表变为 [1, 2, 3, 4, 6, 10]
# 第三轮： 3 -> 6, 9, 15 ，出现重复的丑数 6
# 为了避免重复，我们可以用三个指针 aaa , bbb, ccc ，分别表示下一个丑数是当前指针指向的丑数乘以 222 , 333 , 555 。

# 利用三个指针生成丑数的算法流程：

# 初始化丑数列表 resresres ，首个丑数为 111 ，三个指针 aaa , bbb, ccc 都指向首个丑数。
# 开启循环生成丑数：
# 计算下一个丑数的候选集 res[a]⋅2res[a] \cdot 2res[a]⋅2 , res[b]⋅3res[b] \cdot 3res[b]⋅3 , res[c]⋅5res[c] \cdot 5res[c]⋅5 。
# 选择丑数候选集中最小的那个作为下一个丑数，填入 resresres 。
# 将被选中的丑数对应的指针向右移动一格。
# 返回 resresres 的最后一个元素即可。


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = res[a] * 2, res[b] * 3, res[c] * 5
            res[i] = min(n2, n3, n5)
            if res[i] == n2: a += 1
            if res[i] == n3: b += 1
            if res[i] == n5: c += 1
        return res[-1]