#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 下午3:26
# @Author  : yangguoli
# @File    : 树是否对称.py
# @Software: PyCharm

class Solurion:
    def isSymmetric(self, root):
        if not root:
            return True
        def match(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and match(left.left, right.right) and match(left.right, right.left)
        return match(root, root)