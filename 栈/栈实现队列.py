#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 下午10:13
# @Author  : yangguoli
# @File    : stack_queue.py  栈实现队列
# @Software: PyCharm

# 1、stackPush往stackPop压入数据，需一次性压入所有数据
# 2、stackPop不为空不能压入数据
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）


class Solution:

    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def push_to_pop(self):
        if not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())

    def push(self, node):
        self.push_to_pop()
        self.stackPush.append(node)

    def pop(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("stack is empty")
        self.push_to_pop()
        return self.stackPop.pop()
    
    def peek(self):
        self.push_to_pop()
        return self.stackPop[-1]
    
    def empty(self):
        self.push_to_pop()
        if not self.stackPop:
            return True
        return False


class Solution:
    
    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def push_to_pop(self):
        if not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())

    def push(self, node):
        self.push_to_pop()
        self.stackPush.append(node)

    def pop(self):
        self.push_to_pop()
        self.stackPop.pop()
    
    def peek(self):
       self.push_to_pop()
       return self.stackPop[-1]
    
    def empty(self):
        self.push_to_pop
        if not self.stackPop:
            return True
        return False
