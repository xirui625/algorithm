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
        # 初始化前一个节点为空
        pre = None
        # 当前节点指向链表的头节点
        cur = head
        # 循环遍历链表节点
        while cur:
            # 记录当前节点的下一个节点
            nxt = cur.next
            # 将当前节点的next指针指向前一个节点
            cur.next = pre
            # 更新前一个节点为当前节点
            pre = cur
            # 更新当前节点为下一个节点
            cur = nxt
        # 返回反转后的头节点
        return pre

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 将链表反转
        head = self.reverseList(head)
        # 初始化答案列表
        ans = []
        # 初始化单调栈（节点值）
        st = []  
        # 遍历反转后的链表
        while head:
            # 移除单调栈中小于当前节点值的节点
            while st and st[-1] <= head.val:
                st.pop()  
            # 栈顶就是第 i 个节点的下一个更大元素
            ans.append(st[-1] if st else 0)  
            # 将当前节点值加入单调栈
            st.append(head.val)
            # 移动到下一个节点
            head = head.next
        # 由于是倒着记录答案的，返回前要把答案反转
        return ans[::-1]


        