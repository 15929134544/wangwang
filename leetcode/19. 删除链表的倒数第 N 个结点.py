# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 考察对链表的了解
        dummy = ListNode(0)
        dummy.next = head  # dummy -> 1->2->3->4->5
        # 让slow和fast进行龟兔赛跑

        slow = fast = dummy

        # fast走到第n个元素的地方
        for _ in range(n):
            fast = fast.next

        # fast和slow一起走，直到fast走到最后一个
        # 要确定slow处在倒数第n个元素的前一个元素
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next  # 删除中间的数

        return dummy.next







