#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午3:22
# @Author  : yangguoli
# @File    : intersect_node.py 两链表相交问题
# @Software: PyCharm

# 这段代码是用来找到两个无环链表的第一个相交节点的。让我逐步解释它：

# 首先，代码检查两个输入的链表是否为空，如果有一个为空，则直接返回None，因为两个链表无法相交。
# 接下来，代码通过遍历链表计算它们的长度。这是通过分别遍历两个链表来实现的。遍历完之后，会得到两个链表的长度。
# 然后，代码比较两个链表的最后一个节点是否相同。如果不相同，说明两个链表不相交，直接返回None。
# 如果最后一个节点相同，说明两个链表相交。这时，我们需要重新设置两个指针cur1和cur2，分别指向两个链表的头节点。我们还需要一个变量n来记录两个链表的长度差，以便将两个指针调整到同一起点。
# 如果n大于0，说明第一个链表比第二个链表长，我们就让cur1指向第一个链表的头节点，反之，则让cur1指向第二个链表的头节点。
# 然后，我们让cur1指针先走n步，使得cur1和cur2处于同一起点。
# 最后，我们同时移动cur1和cur2指针，直到它们指向同一个节点，这个节点就是第一个相交的节点，我们将其返回。
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None

        cur1, cur2 = pHead1, pHead2
        len1, len2 = 0, 0

        # 计算链表1的长度
        while cur1:
            len1 += 1
            cur1 = cur1.next

        # 计算链表2的长度
        while cur2:
            len2 += 1
            cur2 = cur2.next

        cur1, cur2 = pHead1, pHead2

        # 长的链表先走多出来的步数
        if len1 > len2:
            for _ in range(len1 - len2):
                cur1 = cur1.next
        elif len2 > len1:
            for _ in range(len2 - len1):
                cur2 = cur2.next

        # 同时向后遍历，直到找到第一个相同的节点
        while cur1 and cur2 and cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        return cur1  # 返回第一个相交节点，如果没有相交点则返回None
