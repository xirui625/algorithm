#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   链表中的下一个更大节点.py
@Time    :   2024/04/29 17:38:38
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 206. 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        head = self.reverseList(head)
        ans = []
        st = []  # 单调栈（节点值）
        while head:
            while st and st[-1] <= head.val:
                st.pop()  # 弹出无用数据
            ans.append(st[-1] if st else 0)  # 栈顶就是第 i 个节点的下一个更大元素
            st.append(head.val)
            head = head.next
        return ans[::-1]  # 由于是倒着记录答案的，返回前要把答案反转

        