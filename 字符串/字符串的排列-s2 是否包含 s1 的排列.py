#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   字符串的排列-s2 是否包含 s1 的排列.py
@Time    :   2024/05/01 16:41:09
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #定义好双指针
        start,cur = 0,len(s1)-1
        #生成两个字典，counter1储存对比target，counter2储存窗口
        counter1,counter2 = collections.Counter(s1),collections.Counter(s2[start:cur])
        # 设定好while循环的边界，因为cur是列表里的索引，所以cur最大只能到len(s2)-1
        while cur <= len(s2)-1:
            #每次循环开始给counter2加上字典右边的相邻的键与值
            counter2[s2[cur]] += 1
            #如果两个字典相等直接返回Ture
            if counter2 == counter1:
                return True
            else:
                #开始滑动窗口，每次给窗口字典最左边的键的值减一
                counter2[s2[start]] -= 1
            #如果递减后最左边的键的值降为零，说明这个键只有一个，直接把这个键从窗口字典中删除
            if counter2[s2[start]] == 0:
                del counter2[s2[start]]
            #两个指针递增
            start+=1
            cur+=1
        # 循环跑完后没有相等的counter2字典，即返回False
        else:
            return False