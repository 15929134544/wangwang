"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,
则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""

# -*- coding:utf-8 -*-
import itertools


class Solution:
    def Permutation(self, ss):
        # 函数的闭包：如果一个函数在另一个函数的作用域内，且引用了
        # 外层函数的变量，则该函数称为闭包
        # 解题思路：
        """
        1.先确定第一个字符，_xx
        ans：存放最后的结果
        new_str:存放每一次的结果
        visited:存放的是每一个字符位上面，已经使用过的字符
        每使用过一个字符就将它pop出去
        最后再将其insert进来

        pop(0)
        new_str = 'a' arr = ['b', 'c'] visited = ['a']
            递归确定第二位
        arr.insert(0, 'a')

        2.确定第二位上的字符
        new_str = 'a'
        arr = ['b', 'c']
        pop(0)
            new_str = 'ab' arr = ['c'] visited = ['b']
                递归的确定第三位数字
                判断arr的个数，如果个数等于1，那么new_str = 'abc', 加到ans中
            arr.insert(1,'b')
        """
        arr = [x for x in ss]
        lens = len(ss)
        if lens <= 0:
            return []
        ans = []
        new_str = ''

        def dfs(arr, new_str):
            lens = len(arr)
            if lens == 1:
                ans.append(new_str + arr[0])
            visited = set()
            for i in range(lens):
                if arr[i] in visited:
                    continue
                visited.add(arr[i])
                char = arr.pop(i)
                new_str += char  # 加入新的字符
                dfs(arr, new_str)
                arr.insert(i, char)
                new_str = new_str[:-1]  # 减去新的字符

        dfs(arr, new_str)
        return ans


s = Solution()
res = s.Permutation('abc')
print(res)