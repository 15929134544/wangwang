"""
输入一颗二叉树的根节点和一个整数，
按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

注：
1.先将序列构建成一颗二叉树
2.对二叉树的每个节点进行遍历
    ！！！
                if sum(map(int, i.split('->'))) == expectNumber:
                res.append(list(map(int, i.split('->'))))
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        treepath = self.dfs(root)
        for i in treepath:
            if sum(map(int, i.split('->'))) == expectNumber:
                res.append(list(map(int, i.split('->'))))
        return res

    def dfs(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        treepath = [str(root.val) + '->' + path for path in self.dfs(root.left)]
        treepath += [str(root.val) + '->' + path for path in self.dfs(root.right)]
        return treepath