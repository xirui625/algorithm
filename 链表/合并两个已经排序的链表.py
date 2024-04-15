#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 上午11:31
# @Author  : yangguoli
# @File    : merge_list.py 合并两个已排序的链表
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge1(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return pHead1 or pHead2
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge1(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge2(pHead1, pHead2.next)
            return pHead2

    def Merge2(self, pHead1, pHead2):
        # write code here
        ret = cur = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        cur.next = pHead1 or pHead2
        return ret.next