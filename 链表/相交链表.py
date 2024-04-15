#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   相交链表.py
@Time    :   2024/04/13 13:55:14
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''


# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# 图示两个链表在节点 c1 开始相交：

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a