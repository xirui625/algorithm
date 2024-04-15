#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午10:44
# @Author  : yangguoli
# @File    : 数组中出现次数超过一半的数字.py
# @Software: PyCharm

class Solution:
    def majorityElement(self, nums):
        #排序之后，不管是什么情况，这个数组中点肯定是多数元素
        # nums.sort()
        # n = len(nums)
        # return nums[(n-1)//2]
        #方法二：摩尔投票法！O(N)和O(1)
        # 1.
        # 排序法思路很简单，排序好之后，由于众数超过元素个数的一半，所以中间位置一定为众数。
        # 2.
        # 摩尔投票法：两个先验知识！
        # a.设众数票数为1，非众数票数为 - 1，那么整个nums数组票数之和一定大于0
        # b.如果前几个数字票数和为0，那么后面所有数字的票数之和一定大于0，即后面数字的众数和之前一样。
        # 那么就可以假设数组第一个数字为众数，开始投票。如果一个区间内票数为0，那么这个区间就不考虑了。

        vote = 0
        for num in nums:
            if vote == 0:
                x = num
            if num == x:
                vote += 1
            else: vote -= 1
        return x