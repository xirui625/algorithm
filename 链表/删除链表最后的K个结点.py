#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:50
# @Author  : yangguoli
# @File    : 删除链表最后的K个结点.py
# @Software: PyCharm

class Solution:
    def FindKthToTail(self, head, k):
        first, second = head, head
        for i in range(k):
            if not first:
                return
            first = first.next
        while first:
            first = first.next
            second = second.next
        return second