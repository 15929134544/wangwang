"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

注：
1.链表的最后一个节点的next是None
2.将链表的值全都放进列表里面
将列表里的值反转时：可以用reversed() sorted()  list[::-1]
reversed()函数生成的是一个迭代器，所以要用list转换一下！！！！！！！！！！
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        list1 = []
        while listNode:
            list1.append(listNode.val)
            listNode = listNode.next
        return list1[::-1]