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
        if head.val == val:
            return head.next  # 如果要删除的节点是头节点，直接返回头节点的下一个节点

        pre, cur = head, head.next  # 初始化前驱节点 pre 和当前节点 cur
        while cur and cur.val != val:
            pre, cur = cur, cur.next  # 遍历链表，找到值为 val 的节点或者到达链表尾部

        if cur:  # 如果找到了值为 val 的节点
            pre.next = cur.next  # 删除该节点，即将前驱节点 pre 的 next 指针指向当前节点 cur 的下一个节点

        return head  # 返回头节点


