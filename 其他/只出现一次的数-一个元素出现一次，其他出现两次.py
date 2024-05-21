#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午10:57
# @Author  : yangguoli
# @File    : 只出现一次的数.py
# @Software: PyCharm


# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            # 使用位运算中的异或操作（^），将当前结果res与当前元素i进行异或运算，
            # 并将结果赋值给res。异或运算的特性是，相同数字异或结果为0，不同数字异或结果为该数字本身。
            res = res ^ i 
        return res