#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 下午8:46
# @Author  : yangguoli
# @File    : 平方根.py
# @Software: PyCharm

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        # 为了照顾到 1 把右边界设置为 x // 2 + 1
        right = x // 2 + 1
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left