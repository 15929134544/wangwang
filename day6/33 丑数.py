"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

注：
标记三个数：
当前最大丑数前面的数*2，*3，*5的结果大于当前最大丑数的

再选取其中最小的一个
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        res = [1]
        min2 = min3 = min5 = 0
        curindex = 1
        while curindex < index:
            minNum = min(res[min2] * 2, res[min3] * 3, res[min5] * 5)
            res.append(minNum)
            while res[min2] * 2 <= minNum:
                min2 += 1
            while res[min3] * 3 <= minNum:
                min3 += 1
            while res[min5] * 5<= minNum:
                min5 += 1
            curindex += 1
        return res[-1]


