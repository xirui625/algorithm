#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午10:09
# @Author  : yangguoli
# @File    : 单链表排序.py
# @Software: PyCharm


class Solution:
    def sortList(self, head):
        # 归并排序：找中点cut，cut到最后，再按顺序归在一起

        # 判断递归边界：若head为空，或head.next为空，说明cut到底了，返回head
        if not head or not head.next:
            return head

        # 找中点cut，找中点一般用快慢指针
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next
        # 此时mid为cut后右边子链表的head，而cut后左链表最后一个指针.next，设为None
        mid, slow.next = slow.next, None

        # 递归cut->排序->合并
        left, right = self.sortList(head), self.sortList(mid)

        # 将left和right合并
        h = res = ListNode(0)  # 建个伪head
        while left and right:
            # 若左子链表的节点小，则加入左链表节点，再往右移一位
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next  # 当前结果链表向右移一位

        # 对剩下的节点，直接拼在结果链表后面
        if left:
            h.next = left
        else:
            h.next = right

        return res.next
