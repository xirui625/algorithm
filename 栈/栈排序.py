#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   栈排序.py
@Time    :   2024/04/02 18:11:58
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
import heapq
# 栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。
# 最多只能使用一个其他的临时栈存放数据，
# 但不得将元素复制到别的数据结构（如数组）中。
# 该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。


class SortedStack:

    def __init__(self):
        self.stack = list()
        heapq.heapify(self.stack)

    def push(self, val: int) -> None:
        heapq.heappush(self.stack,val)

    def pop(self) -> None:
        if not self.isEmpty():
            ref = heapq.heappop(self.stack)
            return ref

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        ref = heapq.heappop(self.stack)
        heapq.heappush(self.stack, ref)
        return ref

    def isEmpty(self) -> bool:
        return len(self.stack) == 0
    


class SortedStack:
    """
    那么入栈时，可以先将比当前元素更小的元素依次出栈，存储到临时栈中，再将当前元素压入栈，最后把临时栈中的元素再放回到原栈中，完成栈中元素的排序。
    """

    def __init__(self):
        self.stack = []
        self.help = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
        else:
            while self.stack and self.stack[-1] < val:
                self.help.append(self.stack.pop())
            self.stack.append(val)
            while self.help:
                self.stack.append(self.help.pop())


    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        return None


    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def isEmpty(self) -> bool:
        return not self.stack
