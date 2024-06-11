#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午5:46
# @Author  : yangguoli
# @File    : 奇偶链表.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        # 分别用于存放奇数位置和偶数位置的节点值
        oddList = []
        evenList = []

        # 遍历链表，将节点值分别放入奇数列表和偶数列表
        index = 1
        while head:
            if index % 2 != 0:
                oddList.append(head.val)
            else:
                evenList.append(head.val)
            head = head.next
            index += 1

        # 合并奇数列表和偶数列表
        result = oddList + evenList

        # 构建新的链表
        dummy = cur = ListNode(0)
        for val in result:
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next
