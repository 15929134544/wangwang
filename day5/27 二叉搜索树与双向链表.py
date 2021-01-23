"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

第一步：将树构造成二叉树，将树的节点加入数组中
第二步：遍历数组的每个节点
    将节点的left作为当前节点的上一个节点
    right作为下一个节点
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        # 没有考虑为空的情况
        if not pRootOfTree:
            return
        self.arr = []
        self.midTraversal(pRootOfTree)
        for i, v in enumerate(self.arr[:-1]):
            v.right = self.arr[i + 1]
            #             v.left = self.arr[i]
            # !!!
            self.arr[i + 1].left = v
        return self.arr[0]

    def midTraversal(self, root):
        # 考虑树为空的情况
        if not root:
            return
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)