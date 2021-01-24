"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。
 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""



# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        if pHead.val == pHead.next.val:
            pnode = pHead.next.next
            while pnode and pnode.val==pHead.val: # 当前第一个重复结点为pHead
                pnode = pnode.next
            return self.deleteDuplication(pnode)  # 递归处理剩余结点
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead