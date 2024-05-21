#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   LFU.py
@Time    :   2024/05/21 20:16:13
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

# 实现 LFUCache 类：

# LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
# int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
# void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。
# 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。

# 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。

# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # 缓存的最大容量
        self.key_map = {}  # 存储 key 到 (value, frequency) 的映射
        self.freq_map = defaultdict(OrderedDict)  # 存储 frequency 到有序字典的映射
        self.min_freq = 0  # 记录当前最小的频率

    def get(self, key: int) -> int:
        if key in self.key_map:  # 如果 key 在缓存中
            value, freq = self.key_map[key]  # 获取对应的值和频率
            self._update(key, value, freq)  # 更新频率
            return value  # 返回值
        return -1  # 如果 key 不在缓存中，返回 -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:  # 如果缓存容量为 0，直接返回
            return
        
        if key in self.key_map:  # 如果 key 在缓存中
            _, freq = self.key_map[key]  # 获取当前的频率
            self._update(key, value, freq)  # 更新频率和值
        else:
            if len(self.key_map) >= self.capacity:  # 如果缓存已满
                self._evict_least_frequent()  # 移除最不经常使用的项
            self.key_map[key] = (value, 1)  # 插入新键值对，并设置初始频率为 1
            self.freq_map[1][key] = value  # 在频率为 1 的有序字典中添加该键
            self.min_freq = 1  # 更新最小频率为 1

    def _update(self, key: int, value: int, freq: int) -> None:
        self.freq_map[freq].pop(key)  # 从当前频率对应的有序字典中移除该键
        if len(self.freq_map[freq]) == 0:  # 如果该频率的有序字典为空
            del self.freq_map[freq]  # 删除该频率的有序字典
            if self.min_freq == freq:  # 如果当前频率是最小频率
                self.min_freq += 1  # 更新最小频率
        new_freq = freq + 1  # 增加频率
        self.freq_map[new_freq][key] = value  # 在新的频率有序字典中添加该键
        self.key_map[key] = (value, new_freq)  # 更新 key_map 中的值和频率

    def _evict_least_frequent(self) -> None:
        if self.min_freq in self.freq_map and self.freq_map[self.min_freq]:  # 如果最小频率存在于 freq_map 中且有对应的键
            key, _ = self.freq_map[self.min_freq].popitem(last=False)  # 移除最不经常使用的项（链表头部）
            del self.key_map[key]  # 从 key_map 中删除该键
            if len(self.freq_map[self.min_freq]) == 0:  # 如果最小频率的有序字典为空
                del self.freq_map[self.min_freq]  # 删除该频率
                self.min_freq += 1  # 更新最小频率

# 测试用例
def test_lfu_cache():
    lfu_cache = LFUCache(2)  # 创建一个容量为 2 的 LFUCache

    lfu_cache.put(1, 1)  # 插入键值对 (1, 1)
    lfu_cache.put(2, 2)  # 插入键值对 (2, 2)
    assert lfu_cache.get(1) == 1  # 返回 1，更新键 1 的频率

    lfu_cache.put(3, 3)  # 插入键值对 (3, 3)，此时容量已满，移除键 2
    assert lfu_cache.get(2) == -1  # 返回 -1 (未找到键 2)

    lfu_cache.put(4, 4)  # 插入键值对 (4, 4)，移除键 1
    assert lfu_cache.get(1) == -1  # 返回 -1 (未找到键 1)
    assert lfu_cache.get(3) == 3  # 返回 3
    assert lfu_cache.get(4) == 4  # 返回 4

    lfu_cache.get(4)  # 再次访问键 4，提升频率
    lfu_cache.put(5, 5)  # 插入键值对 (5, 5)，移除键 3
    assert lfu_cache.get(3) == -1  # 返回 -1 (未找到键 3)
    assert lfu_cache.get(4) == 4  # 返回 4
    assert lfu_cache.get(5) == 5  # 返回 5

    print("所有测试用例通过!")

# 执行测试用例
test_lfu_cache()

