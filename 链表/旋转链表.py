#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 下午11:00
# @Author  : yangguoli
# @File    : 旋转链表.py
# @Software: PyCharm

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        # 计算链表长度 n，同时找到旧尾节点
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        
        # 将链表形成环
        old_tail.next = head
        
        # 计算新的尾节点和新的头节点
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # 断开环
        new_tail.next = None
        
        return new_head


