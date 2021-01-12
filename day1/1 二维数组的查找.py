"""
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

从右下角或者左上角开始
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array[0]) - 1
        cols = len(array) -1
        i = 0
        j = cols
        while j >= 0 and i <= rows:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i += 1
            else:
                j -= 1
        return False