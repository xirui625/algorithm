#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午2:58
# @Author  : yangguoli
# @File    : delete_n_node.py 删除链表的第N个节点
# @Software: PyCharm

class Solution:
    class Solution:
        #删除倒数第K个结点
        def removeNthFromEnd(self, head, k):
            if not head:
                return
            n = 0
            cur = head
            while cur:
                cur = cur.next
                n += 1
            if n == k:
                return head.next
            cur = head
            for i in range(n-k-1):
                cur = cur.next
            cur.next = cur.next.next
            return head


class Solution:
    # 找到倒数第K个结点
    def FindKthToTail(self , pHead , k ):
        first, second = pHead, pHead
        for i in range(k):
            if not first:
                return None
            first = first.next
        while first:
            first = first.next
            second = second.next
        return second
        # write code here

