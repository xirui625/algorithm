#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午4:54
# @Author  : yangguoli
# @File    : 是否回文.py
# @Software: PyCharm

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self , head ):
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        while head:
            if head.val != stack.pop().val:
                return False
            head = head.next
        return True
        # write code here