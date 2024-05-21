#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   最短无序连续子数组.py
@Time    :   2024/04/29 18:16:16
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。
'''
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 先确定我们的小目标，原数组升序后的结果
        target = sorted(nums)
        # 定义头指针和尾指针
        left = 0
        right = len(nums)-1
        # 只要头指针下标小于尾指针，则继续循环
        while left<right:
            # 如果头指针指向的原数组元素与排序后数组元素值相等，就说明还没遇到乱序子数组
            if nums[left]==target[left]:
                # 头指针前进
                left += 1
            # 同理，相等则说明还没遇到乱序子数组的结尾
            if nums[right]==target[right]:
                # 尾指针向头指针方向前进
                right -= 1
            # 需头指针和尾指针位置分别都抵达乱序子数组首尾时，才满足退出条件
            if nums[left]!=target[left] and nums[right]!=target[right]:
                break
        # 如果因为不满足循环条件而退出，说明不存在乱序子数组，直接返回0
        if left>=right:
            return 0
        # 此处是满足退出循环条件的结果，因此返回乱序子数组的长度
        return right-left+1


