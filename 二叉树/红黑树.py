#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   红黑树.py
@Time    :   2024/05/21 20:01:30
@Author  :   yangguoli 
@Version :   1.0
@Desc    :   None
'''

# 每个节点是红色或黑色。
# 根节点是黑色。
# 所有叶子节点（NIL节点）是黑色。
# 如果一个节点是红色，则它的两个子节点都是黑色（即没有两个连续的红色节点）。
# 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点。

class Node:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color='black')  # 哨兵节点（NIL节点）表示叶子节点
        self.root = self.NIL

    def insert(self, key):
        # 创建新节点并插入红黑树
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL
        self._insert_node(new_node)
        self._fix_insert(new_node)

    def _insert_node(self, node):
        # 插入节点到红黑树中
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            # 树是空的，新节点成为根节点
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        node.color = 'red'  # 新插入的节点总是红色

    def _fix_insert(self, node):
        # 修复插入后可能破坏的红黑树性质
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                # 父节点是祖父节点的左子节点
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    # 情况1：叔叔节点是红色
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # 情况2：节点是父节点的右子节点
                        node = node.parent
                        self._left_rotate(node)
                    # 情况3：节点是父节点的左子节点
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                # 父节点是祖父节点的右子节点
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    # 情况1：叔叔节点是红色
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # 情况2：节点是父节点的左子节点
                        node = node.parent
                        self._right_rotate(node)
                    # 情况3：节点是父节点的右子节点
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'black'  # 根节点始终是黑色

    def _left_rotate(self, x):
        # 左旋转操作
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        # 右旋转操作
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def inorder_traversal(self, node, result):
        # 中序遍历红黑树
        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            result.append(node.key)
            self.inorder_traversal(node.right, result)

def test_red_black_tree():
    rbt = RedBlackTree()
    keys = [20, 15, 25, 10, 5, 1, 30, 35]
    for key in keys:
        rbt.insert(key)

    result = []
    rbt.inorder_traversal(rbt.root, result)
    expected = sorted(keys)

    assert result == expected, f"Test failed! Expected {expected}, got {result}"
    print("Test passed!")

# 执行测试用例
test_red_black_tree()
