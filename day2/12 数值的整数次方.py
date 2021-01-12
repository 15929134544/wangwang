"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
"""


class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        else:
            return base ** exponent
