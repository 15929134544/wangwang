"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []
        # 对array中的数字进行异或运算
        tmp = 0
        for i in array:
            tmp ^= i
        # 获取tmp中最低位1的位置
        idx = 0
        while (tmp & 1) == 0:
            tmp >>= 1
            idx += 1
        a = b = 0
        for i in array:
            if self.isBit(i, idx):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def isBit(self, num, idx):
        """
        判断num的二进制从低到高idx位是不是1
        :param num: 数字
        :param idx: 二进制从低到高位置
        :return: num的idx位是否为1
        """
        num = num >> idx
        return num & 1
