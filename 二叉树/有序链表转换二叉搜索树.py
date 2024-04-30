#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   有序链表转换二叉搜索树.py
@Time    :   2024/04/29 18:34:20
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        def helper(l):
            if not l:
                return 
            mid = len(l) // 2
            node = TreeNode(l[mid])
            node.left = helper(l[:mid])
            node.right = helper(l[mid+1:])
            return node
        return helper(stack)