#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午8:54
# @Author  : yangguoli
# @File    : 两两交换链表结点.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def swapLinkedPair(self , head ):
        stack = []
        new_h = tmp = ListNode(0)
        cur = head
        while cur:
            stack.append(cur.val)
            if len(stack) == 2:
                while stack:
                    tmp.next = ListNode(stack.pop())
                    tmp = tmp.next
            cur = cur.next
        if stack:
            tmp.next = ListNode(stack.pop())
            tmp = tmp.next
        return new_h.next


class Solution:
    def swapLinkedPair(self , head ):
        if not head:
            return 
        stack = []
        new_head = tmp = ListNode(0)
        cur = head
        while cur:
            stack.append(cur.val)
            if len(stack) == 2:
                while stack:
                    node = ListNode(stack.pop())
                    tmp.next = node
                    tmp = tmp.next
            cur = cur.next
        while stack:
            node = ListNode(stack.pop())
            tmp.next = node
            tmp = tmp.next
        return new_head.next