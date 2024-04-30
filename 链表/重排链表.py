#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   重排链表.py
@Time    :   2024/04/29 18:09:07
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None

给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 876. 链表的中间结点
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 206. 反转链表
    # 将链表的后半部分逆序，得到逆序后的头节点 head2 = self.reverseList(mid)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        # 遍历链表的前半部分和逆序后的后半部分，依次交替插入节点。
        # 具体操作是将前半部分的下一个节点指向逆序后的后半部分的头节点，
        # 然后更新指针，继续进行操作，直到链表的前半部分遍历完毕。这样就完成了链表的重排。
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2
