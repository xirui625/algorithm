#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 上午11:59
# @Author  : yangguoli
# @File    : k_reverse.py
# @Software: PyCharm

class Solution:

    def __init__(self):
        self.stack = []
        # self.pre = None
        # self.next = None

    def reverseKGroup2(self, head, k):
        if not head:
            return
        cur = head
        while cur:
            self.stack.append(cur.val)
            cur = cur.next
        res = [self.stack[i:i + k] for i in range(0, len(self.stack), k)]
        result = []
        for item in res:
            if len(item) == k:
                result.extend(item[::-1])
            else:
                result.extend(item)
        cur = new_head = ListNode(result[0])
        for item in result:
            cur.next = ListNode(item)
            cur = cur.next
        return new_head

    def reverseKGroup(self , head , k):
        if k < 2:
            return head
        newHeads = cur = head
        pre = None
        while cur:
            next = cur.next
            self.stack.append(cur)
            if len(self.stack) == k:
                pre = self.help(pre, next)
                newHeads = cur if newHeads == head else newHeads
            cur = next
        return newHeads

    def help(self, left, right):
        cur = self.stack.pop()
        if left:
            left.next = cur
        while self.stack:
            next = self.stack.pop()
            cur.next = next
            cur = next
        cur.next = right
        return cur