#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午2:58
# @Author  : yangguoli
# @File    : delete_n_node.py 删除链表的第N个节点
# @Software: PyCharm

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n < 1:
            return head
        # 计算链表的长度
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        # 特殊情况处理：如果要删除的是头节点
        if length == n:
            return head.next
        cur = head
        # 找到要删除节点的前一个节点
        for i in range(length - n -1):
            cur = cur.next
        # 删除节点
        cur.next = cur.next.next
        return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy #快指针
        slow = dummy # 慢指针
        # 快指针先向前移 n+1步
        for _ in range(n + 1):
            fast = fast.next
        # 同时移动快慢指针，知道快指针到达链表末尾
        while fast is not None:
            fast = fast.next
            slow = slow.next
        # 此时的慢指针指向的就是要删除结点的前一个结点
        slow.next = slow.next.next
        # 此时虚拟头结点的下一个结点就是链表的头结点
        return dummy.next



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


