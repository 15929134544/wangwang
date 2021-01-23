"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
对于50%的数据,size≤10 ** 4
对于75%的数据,size≤10 ** 5
对于100%的数据,size≤2∗10 ** 5

超时
"""


# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        sortData = sorted(data)
        count = 0
        for i in sortData:
            pos = data.index(i)
            count += pos
            data.pop(pos)
        return count
