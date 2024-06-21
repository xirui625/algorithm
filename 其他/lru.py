#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 下午3:54
# @Author  : yangguoli
# @File    : lru.py
# @Software: PyCharm

# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

# LRU算法基于一个简单的假设：最近使用的数据很可能在未来继续被使用，而长时间未被使用的数据被再次使用的可能性较小。因此，在需要腾出空间时，LRU算法会移除最近最少使用的数据。

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._access = []
        self._cache = {}


    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        self._access.remove(key)
        self._access.append(key)
        return self._cache[key]


    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._access.remove(key)
        else:
            while len(self._cache) >= self.capacity:
                self._replace()
        self._access.append(key)
        self._cache[key] = value


    def _replace(self):
        del self._cache[self._access.pop(0)]
        


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key        # 节点的键
        self.value = value    # 节点的值
        self.prev = None     # 指向前一个节点的指针
        self.next = None     # 指向后一个节点的指针

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity   # 缓存容量
        self.cache = {}            # 哈希表，用于快速访问节点
        self.head = ListNode()     # 虚拟头节点
        self.tail = ListNode()     # 虚拟尾节点
        self.head.next = self.tail # 初始化链表的头尾关系
        self.tail.prev = self.head

    def _add_node(self, node):
        # 添加节点到链表头部
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # 从链表中移除指定节点
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        # 将节点移动到链表头部，表示最近访问
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # 弹出链表尾部节点
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)   # 将访问的节点移动到链表头部，表示最近使用
        return node.value          # 返回节点的值

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node:
            # 如果缓存中不存在该节点，则创建新节点并加入到链表头部
            newNode = ListNode(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            if len(self.cache) > self.capacity:
                # 如果缓存超过容量，则移除链表尾部节点
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            # 如果缓存中存在该节点，则更新节点的值，并将节点移动到链表头部
            node.value = value
            self._move_to_head(node)
