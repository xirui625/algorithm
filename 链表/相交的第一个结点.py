#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午3:22
# @Author  : yangguoli
# @File    : intersect_node.py 两链表相交问题
# @Software: PyCharm

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 两个无环链表相交结点
        if not pHead1 or not pHead2:
            return None
        cur1 = pHead1
        cur2 = pHead2
        n = 0
        while cur1:
            n += 1
            cur1 = cur1.next
        while cur2:
             n -= 1
             cur2 = cur2.next
        if cur1 != cur2:
            return None
        cur1 = pHead1 if n > 0 else pHead2
        cur2 = pHead2 if cur1 == pHead1 else pHead1
        n = abs(n)
        while n:
            cur1 = cur1.next
            n -= 1
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1

    def FindFirstCommonNode2(self, pHead1, pHead2):
        # 两个有环链表相交结点
        if not pHead1 or not pHead2:
            return None
        cur1 = pHead1
        cur2 = pHead2
        n = 0
        while cur1:
            n += 1
            cur1 = cur1.next
        while cur2:
             n -= 1
             cur2 = cur2.next
        if cur1 != cur2:
            return None
        cur1 = pHead1 if n > 0 else pHead2
        cur2 = pHead2 if cur1 == pHead1 else pHead1
        n = abs(n)
        while n:
            cur1 = cur1.next
            n -= 1
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1