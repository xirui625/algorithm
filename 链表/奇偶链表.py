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
    def oddEvenList(self , head ):
        nodeList = []
        oddList = []
        evenList = []
        if not head:
            return head

        while head:
            nodeList.append(head.val)
            head = head.next
        for index in range(len(nodeList)):
            if index % 2 == 0:
                oddList.append(nodeList[index])
            else:
                evenList.append(nodeList[index])
        result = oddList + evenList
        cur = head = ListNode(0)
        for val in result:
            cur.next = ListNode(val)
            cur = cur.next
        return head.next

    # newHead1 = ListNode(0)
        # cur1 = newHead1
        # tail = None
        # newHead2 = ListNode(0)
        # cur2 = newHead2
        # for index, node in enumerate(stack1):
        #     if index % 2 == 0:
        #         cur1.next = node
        #         cur1 = cur1.next
        #         tail = cur1
        #     else:
        #         cur2.next = node
        #         cur2 = cur2.next
        # tail.next = newHead2.next
        # return newHead1.next




