"""
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为 O(n).

利用动态规划，dp[i]存储直到下标i的最大结果
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        length = len(array)
        dp = [i for i in array]
        for i in range (1, length):
            dp[i] = max(dp[i-1]+array[i], array[i])
        return max(dp)