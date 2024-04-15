#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午2:34
# @Author  : yangguoli
# @File    : has_ring.py 链表是否有环
# @Software: PyCharm

# 给你一个链表的头节点 head ，判断链表中是否有环。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self , head ):
        # 快慢指针
        # write code here
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle1(self , head ):
        # write code here
        ret = set()
        while head:
            if head in ret:
                return True
            ret.add(head)
            head = head.next

        return False


# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        node = head
        while node:
            if node not in visited:
                visited.add(node)
                node = node.next
            else:
                return node
        return
    

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # 有环的情况下，用一个ans从head开始和慢指针一起走，相交的点就是环的第一个结点
                ans = head
                while ans != slow:
                    ans = ans.next
                    slow = slow.next
                return ans
        return 
