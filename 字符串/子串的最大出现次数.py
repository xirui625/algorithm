#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   子串的最大出现次数.py
@Time    :   2024/05/07 14:47:19
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''
# 给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

# 子串中不同字母的数目必须小于等于 maxLetters 。
# 子串的长度必须大于等于 minSize 且小于等于 maxSize 。
 

# 示例 1：

# 输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# 输出：2
# 解释：子串 "aab" 在原字符串中出现了 2 次。
# 它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
# 示例 2：

# 输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# 输出：2
# 解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
# 示例 3：

# 输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# 输出：3
# 示例 4：

# 输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# 输出：0

from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int,
                maxSize: int) -> int:
        if not s:
            return 0

        # 如果字符串长度小于最小长度，直接返回
        if len(s) < minSize:
            return 0

        # 滑窗左边界
        left = 0
        # 滑窗右边界
        right = 0

        # 存储需要计算的子串
        sub_s = ''
        # 存储所有符合条件的子串，便于后面统一比较最大值
        sub_s_L = []

        # 开始滑窗遍历
        while right < len(s):
            # 滑窗的大小
            size = right - left
            if size > maxSize:
                # 大于最大长度，说明不能再扩大窗口了，此时需要缩小窗口，因此左边界前进
                left += 1
                # 相应的窗口子串也需要更新
                sub_s = sub_s[1:]
            elif size >= minSize:
                # 滑窗大小已经满足题目要求，开始处理子串
                if len(set(sub_s)) <= maxLetters:
                    # 子串不同字符数满足要求，找到一个符合条件的，存储起来
                    sub_s_L.append(sub_s)
                # 滑窗继续缩小范围，找出更多可能符合条件的子串（因为滑窗的大小是一个范围值）
                left += 1
                sub_s = sub_s[1:]
            else:
                # 滑窗大小没有达到要求，继续扩大窗口，同时更新窗口子串
                sub_s += s[right]
                right += 1

        # 注意不要遗漏最后的子串处理
        if minSize <= len(sub_s) <= maxSize and len(set(sub_s)) <= maxLetters:
            sub_s_L.append(sub_s)

        if not sub_s_L:
            return 0
        # 计数比较出现频率最多的子串
        return Counter(sub_s_L).most_common(1)[0][1]


if __name__ == '__main__':
    test = Solution()
    print(test.maxFreq("abcde", maxLetters=2, minSize=3, maxSize=3))
