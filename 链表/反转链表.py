#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 上午11:08
# @Author  : yangguoli
# @File    : reverse_list.py 翻转单向双向链表
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class DoubleListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.last = None

class Solution:

    def __init__(self):
        pass

    # 返回ListNode
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            # 记录下一个结点
            next = cur.next
            # 改变指向
            cur.next = pre
            # 更新pre
            pre = cur
            # 更新cur
            cur = next
        return pre

    def ReverseDoubleList(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            cur.last = next
            pre = cur
            cur = next
        return pre
    

