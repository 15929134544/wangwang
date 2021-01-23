"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针random指向一个随机节点），
请对此链表进行深拷贝，并返回拷贝后的头结点。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


!!!链表指针的变换
注：分为三个步骤：
1.将每个节点复制一个
A' = A.next
2.给每个新节点复制random
A'.random = A.random.next
3.拆分新旧链表
temp = current.next
current.next = temp.next
temp.next = temp.next.next
current = current.next
"""


# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    def Clone(self, head):
        if not head:
            return None
        current_head = head
        # 1.将链表节点复制，且使复制的节点是被复制节点的下一个节点
        while current_head:
            clone_node = RandomListNode(current_head.label)
            clone_node.next = current_head.next
            current_head.next = clone_node
            current_head = current_head.next.next
        # 2.复制随机节点给新节点    A'.random = A.random
        current_head = head
        while current_head:
            current_head.next.random = current_head.random if current_head.random else None
            current_head = current_head.next.next
        # 3.拆分新旧两个链表
        current_head = head
        clone_node = head.next
        while current_head:
            temp = current_head.next
            current_head.next = temp.next
            temp.next = temp.next.next if temp.next else None
            current_head = current_head.next
        return clone_node



