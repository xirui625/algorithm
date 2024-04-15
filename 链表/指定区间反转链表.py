#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午10:36
# @Author  : yangguoli
# @File    : 指定区间反转链表.py
# @Software: PyCharm
from linked_list import ListNode


# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 


class Solution:
    def reverseBetween(self, head, left, right):

        dummy = ListNode(next=head)
        p0 = dummy
        #移动指针 p0 到第 left 位置的前一个节点
        for _ in range(1, left):
            p0 = p0.next
        pre = p0.next
        cur = p0.next.next
        #反转 left 到 right 位置之间的节点的指针
        for _ in range(left, right):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        # 区间内的前一个节点与反转后的链表的尾部连接起来了，连接尾
        p0.next.next = cur
        # 指定区间的前一个节点 p0 的 next 指针重新指向了区间内节点反转后的第一个节点 pre, 连接头
        p0.next = pre
        return dummy.next

