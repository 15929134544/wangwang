"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

注：
加入新元素，不需要考虑栈12是否空
弹出元素时，需要考虑两种情况：
1.栈2不空，直接弹出
2.栈2空
    栈1不空，弹栈1的元素给栈2
    栈1空，返回-1
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()

        return -1