#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   环形链表求环的长度.py
@Time    :   2024/05/06 22:56:41
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head):
    slow = head  # 慢指针
    fast = head  # 快指针

    # 寻找相遇点
    while fast and fast.next:
        slow = slow.next  # 慢指针每次移动一步
        fast = fast.next.next  # 快指针每次移动两步
        if slow == fast:  # 如果两指针相遇，说明有环
            break

    if not fast or not fast.next:
        return None  # 如果快指针或快指针的下一个节点为None，说明没有环

    # 计算环的长度
    cycle_length = 1  # 环的长度至少为1
    fast = fast.next  # 让快指针再向前移动一步
    while slow != fast:
        fast = fast.next  # 快指针每次移动一步
        cycle_length += 1  # 每移动一次，环的长度加1

    return cycle_length

# 示例用法
# 创建链表：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 5 (环的起点是节点5)
head = ListNode(1)
current = head
for i in range(2, 11):
    current.next = ListNode(i)
    current = current.next

# 创建环
cycle_start = head
for _ in range(4):
    cycle_start = cycle_start.next
current.next = cycle_start

# 检测环并计算环的长度
cycle_length = detectCycle(head)
print("环的长度:", cycle_length)  # 输出环的长度