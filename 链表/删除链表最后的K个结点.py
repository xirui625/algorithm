#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:50
# @Author  : yangguoli
# @File    : 删除链表最后的K个结点.py
# @Software: PyCharm

class Solution:
    def FindKthToTail(self, head, k):
        # 初始化两个指针，都指向链表的头节点
        first, second = head, head
        
        # 第一个指针先走 k 步
        for i in range(k):
            if not first:  # 处理 k 大于链表长度的情况
                return None
            first = first.next
        
        # 第一个指针走到末尾时，第二个指针即为倒数第 k 个节点
        while first:
            first = first.next
            second = second.next
        
        return second
