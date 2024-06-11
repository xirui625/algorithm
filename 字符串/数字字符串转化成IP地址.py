#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:17
# @Author  : yangguoli
# @File    : 数字字符串转化成IP地址.py
# @Software: PyCharm

# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

class Solution:
    def restoreIpAddresses(self, s):
        n = len(s)
        ip_list = []
        
        # 使用三重循环遍历所有可能的分割情况
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # 将 '.' 插入到字符串中
                    str1 = list(s)
                    str1.insert(k, '.')
                    str1.insert(j, '.')
                    str1.insert(i, '.')
                    str1 = ''.join(str1)  # 将列表转换为字符串
                    # 检查生成的 IP 地址是否有效
                    if self.isip(str1):
                        ip_list.append(str1)
        return ip_list

    def isip(self, ip):
        ip = ip.split('.')  # 将 IP 地址按 '.' 分割为列表
        if len(ip) == 4:  # IP 地址必须由四部分组成
            for i in ip:
                if int(i) > 255:  # 每部分数字必须在 0-255 范围内
                    return False
                if len(i) >= 2 and i[0] == '0':  # 每部分数字不能以 0 开头，除非是单个 0
                    return False
            return True
        else:
            return False  # 如果分割后的列表不是 4 个部分，则不是有效的 IP 地址
