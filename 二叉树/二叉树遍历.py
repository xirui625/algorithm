#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午9:00
# @Author  : yangguoli
# @File    : 二叉树遍历.py
# @Software: PyCharm



class Solution:
    def preOrderRecur1(self, head):
        if not head:
            return None
        print head.value
        self.preOrderRecur1(head.left)
        self.preOrderRecur1(head.right)

    #非递归
    def preOrderRecur2(self, head):
        if not head:
            return None
        stack = []
        stack.append(head)
        while stack:
            node = stack.pop()
            print node.value
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


    def inOrderRecur1(self, head):
        if not head:
            return None
        self.inOrderRecur1(head.left)
        print head.value
        self.inOrderRecur1(head.right)

    def inOrderRecur2(self, head):
        if not head:
            return None
        stack = []
        while stack or head:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                print head.value
                head = head.right


    def posOrderRecur1(self, head):
        if not head:
            return None
        self.posOrderRecur1(head.left)
        self.posOrderRecur1(head.right)
        print head.value

    def posOrderRecur2(self, head):
        if not head:
            return None
        stack1 = []
        stack2 = []
        stack1.append(head)
        while stack1:
            head = stack1.pop()
            stack2.append(head)
            if head.left:
                stack1.append(head.left)
            if head.right:
                stack1.append(head.right)
        while stack2:
            print stack2.pop().value

    def levelOrder(self, head):
        self.res = []
        def helper(root, i=0):
            if not root:
                return
            if len(self.res) == i:
                self.res.append([root.val])
            else:
                self.res[i].append(root.val)
            helper(root.left, i+1)
            helper(root.right, i+1)
        helper(head)
        return self.res
    
    
    def level_helper(self, head):
        self.res = []
        def helper(root, i):
            if not root:
                return
            if len(self.res) == 1:
                self.res.append([root.val])
            else:
                self.res[i].append(root.val)
            helper(root.left, i+1)
            helper(root.right, i+1)
        helper(head)
        return self.res
        
    

