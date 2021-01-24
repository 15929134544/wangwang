"""
给定一个数组和滑动窗口的大小，
找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}，
 {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
 {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
窗口大于数组长度的时候，返回空
"""


# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or len(num) < size or size < 1:
            return []
        if size == 1:
            return num

        res = []
        # 假设当前最大值是第一个数
        tmp = [0]
        res = []
        for i in range(len(num)):
            if i - tmp[0] > size - 1:
                tmp.pop(0)
            while len(tmp) > 0 and num[i] >= num[tmp[-1]]:
                tmp.pop()
            tmp.append(i)
            if i >= size - 1:
                res.append(num[tmp[0]])
        return res