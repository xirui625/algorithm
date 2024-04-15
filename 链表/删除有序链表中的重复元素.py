#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午5:08
# @Author  : yangguoli
# @File    : 删除有序链表中的重复元素.py 保留
# @Software: PyCharm
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。



class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return
        stack = []
        pre = head
        cur = head.next
        stack.append(head.val)
        while cur:
            if cur.val in stack:
                pre.next = cur.next
            else:
                stack.append(cur.val)
                pre = cur
            cur = cur.next
        return head

