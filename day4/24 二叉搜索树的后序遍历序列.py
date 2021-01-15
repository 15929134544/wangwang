"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。
"""


import bisect


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        def verify(sequence):
            if not sequence:
                return True
            pos = bisect.bisect_right(sequence[:-1], sequence[-1])
            left, right = sequence[:pos], sequence[pos:-1]
            for i in left:
                if i > sequence[-1]:
                    return False
            for i in right:
                if i < sequence[-1]:
                    return False
            return verify(left) and verify(right)

        return verify(sequence)
