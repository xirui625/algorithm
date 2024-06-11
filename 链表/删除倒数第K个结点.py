#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午2:58
# @Author  : yangguoli
# @File    : delete_n_node.py 删除链表的第N个节点
# @Software: PyCharm

class Solution:
    def removeNthFromEnd(self, head, k):
        if not head:
            return None
        
        # 计算链表的长度
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        
        # 特殊情况处理：如果要删除的是头节点
        if n == k:
            return head.next
        
        # 找到要删除节点的前一个节点
        cur = head
        for i in range(n - k - 1):
            cur = cur.next
        
        # 删除节点
        cur.next = cur.next.next
        
        return head



class Solution:
    def FindKthToTail(self, pHead, k):
        # 定义两个指针，都指向链表的头节点
        first, second = pHead, pHead
        
        # 第一个指针先走 k 步
        for i in range(k):
            if not first:  # 处理 k 大于链表长度的情况
                return None
            first = first.next
        
        # 第一个指针走到末尾时，第二个指针即为倒数第 k 个节点
        while first:
            first = first.next
            second = second.next
        
        return second


