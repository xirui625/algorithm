#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 下午4:49
# @Author  : yangguoli
# @File    : 验证IP地址.py
# @Software: PyCharm
# 给定一个字符串 queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；如果不是上述类型的 IP 地址，返回 "Neither" 。
#
class Solution:
    def solve(self , IP ):
        # write code here
        if '.' in IP:
            for ip in IP.split('.'):
                # 判断是不是数字，是不是空字符串，是不是以0开头，是不是在0-255之间
                if ip.isdigit() is False or ip == '' or ip[0] == '0' or (not 0 <= int(ip) <= 255):
                    return 'Neither'
            return 'IPv4'
        if ':' in IP:
            for ip in IP.split(':'):
                # 判断是不是空字符串，是不是都是0组成的
                if ip == '' or (len(ip) > 1 and len(ip) == ip.count('0')):
                    return 'Neither'
        return 'IPv6'
