#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午2:48
# @Author  : yangguoli
# @File    : ring_head.py 求环的入口
# @Software: PyCharm
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 初始时，定义快慢指针都指向链表的头节点
        slow = fast = pHead
        
        # 使用快慢指针判断是否有环
        while fast and fast.next:
            slow = slow.next       # 慢指针每次移动一步
            fast = fast.next.next  # 快指针每次移动两步
            if slow == fast:       # 如果快慢指针相遇，说明链表中有环
                # 将其中一个指针重新指向链表头部，然后两个指针每次移动一步，再次相遇的位置即为环的入口节点
                fast = pHead
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow  # 返回环的入口节点
        
        return None  # 如果没有环，返回None
