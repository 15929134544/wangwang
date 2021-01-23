"""
输入一个递增排序的数组和一个数字S，
在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        start = 0
        end = len(array) - 1
        res = []
        while start < end:
            if array[start]+array[end] == tsum:
                res.append([array[start],array[end]])
                start +=1
                end -=1
            elif array[start]+array[end] > tsum:
                end -=1
            else:
                start +=1
        if not res:
            return []
        res = min(res,key=lambda x:x[0]*x[1])
        return res