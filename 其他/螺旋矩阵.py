#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 下午6:23
# @Author  : yangguoli
# @File    : 螺旋矩阵.py
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# @Software: PyCharm

class Solution:
    # class Solution:: 这是一个名为Solution的类的定义。通常在LeetCode等在线编程平台上，算法问题的解决方案需要封装在一个类中，以便通过类的实例调用解决方案方法。

    # def spiralOrder(self, matrix):: 这是一个名为spiralOrder的方法，它接受self（类实例）和matrix作为参数。该方法将返回矩阵的螺旋顺序遍历结果。

    # res = []: 创建一个空列表res，用于存储螺旋顺序遍历的结果。

    # while matrix:: 这是一个while循环，只要矩阵matrix不为空，就会一直执行循环。

    # res += matrix[0]: 将矩阵的第一行（即上边界）添加到结果列表res中。

    # matrix = list(map(list, zip(*matrix[1:])))[::-1]: 这一行代码用于更新矩阵，以便进行下一次迭代。让我们逐步解释：

    # matrix[1:]: 从矩阵中取出第二行到最后一行，即去掉第一行（已经加入结果列表中）。

    # zip(*matrix[1:]): 使用zip函数将剩余的行进行转置，这样每一列就变成了每一行。

    # map(list, ...): 将转置后的元组序列转换为列表。

    # [::-1]: 将转置后的矩阵倒序，以保证下一次迭代仍然是按照顺时针方向遍历。

    # return res: 返回螺旋顺序遍历的结果。
    def spiralOrder(self , matrix ):
        res = []
        while matrix:
            res += matrix[0]
            matrix = list(map(list, zip(*matrix[1:])))[::-1]
        return res