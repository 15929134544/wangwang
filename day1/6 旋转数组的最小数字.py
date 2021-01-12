"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

思路：
二分查找：出现有序，最好使用二分查找
mid > high 说明最小的数在右半边
mid < low  说明最小的数在左半边
"""


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        low = 0
        high = len(rotateArray) - 1

        if high == 0:
            return 0
        while low < high:
            mid = (low + high) // 2
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            else:
                high = mid
        return rotateArray[low]
