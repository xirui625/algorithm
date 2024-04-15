#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   queue.py
@Time    :   2024/03/18 23:00:35
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

from link.node import LinkedListNode


class LinkedListQueue:
    def __init__(self) -> None:
        self._front = None
        self._rear = None
        self._size = 0
        
    def size(self):
        return self._size
    
    def is_empty(self):
        return not self._front
    
    def push(self, value):
        node = LinkedListNode(value)
        if self.is_empty():
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1
        
    def peek(self):
        if self.is_empty():
            raise Exception('queue is empty')
        return self._front.value
    
    def pop(self):
        num = self.peek()
        self._front = self._front.next
        self._size -= 1
        return num
    

class ListQueue:
    def __init__(self, size) -> None:
        self._nums = [0] * size
        self._front = 0
        self._size = 0
    
    def size(self):
        return self._size
    
    def capacity(self):
        return len(self._nums)
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, value):
        if self._size == self.capacity:
            raise Exception('queue is full')
        # 计算下一个队尾所以
        rear = (self._front + self._size) % self.capacity()
        self._nums[rear] = value
        self._size += 1
    
    def peek(self):
        if self.is_empty():
            raise Exception('queue is emppty')
        return self._nums[self._front]
    
    def pop(self):
        num = self.peek()
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        