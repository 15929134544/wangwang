"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        p1 = pHead
        p2 = pHead
        while(True):
            if not p2.next:
                return None
            p1 = p1.next
            p2 = p2.next.next
            if p1==p2:
                break
        p1=pHead
        while p1!=p2:
            p1=p1.next
            p2=p2.next
        return p2