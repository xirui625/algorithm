#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午4:23
# @Author  : yangguoli
# @File    : merge_more_list.py 合并K个已排序的链表
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# @param lists ListNode类一维数组
# @return ListNode类
#
class Solution:
    def mergeKLists(self , lists ):
        ret = []
        for head in lists:
            while head:
                ret.append(head.val)
                head = head.next
        ret.sort()
        head = ListNode(0)
        cur = head
        for val in ret:
            # node = ListNode(val)
            cur.next = ListNode(val)
            cur = cur.next
        return head.next