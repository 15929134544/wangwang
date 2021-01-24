"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.list = []

    def KthNode(self, pRoot, k):
        # write code here
        if pRoot == None or k == 0:
            return None
        self.mid(pRoot)
        if k > len(self.list):
            return None
        return self.list[k - 1]

    def mid(self, pRoot):
        if pRoot:
            self.mid(pRoot.left)
            self.list.append(pRoot)
            self.mid(pRoot.right)