#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 下午4:29
# @Author  : yangguoli
# @File    : 打家劫舍.py
# @Software: PyCharm

# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# cur, pre = max(pre+num, cur), cur

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cur：当前房屋能够获取的最大金额。
        # pre：上一个房屋能够获取的最大金额。
        # 如果选择偷窃当前房屋，则不能偷窃上一个房屋最大金额为 pre + num。
        # 如果选择不偷窃当前房屋，则当前房屋能够获取的最大金额与上一个房屋相同, cur
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur

        # write code here