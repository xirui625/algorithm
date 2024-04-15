#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午9:56
# @Author  : yangguoli
# @File    : 链表加1.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def plusOne(self , head ):
    #     stack1 = []
    #     stack2 = []
    #     while head:
    #         stack1.append(head.val)
    #         head = head.next
    #     top = stack1.pop() + 1
    #     ca = int(top / 10)
    #     stack2.append(int(top % 10))
    #     while stack1:
    #         num = stack1.pop()
    #         total = num + ca
    #         ca = int(total / 10)
    #         stack2.append(int(total % 10))
    #     if ca:
    #         stack2.append(ca)
    #     newHead = newTail = ListNode(stack2.pop())
    #     while stack2:
    #         newTail.next = ListNode(stack2.pop())
    #         newTail = newTail.next
    #     return newHead
    class Solution(object):
        def plusOne(self, head):
            st = []
            while head:
                st.append(head.val)
                head = head.next
            carry = 0
            dummy = ListNode(0)
            adder = 1
            while st or adder != 0 or carry > 0:
                digit = st.pop() if st else 0
                sum = digit + adder + carry
                carry = 1 if sum >= 10 else 0
                sum = sum - 10 if sum >= 10 else sum
                cur = ListNode(sum)
                cur.next = dummy.next
                dummy.next = cur
                adder = 0
            return dummy.next