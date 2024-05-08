#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   比较版本号.py
@Time    :   2024/04/29 17:58:01
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 给你两个版本号 version1 和 version2 ，请你比较它们。

# 版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。

# 比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。

class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        首先将两个字符串版本号根据.划分，并将每位修订号转换为整数，
        这样自动就去除了前导0带来的影响，
        然后按照最大数组长度同步循环两拆分好后的修订好，
        如果下标超了就意味着这个版本号在这位默认0，
        最后只需要比较哪个修订号更大即可
        """
        vers1 = list(map(lambda x: int(x), version1.split(".")))
        vers2 = list(map(lambda x: int(x), version2.split(".")))
        print(vers1, vers2)
        for i in range(max(len(vers1), len(vers2))):
            v1 = vers1[i] if i<len(vers1) else 0
            v2 = vers2[i] if i<len(vers2) else 0
            if v1 > v2: 
                return 1
            elif v1 < v2: 
                return -1
        return 0

version1 = "1.01"
version2 = '1.001'
so = Solution().compareVersion(version1, version2)