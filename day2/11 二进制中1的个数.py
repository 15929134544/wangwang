"""
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。

注：python的int型不限位数，所以只需对负数的二进制整体加一
"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n).count('1') if n>=0 else bin(2**32+n).count('1')


