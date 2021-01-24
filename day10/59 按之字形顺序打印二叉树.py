"""
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第
二层按照从右至左的顺序打印，第三行
按照从左到右的顺序打印，其他行以此类推。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        lis = []
        lisnode1 = [pRoot]
        lisnode2 = []
        while len(lisnode1)>0:
            li = []
            while len(lisnode1)>0:
                p = lisnode1.pop(0)
                li.append(p.val)
                if p.left:
                    lisnode2.append(p.left)
                if p.right:
                    lisnode2.append(p.right)
            lisnode1 = lisnode2
            lisnode2 = []
            if len(lis)%2==1:
                li.reverse()
            lis.append(li)
        return lis