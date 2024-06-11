#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午5:08
# @Author  : yangguoli
# @File    : 删除有序链表中的重复元素.py 保留
# @Software: PyCharm
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。



class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head  # 如果链表为空，直接返回

        stack = []  # 初始化一个栈，用于记录已经遍历过的节点值
        pre = head  # 前驱节点初始化为头节点
        cur = head.next  # 当前节点初始化为头节点的下一个节点
        stack.append(head.val)  # 将头节点的值压入栈中，表示已经遍历过

        while cur:
            if cur.val in stack:  # 如果当前节点的值已经在栈中存在，说明是重复节点
                pre.next = cur.next  # 删除当前节点，即将前驱节点的 next 指针指向当前节点的下一个节点
            else:
                stack.append(cur.val)  # 将当前节点的值压入栈中，表示已经遍历过
                pre = cur  # 更新前驱节点为当前节点

            cur = cur.next  # 移动到下一个节点继续遍历

        return head  # 返回处理后的链表
