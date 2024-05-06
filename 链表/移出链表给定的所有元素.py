#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   移出链表元素.py
@Time    :   2024/05/06 18:29:34
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head) #添加一个虚拟节点
        cur = dummy_head
        while(cur.next!=None):
            if(cur.next.val == val):
                cur.next = cur.next.next #删除cur.next节点
            else:
                cur = cur.next
        return dummy_head.next