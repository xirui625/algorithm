#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 下午10:16
# @Author  : yangguoli
# @File    : 合并两个有序数组.py
# @Software: PyCharm

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        如果从小到大合并，需要使用辅助数组，空间复杂度O(m+n)。
        因nums1后面已经预留出足够的空间，可以反过来从大到小，每次从2个数组末尾取最大的放到nums1末尾，直至1个数组为空。
        """
        # nums1[:] = sorted(nums1[:m] + nums2)
        # return nums1
        head = m + n - 1
        p1, p2 = m - 1, n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[head] = nums1[p1]
                p1 -= 1
            else:
                nums1[head] = nums2[p2]
                p2 -= 1
            head -= 1
        # nums2剩余元素复制过去
        while p2 >= 0:
            nums1[head] = nums2[p2]
            p2 -= 1
            head -= 1