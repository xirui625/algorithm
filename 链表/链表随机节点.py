#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   链表随机节点.py
@Time    :   2024/04/29 17:36:47
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.attr = []
        while head:
            self.attr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.attr)