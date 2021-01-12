"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法

注意：
1.考虑当输入为0的时候的输出结果
2.所以在数组中加入一个0
此时输出的下标就是number
那么也应该考虑数组长度的条件设置
"""


class Solution:
    def rectCover(self, number):
        # write code here
        res = [0, 1, 2]
        while len(res) <= number:
            res.append(res[-1]+res[-2])
            print(len(res))
        return res[number]


s = Solution()
print(s.rectCover(4))