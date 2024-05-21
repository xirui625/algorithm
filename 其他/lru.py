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
        
        