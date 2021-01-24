"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        current_que = [pRoot]
        next_que = []
        output = []
        while current_que:
            current_value = []
            for i in current_que:
                current_value.append(i.val)
                if i.left:
                    next_que.append(i.left)
                if i.right:
                    next_que.append(i.right)
            output.append(current_value)
            current_que = next_que
            next_que = []
        return output
