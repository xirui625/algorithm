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
    def deleteDuplicates(self, head):
        if not head:
            return head  # 如果链表为空，直接返回

        tmp = ListNode(0)  # 创建一个临时节点 tmp，并将其 next 指针指向头节点 head
        tmp.next = head
        cur = tmp  # cur 指针初始化为 tmp，用于遍历链表

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                # 如果当前节点的值与下一个节点的值相等
                data = cur.next.val  # 记录重复的节点值
                # 删除所有值为 data 的节点，直到遇到不是 data 的节点为止
                while cur.next and cur.next.val == data:
                    cur.next = cur.next.next
            else:
                # 如果当前节点与下一个节点的值不相等，继续向后遍历
                cur = cur.next

        return tmp.next  # 返回处理后的链表，从 tmp 的下一个节点开始

