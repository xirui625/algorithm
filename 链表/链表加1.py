#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 下午9:56
# @Author  : yangguoli
# @File    : 链表加1.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def plusOne(self, head):
        # 用于存储链表中的节点值
        st = []
        # 遍历链表，将节点值存入列表中
        while head:
            st.append(head.val)
            head = head.next
        # 初始化进位和虚拟头节点
        carry = 0
        dummy = ListNode(0)
        # 初始要加的数为1
        adder = 1
        # 当链表还有节点值未处理、加的数不为0或有进位时，循环执行
        while st or adder != 0 or carry > 0:
            # 如果列表不为空，弹出当前节点值；否则当前值为0
            digit = st.pop() if st else 0
            # 计算当前位的和，包括当前节点值、加的数以及进位
            sum = digit + adder + carry
            # 更新进位，如果当前位的和大于等于10，则进位为1，否则为0
            carry = 1 if sum >= 10 else 0
            # 如果当前位的和大于等于10，则当前值需要减去10，否则不变
            sum = sum - 10 if sum >= 10 else sum
            # 创建新的节点，值为当前位的和
            cur = ListNode(sum)
            # 将新节点的下一个节点指向结果链表的头节点
            cur.next = dummy.next
            # 将虚拟头节点的下一个节点指向新节点，新节点成为结果链表的新的头节点
            dummy.next = cur
            # 更新加的数为0，因为已经加过了
            adder = 0
        # 返回结果链表的头节点
        return dummy.next
