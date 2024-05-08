#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午10:12
# @Author  : yangguoli
# @File    : 删除指定结点.py
# @Software: PyCharm
# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

# 返回删除后的链表的头节点。

# 示例 1:

# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
# 示例 2:

# 输入: head = [4,5,1,9], val = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

# 说明：

# 题目保证链表中节点的值互不相同
# 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def removeNode(self, head, num):
#         stack = []
#         while head:
#             if head.val != num:
#                 stack.append(head.val)
#             head = head.next
#         newHead = newTail = ListNode(stack[0])
#         for val in stack:
#             newTail.next = ListNode(val)
#             newTail = newTail.next
#         return newHead
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head

