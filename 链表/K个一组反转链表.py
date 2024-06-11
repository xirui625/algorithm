#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 上午11:59
# @Author  : yangguoli
# @File    : k_reverse.py
# @Software: PyCharm

# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# 困难程度，先忽略

class Solution:
    def __init__(self):
        self.stack = []  # 初始化一个空栈，用于存储待反转的节点

    def reverseKGroup(self, head, k):
        if k < 2:
            return head  # 如果 k 小于 2，直接返回头节点，不需要反转

        newHeads = cur = head  # 初始化指向新反转链表头节点和当前节点的指针
        pre = None  # 初始化前一个反转段的尾节点

        while cur:
            next_node = cur.next  # 保存当前节点的下一个节点

            self.stack.append(cur)  # 将当前节点压入栈中，准备反转

            if len(self.stack) == k:  # 如果栈中节点数达到 k，进行反转操作
                pre = self.reverse(pre, next_node)  # 反转当前段，并与前一段连接
                newHeads = cur if newHeads == head else newHeads  # 更新新链表头节点

            cur = next_node  # 移动到下一个节点

        return newHeads  # 返回新链表的头节点

    def reverse(self, left, right):
        cur = self.stack.pop()  # 弹出栈顶节点作为新的反转段头节点

        if left:
            left.next = cur  # 将前一段的尾节点连接到新的反转段头节点

        while self.stack:
            next_node = self.stack.pop()  # 从栈中依次弹出节点，进行反转操作
            cur.next = next_node  # 当前节点指向下一个节点
            cur = next_node  # 移动当前节点指针

        cur.next = right  # 将反转段的尾节点连接到下一段

        return cur  # 返回反转段的尾节点
