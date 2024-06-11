#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午9:09
# @Author  : yangguoli
# @File    : 划分链表.py
# @Software: PyCharm


class Solution:
    def partition(self, head, x):
        sH = sT = None  # sH 和 sT 分别表示小于 x 的链表的头部和尾部
        oH = oT = None  # oH 和 oT 分别表示大于等于 x 的链表的头部和尾部
        
        while head:
            next = head.next  # 保存下一个节点的引用，因为当前节点将会移动到另一个链表
            
            head.next = None  # 断开当前节点与原链表的连接
            
            if head.val < x:
                # 将当前节点加入小于 x 的链表中
                if not sH:
                    sH = sT = head
                else:
                    sT.next = head
                    sT = sT.next
            else:
                # 将当前节点加入大于等于 x 的链表中
                if not oH:
                    oH = oT = head
                else:
                    oT.next = head
                    oT = oT.next
            
            head = next  # 移动到下一个节点
        
        # 将小于 x 的链表和大于等于 x 的链表连接起来
        if sT:
            sT.next = oH
        
        # 返回头部节点，如果没有小于 x 的节点，直接返回大于等于 x 的节点
        return sH if sH else oH



# 链表 head 按照给定值 x 分成三部分：小于 x 的部分、等于 x 的部分和大于 x 的部分
class Solution:
    def partition(self, head, x):
        sH = sT = None  # 小于 x 的链表
        eH = eT = None  # 等于 x 的链表
        bH = bT = None  # 大于 x 的链表
        
        while head:
            next = head.next  # 保存下一个节点的引用，因为当前节点将会移动到另一个链表
            
            head.next = None  # 断开当前节点与原链表的连接
            
            if head.val < x:
                # 将当前节点加入小于 x 的链表中
                if not sH:
                    sH = sT = head
                else:
                    sT.next = head
                    sT = sT.next
            elif head.val == x:
                # 将当前节点加入等于 x 的链表中
                if not eH:
                    eH = eT = head
                else:
                    eT.next = head
                    eT = eT.next
            else:
                # 将当前节点加入大于 x 的链表中
                if not bH:
                    bH = bT = head
                else:
                    bT.next = head
                    bT = bT.next
            
            head = next  # 移动到下一个节点
        
        # 连接三个部分的链表
        if sT:
            sT.next = eH
            eT = eT if eT else sT
        
        if eT:
            eT.next = bH
        
        # 返回头部节点，如果某个部分为空，直接返回下一个部分的头节点
        return sH or eH or bH

