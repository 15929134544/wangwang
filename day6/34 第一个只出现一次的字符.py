"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个
只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）


"""


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) < 0:
            return -1
        l = [0] * 256
        for i in s:
            l[ord(i)] += 1
        for j in s:
            if l[ord(j)] == 1:
                return s.index(j)
                break
        return -1