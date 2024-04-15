#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午2:48
# @Author  : yangguoli
# @File    : ring_head.py 求环的入口
# @Software: PyCharm
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow = fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while pHead != slow:
                    slow = slow.next
                    pHead = pHead.next
                return slow
        return None