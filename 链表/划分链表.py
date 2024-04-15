#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午9:09
# @Author  : yangguoli
# @File    : 划分链表.py
# @Software: PyCharm


class Solution:
    def partition(self , head , x ):
        sH = sT = None
        oH = oT = None
        while head:
            next = head.next
            head.next = None
            if head.val < x:
                if not sH:
                    sH = sT = head
                else:
                    sT.next = head
                    sT = sT.next
            else:
                if not oH:
                    oH = oT = head
                else:
                    oT.next = head
                    oT = oT.next
            head = next
        if sT:
            sT.next = oH
        return sH if sH else oH

    def partition2(self, head, x):
        sH = sT = None
        eH = eT = None
        bH = bT = None
        while head:
            next = head.next
            head.next = None
            if head.val < x:
                if not sH:
                    sH = sT = head
                else:
                    sT.next = head
                    sT = sT.next
            elif head.val == x:
                if not eH:
                    eH = eT = head
                else:
                    eT.next = head
                    eT = eT.next
            else:
                if not bH:
                    bH = bT = head
                else:
                    bT.next = head
                    bT = bT.next
            head = next
        if sT:
            sT.next = eH
            eT = eT if eT else sT

        if eT:
            eT.next = bH
        return sH or eH or bH

        # write code here
