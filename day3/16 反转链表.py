"""
输入一个链表，反转链表后，输出新链表的表头。
"""


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # 1.将头节点换成尾节点，并且将头节点的next设置为空
        # 2.将后面的结点的next指向前一个节点
        # 3.需要一个指针指向一个没有翻转的节点
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        left = pHead
        mid = pHead.next
        right = mid.next
        left.next = None
        while right != None:
            mid.next = left
            left = mid
            mid = right
            right = right.next
        mid.next = left
        return mid

