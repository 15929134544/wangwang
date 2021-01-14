"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


class Solution:
    def jumpFloorII(self, number):
        # write code here
        res = [1, 2]
        while len(res) < number:
            # ** 表示次方
            res.append(2**(number-1))
        return res[number-1]