"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。


遍历结点，求出最大的深度

再判断高度差
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.get_depth(pRoot.left)
        right = self.get_depth(pRoot.right)

        if abs(left - right) > 1:
            return False
        else:
            return True

    def get_depth(self, root):
        if not root:
            return 0

        left_num = self.get_depth(root.left)
        right_num = self.get_depth(root.right)

        return max(left_num, right_num) + 1