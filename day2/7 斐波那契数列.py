"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，
第1项是1）。
n≤39

注意：第n项下标就是n
"""


class Solution:
    def Fibonacci(self, n):
        res = [0, 1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]


s = Solution()
print(s.Fibonacci(4))