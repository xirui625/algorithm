#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   盛最多水的容器.py
@Time    :   2024/05/01 17:12:00
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
'''
class Solution:
# i, j, res = 0, len(height) - 1, 0：初始化两个指针 i 和 j，分别指向数组 height 的第一个和最后一个元素，同时初始化变量 res 用于存储最大储水量，初始值为 0。
# while i < j:：使用一个 while 循环，当 i 小于 j 时，执行以下操作：
# if height[i] < height[j]:：如果第 i 个柱子的高度小于第 j 个柱子的高度，说明以第 i 个柱子为左边界形成的容器的高度受限于第 i 个柱子的高度，因此容器的容量取决于第 i 个柱子的高度乘以两个柱子之间的距离 (j - i)。
# res = max(res, height[i] * (j - i))：更新 res 的值为当前 res 和通过第 i 个柱子和第 j 个柱子形成的容器的容量的较大值。
# i += 1：移动指针 i，将其指向下一个柱子，继续检查下一个可能的容器。
# else:：如果第 i 个柱子的高度不小于第 j 个柱子的高度，说明以第 j 个柱子为右边界形成的容器的高度受限于第 j 个柱子的高度，因此容器的容量同样取决于第 j 个柱子的高度乘以两个柱子之间的距离 (j - i)。
# res = max(res, height[j] * (j - i))：更新 res 的值为当前 res 和通过第 i 个柱子和第 j 个柱子形成的容器的容量的较大值。
# j -= 1：移动指针 j，将其指向上一个柱子，继续检查下一个可能的容器。
# return res：返回最终计算出的最大储水量。
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

