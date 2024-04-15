#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午5:26
# @Author  : yangguoli
# @File    : 删除有序链表中重复元素.py （不保留）
# @Software: PyCharm
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self , head ):
        if not head:
            return head
        tmp = ListNode(0)
        tmp.next = head
        cur  = tmp
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                data = cur.next.val
                while cur.next and cur.next.val == data:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return tmp.next
