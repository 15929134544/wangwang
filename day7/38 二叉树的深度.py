"""
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。


遍历每个结点：
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        res= [pRoot]
        depth = 0
        while res:
            tmp = []
            for node in res:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res = tmp
            depth += 1
        return depth