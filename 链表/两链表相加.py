#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午3:41
# @Author  : yangguoli
# @File    : add_link_list.py 两链表相加
# @Software: PyCharm

# 两数相加 II
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addInList(self, head1, head2):
        stack1 = []
        stack2 = []
        # l1入栈
        while head1:
            stack1.append(head1.val)
            head1 = head1.next
        while head2:
            stack2.append(head2.val)
            head2 = head2.next

        node = pre = None
        carry = 0

        while stack1 and stack2:
            num = stack1.pop() + stack2.pop() + carry
            # 求进位数
            carry = int(num / 10)
            tmp = num % 10
            pre = node
            node = ListNode(tmp)
            node.next = pre
            # head = node

        s = stack1 if stack1 else stack2
        while s:
            num = s.pop() + carry
            carry = int(num / 10)
            tmp = num % 10
            pre = node
            node = ListNode(tmp)
            node.next = pre
            # head = node

        if carry == 1:
            pre = node
            node = ListNode(carry)
            node.next = pre
            # head = node
        return node
    


# 两数相加
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。




