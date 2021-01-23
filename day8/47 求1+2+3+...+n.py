"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case
等关键字及条件判断语句（A?B:C）。
"""


# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        s = n
        flag = s and self.Sum_Solution(n-1)
        return s+flag