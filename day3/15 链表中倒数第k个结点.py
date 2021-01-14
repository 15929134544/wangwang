"""
输入一个链表，输出该链表中倒数第k个结点。

python可以不用双指针

注：
倒数第k个节点，下标就是-k
"""


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        list = []
        while head:
            list.append(head)
            head = head.next
        if k> len(list) or k < 1:
            return
        return list[-k]
