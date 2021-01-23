"""
统计一个数字在升序数组中出现的次数。


二分法查找
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) < 1:
            return 0
        mid = len(data) // 2
        if data[mid] == k:
            left, right = mid, mid
            for i in range(mid, -1, -1):
                if data[i] == k:
                    left -= 1
            for j in range(mid+1, len(data)):
                if data[j] == k:
                    right += 1
            return right - left
        elif data[mid] > k:
            return self.GetNumberOfK(data[:mid], k)
        else:
            return self.GetNumberOfK(data[mid+1:], k)