#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午10:12
# @Author  : yangguoli
# @File    : 删除指定结点.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def removeNode(self, head, num):
#         stack = []
#         while head:
#             if head.val != num:
#                 stack.append(head.val)
#             head = head.next
#         newHead = newTail = ListNode(stack[0])
#         for val in stack:
#             newTail.next = ListNode(val)
#             newTail = newTail.next
#         return newHead
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head

